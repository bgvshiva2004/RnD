# Generated by Django 4.2.6 on 2024-01-17 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_table_info_five_apr_alter_table_info_five_aug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project_details',
            name='end_month',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='project_details',
            name='start_month',
            field=models.IntegerField(null=True),
        ),
    ]
