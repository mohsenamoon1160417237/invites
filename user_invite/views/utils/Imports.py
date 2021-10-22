from django.shortcuts import (render , 
                              get_object_or_404 , 
                              redirect
                             )

#models
from user_invite.models.KeycloakUserEntity import KeycloakUserEntity
from user_invite.models.KeycloakRealm import KeycloakRealm
from user_invite.models.UserInvite import UserInvite
from user_invite.models.UserJoinRoom import UserJoinRoom
from user_invite.models.Notification import Notification
from user_invite.models.CommentNotifications import CommentNotifications


from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics ,  status
from rest_framework.response import Response
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings

from datetime import datetime
from django.db import connections

#forms
from user_invite.forms.CommentNotifications import CommentNotificationsForm
from user_invite.forms.UserRoom import UserRoomForm

from django.views import View
from django.http import JsonResponse

from user_invite.model_serializers.KeycloakRealm import KeycloakRealmSerializer
from user_invite.model_serializers.KeycloakUserEntity import KeycloakUserEntitySerializer
from user_invite.model_serializers.UserInvite import UserInviteSerializer
from user_invite.model_serializers.UserJoinRoom import UserJoinRoomSerializer
from user_invite.model_serializers.Notification import NotificationSerializer
from user_invite.model_serializers.CommentNotifications import CommentNotificationSerializer
from .PageNumberPagination import (LargeResultPagination,
                                   MediumResultPagination)