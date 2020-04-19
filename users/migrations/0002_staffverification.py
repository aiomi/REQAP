# Generated by Django 3.0.4 on 2020-04-19 20:13

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffVerification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selfie', models.ImageField(blank=True, null=True, upload_to='staffs')),
                ('id_card', models.ImageField(blank=True, null=True, upload_to='staffs')),
                ('is_verified', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('staff', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.Staff')),
            ],
        ),
    ]
