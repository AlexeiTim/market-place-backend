from rest_framework import viewsets
from wallet import models, serializers
from django.core.exceptions import PermissionDenied


class WalletViewSet(viewsets.ModelViewSet):
    queryset = models.Wallet.objects.all()
    serializer_class = serializers.WalletSerializer
    pagination_class = None

    def get_queryset(self):
        return models.Wallet.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        if models.Wallet.objects.filter(user=self.request.user).exists():
            raise PermissionDenied("Wallet already exists for this user.")
        serializer.save(user=self.request.user)


