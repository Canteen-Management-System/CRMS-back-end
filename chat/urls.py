# from django.urls import path
# from .views import app_index,room_name

# app_name = 'chat'
# urlpatterns = [
#     path('', app_index, name="index"),
#     path('<str:name>/', room_name, name='room'),

# ]

from django.urls import include, re_path

from chat.api.viewset import ChatList

urlpatterns = [
    re_path(r'^chat/$', ChatList.as_view(), name='chat-get-list'),
    re_path(r'^chat/(?P<from_id>.+)&(?P<to_id>.+)/$', ChatList.as_view(), name='chat-list'),
]