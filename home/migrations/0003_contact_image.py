# Generated by Django 4.2.1 on 2023-05-30 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_name_contact_first_name_contact_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='image',
            field=models.ImageField(default=1, upload_to='contact/', verbose_name='Изображение'),
            preserve_default=False,
        ),
    ]