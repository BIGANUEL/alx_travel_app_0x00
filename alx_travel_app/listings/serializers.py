from rest_framework import serializers
from .models import Listing, Booking

class ListingSerializer(serializers.ModelSerializer):
    """Serializer for Listing model"""
    class Meta:
        model = Listing
        fields = [
            'id', 'title', 'description', 'address', 'city', 'country',
            'property_type', 'price_per_night', 'max_guests', 'bedrooms',
            'beds', 'baths', 'amenities', 'host', 'created_at', 'updated_at'
        ]
        read_only_fields = ['host', 'created_at', 'updated_at']

class BookingSerializer(serializers.ModelSerializer):
    """Serializer for Booking model"""
    class Meta:
        model = Booking
        fields = [
            'id', 'listing', 'guest', 'check_in', 'check_out',
            'total_price', 'status', 'created_at', 'updated_at'
        ]
        read_only_fields = ['guest', 'total_price', 'created_at', 'updated_at']
