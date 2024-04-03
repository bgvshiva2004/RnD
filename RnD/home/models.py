from django.db import models
from django.utils import timezone


# Create your models here.
class project_details(models.Model):
    Project_Fellowship_No = models.CharField(max_length=20,null=True,blank=True,default=None)
    Project_file_name = models.CharField(max_length=20,null=True,blank= True)
    PI_of_Project = models.CharField(max_length=20,blank=True,null=True)
    Sanctioned_Date = models.DateField(null=True)
    Project_Start_Date = models.DateField(null=True)
    Project_Closure_Date = models.DateField(null=True)
    Title_of_Project = models.CharField(max_length=50,blank=True,null=True)
    project_duration =models.IntegerField(null=True)
    financial_year_start_index = models.IntegerField(null=True)
    financial_year_end_index = models.IntegerField(null=True)
    start_month = models.IntegerField(null=True)
    end_month = models.IntegerField(null=True)
    funding_agency = models.CharField(max_length=100,blank=True,null=True)
    Co_PI_of_Project = models.CharField(max_length=100,blank=True,null=True)
    Country = models.CharField(max_length=100,blank=True,null=True)
    Country_Involved = models.CharField(max_length=100,blank=True,null=True)
    Department = models.CharField(max_length=100,blank=True,null=True)
    Category = models.CharField(max_length=100,blank=True,null=True)
    Details_of_Donors= models.CharField(max_length=100,blank=True,null=True)
    remark = models.TextField(null=True, blank=True)
    scheme_name = models.CharField(max_length=255, null=True, blank=True)
    scheme_code = models.CharField(max_length=50, null=True, blank=True)
    received_amount =models.CharField(max_length=50, null=True, blank=True)
    date_of_receipt_amount = models.DateField(default=timezone.now, null=True, blank=True)
    provisional_uc = models.TextField(null=True, blank=True)
    audited_uc = models.TextField(null=True, blank=True)
    link_uc = models.URLField(null=True, blank=True)
    sanction_letters_link = models.URLField(null=True, blank=True)
    total_project_cost = models.CharField(max_length=50, null=True, blank=True)
    fellowship_type = models.CharField(max_length=100, null=True, blank=True)
    TASK_CHOICES = [
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
    ]

    task = models.CharField(
        max_length=10,
        choices=TASK_CHOICES,
        default='ongoing',
    )