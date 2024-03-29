from django.urls import path
from users import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView

app_name = 'users'

urlpatterns = [
    path('login/',views.UserLoginView.as_view(), name = 'login'),
    path('registration/',views.UserRegistartionView.as_view(), name = 'registration'),
    path('profile/<int:pk>/', login_required(views.UserProfileView.as_view()), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout')

]
