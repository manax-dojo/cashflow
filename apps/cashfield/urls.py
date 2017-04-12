from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^dashboard/$',
        view=views.HomeView.as_view(),
        name='home'
    ),
    ### container
    url(
        regex=r'^container/list/$',
        view=views.ContainerListView.as_view(),
        name='container_list'
    ),
    url(
        regex=r'^container/add/$',
        view=views.ContainerAddView.as_view(),
        name='container_add'
    ),
    url(
        regex=r'^container/(?P<id>[^/]+)/$',
        view=views.ContainerDetailView.as_view(),
        name='container_detail'
    ),
#    url(
#        regex=r'^container/(?P<id>[^/]+)/edit/$',
#        view=views.ContainerUpdateView.as_view(),
#        name='container_update'
#    ),
#    url(
#        regex=r'^container/(?P<id>[^/]+)/delete/$',
#        view=views.ContainerDeleteView.as_view(),
#        name='container_delete'
#    ),
    url(
        regex=r'^container/$',
        view=views.ContainerHomeView.as_view(),
        name='container_home'
    ),
    ### /container
    ### channel
    url(
        regex=r'^channel/list/$',
        view=views.ChannelListView.as_view(),
        name='channel_list'
    ),
    url(
        regex=r'^channel/add/$',
        view=views.ChannelAddView.as_view(),
        name='channel_add'
    ),
    url(
        regex=r'^channel/(?P<id>[^/]+)/$',
        view=views.ChannelDetailView.as_view(),
        name='channel_detail'
    ),
#    url(
#        regex=r'^channel/(?P<id>[^/]+)/edit/$',
#        view=views.ChannelUpdateView.as_view(),
#        name='channel_update'
#    ),
#    url(
#        regex=r'^channel/(?P<id>[^/]+)/delete/$',
#        view=views.ChannelDeleteView.as_view(),
#        name='channel_delete'
#    ),
    url(
        regex=r'^channel/$',
        view=views.ChannelHomeView.as_view(),
        name='channel_home'
    ),
    ### /channel
    ### transfer
    url(
        regex=r'^transfer/list/$',
        view=views.TransferListView.as_view(),
        name='transfer_list'
    ),
    url(
        regex=r'^transfer/add/$',
        view=views.TransferAddView.as_view(),
        name='transfer_add'
    ),
    url(
        regex=r'^transfer/(?P<id>[^/]+)/$',
        view=views.TransferDetailView.as_view(),
        name='transfer_detail'
    ),
#    url(
#        regex=r'^transfer/(?P<id>[^/]+)/edit/$',
#        view=views.TransferUpdateView.as_view(),
#        name='transfer_update'
#    ),
#    url(
#        regex=r'^transfer/(?P<id>[^/]+)/delete/$',
#        view=views.TransferDeleteView.as_view(),
#        name='transfer_delete'
#    ),
    url(
        regex=r'^transfer/$',
        view=views.TransferHomeView.as_view(),
        name='transfer_home'
    ),
    ### /transfer
]
