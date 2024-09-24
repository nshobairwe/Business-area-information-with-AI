from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),  # Changed to the root URL
    path('register/', views.registerPage, name='reg'),  # Changed URL name for registration
    path('loginpage/', views.loginPage, name='log'),  # Changed URL name for login
    path('dashboard/', views.dashboardU, name='dash'),  # Changed URL name for dashboard
    path('logout/', views.logoutUser, name='logout'),  # Changed URL name for logout
    path('submit_comment/', views.submit_comment, name='submit_comment'),

    # You had a typo in 'password_reset_done'
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="forgetpass.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_send.html"), name="password_reset_done"),  # Corrected 'passwrord_reset_done' to 'password_reset_done'
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="pass_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="pass_reset_done.html"), name="password_reset_complete"),
]
