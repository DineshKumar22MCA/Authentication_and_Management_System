from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.hashers import check_password,make_password
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import BasePasswordHasher

from .models import *


def index(request):
        try:
            return render(request,"index.html")
        except Exception as e:
            return HttpResponse({str(e)})
        

def signup(request):
    try:
        if request.method=="POST":
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email_id = request.POST.get('email_id')
            user_name = request.POST.get('user_name')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            
            try:
                if password == confirm_password:
                    password = make_password(password)
                    Admin.objects.create(first_name=first_name,last_name=last_name,
                                            email_id=email_id,user_name=user_name,
                                            password=password)
                    messages.success(request,"your account has been created successfully")
                    return redirect('index')
                else:
                    messages.error(request,"password didn't matching")
                    redirect('signup')
            except IntegrityError as e:
                 messages.error(request,"user name already exist ")
                 return redirect('signup')
            except Exception as e :
                 return HttpResponse({str(e)})
            
        else:
            return render(request,"signup.html")
        
    except Exception as e:
          messages.error(request, "Something went wrong. Please try again!")
          return redirect('index')





def signin(request):
    try:
        if request.method == "POST":
            user_name = request.POST.get('user_name')
            password = request.POST.get('password')
            try:
                admin = Admin.objects.get(user_name=user_name)
                if user_name==admin.user_name and check_password(password, admin.password):
                    global first_name
                    first_name = admin.first_name
                    return redirect("home")
                else:
                    messages.error(request, "Invalid username or password")
                    return redirect('signin')
            except Admin.DoesNotExist:
                messages.error(request, "Invalid username or password")
                return redirect('signin')
            except Exception as e:
                messages.error(request, "An error occurred while signing in")
                print(e)
                return redirect('signin')
        else:
            return render(request, "signin.html")
        
    except Exception as e:
        messages.error(request, "Something went wrong. Please try again!")
        return redirect('index')

    

def reset_password(request):
    try:
        print(1)
        if request.method=="POST":
            print(2)
            user_name = request.POST.get('user_name')
            old_password = request.POST.get('old_password')
            new_password = request.POST.get('new_password')
            password = make_password(new_password)
            admin = Admin.objects.get(user_name=user_name)
            if admin.user_name == user_name and check_password(old_password,admin.password):
                admin.password = password
                admin.save()
                messages.success(request,"password reset successfully")
                return redirect("signin")
            else:
                messages.error(request,"password mismatch")
                return redirect("reset_password")

        return render(request,"reset_password.html")
    except Exception as e :
        print(e)
        messages.error(request,"str(e)")
        return redirect('reset_password')




def home(request):
    try:
        all_data = User.objects.all()
        admin = first_name
        print(first_name)
        print(admin)
        return render(request,"home.html",{"admin":admin,"all_data":all_data})
    except Exception as e :
        print(e)
        messages.error(request,"something went wrong.please try again!.")
        return redirect("signin")


def insert(request):
    try:
        if request.method == "POST":
            name = request.POST.get('name')
            age = request.POST.get('age')
            city = request.POST.get('city')
            admin = first_name

            user = User(name=name,age=age,city=city,admin=admin)
            user.save()

            if user:
                messages.success(request,"user created successfully")
                return redirect('home')
            else:
                messages.error(request,"user not created ,please try again!.")
                return redirect('insert')
            
        else:
            return render(request,"insert.html")
    except Exception as e:
        messages.error(request,"something went wrong.please try again!.")
        return redirect("home")
    


def edit(request,id):
    try:
        user = User.objects.get(id=id)
        if request.method=="POST":
            user = User.objects.get(id=id)
            name = request.POST.get('name')
            age = request.POST.get('age')
            city = request.POST.get('city')
            if user:
                user.name = name
                user.age = age
                user.city = city
                user.save()
                messages.success(request,"user data updated")
                return redirect("home")
            else:
                messages.error(request,"user doesn't exist")
                return redirect('home')
        else:
            return render(request,"edit.html",{"user":user})
    except Exception as e:
        messages.error(request,"something went wrong.please try again!.")
        return redirect("home")



def delete(request,id):
    try:
        user = User.objects.get(id=id)

        if user:
            user.delete()
            messages.success(request,"user deleted successfully")
            return redirect('home')
        else:
            messages.error(request,"user does not exist")
            return redirect('home')
        
    except Exception as e:
        messages.error(request,"something went wrong.please try again!.")
        return redirect("home")



def signout(request):
    try:
        logout(request)
        messages.success(request, "Logged Out Successfully!!")
        return redirect('index')
    except Exception as e :
        print(e)
        messages.error(request,"Logged Out Successfully!! ")
        return redirect('index')