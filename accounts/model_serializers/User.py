from rest_framework import serializers
from accounts.models.User import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = ['phone_number',
                  'email',
                  'first_name',
                  'last_name',
                  'company_name']

    def create(self , validated_data):

        return User.objects.create(**validated_data)

