# Generated by Django 2.1.7 on 2019-02-26 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20190226_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Статус'),
        ),
    ]