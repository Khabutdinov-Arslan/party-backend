from django.urls import path
from .views import *

urlpatterns = [
	path('hello/', HelloView.as_view()),
	path('events/', EventList.as_view()),
	path('event/<id>/', EventDescription.as_view()),
	path('users/create/', CreateUser.as_view()),
	path('events/create/', CreateEvent.as_view())
	#path('create/', PostCreate.as_view()),
	#path('get_all/', PostList.as_view()),
	#path('drop/<int:pk>', PostDrop.as_view()),
]