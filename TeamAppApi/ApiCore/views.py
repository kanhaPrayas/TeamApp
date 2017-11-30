# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#Modules Imports related to Django starts here
from django.shortcuts import render
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt, csrf_protect, \
	requires_csrf_token, ensure_csrf_cookie
from django.http import HttpResponse, HttpResponseRedirect, \
	HttpResponseNotFound, HttpResponseBadRequest
from django.utils.decorators import method_decorator
from django.db.models import Count
from django.core import serializers
from django.core.exceptions import ValidationError
from django.forms.models import model_to_dict
from rest_framework import generics
#Modules Imports related to Django ends here

#Python System module imports starts here
from datetime import datetime
import json
import inspect
#Python System module imports ends here

#Project related module imports starts here
from TeamAppApi.constants import *
from .models import *
from .serializers import TeamSerializer
#Project related module imports ends here


class Member(View):
	def __init__(self):
		self.response = {}

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
	   return super(Member, self).dispatch(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):

		#Load the member fields to member_data
		try:
			member_data = json.loads(request.body)
		except ValueError,e:
			return HttpResponseBadRequest(json.dumps(INVALID_INPUT_JSON), 
						content_type='application/json')

		#Create a Team object
		member = Team(**member_data)

		#Validate all vields coming for a member
		try:
			member.clean_fields()
		except ValidationError,e:
			#Return 4xx for validation errors
			return HttpResponseBadRequest(json.dumps(e.message_dict), 
						content_type='application/json')
		
		#Save the new member
		member.save()
		return HttpResponse(json.dumps(model_to_dict(member)), 
						content_type='application/json')

	def get(self, request, *args, **kwargs):

		#Delete all keys in the kwargs if the value is None
		kwargs = dict((k, v) for k, v in kwargs.iteritems() if v)


		#Filter team members based on the keys in kwargs
		member_arr = Team.objects.filter(**kwargs)\
							.values('id', 'first_name', 'last_name',\
							'age','role','phone','email','status')\
							.exclude(status=DELETED_STATUS)
		if len(member_arr) == 0:
			return HttpResponseNotFound(json.dumps(NO_MEMBER_ERROR),
							content_type='application/json')

		return HttpResponse(json.dumps(list(member_arr)),
							content_type='application/json')

	def put(self, request, *args, **kwargs):

		#Load the member fields to member_data
		try:
			member_data = json.loads(request.body)
		except ValueError,e:
			return HttpResponseBadRequest(json.dumps(INVALID_INPUT_JSON), 
						content_type='application/json')

		#get the team object
		try:
			member = Team.objects.get(id = kwargs["id"])

		except (Team.DoesNotExist, KeyError, ValueError) as e:
			return HttpResponseBadRequest(json.dumps(INVALID_INPUT_JSON), 
						content_type='application/json')

		#Set all keys with new values
		for (key, value) in member_data.items():
			setattr(member, key, value)

		#Validate all vields coming for a member
		try:
			member.clean_fields()
		except ValidationError,e:
			#Return 4xx for validation errors
			return HttpResponseBadRequest(json.dumps(e.message_dict), 
						content_type='application/json')
		
		#Save the updated member
		member.save()
		return HttpResponse(json.dumps(model_to_dict(member)), 
						content_type='application/json')

	def delete(self, request, *args, **kwargs):

		#Load the member fields to member_data
		try:
			member_data = json.loads(request.body)
		except ValueError,e:
			return HttpResponseBadRequest(json.dumps(INVALID_INPUT_JSON), 
						content_type='application/json')

		#get the team object
		try:
			member = Team.objects.get(id = member_data["id"])

		except (Team.DoesNotExist, KeyError, ValueError) as e:
			return HttpResponseBadRequest(json.dumps(NO_MEMBER_ERROR), 
						content_type='application/json')

		else:
			member.status= -1
			member.save()
		return HttpResponse(json.dumps(self.response), 
						content_type='application/json')

	def serialize_obj(self,obj):
		return dict(obj)

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new member."""
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Team.objects.all()
    serializer_class = TeamSerializer



