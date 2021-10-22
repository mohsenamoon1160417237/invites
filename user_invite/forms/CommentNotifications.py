from django import forms
from user_invite.models.CommentNotifications import CommentNotifications



class CommentNotificationsForm(forms.ModelForm):


    class Meta:

        model = CommentNotifications

        fields = ['title' , 
                  'body']