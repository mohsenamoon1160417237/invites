from .url_imports import *


urlpatterns = [

    #customer registration urls
    path('register_c/first_p/' , FirstPhaseC.as_view() , name='first_phase_c'),
    path('register_c/second_p/<int:id>/<str:url_name>/' , SecondPhaseC.as_view() , name='second_phase_c'),

    #buisinessman registration urls
    path('register_b/first_p/' , FirstPhaseB.as_view() , name='first_phase_b'),
    path('register_b/second_p/<int:id>/<str:url_name>/' , SecondPhaseB.as_view() , name='second_phase_b'),
    path('register_b/third_p/<int:id>/<str:url_name>/' , ThirdPhaseB.as_view() , name='third_phase_b'),

    #Authentication urls
    path('login/' , LoginView.as_view() , name='login'),
    path('logout/' , Logout.as_view() , name='logout'),

    #Home url
    path('home/' ,Home.as_view() , name='home'),
]