# Generated by Django 5.0.1 on 2024-01-27 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_project_details_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_details',
            name='received_amount',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='project_details',
            name='total_project_cost',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
