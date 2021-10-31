from rest_framework import serializers
from .models import *

class EventSerializer(serializers.ModelSerializer):
	class Meta:
		model = Event
		fields = '__all__'

	def create(self, validated_data):
		event = super(EventSerializer, self).create(validated_data)
		event.save()
		return event

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username', 'password', 'surname', 'name', 'patronymic', 'department','course')

	def create(self, validated_data):
		user = super(UserSerializer, self).create(validated_data)
		user.set_password(validated_data['password'])
		user.save()
		return user