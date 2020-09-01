from . models import Comment, Post, PostImg
from django import forms
from django.forms import inlineformset_factory, formset_factory

from ckeditor_uploader.widgets import CKEditorUploadingWidget
from ckeditor.widgets import CKEditorWidget

class PostImgForm(forms.ModelForm):

  class Meta:
    model = PostImg
    fields = ('image',)
    max_num = 10
    extra = 0
PostImgFormset = formset_factory(PostImgForm, extra=0, can_delete=False)

class PostForm(forms.ModelForm):
  """docstring for PostForm"""
  # def __init__(self, arg):
  #   super(PostForm, self).__init__()
  #   self.arg = arg
  content = forms.CharField(widget=CKEditorUploadingWidget())
  class Meta:
    model = Post
    fields = ('title', 'content', 'author', 'status', 'categories')
    prepopulated_fields = {'slug':('title',)}

  def __init__(self, *args, **kwargs):
    super(PostForm, self).__init__(*args, **kwargs)
    self.fields['author'].empty_label = "Please Select Author"
    
class CommentForm(forms.ModelForm):
  """docstring for CommentForm"""
  # def __init__(self, arg):
  #   super(CommentForm, self).__init__()
  #   self.arg = arg
  class Meta:
    model = Comment
    fields = ('name', 'email', 'body')
    