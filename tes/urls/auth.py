from django.urls import path
from api.views.auth.login import login_api
from api.views.auth.register import register_api
from api.views.auth.logout import logout_api
from api.views.auth.reset import password_reset_request, password_reset_confirm

urlpatterns = [
    path('login/', login_api, name='login_api'),
    path('logout/', logout_api, name='logout_api'),
    path('register/', register_api, name='register_api'),
    path('password-reset/', password_reset_request, name='password_reset_request'),
    path('password-reset/confirm/', password_reset_confirm, name='password_reset_confirm')
]
