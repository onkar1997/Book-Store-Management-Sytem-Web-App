# Generated by Django 4.0.4 on 2022-04-20 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_store_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='store_id',
            field=models.IntegerField(),
        ),
    ]
