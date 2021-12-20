from django.shortcuts import render
from django.contrib.auth import get_user_model, authenticate, login

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
    
def signup(request):
    pass

