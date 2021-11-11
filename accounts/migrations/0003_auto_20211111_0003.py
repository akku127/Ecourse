# Generated by Django 3.2.8 on 2021-11-10 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_subscriptions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='created_on',
        ),
        migrations.AlterField(
            model_name='profile',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='is_lecturer',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='is_student',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
