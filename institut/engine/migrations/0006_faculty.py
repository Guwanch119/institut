# Generated by Django 5.0.1 on 2024-05-07 13:16

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0005_alter_post_body'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
            ],
        ),
    ]
