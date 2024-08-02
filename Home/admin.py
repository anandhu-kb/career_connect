from django.contrib import admin
from .models import RecruiterData
from careers.models import *
from Home.models import *

# Register your models here.
admin.site.register(RecruiterData)


admin.site.register(Joblist)
admin.site.register(Jobapplication)
admin.site.register(InterViewSchedule)

admin.site.register(Education)
admin.site.register(Experiance)
admin.site.register(StudentProfile)
admin.site.register(ResumeWritingTips)

