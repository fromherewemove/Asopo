# Generated by Django 4.1.1 on 2022-11-11 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creators', '0004_remove_creatorfeed_id_creatorfeed_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creatorfeed',
            name='description',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
    ]
