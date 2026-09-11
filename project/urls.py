from django.contrib import admin
from django.urls import path
from users import views as users_views
from admin import views as admin_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', users_views.register_view, name='register'),
    path('login/', users_views.login_view, name='login'),
    path('profile/', users_views.profile_view, name='profile'),
    path('admin-panel/', admin_views.admin_index, name='admin-panel'),
]