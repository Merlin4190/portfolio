from django.db import models
from django.contrib.auth.models import User
# from django.urls import reverse

# Create your models here.
STATUS =(
  (0, 'Draft'),
  (1, 'Publish')
)

class Category(models.Model):
  """docstring for Cateory"""
  # def __init__(self, arg):
  #   super(Cateory, self).__init__()
  #   self.arg = arg
  title= models.CharField(max_length=200, unique=True)
  slug= models.SlugField(max_length=200, unique=True)
  created_on= models.DateTimeField(auto_now_add=True)
  updated_on= models.DateTimeField(auto_now=True)

  # def cat(self):
  #   return self.title

  class Meta:
    """docstring for Meta"""
    ordering = ['-created_on']

  def __str__(self):
    return self.title

  # def get_absolute_url(self):
  #   return reverse('category:category_detail', args=[self.slug])

class Post(models.Model):
  """docstring for Post"""
  # def __init__(self, arg):
  #   super(Post, self).__init__()
  #   self.arg = arg
  title= models.CharField(max_length=200, unique=True)
  slug= models.SlugField(max_length=200, unique=True)
  content= models.TextField(unique=True)
  author= models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post')
  status= models.IntegerField(choices=STATUS, default=0)
  created_on= models.DateTimeField(auto_now_add=True)
  updated_on= models.DateTimeField(auto_now=True)
  # image = models.ImageField(upload_to='images')

  categories = models.ManyToManyField(Category, related_name='posts')

  class Meta:
    """docstring for Meta"""
    ordering = ['-created_on']

  def publish(self):
    self.status = True
    self.save()

  def approved_comments(self):
    return self.comments.filter(active=True)

  def __str__(self):
    return self.title

  # def get_absolute_url(self):
  #   return reverse('nu:post_detail', args=[self.slug])

class Comment(models.Model):
  """docstring for Comment"""
  # def __init__(self, arg):
  #   super(Comment, self).__init__()
  #   self.arg = arg
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
  name = models.CharField(max_length=80)
  email = models.EmailField()
  body = models.TextField()
  created_on = models.DateTimeField(auto_now_add=True)
  active = models.BooleanField(default=False)

  class Meta:
    ordering = ['-created_on']

  def approve(self):
    self.active = True
    self.save()

  def __str__(self):
    return 'Comment {} by {}'.format(self.body, self.name)

class PostImg(models.Model):
  """docstring for PostImg"""
  # def __init__(self, arg):
  #   super(PostImg, self).__init__()
  #   self.arg = arg
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='postImages')
  image = models.ImageField(upload_to='images')

  class Meta:
    """docstring for Meta"""
    ordering = ['-post']

  def __str__(self):
    return str(self.image)
    
    
    