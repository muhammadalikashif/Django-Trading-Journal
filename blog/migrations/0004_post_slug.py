# Generated by Django 4.2.4 on 2023-08-28 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='no-slug-description', max_length=100, unique=True),
        ),
    ]
