from django.urls import path
from .url_imports import *


urlpatterns = [
     
     path('home/<str:user_id>/<str:room_id>/' , HomeView.as_view() , name='home'),

     path('notifications_list/<str:user_id>/' ,
           NotificationsList.as_view() , name='notifications_list'),

     path('invite/mail/<str:user_id>/<str:room_id>/<str:invite_method>/' , 
           MailInviteLink.as_view() , name='mail_invite_link'),
     
     path('invite/check_invite_link/<str:user_id>/<str:room_id>/<str:invite_method>/' ,
           CheckInviteLink.as_view() , name='check_invite_link'),

     path('invite/accept_or_reject_btns/<str:user_id>/<str:room_id>/<str:invite_method>/' ,
           AcceptOrRejectBtns.as_view() , name='accept_or_reject_btns'),

     path('invite/after_accepts_invite/<str:user_id>/<str:room_id>/<str:invite_method>/' ,
            AfterAcceptsInvite.as_view() , name='after_accepts_invite'),

     path('invite/after_rejects_invite/<str:user_id>/<str:room_id>/<str:invite_method>/',
            AfterRejectsInvite.as_view() , name='after_rejects_invite'),

     path('leave/room/<str:user_id>/<str:room_id>/<str:invite_method>/' ,
           LeaveRoom.as_view() , name='leave_room'),
     

     path('invite/sms/<str:phone_number>/<str:room_id>/<str:invite_method>/' ,
           SMSInviteLink.as_view() , name='sms_invite_link') , 
      

     path('' , InputMailAndRoomId.as_view() , 
                name='input_mail_and_room_id'),

     path('users_list/' , KeycloakUserEntityList.as_view(),
                          name='keycloakuserentity-list'),
      
     path('user_detail/<pk>/' , KeycloakUserEntityDetail.as_view(),
                                name='keycloakuserentity-detail'),
      
     path('rooms_list/' , KeycloakRealmList.as_view() , 
                           name='keycloakrealm-list'),

     path('realm_detail/<pk>/' , KeyCloakRealmDetail.as_view() , 
                                  name='keycloakrealm-detail'),

     path('user_invite_detail/<pk>/' , UserInviteDetail.as_view() , 
                                        name='userinvite-detail'),

     path('user_join_detail/<pk>/' , UserJoinRoomDetail.as_view() , 
                                      name='userjoin-detail'),

     path('comments_on_notification/<int:notification_id>/' ,
          CreateCommentNotification.as_view() , name='create_comment_notification'),
]
