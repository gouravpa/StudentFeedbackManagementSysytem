# Generated by Django 3.1.2 on 2020-10-22 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentfeedback', '0013_auto_20201015_0105'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='faculty_QA',
            field=models.CharField(blank=True, default='', max_length=5000),
        ),
    ]
