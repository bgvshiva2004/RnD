# Generated by Django 4.2.6 on 2023-10-23 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_project_details_project_closure_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project_details',
            name='project_duration',
            field=models.IntegerField(null=True),
        ),
    ]
