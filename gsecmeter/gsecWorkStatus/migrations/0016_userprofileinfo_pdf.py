# Generated by Django 2.0.5 on 2018-06-20 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gsecWorkStatus', '0015_remove_userprofileinfo_pdf'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='pdf',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
