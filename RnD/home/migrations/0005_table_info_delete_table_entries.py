# Generated by Django 4.2.6 on 2023-10-22 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_table_data_table_entries'),
    ]

    operations = [
        migrations.CreateModel(
            name='table_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_no', models.IntegerField(null=True)),
                ('one_Grant_Amount', models.IntegerField(null=True)),
                ('one_Apr', models.IntegerField(null=True)),
                ('one_May', models.IntegerField(null=True)),
                ('one_Jun', models.IntegerField(null=True)),
                ('one_Jul', models.IntegerField(null=True)),
                ('one_Aug', models.IntegerField(null=True)),
                ('one_Sep', models.IntegerField(null=True)),
                ('one_Oct', models.IntegerField(null=True)),
                ('one_Nov', models.IntegerField(null=True)),
                ('one_Dec', models.IntegerField(null=True)),
                ('one_Jan', models.IntegerField(null=True)),
                ('one_Feb', models.IntegerField(null=True)),
                ('one_Mar', models.IntegerField(null=True)),
                ('one_expenses', models.IntegerField(null=True)),
                ('one_closing', models.IntegerField(null=True)),
                ('two_Grant_Amount', models.IntegerField(null=True)),
                ('two_Apr', models.IntegerField(null=True)),
                ('two_May', models.IntegerField(null=True)),
                ('two_Jun', models.IntegerField(null=True)),
                ('two_Jul', models.IntegerField(null=True)),
                ('two_Aug', models.IntegerField(null=True)),
                ('two_Sep', models.IntegerField(null=True)),
                ('two_Oct', models.IntegerField(null=True)),
                ('two_Nov', models.IntegerField(null=True)),
                ('two_Dec', models.IntegerField(null=True)),
                ('two_Jan', models.IntegerField(null=True)),
                ('two_Feb', models.IntegerField(null=True)),
                ('two_Mar', models.IntegerField(null=True)),
                ('two_expenses', models.IntegerField(null=True)),
                ('two_closing', models.IntegerField(null=True)),
                ('three_Grant_Amount', models.IntegerField(null=True)),
                ('three_Apr', models.IntegerField(null=True)),
                ('three_May', models.IntegerField(null=True)),
                ('three_Jun', models.IntegerField(null=True)),
                ('three_Jul', models.IntegerField(null=True)),
                ('three_Aug', models.IntegerField(null=True)),
                ('three_Sep', models.IntegerField(null=True)),
                ('three_Oct', models.IntegerField(null=True)),
                ('three_Nov', models.IntegerField(null=True)),
                ('three_Dec', models.IntegerField(null=True)),
                ('three_Jan', models.IntegerField(null=True)),
                ('three_Feb', models.IntegerField(null=True)),
                ('three_Mar', models.IntegerField(null=True)),
                ('three_expenses', models.IntegerField(null=True)),
                ('three_closing', models.IntegerField(null=True)),
                ('four_Grant_Amount', models.IntegerField(null=True)),
                ('four_Apr', models.IntegerField(null=True)),
                ('four_May', models.IntegerField(null=True)),
                ('four_Jun', models.IntegerField(null=True)),
                ('four_Jul', models.IntegerField(null=True)),
                ('four_Aug', models.IntegerField(null=True)),
                ('four_Sep', models.IntegerField(null=True)),
                ('four_Oct', models.IntegerField(null=True)),
                ('four_Nov', models.IntegerField(null=True)),
                ('four_Dec', models.IntegerField(null=True)),
                ('four_Jan', models.IntegerField(null=True)),
                ('four_Feb', models.IntegerField(null=True)),
                ('four_Mar', models.IntegerField(null=True)),
                ('four_expenses', models.IntegerField(null=True)),
                ('four_closing', models.IntegerField(null=True)),
                ('five_Grant_Amount', models.IntegerField(null=True)),
                ('five_Apr', models.IntegerField(null=True)),
                ('five_May', models.IntegerField(null=True)),
                ('five_Jun', models.IntegerField(null=True)),
                ('five_Jul', models.IntegerField(null=True)),
                ('five_Aug', models.IntegerField(null=True)),
                ('five_Sep', models.IntegerField(null=True)),
                ('five_Oct', models.IntegerField(null=True)),
                ('five_Nov', models.IntegerField(null=True)),
                ('five_Dec', models.IntegerField(null=True)),
                ('five_Jan', models.IntegerField(null=True)),
                ('five_Feb', models.IntegerField(null=True)),
                ('five_Mar', models.IntegerField(null=True)),
                ('five_expenses', models.IntegerField(null=True)),
                ('five_closing', models.IntegerField(null=True)),
                ('six_Grant_Amount', models.IntegerField(null=True)),
                ('six_Apr', models.IntegerField(null=True)),
                ('six_May', models.IntegerField(null=True)),
                ('six_Jun', models.IntegerField(null=True)),
                ('six_Jul', models.IntegerField(null=True)),
                ('six_Aug', models.IntegerField(null=True)),
                ('six_Sep', models.IntegerField(null=True)),
                ('six_Oct', models.IntegerField(null=True)),
                ('six_Nov', models.IntegerField(null=True)),
                ('six_Dec', models.IntegerField(null=True)),
                ('six_Jan', models.IntegerField(null=True)),
                ('six_Feb', models.IntegerField(null=True)),
                ('six_Mar', models.IntegerField(null=True)),
                ('six_expenses', models.IntegerField(null=True)),
                ('six_closing', models.IntegerField(null=True)),
                ('seven_Grant_Amount', models.IntegerField(null=True)),
                ('seven_Apr', models.IntegerField(null=True)),
                ('seven_May', models.IntegerField(null=True)),
                ('seven_Jun', models.IntegerField(null=True)),
                ('seven_Jul', models.IntegerField(null=True)),
                ('seven_Aug', models.IntegerField(null=True)),
                ('seven_Sep', models.IntegerField(null=True)),
                ('seven_Oct', models.IntegerField(null=True)),
                ('seven_Nov', models.IntegerField(null=True)),
                ('seven_Dec', models.IntegerField(null=True)),
                ('seven_Jan', models.IntegerField(null=True)),
                ('seven_Feb', models.IntegerField(null=True)),
                ('seven_Mar', models.IntegerField(null=True)),
                ('seven_expenses', models.IntegerField(null=True)),
                ('seven_closing', models.IntegerField(null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='table_entries',
        ),
    ]
