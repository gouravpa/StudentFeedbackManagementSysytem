# Generated by Django 3.1.2 on 2020-11-09 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentfeedback', '0014_signup_faculty_qa'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signup',
            old_name='faculty_QA',
            new_name='faculty_QA_1',
        ),
    ]