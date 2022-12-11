from django.urls import include, path
from django.conf.urls import url

from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.cache import cache_page
urlpatterns = [
    path('',views.landingpage, name='landingpage'),
    path('blog',views.blog, name='blog'),
    path('blog_single',views.blog_single, name='blog'),
    path('login_incubator',views.login_incubator, name='login_incubator'),
    path('register',views.register, name='register'),
    path('register_user',views.register_user, name='register_user'),
    path('details_fill',views.details_fill, name='details_fill'),
    
    path('demo',views.demo, name='demo'),
    path('resume_show',views.resume_show, name='resume_show'),
    path('skill_new_add',views.skill_new_add, name='skill_new_add'),   
    path('skill_education_done',views.skill_education_done, name='skill_education_done'),
    path('skill_experience_done',views.skill_experience_done, name='skill_experience_done'),
    path('add_work_extra',views.add_work_extra, name='add_work_extra'),   

    path('company',views.company, name='company'),

    path('person_show/<str:id>',views.person_show, name='person_show'),   
    
    path('job_show/<str:id>/<str:exp>',views.job_show, name='job_show'),
    
    path('job_delete/<str:id>',views.job_delete, name='job_delete'),   
    

    path('hiring_done/<str:company_id>/<str:person_id>',views.hiring_done, name='hiring_done'),   
    
    path('person_search',views.person_search, name='person_search'),

    path('person_search_show/<str:skill_req>/<str:exp>/<str:free>',views.person_search_show, name='person_search_show'), 
    
    path('logout_user',views.logout_user, name='logout_user'), 

    path('register_company',views.register_company, name='register_company'), 

    path('thanks_registration',views.thanks_registration, name='thanks_registration'), 
    
    path('search_jobs',views.search_jobs, name='search_jobs'), 

    path('job_listing',views.job_listing, name='job_listing'),

    path('job_listing_filter/<str:job>/<str:date>/<str:sort>/<str:search_key>',views.job_listing_filter, name='job_listing_filter'),

    path('job_view/<str:id>',views.job_view, name='job_view'),   
    
    path('application_submit/<str:company_id>/<str:person_id>',views.application_submit, name='application_submit'),   
    
    path('revenue_add',views.revenue_add, name='revenue_add'),
    
    path('job_posting_done',views.job_posting_done, name='job_posting_done'),

    
    
    path('search_jobs_keyword',views.search_jobs_keyword, name='search_jobs_keyword'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
