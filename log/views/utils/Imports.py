from django.shortcuts import (render,
                              get_object_or_404,
                              redirect)
from rest_framework.response import Response
from rest_framework import status
from log.models.PostLog import PostLog
from log.models.PostTag import PostTag
from log.models.PostLabel import PostLabel
from log.models.FileUpload import FileUpload
from rest_framework.generics import GenericAPIView
from log.model_serializers.PostLabel import PostLabelSerializer
from log.model_serializers.PostLog import PostLogSerializer
from log.model_serializers.PostTag import PostTagSerializer
from log.model_serializers.FileUpload import FileUploadSerializer
from accounts.models.User import User
import datetime
from log.tasks.post_schedule import post_schedule
from log.views.modules.File import FileModule