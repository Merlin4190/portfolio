from . models import Profile, Skill, Contact, Portfolio, WorkExperience, Education, Achievement
from django.contrib.auth.models import User, auth
from django import forms 
from django.forms import (formset_factory, inlineformset_factory, modelformset_factory, BaseModelFormSet)

from ckeditor_uploader.widgets import CKEditorUploadingWidget
from ckeditor.widgets import CKEditorWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

class LoginForm(forms.Form):
  """docstring for LoginForm"""
  username = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'name': 'uname'}))
  password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'name': 'password'}))

class RegisterForm(forms.Form):
  """docstring for RegisterForm"""
  username = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'name': 'uname'}))
  email = forms.EmailField(max_length=20, widget=forms.TextInput(attrs={'name': 'email'}))
  password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'name': 'password'}))

class UpdateAccount(forms.ModelForm):
  """docstring for ProfileForm"""
  # bio = forms.CharField( widget=forms.Textarea )
  class Meta:
    model = User
    fields = ('username', 'first_name', 'last_name',)

class ProfileForm(forms.ModelForm):
  """docstring for ProfileForm"""
  bio = forms.CharField(widget=CKEditorWidget(attrs={'id': 'bio', 'class': '.form-control', 'style': 'font-family: VT323;', 'required': True, 'placeholder': 'Bio'}))
  # avatar = forms.ImageField(widget=CKEditorUploadingWidget())
  class Meta:
    model = Profile
    fields = ('template', 'name', 'avatar', 'bio', 'position', 'dob', 'email', 'marital_status', 'industry', 'pininterest_url'
      , 'linkedin_url', 'instagram_url', 'twitter_url', 'facebook_url', 'youtube_url', 'upload_cv')
    widgets = {
      'name': forms.TextInput(
          attrs={'id': 'name', 'class': '.form-control', 'style': 'font-family: VT323;', 'required': True, 'placeholder': 'Name'}
      ),
      'position': forms.TextInput(
          attrs={'id': 'position', 'class': '.form-control', 'style': 'font-family: VT323;', 'required': True, 'placeholder': 'Position e.g Web Developer, Civil Engineer, Data Analyst etc'}
      ),   
      'dob': forms.TextInput(
          attrs={'type': 'date', 'id': '.form-control', 'class': 'geo', 'data-geo': 'location', 'required': False, 'placeholder': 'leave blank to use your location'}
      ),
    }
    labels = {
      'dob':'Date of Birth',
      'pininterest_url':'Pin Interest url',
      'template': 'Template Type',
      'upload_cv': 'Upload CV'
    }
  def __init__(self, *args, **kwargs):
    super(ProfileForm, self).__init__(*args, **kwargs)
    self.fields['marital_status'].empty_label = "Please Select Marital Status"
    self.fields['industry'].empty_label = "Please Select industry"
    self.fields['pininterest_url'].required = False
    self.fields['youtube_url'].required = False
    self.fields['facebook_url'].required = False
    self.fields['twitter_url'].required = False
    self.fields['linkedin_url'].required = False
    self.fields['instagram_url'].required = False
    self.fields['template'].empty_label = "Please Select Type"
    
class ContactForm(forms.ModelForm):
  """docstring for ContactForm"""
  class Meta:
    model = Contact
    fields = ('address', 'city', 'state', 'zip_code', 'email', 'phone',)

  def __init__(self, *args, **kwargs):
    super(ContactForm, self).__init__(*args, **kwargs)
    self.fields['zip_code'].required = False

ContactFormset = formset_factory(ContactForm, extra=1, can_delete=False)

class SkillForm(forms.ModelForm):
  """docstring for SkillForm"""
  class Meta:
    model = Skill
    fields = ('title', 'percentage_rank',)

SkillFormset = formset_factory(SkillForm, extra=1, can_delete=False)

class PortfolioForm(forms.ModelForm):
  class Meta:
    model = Portfolio
    fields = ('portfolio_type','image',)

  def __init__(self, *args, **kwargs):
    super(PortfolioForm, self).__init__(*args, **kwargs)
    self.fields['portfolio_type'].empty_label = "Please Select Type"
    self.fields['portfolio_type'].required = False
    self.fields['image'].required = False

PortfolioFormset = formset_factory(PortfolioForm, extra=1, can_delete=False)

class ExperienceForm(forms.ModelForm):
  description = forms.CharField(widget=CKEditorWidget())
  class Meta:
    model = WorkExperience
    fields = ('work_place', 'job_title', 'description', 'start_date', 'end_date')

ExperienceFormset = formset_factory(ExperienceForm, extra=1, can_delete=False)

class EducationForm(forms.ModelForm):
  description = forms.CharField(widget=CKEditorWidget())
  class Meta:
    model = Education
    fields = ('school', 'qualification', 'description', 'start_date', 'end_date')

