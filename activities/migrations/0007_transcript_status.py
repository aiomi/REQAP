# Generated by Django 3.0.4 on 2020-05-02 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0006_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='transcript',
            name='status',
            field=models.CharField(choices=[('initiated', 'Initiated'), ('paid', 'Paid'), ('approved', 'Approved'), ('denied', 'Denied')], default='initiated', max_length=10),
        ),
    ]
