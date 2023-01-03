from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from .models import Subscription, Plan, Service
from .serializers import SubscriptionSerializer


class SubscriptionViewSet(ReadOnlyModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
# class ServiceViewSet(ModelViewSet):
#     queryset =
