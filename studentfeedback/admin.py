from django.contrib import admin
from .models import UserQuery,SignUp,Faculty,FacultyQuestion,FacultyAnswer,CollegeQuestion


# Register your models here.

class CustFaculty(admin.ModelAdmin):
    list_display = ('id','faculty_name','course')

class CustFacultyQue(admin.ModelAdmin):
    list_display = ('id','que_text','faculty_id')

class CustFacultyAns(admin.ModelAdmin):
    list_display = ('id','ans_text','question_id')
    list_display_links = ('id','ans_text','question_id')

class CustSignUps(admin.ModelAdmin):
    list_display = ['firstname','lastname','email','phone']
    list_display_links = ('firstname','lastname','email','phone')



admin.site.register(UserQuery)
admin.site.register(SignUp,CustSignUps)
admin.site.register(Faculty,CustFaculty)
admin.site.register(FacultyQuestion,CustFacultyQue)
admin.site.register(FacultyAnswer,CustFacultyAns)
admin.site.register(CollegeQuestion)
