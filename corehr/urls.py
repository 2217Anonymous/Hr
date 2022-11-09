"""corehr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from cgitb import handler
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from corehr import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',views.index,name="index"),
    path('accounts/',include("authentication.urls")),
    path('hr-dashboard/',include("admin.urls")),
    path('master/',include('master.urls')),
    path('settings/',include('settings.urls')),
    path('employee/',include('employees.urls')),

    path('__debug__/', include('debug_toolbar.urls')),

    path('api/', include('api.urls')),
    path('auth-api/', include('rest_framework.urls')),

    path('api/token/',TokenObtainPairView.as_view()),
    path('api/token/refresh/',TokenRefreshView.as_view()),
]
handler404 = 'authentication.views.error_404' 
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


