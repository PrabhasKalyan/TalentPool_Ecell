from django.db import models

class Faculty(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    department = models.CharField(max_length=100, null=True, blank=True)
    designation = models.CharField(max_length=100, null=True, blank=True)
    college = models.CharField(max_length=100, null=True, blank=True)
    profile_url = models.URLField(null=True, blank=True)
    research_areas = models.JSONField(default=list, null=True, blank=True)
    
    def __str__(self):
        return self.name


class Intern(models.Model):
    name_of_org = models.CharField(max_length=256)
    industry = models.CharField(max_length=256)
    yoe = models.PositiveIntegerField()
    location = models.CharField(max_length=256)
    profiles = models.JSONField(default=list)
    pos_available = models.PositiveIntegerField()
    modes= [
        ("Remote","Remote"),
        ("Hybrid","Hybrid"),
        ("On-site","On-site")
    ]
    work_mode = models.CharField(max_length=100)
    job_description = models.CharField(max_length=1000,blank=True,null=True)
    stipend = models.CharField(max_length=256,blank=True,null=True)
    poc_name=models.CharField(max_length=256,blank=True,null=True)
    poc_email=models.EmailField(blank=True,null=True)
    poc_contact=models.CharField(max_length=20,blank=True,null=True)

    def __str__(self):
        return self.name_of_org
    
