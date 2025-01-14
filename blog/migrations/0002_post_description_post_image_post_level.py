# Generated by Django 4.2.4 on 2023-08-28 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.TextField(default='No description available.'),
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='blog_images/default.jpg', upload_to='blog_images/'),
        ),
        migrations.AddField(
            model_name='post',
            name='level',
            field=models.CharField(default='No Level Specified', max_length=20),
        ),
    ]
