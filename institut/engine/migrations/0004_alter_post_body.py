# Generated by Django 5.0.1 on 2024-03-18 12:07

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0003_category_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
