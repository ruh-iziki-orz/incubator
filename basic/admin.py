from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(details_check)
admin.site.register(user_details)
admin.site.register(user_details_education)
admin.site.register(user_details_work)
admin.site.register(user_details_testimonial)
admin.site.register(user_details_social)
admin.site.register(user_details_skills)
admin.site.register(user_details_project)


admin.site.register(company_job_applications)
admin.site.register(company_job)
admin.site.register(company_hired)
admin.site.register(income_company)
admin.site.register(company_details)

admin.site.register(company_or_employee)
