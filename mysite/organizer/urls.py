from django.conf.urls import url


urlpatterns = [
    url(r'^user/(?P<username>[-\w]+)/$', 'organizer.views.list_user',
        name='organizer_list_user'),
    url(r'^create/$', 'organizer.views.list_create',
        name='organizer_list_create'),
    url(r'^edit/(?P<pk_link>\d+)/(?P<pk_list>\d+)/$', 'organizer.views.link_edit',
        name='organizer_link_edit'),
    url(r'^delete/(?P<pk_link>\d+)/(?P<pk_list>\d+)/$', 'organizer.views.link_delete',
        name='organizer_link_delete'),
    url(r'^link_add/(?P<pk>\d+)/$', 'organizer.views.link_add',
        name='organizer_link_add'),
    url(r'^$', 'organizer.views.lists_all', name='organizer_lists_all'),
    url(r'^list/(?P<list_id>\d+)/$', 'organizer.views.list_details', 
    	name='organizer_list_details'),
    url(r'^edit_list/(?P<pk_list>\d+)/$', 'organizer.views.list_edit',
        name='organizer_list_edit'),
]