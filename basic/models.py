from django.db import models
from django.contrib.auth.models import User
# Create your models here.
import datetime
from django.utils import timezone
from datetime import timedelta,date
import datetime as dt



class company_or_employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    catagory = models.CharField(max_length=200,default="employee")
    def __str__(self):
        return self.user.username



class details_check(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    details_uploaded = models.BooleanField(default = False)
    email_verified = models.BooleanField(default = False)
    
    def __str__(self):
        return self.user.username


class user_details(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200,)
    profession = models.TextField(max_length=2000,default="Hard Worker")
    about = models.TextField(max_length=2000,default="noname")
    birthday = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    facts = models.TextField(max_length=200,default="noname")
    clients = models.CharField(max_length=2000)
    projects = models.CharField(max_length=200)
    awards = models.CharField(max_length=200)
    experience_years = models.CharField(max_length=200)
    skills = models.TextField(max_length=20000,default="")
    equity = models.CharField(max_length=20000,default="0")
    freelance = models.CharField(max_length=20000,default="NO")
    ratings = models.CharField(max_length=20000,default="4")
    ratings_sum = models.CharField(max_length=20000,default="4")
    ratings_count = models.CharField(max_length=20000,default="1")
    
    
class user_details_skills(models.Model):
    person = models.ForeignKey(user_details,on_delete=models.CASCADE)
    skills = models.CharField(max_length=200)
    skills_rate = models.CharField(max_length=200)
    

    
    

class user_details_education(models.Model):
    education = models.ForeignKey(user_details,on_delete=models.CASCADE)
    education_college = models.TextField(max_length=2000)
    education_years = models.TextField(max_length=2000)
    education_degree = models.TextField(max_length=2000)
    education_speacialization = models.TextField(max_length=2000)
    education_cgpa = models.TextField(max_length=2000)


class user_details_work(models.Model):
    work = models.ForeignKey(user_details,on_delete=models.CASCADE)
    years = models.TextField(max_length=2000)
    discription = models.TextField(max_length=2000)
    role = models.TextField(max_length=2000)
    employer = models.TextField(max_length=2000,default="NA")

class user_details_testimonial(models.Model):
    testimonial = models.ForeignKey(user_details,on_delete=models.CASCADE)
    name = models.TextField(max_length=2000)
    role = models.TextField(max_length=2000)
    description = models.TextField(max_length=2000)

class user_details_social(models.Model):
    person = models.ForeignKey(user_details,on_delete=models.CASCADE)
    twitter = models.TextField(max_length=2000,default="noname")
    linkedin = models.TextField(max_length=2000,default="noname")
    instagram = models.TextField(max_length=2000,default="noname")
    gmail = models.TextField(max_length=2000,default="noname")
    facebook = models.TextField(max_length=2000,default="noname")
    skype = models.TextField(max_length=2000,default="noname")
    

class user_details_project(models.Model):
    work = models.ForeignKey(user_details,on_delete=models.CASCADE)
    project_duration = models.TextField(max_length=2000)
    link = models.TextField(max_length=2000)
    project_describe = models.TextField(max_length=2000)
    project_name = models.TextField(max_length=2000,default="NA")


class company_details(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.TextField(max_length=2000,default="noname")
    about = models.TextField(max_length=2000,default="noname")
    vision = models.TextField(max_length=2000,default="noname")
    size = models.TextField(max_length=2000,default="noname")
    funding = models.TextField(max_length=2000,default="noname")
    address = models.TextField(max_length=2000,default="noname")
    website = models.TextField(max_length=2000,default="noname")
    email = models.TextField(max_length=2000,default="noname")
    
    
    
    


class income_company(models.Model):
    comapny = models.ForeignKey(company_details,on_delete=models.CASCADE)
    month_number = models.CharField(max_length=200,default="1")
    year = models.CharField(max_length=200,default="2022")
    value = models.CharField(max_length=200,default="2022")
    
    
class company_hired(models.Model):
    comapny = models.ForeignKey(company_details,on_delete=models.CASCADE)
    person = models.ForeignKey(user_details,on_delete=models.CASCADE)
    name = models.TextField(max_length=2000,default="noname")
    hire_id = models.TextField(max_length=2000,default="noname")
    


class company_job(models.Model):
    comapny = models.ForeignKey(company_details,on_delete=models.CASCADE)
    role = models.CharField(max_length=200,default="2022")
    experience = models.CharField(max_length=200,default="0")
    description = models.TextField(max_length=2000,default="noname")
    salary = models.CharField(max_length=200,default="2022")
    skills = models.CharField(max_length=200,default="C++")
    location = models.TextField(max_length=2000,default="noname")
    country = models.TextField(max_length=2000,default="noname")
    catagory = models.TextField(max_length=2000,default="noname")
    date = models.DateField(default=datetime.date.today)
    equity = models.TextField(max_length=2000,default="NO")
    
    


class company_job_applications(models.Model):
    job = models.ForeignKey(company_job,on_delete=models.CASCADE)
    person = models.ForeignKey(user_details,on_delete=models.CASCADE)
    name = models.TextField(max_length=2000,default="noname")
    hire_id = models.TextField(max_length=2000,default="noname")