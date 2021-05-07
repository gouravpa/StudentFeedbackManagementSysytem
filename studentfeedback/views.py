from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect,get_object_or_404
from studentfeedback.models import UserQuery,SignUp,FacultyAnswer,CollegeQuestion,Faculty,FacultyQuestion
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'index.html')

def signup(request):
    if request.method == "POST":
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        try:
            signup = get_object_or_404(SignUp,email=email)
            if email == signup.email:
                messages.error(request,'This email is already registered!')
                return redirect('signup')
        except Exception as e:
            print(e)
            SignUp(firstname=firstname,lastname=lastname,email=email,phone=phone,password=password).save()
            messages.success(request,"Your account created successfully!")
            print('bye')
            return redirect('login')
    return render(request,"signup.html")

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        print(email)
        password = request.POST.get('password')
        print(password)
        try:
            signup = SignUp.objects.get(email=email)
            print(signup.email)
            print(signup.password)
            if password == signup.password:
                request.session['fullname'] = signup.firstname + ' ' + signup.lastname
                request.session['email'] = signup.email
                name = request.session.get('fullname')
                print(name)
                print(signup.password)
                return redirect('profile')
            else:
                messages.error(request,'Wrong Password!')
                return redirect('login')
        except Exception as e:
            messages.error(request,'we are not able to find this email! please register first.')
            return redirect('login')
    return render(request,'login.html')

def profile(request):
    name = request.session.get('fullname')
    return render(request,'profile.html',{'name':name})

def logout(request):
    request.session.flush()
    messages.success(request,'You are logged out!')
    return redirect('login')

def copyprofile(request):
    faculty = Faculty.objects.all()
    name = request.session.get('fullname')
    return render(request,'copyprofile.html',{'faculty':faculty,'name':name})

def facultyform(request,id):
    faculty = Faculty.objects.get(id=id)
    facultyquestion = faculty.facultyquestion_set.all()
    email = request.session.get('email')
    if request.method == "POST":
        que_list=[]
        ans_list=[]
        for i in range(1,70):
            i = str(i)
            que = request.POST.get('q'+i,"")
            ans = request.POST.get('fans'+i,"")
            que_list.append(que)
            ans_list.append(ans)
        print(que_list)
        print(ans_list)
        x = dict(zip(que_list,ans_list))
        y = faculty.faculty_name + ', course : ' + faculty.course
        mydict = {}
        mydict[y] = x
        fac = SignUp.objects.get(email=email)
        print(email)
        print(fac.faculty_QA_1)
        
        if faculty.faculty_name == 'Mr. Sunil Kushwah' and fac.faculty_QA_1=="":
            msg = messages.success(request,f'Your feedback for {faculty.faculty_name} is submitted successfully.')
            SignUp.objects.filter(email=email).update(faculty_QA_1=mydict)
            return redirect('profile')
        if faculty.faculty_name == 'Ms Priyanka D' and fac.faculty_QA_2=="":
            msg = messages.success(request,f'Your feedback for {faculty.faculty_name} is submitted successfully.')
            SignUp.objects.filter(email=email).update(faculty_QA_2=mydict)
            return redirect('profile')
        if faculty.faculty_name == 'Ms Swati Tahiliani' and fac.faculty_QA_3=="":
            msg = messages.success(request,f'Your feedback for {faculty.faculty_name} is submitted successfully.')
            SignUp.objects.filter(email=email).update(faculty_QA_3=mydict)
            return redirect('profile')
        if faculty.faculty_name == 'Ms Anusha Jain' and fac.faculty_QA_4=="":
            msg = messages.success(request,f'Your feedback is {faculty.faculty_name} submitted successfully.')
            SignUp.objects.filter(email=email).update(faculty_QA_4=mydict)
            return redirect('profile')
        if faculty.faculty_name == 'Mr. Suresh Jain' and fac.faculty_QA_5=="":
            msg = messages.success(request,f'Your feedback for {faculty.faculty_name} is submitted successfully.')
            SignUp.objects.filter(email=email).update(faculty_QA_5=mydict)
            return redirect('profile')
        if faculty.faculty_name == 'Mr. Hitesh Kaag' and fac.faculty_QA_6=="":
            msg = messages.success(request,f'Your feedback for {faculty.faculty_name} is submitted successfully.')
            SignUp.objects.filter(email=email).update(faculty_QA_6=mydict)
            return redirect('profile')
        if faculty.faculty_name == 'Mr. Saurabh Dave' and fac.faculty_QA_7=="":
            msg = messages.success(request,f'Your feedback for {faculty.faculty_name} is submitted successfully.')
            SignUp.objects.filter(email=email).update(faculty_QA_7=mydict)
            return redirect('profile')
        msg = messages.error(request,f'You have already filled the form for {faculty.faculty_name}')
        return redirect('profile')
        
        
        return redirect('profile')
    return render(request,'facultyquestions.html',{'id':id,'faculty':faculty,'facultyquestion':facultyquestion})

def collegeform(request):
    email = request.session.get('email')
    if request.method == "POST":    
        q1 = request.POST.get('q1')
        q2 = request.POST.get('q2')
        q3 = request.POST.get('q3')
        q4 = request.POST.get('q4')
        q5 = request.POST.get('q5')
        q6 = request.POST.get('q6')
        q7 = request.POST.get('q7')
        q8 = request.POST.get('q8')
        q9 = request.POST.get('q9')
        q10 = request.POST.get('q10')
        q11 = request.POST.get('q11')
        q12 = request.POST.get('q12')
        q13 = request.POST.get('q13')
        q14 = request.POST.get('q14')
        q15 = request.POST.get('q15')

        a1 = request.POST.get('facq1')
        a2 = request.POST.get('facq2')
        a3 = request.POST.get('facq3')
        a4 = request.POST.get('facq4')
        a5 = request.POST.get('facq5')
        a6 = request.POST.get('facq6')
        a7 = request.POST.get('facq7')
        a8 = request.POST.get('facq8')
        a9 = request.POST.get('facq9')
        a10 = request.POST.get('facq10')
        a11 = request.POST.get('facq11')
        a12 = request.POST.get('facq12')
        a13 = request.POST.get('facq13')
        a14 = request.POST.get('facq14')
        a15 = request.POST.get('facq15')
        try : 
            CollegeQuestion.objects.get(email=email)
            messages.error(request,"You have already filled form!")
            return redirect('collegeform')
        except Exception as e:
            collegequeans = CollegeQuestion(email=email,que1=q1,que2=q2,que3=q3,que4=q4,que5=q5,que6=q6,que7=q7,que8=q8,que9=q9,que10=q10,que11=q11,que12=q12,que13=q13,que14=q14,que15=q15,ans1=a1,ans2=a2,ans3=a3,ans4=a4,ans5=a5,ans6=a6,ans7=a7,ans8=a8,ans9=a9,ans10=a10,ans11=a11,ans12=a12,ans13=a13,ans14=a14,ans15=a15)
            collegequeans.save()
            messages.success(request,"Thankyou for fill feedback form!")
            return redirect('collegeform')
    return render(request,'collegeform.html')

def contactus(request):
    if request.method == "POST":
        email = request.POST.get('email')
        name = request.POST.get('name')
        comment = request.POST.get('comment')
        UserQuery(name=name,email=email,query_desc=comment).save()
        return redirect('profile')
    return render(request,'contactus.html')

