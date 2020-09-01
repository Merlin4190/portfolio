from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
# from my_portfolio.views import GeneratePdf

urlpatterns = [
    # path('', views.PostList.as_view(), name='home'),
    path('', views.index, name='index'),
    
    path('users/register', views.register, name='register'),
    path('users/login/', views.login, name='login'),
    path('users/signup/', views.signup, name='signup'),
    path('users/signin/', views.signin, name='signin'),
    path('users/logout', views.logout, name='logout'),
    path('users/update', views.update_account, name='update_account'),
    path('users/change_password', auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html', success_url='/'), name='password_change'),
    path('users/reset_password', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name='password_reset'),
    path('users/reset_password/done', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('users/reset_password/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('users/reset_password/complete', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),

    path('new/profile_form/', views.profile_form, name='profile_form'),
    path('profile/all/', views.all_profiles, name='all_profiles'),
    path('profile/<slug:slug>/<int:pk>', views.view_profile, name='view_profile'),
    path('profile/download/<slug:slug>/<int:pk>', views.download_cv, name='download_cv'),
    # path('profile/download', GeneratePdf.as_view(), name='download_pdf'),
    path('profile/<slug:slug>/<int:pk>/edit/', views.edit_profile, name='edit_profile'),
    path('post/<slug:slug>/<int:pk>/delete/', views.delete_profile, name='delete_profile'),
    # path("profile/search/", views.search, name="search_results"),
    path("profile/search/", views.searchposts, name="searchposts"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)