import pdfkit
import os

from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse, FileResponse, HttpResponseNotFound
from django.db.models import Q
# from django.template.loader import render_to_string
# from django.http import JsonResponse
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.utils import timezone
from django.utils.text import slugify
from .models import Profile, Contact, Skill, PortfolioCategory, Portfolio, WorkExperience, Education, Achievement, Template
from .forms import (inlineformset_factory, ProfileForm, ContactFormset, SkillFormset, PortfolioFormset, 
ExperienceFormset, EducationFormset, AchievementFormset, LoginForm, RegisterForm, UpdateAccount)
from django.views.generic import View
# from django.template import Context
# from django.template.loader import get_template
# from .utils import render_to_pdf

# Create your views here.
def index(request):
  templates= Template.objects.all()
  return render(request, 'index.html', {'templates':templates})

def all_profiles(request):
  # user = get_object_or_404(User, username=name)
  pk = request.user.pk
  profiles = Profile.objects.filter(user_id=pk)

  context = {'profiles': profiles[:5] }
  return render(request, 'all_profiles.html', context)

def view_profile(request, slug, pk):
  template_professional = 'professional.html'
  template_boxed = 'boxed.html'
  template_business = 'business.html'

  profile = get_object_or_404(Profile, slug=slug, pk=pk)
  contacts = profile.contact_profile.filter()

  # portfolios = profile.portfolio_profile.all().distinct()
  portfolios = Profile.objects.get(pk=pk).portfolio_profile.all()
  types = profile.portfolio_profile.filter().order_by('-portfolio_type_id').distinct('portfolio_type')

  if profile.template_id == 1:
    return render(request, template_boxed, {'profile': profile, 'contact': contacts, 'types': types})
  
  elif profile.template_id == 2:
    return render(request, template_professional, {'profile': profile, 'contact': contacts, 'types': types})

  elif profile.template_id == 3:
    return render(request, template_business, {'profile': profile, 'contact': contacts, 'types': types})

'''
def pdf(request):

    # Create a URL of our project and go to the template route
    projectUrl = request.get_host() + '/view_profile'
    options = {
      'page-size': 'Letter',
      'margin-top': '0.75in',
      'margin-right': '0.75in',
      'margin-bottom': '0.75in',
      'margin-left': '0.75in',
      'encoding': "UTF-8",
      'no-outline': None
    }
    pdf = pdfkit.from_url(projectUrl, options=options)
    # Generate download
    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="profolio.pdf"'

    return response
'''

def profile_form(request):
  if request.method == 'POST':
    profile_form = ProfileForm(request.POST, request.FILES)
    contact_form = ContactFormset(request.POST, prefix='contact')
    skill_forms = SkillFormset(request.POST, prefix='skills')
    portfolio_forms = PortfolioFormset(request.POST, request.FILES, prefix='portfolios')
    experience_forms = ExperienceFormset(request.POST, prefix='experiences')
    education_forms = EducationFormset(request.POST, prefix='educations')
    achievement_forms = AchievementFormset(request.POST, prefix='achievements')

    if (profile_form.is_valid() and contact_form.is_valid() and skill_forms.is_valid() 
        and portfolio_forms.is_valid() and experience_forms.is_valid()
        and education_forms.is_valid() and achievement_forms.is_valid()):

      profile = profile_form.save(commit=False)
      profile.slug = slugify(profile.name)
      profile.avatar = request.FILES['avatar']
      profile.created_on = timezone.now()
      profile.user = request.user
      profile.save()
      
      for cf in contact_form:
        new_cf = cf.save(commit=False)
        new_cf.profile = profile
        new_cf.save()
      
      for sf in skill_forms:
        new_sf = sf.save(commit=False)
        new_sf.profile = profile
        new_sf.save()

      for pf in portfolio_forms:
        new_pf = pf.save(commit=False)
        new_pf.profile = profile
        new_pf.save()

      for xf in experience_forms:
        new_xf = xf.save(commit=False)
        new_xf.profile = profile
        new_xf.save()

      for ef in education_forms:
        new_ef = ef.save(commit=False)
        new_ef.profile = profile
        new_ef.save()

      for af in achievement_forms:
        new_af = af.save(commit=False)
        new_af.profile = profile
        new_af.save()
      messages.success(request, "New profile saved!")
      return redirect('view_profile', slug=profile.slug, pk=profile.pk)

    else:
      print(profile_form.errors, contact_form.errors, skill_forms.errors, portfolio_forms.errors, experience_forms.errors,
        education_forms.errors, achievement_forms.errors)

  else:
    profile_form = ProfileForm()
    contact_form = ContactFormset(prefix='contact')
    skill_forms = SkillFormset(prefix='skills')
    portfolio_forms = PortfolioFormset(prefix='portfolios')
    experience_forms = ExperienceFormset(prefix='experiences')
    education_forms = EducationFormset(prefix='educations')
    achievement_forms = AchievementFormset(prefix='achievements')

  return render(request, 'profile_form.html', {'profile_form':profile_form, 'contact_form':contact_form, 
  'skill_forms':skill_forms, 'portfolio_forms':portfolio_forms, 'experience_forms':experience_forms, 
  'education_forms':education_forms, 'achievement_forms':achievement_forms})

