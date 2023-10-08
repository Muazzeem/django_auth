from django.urls import path
from .views import CustomUserCreateView, CustomUserLoginView, UserDetailView, CustomUserLogoutView

urlpatterns = [
    path('signup/', CustomUserCreateView.as_view(), name='signup'),
    path('login/', CustomUserLoginView.as_view(), name='login'),
    path("home/", UserDetailView.as_view(), name="home"),
    path('logout/', CustomUserLogoutView.as_view(), name='logout'),
]
