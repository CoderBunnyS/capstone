# Generated by Django 3.1.4 on 2020-12-07 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preschool', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='Age',
            new_name='age',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='ChildName',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='ParentName',
        ),
        migrations.AddField(
            model_name='profile',
            name='allergies',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='childname',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='dob',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='', max_length=254, unique=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='parentname',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='phonenum',
            field=models.CharField(default='', max_length=10),
        ),
    ]