def edit_profile(request, slug, pk):

  profile = get_object_or_404(Profile, slug=slug, pk=pk)
  ContactFormset = inlineformset_factory(Profile, Contact, fields=('address', 'city', 'state', 'zip_code', 'email', 'phone'), extra=1)
  SkillFormset = inlineformset_factory(Profile, Skill, fields=('title', 'percentage_rank'), extra=1)
  PortfolioFormset = inlineformset_factory(Profile, Portfolio, fields=('portfolio_type','image',), extra=1)
  ExperienceFormset = inlineformset_factory(Profile, WorkExperience, fields=('work_place', 'job_title', 'description', 'start_date', 'end_date'), extra=1)
  EducationFormset = inlineformset_factory(Profile, Education, fields=('school', 'qualification', 'description', 'start_date', 'end_date'), extra=1)
  AchievementFormset = inlineformset_factory(Profile, Achievement, fields=('number', 'title'), extra=1)

  if request.method == 'POST':
    profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
    contact_form = ContactFormset(request.POST, prefix='contact', instance=profile)
    skill_forms = SkillFormset(request.POST, prefix='skills', instance=profile)
    portfolio_forms = PortfolioFormset(request.POST, request.FILES, prefix='portfolios', instance=profile)
    experience_forms = ExperienceFormset(request.POST, prefix='experiences', instance=profile)
    education_forms = EducationFormset(request.POST, prefix='educations', instance=profile)
    achievement_forms = AchievementFormset(request.POST, prefix='achievements', instance=profile)

    if (profile_form.is_valid() and contact_form.is_valid() and portfolio_forms.is_valid() and skill_forms.is_valid() 
      and experience_forms.is_valid() and education_forms.is_valid() and achievement_forms.is_valid()):

      profile = profile_form.save(commit=False)
      profile.slug = slugify(profile.name)
      profile.created_on = timezone.now()
      profile.user = request.user
      profile.save()

      for cf in contact_form:
        new_cf = cf.save(commit=False)
        new_cf.profile = profile
        new_cf.save()
      
      for sf in skill_forms:
        new_sf = sf.save(commit=False)
        new_sf.profile = profile
        new_sf.save()

      for pf in portfolio_forms:
        new_pf = pf.save(commit=False)
        new_pf.profile = profile
        new_pf.save()

      for xf in experience_forms:
        new_xf = xf.save(commit=False)
        new_xf.profile = profile
        new_xf.save()

      for ef in education_forms:
        new_ef = ef.save(commit=False)
        new_ef.profile = profile
        new_ef.save()

      for af in achievement_forms:
        new_af = af.save(commit=False)
        new_af.profile = profile
        new_af.save()
      return redirect('view_profile', slug=profile.slug, pk=profile.pk)

  else:
    profile_form = ProfileForm(instance=profile)
    contact_form = ContactFormset(prefix='contact', instance=profile)
    skill_forms = SkillFormset(prefix='skills', instance=profile)
    portfolio_forms = PortfolioFormset(prefix='portfolios', instance=profile)
    experience_forms = ExperienceFormset(prefix='experiences', instance=profile)
    education_forms = EducationFormset(prefix='educations', instance=profile)
    achievement_forms = AchievementFormset(prefix='achievements', instance=profile)

  return render(request, 'profile_form.html', {'profile_form':profile_form, 
    'contact_form':contact_form, 'skill_forms':skill_forms, 'portfolio_forms':portfolio_forms, 
    'experience_forms':experience_forms, 'education_forms':education_forms,
    'achievement_forms':achievement_forms})

