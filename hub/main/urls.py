from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('loc', views.locations, name='location'),
    path('reg_event', views.created_event, name='reg_event'),
    path('loc/<int:location_id>/', views.get_location, name='loc_get'),
    path('loc/<int:location_id>/edit', views.edit_loc, name='loc_edit'),
    path('coment', views.show_coment, name='coment'),
    path('coment/add_comet', views.create_comment, name='add_coment'),

]