from django.shortcuts import render
from django.contrib.auth import get_user_model, authenticate, login
import re

User = get_user_model()
# Create your views here.
def login_view(request):
    if request.method == "GET":
        return render(request, 'accounts/login.html')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            return render(request, 'accounts/login.html', {'msgs':['Error! Username and Password do not match.']})
        login(request, user)
        return render(request, 'accounts/login.html', {'msgs':['Success! You have now logged in as '+username]})
        # change to redirect ^
    
def signup_view(request):
    if request.method == "GET":
        return render(request, 'accounts/register.html')
    if request.method == "POST":
        username = request.POST["username"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        pw1 =  request.POST["password1"]
        pw2 =  request.POST["password2"]
        msgs = []
        same_username = User.objects.filter(username=username)
        same_email = User.objects.filter(email=email)
        regex = re.compile('[-@!#$%^&*()<>?/\|}{~:\'" ]')
        if pw1 != pw2:
            msgs.append("Error! Passwords do not match. ")
        elif len(pw1) < 7:
            msgs.append("Error! Password too short. ")
        if len(same_username) > 0:
            msgs.append("Error! Username Taken. ")
        elif regex.search(username) != None:
            msgs.append("Error! Invalid username. ") 
        if len(same_email) > 0:
            msgs.append("Error! Email Taken. ")
        if len(msgs) == 0:  #If no errors uptil this point, check for edge cases:
            if username=="settings" or username=="requests" or username=="activity" or username=="search" or username=="manage_req":
                msgs.append("Error! Invalid username.")
        if len(msgs) > 0:
            return render(request, 'accounts/register.html', {'msgs': msgs})

        user = User.objects.create_user(username=username, password=pw1, email=email, last_name=last_name, first_name=first_name)
        user.save()
        return render(request, 'accounts/register.html', {'msgs':['Success! Please proceed to login']})

