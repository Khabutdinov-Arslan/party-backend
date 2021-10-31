from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *


class HelloView(APIView):
	permission_classes = [IsAuthenticated]

	def get(self, request):
		content = {'user': request.user.id}
		return Response(content)

class EventList(generics.ListAPIView):
	serializer_class = EventSerializer
	queryset = Event.objects.all()

class EventDescription(generics.ListAPIView):
	serializer_class = EventSerializer

	def get_queryset(self):
		event_id = self.kwargs.get("id");
		queryset = Event.objects.filter(id=event_id)
		return queryset

class CreateUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CreateEvent(generics.CreateAPIView):
	queryset = Event.objects.all()
	serializer_class = EventSerializer
	#permission_classes = [IsAuthenticated]

	def get(self, request):
		return Response(request)
