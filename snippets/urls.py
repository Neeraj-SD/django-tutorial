from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'snippets', views.SnippetViewSet, basename='snippet')

# urlpatterns = [
#     path('', views.api_root),
#     path('snippets/', views.SnippetListG.as_view(), name='snippet-list'),
#     path('snippets/<int:pk>/', views.SnippetDetailG.as_view(), name='snippet-detail',),
#     path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name='snippet-highlight'),
#     path('users/', views.UserList.as_view(), name='user-list'),
#     path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
# ]

urlpatterns = [
    path('', include(router.urls)) 
    ]

# urlpatterns = format_suffix_patterns(urlpatterns)