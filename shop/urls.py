from django.conf.urls import url
from django.urls import path
#from django.contrib.auth import views as auth_views
#from django.contrib.auth.views import logout, password_change as pwd_change, password_change_done as pwd_change_done, password_reset as reset, password_reset_done as reset_done, password_reset_confirm as reset_confirm, password_reset_complete as reset_complete
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.urls import path
from . import views


app_name = 'shop'

urlpatterns = [
    #url(r'^logout/$', logout, name='logout'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    url(r'^register/$', views.register, name='register'),

    path('password_change/', auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('shop:password_change_done')), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(success_url=reverse_lazy('shop:password_reset_done')), {'email_template_name': 'registration/password_reset_email.html'}, name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('shop:password_reset_complete')), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    #url(r'^register_done/$', views., name='register'),
    # change password urls
    #url(r'^password-change/$', pwd_change, name='password_change'),
    #url(r'^password-change/done/$', pwd_change_done, name='password_change_done'),
    #url(r'^password-change/$', pwd_change, {'post_change_redirect': '/password-change/done/'}, name='password_change'),
# restore password urls
    #url(r'^password-reset/complete/$', reset_complete, name='password_reset_complete'),
    #url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', reset_confirm, {'post_reset_redirect': '/password-reset/complete/'}, name='password_reset_confirm'),
    #url(r'^password-reset/done/$', reset_done, name='password_reset_done'),
    #url(r'^password-reset/$', reset, {'post_reset_redirect': '/password-reset/done/', 'email_template_name': 'registration/password_reset_email.html'}, name='password_reset'),
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list,
         name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail,
         name='product_detail'),
    path('about', views.about, name='about'),
    path('deals', views.deals, name='deals'),
    path('contact', views.contact, name='contact'),
]