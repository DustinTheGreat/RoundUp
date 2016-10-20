from django import forms
from django.forms import ModelForm
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.models import User

User = get_user_model()
class UserLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

	def clean(self, *args, **kwargs):
		username= self.cleaned_data.get('username')
		password= self.cleaned_data.get('password')
		user = authenticate(username=username, password=password)
		if not user:
			raise forms.ValidationError("this user does not exsist")
		if not user.check_password(password):
			raise forms.ValidationError("Incorrect password")
		if not user.is_active:
			raise forms.ValidationError("This account is not active")
		return super(UserLoginForm, self).clean(*args, **kwargs)

class UserRegisterForm(forms.ModelForm):
	email = forms.EmailField(label='email')
	email2 = forms.EmailField(label='email2')

	class Meta:
		model = User
		fields = ('username','email','email2', 'password')
	def clean_email2(self):
		email = self.cleaned_data.get('email')
		email2 = self.cleaned_data.get('email2')
		if email != email2:
			raise forms.ValidationError("emails must match")
		return email