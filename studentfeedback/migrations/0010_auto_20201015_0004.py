# Generated by Django 3.1.2 on 2020-10-14 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentfeedback', '0009_collegequestion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collegequestion',
            old_name='ans',
            new_name='ans1',
        ),
        migrations.RemoveField(
            model_name='collegequestion',
            name='que',
        ),
        migrations.AddField(
            model_name='collegequestion',
            name='ans10',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='collegequestion',
            name='ans2',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='collegequestion',
            name='ans3',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='collegequestion',
            name='ans4',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='collegequestion',
            name='ans5',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='collegequestion',
            name='ans6',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='collegequestion',
            name='ans7',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='collegequestion',
            name='ans8',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='collegequestion',
            name='ans9',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='collegequestion',
            name='que1',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='collegequestion',
            name='que10',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='collegequestion',
            name='que2',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='collegequestion',
            name='que3',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='collegequestion',
            name='que4',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='collegequestion',
            name='que5',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='collegequestion',
            name='que6',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='collegequestion',
            name='que7',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='collegequestion',
            name='que8',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='collegequestion',
            name='que9',
            field=models.CharField(default='', max_length=200),
        ),
    ]