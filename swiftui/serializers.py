from swiftui.models import Bank
from rest_framework import serializers


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ['name', 'category', 'description', 'active', 'balance']