EducationFormset = formset_factory(EducationForm, extra=1, can_delete=False)

'''
class BasePortfolioFormSet(BaseModelFormSet):
  def __init__(self, *args, **kwargs):
    super(BasePortfolioFormSet, self).__init__(*args, **kwargs)
    self.queryset = Portfolio.objects.filter(image__startswith='O')
PortfolioFormset = modelformset_factory(
    Portfolio,
    fields=('portfolio_type','image',),
    formset=BasePortfolioFormSet,
    extra=1,
    widgets={'portfolio_type': forms.Select(attrs={
            'class': 'form-control',
            'placeholder': 'Please Select Type'
        })
    }
)
class BaseExperienceFormSet(BaseModelFormSet):
  def __init__(self, *args, **kwargs):
    super(BaseExperienceFormSet, self).__init__(*args, **kwargs)
    self.queryset = WorkExperience.objects.filter(work_place__startswith='O', 
      job_title__startswith='O', description__startswith='O', start_date__startswith='O', end_date__startswith='O')

ExperienceFormset = modelformset_factory(
    WorkExperience,
    fields=('work_place', 'job_title', 'description', 'start_date', 'end_date'),
    extra=1,
    formset=BaseExperienceFormSet,
    # description = forms.CharField(widget=CKEditorUploadingWidget())
    widgets = {
      'work_place': forms.TextInput(
          attrs={'id': 'work_place', 'class': '.form-control', 'style': 'font-family: VT323;', 'required': False, 'placeholder': 'Company/Oragnaisation Name'}
      ),
      'job_title': forms.TextInput(
          attrs={'id': 'job_title', 'class': '.form-control', 'style': 'font-family: VT323;', 'required': False, 'placeholder': 'Position Held'}
      ),
      'description': forms.Textarea(
          attrs={'id': 'job_description', 'class': '.form-control', 'style': 'font-family: VT323;', 'required': False, 'placeholder': 'Job Details'}
      ),
      'start_date': forms.TextInput(
          attrs={'type': 'date', 'id': 'start_date', 'class': '.form-control', 'required': False, 'placeholder': 'Date started'}
      ),
      'end_date': forms.TextInput(
          attrs={'type': 'date', 'id': 'end_date', 'class': '.form-control', 'required': False, 'placeholder': 'Date ended. Leave blank if you are still on the job'}
      ),
    }
)

class BaseEducationFormSet(BaseModelFormSet):
  def __init__(self, *args, **kwargs):
    super(BaseEducationFormSet, self).__init__(*args, **kwargs)
    self.queryset = Education.objects.filter(school__startswith='O', qualification__startswith='O', 
      description__startswith='O', start_date__startswith='O', end_date__startswith='O')

EducationFormset = modelformset_factory(
    Education,
    fields=('school', 'qualification', 'description', 'start_date', 'end_date'),
    formset=BaseEducationFormSet,
    extra=1,
    widgets = {
      'school': forms.TextInput(
          attrs={'id': 'school', 'class': '.form-control', 'style': 'font-family: VT323;', 'required': False, 'placeholder': 'School Name'}
      ),
      'qualification': forms.TextInput(
          attrs={'id': 'qualification', 'class': '.form-control', 'style': 'font-family: VT323;', 'required': False, 'placeholder': 'qualification'}
      ),
      'description': forms.Textarea(
          attrs={'id': 'edu_description', 'class': '.form-control', 'style': 'font-family: VT323;', 'required': False, 'placeholder': 'School Experience/Achievements'}
      ),
      'start_date': forms.TextInput(
          attrs={'type': 'date', 'id': 'start_date', 'class': '.form-control', 'required': False, 'placeholder': 'Date started'}
      ),
      'end_date': forms.TextInput(
          attrs={'type': 'date', 'id': 'end_date', 'class': '.form-control', 'required': False, 'placeholder': 'Date ended. Leave blank if program is still running'}
      ),
    }
)
'''

class BaseAchievementFormSet(BaseModelFormSet):
  def __init__(self, *args, **kwargs):
    super(BaseAchievementFormSet, self).__init__(*args, **kwargs)
    self.queryset = Achievement.objects.filter(title__startswith='O', number__startswith='O')

AchievementFormset = modelformset_factory(
    Achievement,
    fields=('number', 'title'),
    formset=BaseAchievementFormSet,
    extra=1,
    widgets = {      
      'number': forms.TextInput(
          attrs={'type': 'number', 'id': 'number', 'class': '.form-control', 'required': False, 'placeholder': 'Number of Awards'}
      ),
      'title': forms.TextInput(
          attrs={'id': 'title', 'class': '.form-control', 'required': False, 'placeholder': 'Title/Name of Award/Competition'}
      ),
    }
)
    