from django.shortcuts import render
from django.db.models import Prefetch
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from clients.models import Client
from .models import Subscription, Plan, Service
from .serializers import SubscriptionSerializer


class SubscriptionViewSet(ReadOnlyModelViewSet):
    queryset = Subscription.objects.all().prefetch_related(
        'plan',
        Prefetch('client', queryset=Client.objects.all().select_related('user').only('company_name',
                                                                                     'user__email'))
        )
    serializer_class = SubscriptionSerializer
