from django.db import models

# Create your models here.
class prediction(models.Model):
    brand = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    model_year = models.IntegerField()
    Transmission = models.CharField(max_length=30)
    Engine_size = models.IntegerField()
    Fuel_type = models.CharField(max_length=30)
    Drivetrain = models.IntegerField()
    Lot_no = models.IntegerField()
    Kilometer = models.IntegerField()
    Price = models.IntegerField()

    
    def __str__(self):
        return self.brand

from rest_framework import serializers

class predictionSerializer(serializers.Serializer):
    brand = serializers.CharField(max_length=30)
    model = serializers.CharField(max_length=30)
    model_year = serializers.IntegerField()
    Transmission = serializers.CharField(max_length=30)
    Engine_size = serializers.IntegerField()
    Fuel_type = serializers.CharField(max_length=30)
    Drivetrain = serializers.IntegerField()
    Lot_no = serializers.IntegerField()
    Kilometer = serializers.IntegerField()
    Price = serializers.IntegerField()         