from user_invite.model_serializers.UserInvite import UserInviteSerializer
from user_invite.models.UserInvite import UserInvite
from rest_framework import generics




class UserInviteDetail(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = UserInviteSerializer
    queryset = UserInvite.objects.all()