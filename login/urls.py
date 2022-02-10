from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('',views.login, name='login'),
    path('token/',views.GetToken.as_view(), name='token'),
    path('register/',views.register, name='register'),
    path('logout/',LogoutView.as_view(template_name='logout.html'), name='logout'),
] 