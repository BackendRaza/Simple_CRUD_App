#from django.db.models.fields import EmailField
from django.core.checks import messages
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.hashers import make_password
from .models import *

def index(request):
    userposts = Posts.objects.all()
    return render(request, "index.html", {'post': userposts})
    

def insertView(request):
    return render(request, "st_form.html")

def insert_data(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['umail']
    cont = request.POST['cont']
    #all_data = student.objects.all()
    newuser = student.objects.create(FirstName=fname,LastName=lname,Email=email,Contact=cont)
    # return render(request, "show.html",  {'key': all_data})
    return redirect(showData)

def showData(request):
    all_data = Userr.objects.all()
    return render(request, "show.html", {'key': all_data})

def editData(request, pk):
    get_data = Userr.objects.get(id=pk)
    return render(request, "update.html", {"key1": get_data})

def updateData(request, pk):
    udata = Userr.objects.get(id=pk)
    udata.FirstName = request.POST['fname']
    udata.LastName = request.POST['lname']
    udata.Email = request.POST['umail']
    udata.Contact = request.POST['cont']
    udata.ProfilePic = request.FILES['dp']
    udata.save()
    return redirect(showData)

def deleteData(request, pk):
    deldata = Userr.objects.get(id=pk)
    deldata.delete()
    return redirect(showData)

# Registeration Form with email and password validation

def newreg(request):
    return render(request, "register.html")

def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        umail = request.POST['umail']
        contact = request.POST['cont']
        password = request.POST['pass']
        cpassword = request.POST['cpass']
        profilepic = request.FILES['dp']

        #validate email id if it already exist
        user = Userr.objects.filter(Email=umail)

        if user:
            message = "Email address you entered already exist"
            return render(request, "register.html", {"msg":message})
        else:
            if password == cpassword:
                newuser = Userr.objects.create(FirstName=fname, LastName=lname, Email=umail, Contact=contact, Password=password, ProfilePic=profilepic)
                message = "Registeration successfull"
                return render(request,"index.html", {"msg":message})
            else:
                message = "Both Password Fields doesn't match"
                return render(request, "register.html", {"msg":message})

def loginPage(request):
    return render(request, "login.html")

def loginUser(request):
    if request.method == "POST":
        uemail = request.POST["uemail"]
        upass = request.POST["upass"]

        user = Userr.objects.get(Email=uemail)

        if user:
            if user.Password == upass:
                request.session['FisrtName'] = user.FirstName
                request.session['LastName'] = user.LastName
                request.session['Email'] = user.Email
                request.session['ProfilePic'] = user.ProfilePic.url
                message = "Login Successful!!!"
                # return render(request, "index.html", {'msg': message})
                return redirect(index)
            else:
                message = "Password is incorrect"
                return render(request, "login.html", {'msg': message})
        else:
            message = "This email does not exist!! Please Register"
            return render(request, "login.html", {'msg': message})

def logout(request):
    request.session.clear()
    message = "User Logged out!!!!!!"
    return redirect(index)


# POSTS

# def createPost(request):
#     if request.method == "POST":
