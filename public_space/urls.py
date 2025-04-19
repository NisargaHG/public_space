from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.http import HttpResponse  # Add this if not already imported

def home(request):
    return HttpResponse("🚀 Your Django app is live on Render!")

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('space/', include('space.urls')),
    path('', include('space.urls')),  
]
