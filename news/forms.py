
from django import forms
from .models import LatestNews, BangladeshNews, PoliticsNews,WorldNews,SportsNews,TradeNews,TechnologyNews,EntertainmentNews
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Base form class to be inherited
class SignUpForms(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {
            'username':'User Name',
            'first_name':'First Name',
            'last_name':'Last Name',
            'email':'Email',
        }
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            }

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password = forms.CharField(label=_('Password'),strip=False,widget=forms.PasswordInput(attrs={'autofocus':True,'class':'form-control'}))
    

class NewsBaseForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        labels = {
            'image': 'Image',
            'title': 'Title',
            'desc': 'Description'
        }
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control'}),
        }

# Inherit the base form for Latest News
class LatestNewsForm(NewsBaseForm):
    class Meta(NewsBaseForm.Meta):
        model = LatestNews

# Inherit the base form for Bangladesh News
class BangladeshNewsForm(NewsBaseForm):
    class Meta(NewsBaseForm.Meta):
        model = BangladeshNews 

# Inherit the base form for Politics News
class PoliticsNewsForm(NewsBaseForm):
    class Meta(NewsBaseForm.Meta):
        model = PoliticsNews  

# Inherit the base form for World News
class WorldNewsForm(NewsBaseForm):
    class Meta(NewsBaseForm.Meta):
        model = WorldNews  

# Inherit the base form for Sports News
class SportsNewsForm(NewsBaseForm):
    class Meta(NewsBaseForm.Meta):
        model = SportsNews  

# Inherit the base form for Trade News
class TradeNewsForm(NewsBaseForm):
    class Meta(NewsBaseForm.Meta):
        model = TradeNews  

# Inherit the base form for Technology News
class TechnologyNewsForm(NewsBaseForm):
    class Meta(NewsBaseForm.Meta):
        model = TechnologyNews 

# Inherit the base form for Entertainment News
class EntertainmentNewsForm(NewsBaseForm):
    class Meta(NewsBaseForm.Meta):
        model = EntertainmentNews 