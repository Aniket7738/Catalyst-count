from django.db import models
from django.utils import timezone


# Create your models here.

class process_data(models.Model):
    id = models.IntegerField(primary_key=True)
    organization_name = models.CharField(max_length=300, blank=True, null=True)
    domain = models.CharField(max_length=300, blank=True, null=True)
    year_founded = models.IntegerField(blank=True, null=True)
    industry_type = models.CharField(max_length=300, blank=True, null=True)
    size_range = models.CharField(max_length=300,blank=True, null=True)
    locality = models.CharField(max_length=300, blank=True, null=True)
    country = models.CharField(max_length=300, blank=True, null=True)
    link_url = models.URLField(max_length=300, blank=True, null=True)
    current_employee_estimate = models.IntegerField(blank=True, null=True)
    total_employee_estimate = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.organization_name
