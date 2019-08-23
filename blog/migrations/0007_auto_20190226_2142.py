# Generated by Django 2.1.7 on 2019-02-26 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190226_1700'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a book genre (e.g. Science Fiction, French Poetry etc.)', max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(max_length=255, verbose_name='Почта'),
        ),
        migrations.AddField(
            model_name='order',
            name='zstatus',
            field=models.ManyToManyField(help_text='Select a genre for this book', to='blog.Status'),
        ),
    ]