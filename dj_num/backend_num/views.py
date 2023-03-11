from django.shortcuts import render
from rest_framework.views import APIView
from .models import Sales
from .serializer import SalesSerializer
from rest_framework.response import Response

# Create your views here.
class SalesView(APIView):
	def get(self, request):
		output = [
		{
			"id": output.id,
			"contract": output.contract,
			"price": output.price,
			"delivery_date": output.delivery_date,
			"rub_price": output.rub_price
		} for output in Sales.objects.all()

		]
		return Response(output)