from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from locations_crud.serialization import *

class LocationsAPI(APIView):
	def get(self,request):
		model = Locations.objects.all()
		serializer = LocSerializer(model,many = True)
		return Response(serializer.data)

	def post(self,request):
		serializer = LocSerializer(data = request.data)
		if(serializer.is_valid()):
			serializer.save()
			return Response(serializer.data,status.HTTP_201_CREATED)
		return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)

	#def put(self,request):
class LocationsAPIDetails(APIView):
	def get_by_id(self,booking_id):
		model = None
		try:
			model = Locations.objects.get(booking_id=booking_id)
		except Locations.DoesNotExist:
			pass
		return model

	def get(self,request,booking_id):
		model = self.get_by_id(booking_id)
		if(model == None):
			return Response(f"BOOKING ID '{booking_id}' NOT FOUND",status.HTTP_404_NOT_FOUND)
		serializer = LocSerializer(model)
		return Response(serializer.data)

	def put(self,request,booking_id):
		model = self.get_by_id(booking_id)
		if(model == None):
			return Response(f"BOOKING ID '{booking_id}' NOT FOUND",status.HTTP_404_NOT_FOUND)
		if("booking_id" in request.data):
			request.data["booking_id"] = booking_id
		serializer = LocSerializerOptional(model,data = request.data)
		if(serializer.is_valid()):
			#return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
			serializer.save()
			return Response(serializer.data,status.HTTP_201_CREATED)
		return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)

	def delete(self,request,booking_id):
		model = self.get_by_id(booking_id)
		if(model == None):
			return Response(f"BOOKING ID '{booking_id}' NOT FOUND",status.HTTP_404_NOT_FOUND)
		model.delete()
		return Response(status.HTTP_204_NO_CONTENT)

class UserAuthAPI(ObtainAuthToken):
#class UserAuthAPI(APIView):
	def post(self,request,*args,**kwargs):
		serializer = self.serializer_class(data=request.data,
			context={'request': request})
		serializer.is_valid(raise_exception=True)
		user = serializer.validated_data['user']
		token, created = Token.objects.get_or_create(user=user)
		return Response(token.key)