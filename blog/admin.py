from django.contrib import admin
from . models import Post, Comment, Category, PostImg

# Register your models here.
# class ThingInline(admin.StackedInline):
#   model = Category

class PostImgAdmin(admin.ModelAdmin):
  pass

class PostImgInline(admin.StackedInline):
  model = PostImg
  max_num = 10
  extra = 0

class PostAdmin(admin.ModelAdmin):
  """docstring for PostAdmin"""

  list_display = ('title', 'slug', 'status', 'created_on')
  list_filter = ('status',)
  search_fields = ['title', 'content']
  prepopulated_fields = {'slug':('title',)}
  inlines = [PostImgInline,]

  # def __init__(self, arg):
  #   super(PostAdmin, self).__init__()
  #   self.arg = arg

admin.site.register(PostImg, PostImgAdmin)
admin.site.register(Post, PostAdmin)
@admin.register(Comment)
# @admin.register(Category)

class CommentAdmin(admin.ModelAdmin):
  """docstring for CommentAdmin"""
  # def __init__(self, arg):
  #   super(CommentAdmin, self).__init__()
  #   self.arg = arg
  list_display = ('name', 'body', 'post', 'created_on', 'active')
  list_filter = ('active', 'created_on')
  search_fields = ('name', 'email', 'body')
  actions = ['approve_comments']

  def approve_comments(self, requests, queryset):
    queryset.update(active=False)

class CategoryAdmin(admin.ModelAdmin):
  """docstring for CategoryAdmin"""
  list_display = ('title', 'slug', 'created_on')
  search_fields = ['title',]
  prepopulated_fields = {'slug':('title',)}
    
admin.site.register(Category, CategoryAdmin)


