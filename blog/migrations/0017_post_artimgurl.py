# Generated by Django 2.1.5 on 2019-08-22 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_remove_post_artimgurl'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='artimgurl',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Адрес картинки'),
        ),
    ]
