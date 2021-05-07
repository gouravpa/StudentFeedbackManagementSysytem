from django.db import models

# Create your models here.

class UserQuery(models.Model):
    email = models.EmailField(default='')
    name = models.CharField(max_length=100)
    query_desc = models.CharField(max_length=2000)

    def __str__(self):
        return self.email

    
class SignUp(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=30)
    faculty_QA_1 = models.CharField(max_length=5000,default="",blank=True)
    faculty_QA_2 = models.CharField(max_length=5000,default="",blank=True)
    faculty_QA_3 = models.CharField(max_length=5000,default="",blank=True)
    faculty_QA_4 = models.CharField(max_length=5000,default="",blank=True)
    faculty_QA_5 = models.CharField(max_length=5000,default="",blank=True)
    faculty_QA_6 = models.CharField(max_length=5000,default="",blank=True)
    faculty_QA_7 = models.CharField(max_length=5000,default="",blank=True)

    def __str__(self):
        return self.email

class Faculty(models.Model):
    faculty_name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.faculty_name
    

class FacultyQuestion(models.Model):
    que_text = models.CharField(max_length=200)
    faculty = models.ForeignKey(Faculty,on_delete=models.CASCADE)

    def __str__(self):
        return self.que_text[:50] + '...'
    

class FacultyAnswer(models.Model):
    ans_text = models.CharField(max_length=100,default="")
    question = models.ForeignKey(FacultyQuestion,on_delete=models.CASCADE,default=0)
    

    def __str__(self):
        return self.ans_text
    

class CollegeQuestion(models.Model):
    que1 = models.CharField(max_length=200,default="")
    ans1 = models.CharField(max_length=100,blank=True)
    que2 = models.CharField(max_length=200,default="")
    ans2 = models.CharField(max_length=100,blank=True)
    que3 = models.CharField(max_length=200,default="")
    ans3 = models.CharField(max_length=100,blank=True)
    que4 = models.CharField(max_length=200,default="")
    ans4 = models.CharField(max_length=100,blank=True)
    que5 = models.CharField(max_length=200,default="")
    ans5 = models.CharField(max_length=100,blank=True)
    que6 = models.CharField(max_length=200,default="")
    ans6 = models.CharField(max_length=100,blank=True)
    que7 = models.CharField(max_length=200,default="")
    ans7 = models.CharField(max_length=100,blank=True)
    que8 = models.CharField(max_length=200,default="")
    ans8 = models.CharField(max_length=100,blank=True)
    que9 = models.CharField(max_length=200,default="")
    ans9 = models.CharField(max_length=100,blank=True)
    que10 = models.CharField(max_length=200,default="")
    ans10 = models.CharField(max_length=100,blank=True)
    que11 = models.CharField(max_length=200,default="")
    ans11 = models.CharField(max_length=100,blank=True)
    que12 = models.CharField(max_length=200,default="")
    ans12 = models.CharField(max_length=100,blank=True)
    que13 = models.CharField(max_length=200,default="")
    ans13 = models.CharField(max_length=100,blank=True)
    que14 = models.CharField(max_length=200,default="")
    ans14 = models.CharField(max_length=100,blank=True)
    que15 = models.CharField(max_length=200,default="")
    ans15 = models.CharField(max_length=100,blank=True)

    email = models.EmailField(blank=True)

    def __str__(self):
        return self.email


    


    