from rest_framework.generics import GenericAPIView
from accounts.model_serializers.User import UserSerializer
from accounts.models.User import User


class BaseUserSerializer(GenericAPIView):

    serializer_class = UserSerializer
    queryset = User.objects.all()