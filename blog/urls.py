from django.urls import path,include

from . import views

#api end points 
urlpatterns = [
    path('', views.PostList.as_view()),
    path('api-auth/', include('rest_framework.urls')),#drf authentication url
    path('<int:pk>/', views.PostDetail.as_view())
]