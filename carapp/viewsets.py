from rest_framework import viewsets
from . import models
from . import serializers


from rest_framework.response import Response
from .serializers import CarSpecsSerializer
from carapp.models import CarSpecs, CarPlan
import json
from rest_framework.parsers import JSONParser

class CarSpecsViewset(viewsets.ModelViewSet):
    queryset = models.CarSpecs.objects.all()
    serializer_class = serializers.CarSpecsSerializer


    def create(self, request, *args, **kwargs):
        car_data = request.data

        new_car = CarSpecs.objects.create(car_plan=CarPlan.objects.get(id=car_data["car_plan"]), car_brand=car_data["car_brand"], car_model=car_data[
            "car_model"], production_year=car_data["production_year"], car_body=car_data["car_body"], engine_type=car_data["engine_type"])

        new_car.save()

        serializer = CarSpecsSerializer(new_car)

        return Response(serializer.data)