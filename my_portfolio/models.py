from django.conf import settings
from django.db import models

# Create your models here.
class Template(models.Model):
  """docstring for Marital_status"""
  title = models.CharField(max_length=50)
  design = models.ImageField(upload_to='images/template', default=None)

  def __str__(self):
    return self.title

class MaritalStatus(models.Model):
  """docstring for Marital_status"""
  title = models.CharField(max_length=50)

  def __str__(self):
    return self.title

class Industry(models.Model):
  """docstring for Marital_status"""
  title = models.CharField(max_length=200, unique=True)
  slug= models.SlugField(max_length=200, unique=True)

  def __str__(self):
    return self.title

class PortfolioCategory(models.Model):
  """docstring for Cateory"""
  title= models.CharField(max_length=200, unique=True)
  slug= models.SlugField(max_length=200, unique=True)
  created_on= models.DateTimeField(auto_now_add=True)
  updated_on= models.DateTimeField(auto_now=True)

  class Meta:
    """docstring for Meta"""
    ordering = ['-created_on']

  def __str__(self):
    return self.title

class Profile(models.Model):
  """docstring for Profile"""
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
  # user = models.OneToOneField(User, related_name='profile')
  template = models.ForeignKey(Template, on_delete=models.CASCADE, default=None, null=True, related_name='profile_template')
  name= models.CharField(max_length=200)
  slug= models.SlugField(max_length=200)
  bio = models.CharField(max_length=140)
  avatar = models.ImageField(upload_to='images/avatar', default=None)
  position= models.CharField(max_length=200)
  dob= models.DateField(max_length=8)
  email= models.EmailField(max_length=200)
  marital_status = models.ForeignKey(MaritalStatus, on_delete=models.CASCADE, related_name='profile_status')
  industry = models.ForeignKey(Industry, on_delete=models.CASCADE, related_name='profiles_industry')
  pininterest_url = models.URLField(max_length=200, blank=True)
  linkedin_url = models.URLField(max_length=200, blank=True)
  instagram_url = models.URLField(max_length=200, blank=True)
  twitter_url = models.URLField(max_length=200, blank=True)
  facebook_url = models.URLField(max_length=200, blank=True)
  youtube_url = models.URLField(max_length=200, blank=True)
  upload_cv = models.FileField(upload_to='files/cv', blank=True, null=True)
  created_on= models.DateTimeField(auto_now_add=True)
  updated_on= models.DateTimeField(auto_now=True)

  # portfolios = models.ManyToManyField(Portfolio, related_name='profiles')

  class Meta:
    """docstring for Meta"""
    ordering = ['-created_on']

  def __str__(self):
    return self.name

class Skill(models.Model):
  """docstring for Contact"""
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='skill_profile')
  title = models.CharField(max_length=20, unique=True)
  percentage_rank = models.IntegerField()
  created_on = models.DateTimeField(auto_now_add=True)

class Contact(models.Model):
  """docstring for Contact"""
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='contact_profile')
  address = models.CharField(max_length=200)
  city = models.CharField(max_length=200)
  state = models.CharField(max_length=200)
  zip_code = models.IntegerField()
  email = models.EmailField(max_length=200)
  phone = models.CharField(max_length=15)
  created_on = models.DateTimeField(auto_now_add=True)

  class Meta:
    """docstring for Meta"""
    ordering = ['-created_on']

  def __str__(self):
    return self.email

class Portfolio(models.Model):
  """docstring for Portfolio"""
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='portfolio_profile')
  portfolio_type = models.ForeignKey(PortfolioCategory, on_delete=models.CASCADE, related_name='portfolios_type')
  image = models.ImageField(upload_to='images/portfolio', default=None)
  created_on = models.DateTimeField(auto_now_add=True)

  class Meta:
    """docstring for Meta"""
    ordering = ['-created_on']

  def __str__(self):
    return str(self.image)

class WorkExperience(models.Model):
  """docstring for Work"""
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='work_profile')
  work_place = models.CharField(max_length=200)
  job_title = models.CharField(max_length=200)
  description = models.CharField(max_length=200)
  start_date= models.DateField(max_length=20)
  end_date= models.DateField(max_length=20)
  created_on = models.DateTimeField(auto_now_add=True)

  class Meta:
    """docstring for Meta"""
    ordering = ['-start_date']

  def __str__(self):
    return self.job_title

class Education(models.Model):
  """docstring for Education"""
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='education_profile')
  school = models.CharField(max_length=200)
  qualification = models.CharField(max_length=200)
  description = models.CharField(max_length=200)
  start_date= models.DateField(max_length=20)
  end_date= models.DateField(max_length=20)
  created_on = models.DateTimeField(auto_now_add=True)

  class Meta:
    """docstring for Meta"""
    ordering = ['-start_date']

  def __str__(self):
    return self.school

class Achievement(models.Model):
  """docstring for Achievement"""
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='achievement_profile')
  number = models.IntegerField()
  title = models.CharField(max_length=200)
  created_on = models.DateTimeField(auto_now_add=True)

  class Meta:
    """docstring for Meta"""
    ordering = ['-created_on']

  def __str__(self):
    return self.title