# Generated by Django 5.0.6 on 2024-06-13 10:40

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hindu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('_id', models.CharField(db_column='_id', default=uuid.uuid1, editable=False, max_length=45, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('dob', models.DateField()),
                ('gotram', models.CharField(blank=True, max_length=200)),
                ('verification_otp', models.CharField(blank=True, max_length=6, null=True)),
                ('verification_otp_created_time', models.DateTimeField(null=True)),
                ('verification_otp_resend_count', models.IntegerField(default=0)),
                ('status', models.CharField(max_length=50)),
                ('username', models.CharField(db_column='username', max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('forgot_password_otp', models.CharField(blank=True, max_length=6, null=True)),
                ('forgot_password_otp_created_time', models.DateTimeField(null=True)),
                ('forgot_password_otp_resend_count', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'profile',
            },
        ),
    ]