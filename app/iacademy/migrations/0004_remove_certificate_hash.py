# Generated by Django 3.2.11 on 2023-01-20 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iacademy', '0003_auto_20230120_1717'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='certificate',
            name='hash',
        ),
    ]