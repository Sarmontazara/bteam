# Generated by Django 2.1.5 on 2019-03-04 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20190226_2211'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='prace',
            new_name='price',
        ),
        migrations.RemoveField(
            model_name='order',
            name='desc',
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(max_length=200, verbose_name='ИМЯ'),
        ),
    ]