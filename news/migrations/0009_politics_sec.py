# Generated by Django 5.0 on 2024-09-17 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_alter_bangladesh_title_alter_latest_news_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='politics_sec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='news_images/')),
                ('title', models.CharField(max_length=250)),
                ('desc', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
