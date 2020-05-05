from django.db import models

# Create your models here.
class Locations(models.Model):
	booking_id = models.IntegerField(unique = True)
	user_id = models.IntegerField()
	vehicle_model_id = models.IntegerField()
	package_id = models.FloatField(blank=True,null=True)
	travel_type_id = models.IntegerField()
	from_area_id = models.FloatField(blank=True,null=True)
	to_area_id = models.FloatField(blank=True,null=True)
	from_city_id = models.FloatField(blank=True,null=True)
	to_city_id = models.FloatField(blank=True,null=True)
	from_date = models.DateTimeField()
	to_date = models.DateTimeField(blank=True,null=True)
	online_booking = models.IntegerField()
	mobile_site_booking = models.IntegerField()
	booking_created = models.DateTimeField()
	from_lat = models.FloatField(blank=True,null=True)
	from_long = models.FloatField(blank=True,null=True)
	to_lat = models.FloatField(blank=True,null=True)
	to_from_long = models.FloatField(blank=True,null=True)
	Car_Cancellation = models.IntegerField()

	def __str__(self):
		return str(self.booking_id)