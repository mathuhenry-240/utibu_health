# Generated by Django 5.0.3 on 2024-03-27 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utibuapp', '0003_alter_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Tags',
        ),
    ]
