from rest_framework import serializers

from parking_project.account.models import Account


class AccountSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    email = serializers.CharField(source='user.email')

    class Meta:
        model = Account
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_no')
        read_only_fields = ('username',)

    def update(self, instance, validated_data):
        validated_user = validated_data.pop('user', {})

        user_fields = ['first_name', 'last_name', 'email']
        for field_name in user_fields:
            if field_name in validated_user:
                setattr(instance.user, field_name, validated_user[field_name])
            instance.user.save()

        return super(AccountSerializer, self).update(instance, validated_data)
