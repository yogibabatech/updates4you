# Generated by Django 4.2.1 on 2023-07-05 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_product_overall_ratings_alter_product_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='query',
            field=models.CharField(default='searchitem', max_length=5000),
        ),
    ]
