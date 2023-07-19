from django.urls import path
from .views import (
    BlogDetailView,
    IndexView,
    CategoryView,
    CommentCreate,
    NewBlogView
)


app_name = 'blog'

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('new/', NewBlogView.as_view(), name='new'),
    path('detail/<int:pk>/', BlogDetailView.as_view(), name='detail'),
    path('category/<str:category>/', CategoryView.as_view(), name='category'),
    path('comment/create/<int:pk>', CommentCreate.as_view(), name='comment_create')
]
