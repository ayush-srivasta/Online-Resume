# Generated by Django 4.0.6 on 2022-07-11 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_alter_resume_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='file',
            field=models.FileField(upload_to='pdf'),
        ),
    ]
