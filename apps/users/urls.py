from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.UserListView.as_view(),
        name='list'
    ),
    url(
        regex=r'^login/$', 
        view=views.login, 
        name='account_login' 
    ), 
    url( 
        regex=r'^logout/$', 
        view=views.logout, 
        name='account_logout' 
    ), 
    url( 
        regex=r'^signup/$', 
        view=views.signup, 
        name='account_signup' 
    ), 
    url( 
        regex=r'^~redirect/$',
        view=views.UserRedirectView.as_view(),
        name='redirect'
    ),
    url(
        regex=r'^(?P<username>[\w.@+-]+)/$',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),
    url(
        regex=r'^~update/$',
        view=views.UserUpdateView.as_view(),
        name='update'
    ),
]
