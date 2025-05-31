from django.urls import path
from .views import HomeListVeiw,PostDetailVeiw,PostCreateView
urlpatterns = [
    path('',HomeListVeiw.as_view(),name='home'),
    path('post/<int:pk>',PostDetailVeiw.as_view(),name='post_detail'),
    path('post/new/' , PostCreateView.as_view(), name='post_new')
]