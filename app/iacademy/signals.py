from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
import redis

# Redis setup
SERVER_IP = '127.0.0.1'
SERVER_PORT = 6379
PASSWORD = ''
DB = 0
r = redis.StrictRedis(host=SERVER_IP,
                      port=SERVER_PORT,
                      password=PASSWORD,
                      db=DB,
                      charset="utf-8",
                      decode_responses=True)


@receiver(user_logged_in)
def check_last_ip(sender, user, request, **kwargs):
    is_ip_different = False
    username = request.user.username
    last_ip = r.get(username)
    current_ip = request.META['REMOTE_ADDR']
    if last_ip is None:
        r.set(username, current_ip)
    elif current_ip != last_ip:
        r.set(username, current_ip)
        is_ip_different = True
    print(f'is_ip_different: {is_ip_different}')
    print(f'current: {current_ip}, last: {last_ip}')
    return is_ip_different
