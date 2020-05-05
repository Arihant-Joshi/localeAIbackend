from rest_framework import serializers
from locations_crud.models import Locations

class LocSerializer(serializers.ModelSerializer):
	class Meta:
		model = Locations
		fields = "__all__"

class LocSerializerOptional(serializers.ModelSerializer):
	booking_id = serializers.IntegerField(required=False)
	user_id = serializers.IntegerField(required=False)
	vehicle_model_id = serializers.IntegerField(required=False)
	package_id = serializers.FloatField(required=False)
	travel_type_id = serializers.IntegerField(required=False)
	from_area_id = serializers.FloatField(required=False)
	to_area_id = serializers.FloatField(required=False)
	from_city_id = serializers.FloatField(required=False)
	to_city_id = serializers.FloatField(required=False)
	from_date = serializers.DateTimeField(required=False)
	to_date = serializers.DateTimeField(required=False)
	online_booking = serializers.IntegerField(required=False)
	mobile_site_booking = serializers.IntegerField(required=False)
	booking_created = serializers.DateTimeField(required=False)
	from_lat = serializers.FloatField(required=False)
	from_long = serializers.FloatField(required=False)
	to_lat = serializers.FloatField(required=False)
	to_from_long = serializers.FloatField(required=False)
	Car_Cancellation = serializers.IntegerField(required=False)
	class Meta:
		model = Locations
		#fields = ("booking_id","user_id","vehicle_model_id","package_id","travel_type_id","from_area_id","to_area_id","from_city_id","to_city_id","from_date","to_date","online_booking","mobile_site_booking","booking_created","from_lat","from_long","to_lat","to_from_long","Car_Cancellation")
		fields = "__all__"