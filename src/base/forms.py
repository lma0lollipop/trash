from django.forms import ModelForm
from .models import UserProfile



class UserCreateForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        #exclude = ['private',]