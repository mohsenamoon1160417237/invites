from django import forms




class UserRoomForm(forms.Form):

    user_email = forms.EmailField()
    room_id = forms.CharField(max_length=50)