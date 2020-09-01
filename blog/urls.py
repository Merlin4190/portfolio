from . import views
from django.urls import path

urlpatterns = [
    # path('', views.PostList.as_view(), name='home'),
    path('', views.post_list, name='blog'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('cat/<slug:slug>/', views.category_list, name='category_list'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<slug:slug>/edit/', views.post_edit, name='post_edit'),
    path('post/drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/<slug:slug>/publish/', views.post_publish, name='post_publish'),
    path('post/<slug:slug>/delete/', views.post_delete, name='post_delete'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    # path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]