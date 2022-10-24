"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from tutorial.quickstart import views
from rest_framework import routers
from rest_framework.authtoken import views
from tutorial.views import GoogleLogin
from rest_framework_simplejwt.views import TokenVerifyView

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)
# router.register(r'snippets', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('', include(router.urls)),
    path('', include('snippets.urls')),
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', views.obtain_auth_token),
    path('token/verify', TokenVerifyView.as_view()),
    path('auth/google/', GoogleLogin.as_view(), name='google_login'),
    path('__debug__/', include('debug_toolbar.urls')),
    # path(r'^accounts/', include('allauth.urls'), name='socialaccount_signup'),
]
