from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.utils import timezone
from django.utils.text import slugify
from .models import Profile, Contact, PortfolioCategory, Portfolio
from .forms import ProfileForm, PortfolioForm, ContactForm

# Create your views here.
def index(request):
  return render(request, 'index.html', {})

@login_required
def profile_form(request):
  if request.method == 'POST':
    profile_form = ProfileForm(request.POST, instance=Profile())
    contact_form = ContactForm(request.POST)
    portfolio_forms = PortfolioForm(request.POST, prefix=str(x), instance=Portfolio())

    if profile_form.is_valid() and contact_form.is_valid() and all([pf.is_valid() for pf in portfolio_forms]):
      profile = profile_form.save(commit=False)
      profile.slug = slugify(profile.name)
      profile.created_on = timezone.now()
      profile.save()
      # post_form.save_m2m()
      for pf in portfolio_forms:
        new_pf = pf.save(commit=False)
        new_pf.profile = profile
        new_pf.save()

      return redirect('view_portfolio', slug=profile.slug, pk=profile.pk)

  else:
    profile_form = ProfileForm(instance=Profile())
    contact_form = ContactForm()
    portfolio_forms = [PortfolioForm(prefix=str(x), instance=Portfolio()) for x in range(0,3)]
    # post_img_form = PostImgForm()
  return render(request, 'profile_form.html', {'profile_form':profile_form, 
    'contact_form':contact_form, 'portfolio_forms':portfolio_forms})

@login_required
def view_portfolio(request, slug, pk):
  template_name = 'portfolio.html'

  profile = get_object_or_404(Profile, slug=slug, pk=pk)
  contacts = profile.contact_profile.filter()

  # portfolios = profile.portfolio_profile.all().distinct()
  portfolios = Profile.objects.get(pk=pk).portfolio_profile.all()
  types = profile.portfolio_profile.filter().order_by('-portfolio_type_id').distinct('portfolio_type')

  return render(request, template_name, {'profile': profile, 'contact': contacts, 'types': types})

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
        user.save();
        messages.info(request, 'User created', extra_tags='register')
        return redirect('login')

    else:
      messages.info(request, 'password length is too small', extra_tags='register')
      return redirect('register')
    return redirect('/')
  else:

    return render(request, "registration/login.html")
'''
def login(request):
  if request.method == 'POST':
    uname = request.POST['uname']
    # email = request.POST['email']
    password = request.POST['password']

    user = auth.authenticate(username=uname, password=password)

    if user is not None:
      auth.login(request, user)
      return redirect('/')
    else:
      messages.info(request, 'Wrong email or password', extra_tags='login')
      return redirect('')
  else:
    return render(request, "login.html")
'''
def logout(request):
  auth.logout(request)
  return redirect('/')
