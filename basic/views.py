from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
import requests
from django.conf import settings
from django.core.mail import send_mail

from datetime import datetime, timedelta,date,timezone


def landingpage(request):
    context = {
    }
    return render(request, 'landingpage.html', context=context)

def blog(request):
    context = {
    }
    return render(request, 'blog.html', context=context)


def blog_single(request):
    context = {
    }
    return render(request, 'blog-single.html', context=context)


def login_incubator(request):
    if request.method == 'POST':
        name = request.POST.get('email')
        password = request.POST.get('password')
        print(name)
        print(password)
        user = authenticate(username=name, password=password)
        print(user)
        if user is not None:
            print(" asdasdsad")
            login(request, user)
            obj = company_or_employee.objects.get(user = request.user)
            if obj.catagory == 'employee':
                obj1 = details_check.objects.get(user = request.user)
                if obj1.details_uploaded:
                    return HttpResponseRedirect("/resume_show")
                return HttpResponseRedirect("/details_fill")
            else:
                return HttpResponseRedirect("/company")        
    context = {
    }
    return render(request, 'login_page.html', context=context)


def register(request):
    logout(request)
    context = {
    }
    return render(request, 'signup.html', context=context)

def register_user(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    password = request.POST.get('password')
    try:
        already_exists = User.objects.get(username = email)
        val = 1
        context = {
            'val':val,
        }
        return render(request, 'signup.html', context=context)
    except:

        
        obj = User(username=email,password=password,email=email)
        obj.save()


        ob = User.objects.get(username = email)
        obj1 = details_check(user = ob)
        obj1.save()

        obj2 = company_or_employee(user = ob)
        obj2.save()
        
        user = authenticate(username=email, password=password)
        # subject = 'welcome to Incubator world'
        # message = f'Hi ' + str(name) +', thank you for registering.'
        # email_from = settings.EMAIL_HOST_USER
        # recipient_list = [email,]
        # send_mail( subject, message, email_from, recipient_list )
        # login(request, user)    
        
        context = {
            
        }
        return HttpResponseRedirect("/login_incubator")


def details_fill(request):
    context = {
    }
    return render(request, 'details_new.html', context=context)


def resume_show(request):
    obj = user_details.objects.get(user = request.user)
    obj1 = {}
    obj2 = {}
    obj3 = {}
    obj4 = {}
    obj5 = {}
    obj6 = {}

    try:
        obj1 = user_details_social.objects.get(person = obj)
    except:
        pass

    try:
        obj2 = user_details_skills.objects.filter(person=obj).all()
    except:
        pass

    try:   
        obj3 = user_details_education.objects.filter(education=obj).all()
    except:
        pass

    try:   
        obj4 = user_details_work.objects.filter(work=obj).all()
    except:
        pass

    try:   
        obj5 = user_details_project.objects.filter(work=obj).all()
    except:
        pass
    
    try:   
        obj6 = user_details_testimonial.objects.filter(testimonial=obj).all()
    except:
        pass
    

    context = {
        'obj':obj,
        'obj1':obj1,
        'obj2':obj2,
        'obj3':obj3,
        'obj4':obj4,
        'obj5':obj5,
    }
    
    return render(request, 'resume.html', context=context)

def demo(request):
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    experience = request.POST.get('experience')
    phone = request.POST.get('phone')
    birth_month = request.POST.get('birth_month')
    birth_date = request.POST.get('birth_date')
    birth_year = request.POST.get('birth_year')
    about = request.POST.get('about')
    linkedin = request.POST.get('linkedin')
    twitter = request.POST.get('twitter')
    instagram = request.POST.get('instagram')
    projects = request.POST.get('projects')
    awards = request.POST.get('awards')
    clients = request.POST.get('clients')
    equity = request.POST.get('equity')
    address = request.POST.get('address')
    freelance = request.POST.get('freelance')
    obj = user_details(user = request.user,full_name = first_name + ' ' + last_name,about = about,phone = phone,projects = projects,awards = awards,birthday = birth_date + '/' + birth_month + '/'+ birth_year,experience_years = experience,city = address,equity = equity,freelance=freelance)
    obj.save()    

    obj1 = user_details_social(person = obj,twitter = twitter,linkedin = linkedin,skype = instagram)
    obj1.save()
    
    obj2 = details_check.objects.get(user = request.user)
    obj2.details_uploaded = True
    obj2.save()

    return HttpResponseRedirect("/resume_show")


def skill_new_add(request):
    try:
        skills = request.POST.get('skills')
        
        skills_rate = request.POST.get('skills_rate')
        
        print(skills)
        print(skills_rate)

        obj = user_details.objects.get(user = request.user)
        
        obj.skills += str(skills) + ','
        obj.save()

        obj1 = user_details_skills(person=obj,skills = skills,skills_rate = skills_rate)
        
        
        obj1.save()

        return HttpResponseRedirect("/resume_show")
    except:
        return HttpResponseRedirect("/resume_show")



def skill_education_done(request):
    try:
        college = request.POST.get('college')
        
        degree = request.POST.get('degree')

        speacialization = request.POST.get('speacialization')

        cgpa = request.POST.get('cgpa')
        
        education_year = request.POST.get('education_year')
        
        obj = user_details.objects.get(user = request.user)
        
        obj1 = user_details_education(education=obj,education_college = college,education_years = education_year,education_degree = degree,education_speacialization = speacialization,education_cgpa = cgpa)
        
        obj1.save()

        return HttpResponseRedirect("/resume_show")
    except:
        return HttpResponseRedirect("/resume_show")



def skill_experience_done(request):
    try:
        employer = request.POST.get('employer')
        
        role = request.POST.get('role')

        years = request.POST.get('years')

        role_describe = request.POST.get('role_describe')
        
        
        obj = user_details.objects.get(user = request.user)
        
        obj1 = user_details_work(work=obj,years = years,discription = role_describe,role = role,employer = employer)
        obj1.save()

        return HttpResponseRedirect("/resume_show")
    except:
        return HttpResponseRedirect("/resume_show")


def add_work_extra(request):
    try:
        project_name = request.POST.get('project_name')
        
        project_duration = request.POST.get('project_duration')

        link = request.POST.get('link')

        project_describe = request.POST.get('project_describe')
        
        
        obj = user_details.objects.get(user = request.user)
        
        obj1 = user_details_project(work=obj,project_duration = project_duration,link = link,project_describe = project_describe,project_name = project_name)
        
        obj1.save()

        return HttpResponseRedirect("/resume_show")
    except:
        return HttpResponseRedirect("/resume_show")



def company(request):
    company_details_to_pass = company_details.objects.get(user = request.user)

    currentYear = str(datetime.now().year)
    
    currentMonth = str(datetime.now().month)

    income = income_company.objects.filter(year = currentYear).all()


    current_income = 0
    year_income = 0

    income_to_show = [0,0,0,0,0,0,0,0,0,0,0,0]
    
    for i in income:
        if i.month_number == currentMonth:
            current_income = i.value
        year_income += int(i.value)
        a = int(i.value)
        print(i.month_number)
        income_to_show[int(i.month_number) - 1] += a

    person_hired = company_hired.objects.filter(comapny = company_details_to_pass).count()
    job = company_job.objects.filter(comapny = company_details_to_pass)
    job_count = job.count()

    hired = company_hired.objects.filter(comapny = company_details_to_pass)

    print(hired)

    context = {
        'income_to_show':income_to_show,
        'hired':hired,
        'person_hired':person_hired,
        'company_details_to_pass':company_details_to_pass,
        'year_income':year_income,
        'income':income,
        'current_income':current_income,
        'job_count':job_count,
        'job':job, 
    }
    return render(request, 'company.html', context=context)





def person_show(request,id):

    obj = user_details.objects.get(id = id)
    company = company_details.objects.get(user = request.user)
    obj1 = {}
    obj2 = {}
    obj3 = {}
    obj4 = {}
    obj5 = {}
    obj6 = {}

    try:
        obj1 = user_details_social.objects.get(person = obj)
    except:
        pass

    try:
        obj2 = user_details_skills.objects.filter(person=obj).all()
    except:
        pass

    try:   
        obj3 = user_details_education.objects.filter(education=obj).all()
    except:
        pass

    try:   
        obj4 = user_details_work.objects.filter(work=obj).all()
    except:
        pass

    try:   
        obj5 = user_details_project.objects.filter(work=obj).all()
    except:
        pass
    
    try:   
        obj6 = user_details_testimonial.objects.filter(testimonial=obj).all()
    except:
        pass
    

    context = {
        'obj':obj,
        'obj1':obj1,
        'company':company,
        'obj2':obj2,
        'obj3':obj3,
        'obj4':obj4,
        'obj5':obj5,
    }
    
    return render(request, 'resume_company.html', context=context)



def job_show(request,id,exp):
    job_data = company_job.objects.get(id = id)
    job = company_job_applications.objects.filter(job = job_data)
    obj = {}

    try:
        for i in job:
            try:
                if int(i.person.experience_years) >= int(exp):
                    print(i)
                    obj[i.person.id] = [i.person.full_name,i.person.experience_years,i.person.skills,i.person.equity,i.person.freelance,i.person.ratings]
            except:
                pass
    except:
        pass
    context = {
        'obj':obj,
        'exp':exp,
        'job_data':job_data,
    }
    return render(request, 'company_applications.html', context=context)


def job_delete(request,id):
    job_data = company_job.objects.get(id = id)
    job_data.delete()
    return HttpResponseRedirect("/company")



def hiring_done(request,company_id,person_id):
    comapny = company_details.objects.get(id = company_id)
    person = user_details.objects.get(id = person_id)

    obj = company_hired(comapny = comapny,person = person,name = person.full_name,hire_id = person.id)

    obj.save()
    return HttpResponseRedirect("/company")



def person_search(request):
    company = company_details.objects.get(user = request.user)
    skills_req = request.POST.get('skills_req')
    return HttpResponseRedirect("/person_search_show/" + str(skills_req) + "/0/NA")

    
    

def person_search_show(request,skill_req,exp,free):
    skill = str(skill_req)
    person_object = user_details_skills.objects.filter(skills__contains = skill).order_by('-skills_rate')
    freelancing = str(free)
    obj = {}
    try:
        for i in person_object:
            if int(i.person.experience_years) >= int(exp):
                if freelancing == 'NA':
                    obj[i.person.id] = [i.person.full_name,i.person.experience_years,i.person.skills,i.person.equity,i.person.freelance,i.person.ratings]
                elif freelancing == 'equity':
                    if int(i.person.equity) > 0:
                        obj[i.person.id] = [i.person.full_name,i.person.experience_years,i.person.skills,i.person.equity,i.person.freelance,i.person.ratings]
                else:
                    if i.person.freelance != 'NO':
                        obj[i.person.id] = [i.person.full_name,i.person.experience_years,i.person.skills,i.person.equity,i.person.freelance,i.person.ratings]
    except:
        pass
    context = {
        'skill':skill,
        'obj':obj,
        'exp':exp,
        'freelancing':freelancing,
    }
    return render(request, 'company_person.html', context=context)



def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")


def register_company(request):
    logout(request)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            already_existed = User.objects.get(username = email)
            val = 1
            context = {
                'val':val,
            }
            return render(request, 'sign_up_company.html', context=context)
        except:
            obj = User(username=email,password=password,email=email)
            obj.save()


            ob = User.objects.get(username = email)
            
            
            obj2 = company_or_employee(user = ob,catagory = "company")
            obj2.save()

            # subject = 'welcome to Incubator world'
            # message = f'Hi ' + str(name) +', thank you for registering in geeksforgeeks.'
            # email_from = settings.EMAIL_HOST_USER
            # recipient_list = [email,]
            # send_mail( subject, message, email_from, recipient_list )

            context = {
            }
            return HttpResponseRedirect("/thanks_registration")
    
    context = {
            }
    return render(request, 'sign_up_company.html', context=context)


def thanks_registration(request):
    context = {
            }
    return render(request, 'thanks.html', context=context)

def search_jobs(request):
    obj = company_job.objects.all().order_by('-date')[:10]
    context = {
        'obj':obj,
            }
    return render(request, 'search_jobs.html', context=context)

def job_listing(request):
    obj = company_job.objects.all().order_by('-date')
    print(obj)
    job_count = obj.count()
    job_type = "any"
    date_posting = "any"
    sort_by = "any"
    context = {
        'obj':obj,
        'job_type':job_type,
        'date_posting':date_posting,
        'job_count':job_count,
        'sort_by':sort_by,
            }
    return render(request, 'job_listing.html', context=context)


def job_listing_filter(request,job,date,sort,search_key):
    
    job_type = str(job)
    date_posting = str(date)
    sort_by = str(sort)
    key = str(search_key)
    print(key)
    print(" asdasdsad ")
    if key == 'any':
        print(" sadasd ")
        if job_type == 'any':
            if date_posting == 'any':
                if sort_by == 'any':
                    obj = company_job.objects.all().order_by('-date')
                else:
                    obj = company_job.objects.all().order_by('-salary')
            elif date_posting == '0':
                checkinDate=(datetime.now(timezone.utc) +  timedelta(hours=5.5)).date()
                obj = company_job.objects.filter(date = checkinDate)
            elif date_posting == '1':
                checkinDate=(datetime.now(timezone.utc) +  timedelta(hours=5.5) - timedelta(days=1)).date()
                obj = company_job.objects.filter(date__gte = checkinDate)
            elif date_posting == '2':
                checkinDate=(datetime.now(timezone.utc) +  timedelta(hours=5.5) - timedelta(days=2)).date()
                obj = company_job.objects.filter(date__gte = checkinDate)
            elif date_posting == '3':
                checkinDate=(datetime.now(timezone.utc) +  timedelta(hours=5.5) - timedelta(days=3)).date()
                obj = company_job.objects.filter(date__gte = checkinDate)
            elif date_posting == '5':
                checkinDate=(datetime.now(timezone.utc) +  timedelta(hours=5.5) - timedelta(days=5)).date()
                obj = company_job.objects.filter(date__gte = checkinDate)
            elif date_posting == '10':
                checkinDate=(datetime.now(timezone.utc) +  timedelta(hours=5.5) - timedelta(days=10)).date()
                obj = company_job.objects.filter(date__gte = checkinDate)
        else:
            if date_posting == 'any':
                if sort_by == 'any':
                    obj = company_job.objects.filter(equity = job_type).order_by('-date')
                else:
                    obj = company_job.objects.filter(equity = job_type).order_by('-salary')
            elif date_posting == '0':
                checkinDate=(datetime.now(timezone.utc) +  timedelta(hours=5.5)).date()
                obj = company_job.objects.filter(date = checkinDate,equity = job_type)
            elif date_posting == '1':
                checkinDate=(datetime.now(timezone.utc) +  timedelta(hours=5.5) - timedelta(days=1)).date()
                obj = company_job.objects.filter(date__gte = checkinDate,equity = job_type)
            elif date_posting == '2':
                checkinDate=(datetime.now(timezone.utc) +  timedelta(hours=5.5) - timedelta(days=2)).date()
                obj = company_job.objects.filter(date__gte = checkinDate,equity = job_type)
            elif date_posting == '3':
                checkinDate=(datetime.now(timezone.utc) +  timedelta(hours=5.5) - timedelta(days=3)).date()
                obj = company_job.objects.filter(date__gte = checkinDate,equity = job_type)
            elif date_posting == '5':
                checkinDate=(datetime.now(timezone.utc) +  timedelta(hours=5.5) - timedelta(days=5)).date()
                obj = company_job.objects.filter(date__gte = checkinDate,equity = job_type)
            elif date_posting == '10':
                checkinDate=(datetime.now(timezone.utc) +  timedelta(hours=5.5) - timedelta(days=10)).date()
                obj = company_job.objects.filter(date__gte = checkinDate,equity = job_type)
    else:
        if job_type == 'any':
            if date_posting == 'any':
                if sort_by == 'any':
                    obj = company_job.objects.filter(role__contains = key).order_by('-date')
                else:
                    obj = company_job.objects.filter(role__contains = key).order_by('-salary')
            elif date_posting == '0':
                checkinDate=(datetime.now(timezone.utc) +  timedelta(hours=5.5)).date()
                obj = company_job.objects.filter(date = checkinDate,role__contains = key)
            elif date_posting == '1':
                checkinDate=(datetime.now(timezone.utc) +  timedelta(hours=5.5) - timedelta(days=1)).date()
                obj = company_job.objects.filter(date__gte = checkinDate,role__contains = key)
            elif date_posting == '2':
                checkinDate=(datetime.now(timezone.utc) +  timedelta(hours=5.5) - timedelta(days=2)).date()
                obj = company_job.objects.filter(date__gte = checkinDate,role__contains = key)
            elif date_posting == '3':
                checkinDate=(datetime.now(timezone.utc) +  timedelta(hours=5.5) - timedelta(days=3)).date()
                obj = company_job.objects.filter(date__gte = checkinDate,role__contains = key)
            elif date_posting == '5':
                checkinDate=(datetime.now(timezone.utc) +  timedelta(hours=5.5) - timedelta(days=5)).date()
                obj = company_job.objects.filter(date__gte = checkinDate,role__contains = key)
            elif date_posting == '10':
                checkinDate=(datetime.now(timezone.utc) +  timedelta(hours=5.5) - timedelta(days=10)).date()
                obj = company_job.objects.filter(date__gte = checkinDate,role__contains = key)
        else:
            if date_posting == 'any':
                if sort_by == 'any':
                    obj = company_job.objects.filter(equity = job_type,role__contains = key).order_by('-date')
                else:
                    obj = company_job.objects.filter(equity = job_type,role__contains = key).order_by('-salary')
            elif date_posting == '0':
                checkinDate=(datetime.now(timezone.utc) +  timedelta(hours=5.5)).date()
                obj = company_job.objects.filter(date = checkinDate,equity = job_type,role__contains = key)
            elif date_posting == '1':
                checkinDate=(datetime.now(timezone.utc) +  timedelta(hours=5.5) - timedelta(days=1)).date()
                obj = company_job.objects.filter(date__gte = checkinDate,equity = job_type,role__contains = key)
            elif date_posting == '2':
                checkinDate=(datetime.now(timezone.utc) +  timedelta(hours=5.5) - timedelta(days=2)).date()
                obj = company_job.objects.filter(date__gte = checkinDate,equity = job_type,role__contains = key)
            elif date_posting == '3':
                checkinDate=(datetime.now(timezone.utc) +  timedelta(hours=5.5) - timedelta(days=3)).date()
                obj = company_job.objects.filter(date__gte = checkinDate,equity = job_type,role__contains = key)
            elif date_posting == '5':
                checkinDate=(datetime.now(timezone.utc) +  timedelta(hours=5.5) - timedelta(days=5)).date()
                obj = company_job.objects.filter(date__gte = checkinDate,equity = job_type,role__contains = key)
            elif date_posting == '10':
                checkinDate=(datetime.now(timezone.utc) +  timedelta(hours=5.5) - timedelta(days=10)).date()
                obj = company_job.objects.filter(date__gte = checkinDate,equity = job_type,role__contains = key)

    print(obj)
    job_count = obj.count()
    
    context = {
        'obj':obj,
        'job_type':job_type,
        'date_posting':date_posting,
        'job_count':job_count,
        'sort_by':sort_by,
        'key':key,
            }
    return render(request, 'job_listing.html', context=context)


def job_view(request,id):
    obj = company_job.objects.get(id = id)
    company = obj.comapny
    person = user_details.objects.get(user = request.user)
    
    context = {
        'obj':obj,
        'company':company,
        'person':person,
            }
    return render(request, 'job_view.html', context=context)



def application_submit(request,company_id,person_id):
    company = company_job.objects.get(id = company_id)
    person = user_details.objects.get(id = person_id)
    try:
        obj = company_job_applications.objects.get(job = company,person = person)
    except:
        obj = company_job_applications(job = company,person = person,name = person.full_name,hire_id = person.id)
    obj.save()
    return HttpResponseRedirect("/resume_show")


def revenue_add(request):
    company_details_to_pass = company_details.objects.get(user = request.user)
    revenue = request.POST.get('revenue')
    month = request.POST.get('month')
    try:
        income = income_company.objects.get(comapny = company_details_to_pass,month_number = month)
        income.value = str(int(income.value) + int(revenue))
        income.save()
    except:
        income = income_company(comapny = company_details_to_pass,month_number = month,value = revenue)
        income.save()
    return HttpResponseRedirect("/company")



def job_posting_done(request):
    company_details_to_pass = company_details.objects.get(user = request.user)
    role = request.POST.get('role')
    description = request.POST.get('description')
    experience = request.POST.get('experience')
    skills = request.POST.get('skills')
    location = request.POST.get('location')
    country = request.POST.get('country')
    salary = request.POST.get('salary')
    free = request.POST.get('free')
    catagory = request.POST.get('catagory')
    obj = company_job(comapny = company_details_to_pass,role = role,experience = experience,description = description,salary = salary,skills = skills,location = location,country = country,equity = free,catagory = catagory)
    obj.save()
    return HttpResponseRedirect("/company")


def search_jobs_keyword(request):
    keyword = request.POST.get('keyword')
    return HttpResponseRedirect("/job_listing_filter/any/any/any/"+str(keyword))
