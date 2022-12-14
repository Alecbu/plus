# Generated by Django 4.1.1 on 2022-09-14 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Inf name')),
                ('about', models.TextField(verbose_name='Inf about')),
                ('img', models.ImageField(upload_to='media', verbose_name='Inf image')),
            ],
            options={
                'verbose_name': 'Inf',
                'verbose_name_plural': 'Infs',
            },
        ),
    ]
