# Generated by Django 4.2.1 on 2023-05-09 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_job_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='svg',
            field=models.FileField(default='', upload_to='jobs_svg/'),
            preserve_default=False,
        ),
    ]
