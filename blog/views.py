from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from .forms import UserRegistrationForm, LoginForm, BlogForm, UserForm, AdminForm, ChangePasswordForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from .models import BlogPost
import random
num = random.randrange(1,9)
num1 = random.randrange(1,9)
global str_num 
ab = num+num1
str_num = str(ab)
print(ab)
# Home
def home(request):
    db = BlogPost.objects.all()
    return render(request,'blog/home.html',{'data':db})

#ABout page
def about(request):
    return render(request,'blog/about.html')


#contact page
def contact(request):
    return render(request,'blog/contact.html')

#dashboard page
def dash(request):
    if request.user.is_authenticated:
        db = BlogPost.objects.filter(user=request.user)
        names = request.user.get_full_name()
        return render(request,'blog/dashboard.html',{'datas':db,'name':names})
    else:
        return HttpResponseRedirect('/login')
#login page

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = LoginForm(request, request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                captha = request.POST.get('captha')
                print(str(captha))
                if str_num == str(captha):
                    user = authenticate(username=uname, password=upass)
                    if user is not None:
                        login(request, user)
                        messages.success(request,'You Have Successfuly Login!!!!')
                        return HttpResponseRedirect('/profile')
                else:
                    return HttpResponse("<h4> Invalid Captha</h4>")
                
        else:
            print(type(ab))
            print(type(str_num))
            fm = LoginForm()
        return render(request,'blog/login.html',{'form':fm,'capt':num,'cap1':num1})
    else:
        return HttpResponseRedirect('/dashboard')

#logout page
def usr_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

#signup page
def user_signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = UserRegistrationForm(request.POST)
            if fm.is_valid():
                user = fm.save()
                group =Group.objects.get(name='Auther')
                user.groups.add(group)
                messages.info(request,'Your Account Has Been Created')
        else:
            fm = UserRegistrationForm()
        return render(request,'blog/signup.html',{'form':fm })
    else:
        return HttpResponseRedirect('/dashboard')

#add blog function
def add_post(request):
    if request.user.is_authenticated:
        if  request.method == 'POST':
            fm = BlogForm(request.POST)
            if fm.is_valid():
                de = fm.cleaned_data['desc']
                db = BlogPost(user=request.user,desc=de)
                db.save()
                messages.success(request,'Your Blog has been Created!!!!!')
                fm = BlogForm()
        else:
            fm = BlogForm()
        return render(request,'blog/addpost.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login')


#uodate execting blog
def update_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            db = BlogPost.objects.get(pk=id)
            fm = BlogForm(request.POST,instance=db)
            if fm.is_valid():
                
                fm.save()
                messages.info(request,'Your Response has been save')
        else:
            db = BlogPost.objects.get(pk=id)
            fm = BlogForm(instance=db)
        return render(request,'blog/updatepost.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login')

#delete blog
def delete_post(request, id):
    if request.user.is_authenticated:
        db = BlogPost.objects.get(pk=id)
        db.delete()
        return HttpResponseRedirect('/dashboard')
    else:
        return HttpResponseRedirect('/login')

def changeform(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.user.is_superuser == True:
                fm = AdminForm(instance=request.user,data=request.POST)
            else:
                fm = UserForm(instance=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
        else:
            if request.user.is_superuser == True:
                fm = AdminForm(instance=request.user)
            else:
                fm = UserForm(instance=request.user)
        return render(request,'blog/profile.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login')

def passchange(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = ChangePasswordForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request,'Your Password Has Been Reset!!!!!!!!!!')
                return HttpResponseRedirect('/login')
        else:
            fm = ChangePasswordForm(request.user)
        return render(request,'blog/changepass.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login')