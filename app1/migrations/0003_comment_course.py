# Generated by Django 3.2.8 on 2021-11-10 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20211110_0707'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.course'),
        ),
    ]