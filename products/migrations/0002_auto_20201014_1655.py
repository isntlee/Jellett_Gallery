# Generated by Django 3.1.1 on 2020-10-14 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='offer',
        ),
        migrations.RemoveField(
            model_name='product',
            name='has_sizes',
        ),
        migrations.RemoveField(
            model_name='product',
            name='rating',
        ),
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True,
                                    null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='category',
            name='image_url',
            field=models.URLField(blank=True,
                                  max_length=1024, null=True),
        ),
    ]
