# Generated by Django 4.1.5 on 2023-01-12 23:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diploma', models.CharField(blank=True, max_length=200, null=True)),
                ('nome', models.CharField(max_length=100)),
                ('cognome', models.TextField(max_length=100)),
                ('data_di_nascita', models.DateTimeField(blank=True, null=True)),
                ('data_conseguimento', models.DateTimeField(default=django.utils.timezone.now)),
                ('votazione', models.IntegerField()),
                ('hash', models.CharField(default=None, max_length=32, null=True)),
                ('txId', models.CharField(default=None, max_length=66, null=True)),
                ('author', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
