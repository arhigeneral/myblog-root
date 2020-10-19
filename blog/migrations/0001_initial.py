# Generated by Django 3.1.2 on 2020-10-19 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_image', models.ImageField(upload_to='blog_images/')),
                ('blog_text', models.CharField(max_length=300)),
                ('blog_date', models.DateTimeField()),
                ('blog_title', models.CharField(max_length=30)),
            ],
        ),
    ]
