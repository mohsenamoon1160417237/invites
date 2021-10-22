from user_invite.model_serializers.UserJoinRoom import UserJoinRoomSerializer
from user_invite.models.UserJoinRoom import UserJoinRoom
from rest_framework import generics




class UserJoinRoomDetail(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = UserJoinRoomSerializer
    queryset = UserJoinRoom.objects.all()