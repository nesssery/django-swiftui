from swiftui.models import Bank
from rest_framework import viewsets
from rest_framework import permissions
from swiftui.serializers import BankSerializer


class BankViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    permission_classes = [permissions.IsAuthenticated]
