from django.urls import path
from .views import login_view, signup_view, signout_view
urlpatterns = [
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', signout_view, name='logout')
]