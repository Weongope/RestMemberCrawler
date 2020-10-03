# Generated by Django 3.1.dev20200318185912 on 2020-09-30 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restmember', '0003_auto_20200930_1830'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='member_profession',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='member_profession',
            name='member',
        ),
        migrations.RemoveField(
            model_name='member_profession',
            name='profession',
        ),
        migrations.RemoveField(
            model_name='profession',
            name='members',
        ),
        migrations.AddField(
            model_name='member',
            name='languages',
            field=models.CharField(default='NoLang', max_length=50, verbose_name='Known Languages'),
        ),
        migrations.AddField(
            model_name='member',
            name='profession',
            field=models.CharField(default='Noprof', max_length=50, verbose_name='profession'),
        ),
        migrations.DeleteModel(
            name='Languages',
        ),
        migrations.DeleteModel(
            name='Member_profession',
        ),
        migrations.DeleteModel(
            name='profession',
        ),
    ]