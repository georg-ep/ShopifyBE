# Generated by Django 3.2.6 on 2022-06-30 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20220630_1404'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productsection',
            old_name='image',
            new_name='file',
        ),
    ]
