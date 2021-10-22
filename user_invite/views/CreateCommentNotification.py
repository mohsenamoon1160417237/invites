from user_invite.views.utils.Imports import *




class CreateCommentNotification(generics.GenericAPIView):

    serializer_class = CommentNotificationSerializer
    queryset=CommentNotifications.objects.all()
    pagination_class = MediumResultPagination

    def get(self , request , notification_id , *args , **kwargs):

        form = CommentNotificationsForm()
        previous_comments = CommentNotifications.objects.filter(notification_id=notification_id)

        return render(request , 'comment_notifications_form.html' , {"form" : form,
                                                                     "previous_comments" : previous_comments})
    

    def post(self , request , notification_id , *args , **kwargs):

        new_comment = None
        
        notification = get_object_or_404(Notification ,
                                         id=notification_id)
        

        form = CommentNotificationsForm(data=request.POST)
        
        if form.is_valid():

            new_comment = form.save(commit=False)
            new_comment.notification = notification
            new_comment.save()

            return redirect('create_comment_notification' , notification_id=notification_id)