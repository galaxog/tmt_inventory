from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from interview.order.models import Order, OrderTag
from interview.order.serializers import OrderSerializer, OrderTagSerializer
from interview.order.schemas import OrderIsActiveData


# Create your views here.
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    

class OrderTagListCreateView(generics.ListCreateAPIView):
    queryset = OrderTag.objects.all()
    serializer_class = OrderTagSerializer


class DeactivateOrderView(APIView):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def post(self, request: Request, *args, **kwargs) -> Response:

        id = request.get_query_params.get("status", None)
        is_active = request.data.get("is_active", None)

        try:
            validated_data = OrderIsActiveData({"id": id, "is_active": is_active})
        except Exception as e:
            return Response({'error': str(e)}, status=400)

        serializer = self.serializer_class(data=validated_data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        serializer.save()

        return Response(serializer.data, status=201)


