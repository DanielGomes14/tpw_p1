from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import PasswordChangeForm


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=255, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class UpdateClientForm(UserChangeForm):
    first_name = forms.CharField( max_length=30, required=False, help_text='Optional.',widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=255, help_text='Required. Inform a valid email address.', widget=forms.TextInput(attrs={'class': 'form-control'}))
    username=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class UpdatePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=30,widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(max_length=30,widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(max_length=30,widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = {'old_password', 'new_password1', 'new_password2'}



class PurchaseForm(forms.Form):
    '''
    The first two fields of this form correspond to the form that will be used to complete a purchase( if there are no errors in the process of completion)
    The last one will only be used to when we want to add to favorites ( or remove it from favorites ) a product
    '''
    productid=forms.IntegerField()
    paymenttype=forms.IntegerField()
class FavoritesForm(forms.Form):
    productid =forms.BooleanField(required=False,initial=False);