def delete_profile(request, slug, pk):
  profile = get_object_or_404(Profile, slug=slug, pk=pk)
  profile.delete()
  return redirect("")

def searchposts(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(position__icontains=query) | Q(name__icontains=query)

            results= Profile.objects.filter(lookups).distinct()

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'search.html', context)

        else:
            return render(request, 'search.html')

    else:
        return render(request, 'search.html')

def download_cv(request, slug, pk):
  profile = get_object_or_404(Profile, slug=slug, pk=pk)
  filename = profile.upload_cv.path
  response = FileResponse(open(filename, 'rb'))
  return response

def register(request):

  if request.method == 'POST':
    uname = request.POST['uname']
    # fname = request.POST['fname']
    # lname = request.POST['lname']
    email = request.POST['email']
    password = request.POST['password']
    password_length = len(password)

    if password_length > 8:

      if User.objects.filter(username=uname).exists():
        messages.info(request, 'Username already exist', extra_tags='register')
        return redirect('register')
      elif User.objects.filter(email=email).exists():
        messages.info(request, 'Email already exist', extra_tags='register')
        return redirect('register')
      else:
        user = User.objects.create_user(username=uname, password=password, email=email)
        user.save()
        messages.info(request, 'User created', extra_tags='register')
        return redirect('login')

    else:
      messages.info(request, 'password length is too small', extra_tags='register')
      return redirect('register')
    return redirect('/')
  else:
    return redirect('signup')

def signup(request):
  if request.method == 'POST':
    register_form = RegisterForm(request.POST)
    if register_form.is_valid():
      username = register_form.cleaned_data['username']
      email = register_form.cleaned_data['email']
      password = register_form.cleaned_data['password']
      password_length = len(password)
      if password_length > 8:
        if User.objects.filter(username=username).exists():
          messages.info(request, 'Username already exist', extra_tags='signup')
          return redirect('signup')
        elif User.objects.filter(email=email).exists():
          messages.info(request, 'Email already exist', extra_tags='signup')
          return redirect('signup')
        else:
          user = User.objects.create_user(username=username, password=password, email=email)
          user.save()
          messages.info(request, 'User created', extra_tags='signup')
          return redirect('signin')
      else:
        messages.info(request, 'password length is too small', extra_tags='signup')
        return redirect('signup')
    return redirect('/')
  else:
    login_form = LoginForm()
    register_form = RegisterForm()
    return render(request, "registration/login.html", {'login_form':login_form, 'register_form':register_form})

def login(request):
  if request.method == 'POST':
    uname = request.POST['uname']
    # email = request.POST['email']
    password = request.POST['password']

    user = auth.authenticate(username=uname, password=password)

    if user is not None:
      auth.login(request, user)
      return redirect('all_profiles')
    else:
      messages.info(request, 'Wrong email or password', extra_tags='login')
      return redirect('/')
  else:
    return redirect('signin')
    # return HttpResponseNotFound("<h1>No Page Found</h1>")

def signin(request):
  if request.method == 'POST':
    login_form = LoginForm(request.POST)
    if login_form.is_valid():
      username = login_form.cleaned_data['username']
      password = login_form.cleaned_data['password']
      user = auth.authenticate(username=username, password=password)

      if user is not None:
        auth.login(request, user)
        return redirect('all_profiles')
      else:
        messages.info(request, 'Wrong email or password', extra_tags='signin')
        return redirect('signin')
    else:
      messages.info(request, 'The data is invalid', extra_tags='signin')
      return redirect('signin')
  else:
    login_form = LoginForm()
    register_form = RegisterForm()
    return render(request, "registration/login.html", {'login_form':login_form, 'register_form':register_form})
  
def update_account(request):
  if request.method == 'POST':
    account_form = UpdateAccount(request.POST, instance=request.user)
    if account_form.is_valid():
      account_form.save()
      return redirect('update_account')
  else:
    account_form = UpdateAccount(instance=request.user)
    return render(request, "registration/update.html", {'account_form':account_form})

def logout(request):
  auth.logout(request)
  return redirect('/')
