from rest_framework import serializers
from wallet import models


class WalletSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = models.Wallet
        fields = '__all__'