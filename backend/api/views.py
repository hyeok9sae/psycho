from api import models, serializers
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination


class SmallPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 50


class StoreViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.StoreSerializer
    pagination_class = SmallPagination

    def get_queryset(self):
        name = self.request.query_params.get("name", "")
        queryset = (
            models.Store.objects.all().filter(store_name__contains=name).order_by("id")
        )
        return queryset


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ReviewSerializer
    pagination_class = SmallPagination

    def get_queryset(self):
        store_id = self.request.query_params.get("store_id", "")
        queryset = (
            models.Review.objects.all().filter(store__exact=store_id).order_by("rid")
        )
        return queryset


class HotelViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.HotelSerializer
    pagination_class = SmallPagination

    def get_queryset(self):
        location = self.request.query_params.get("location", "")
        queryset = (
            models.Hotel.objects.all().filter(address1__contains=location).order_by("id")
        )
        return queryset
