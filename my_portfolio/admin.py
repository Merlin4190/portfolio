from django.contrib import admin
from . models import Template, MaritalStatus, Industry, PortfolioCategory, Profile, Contact, Portfolio, WorkExperience, Education, Achievement

# Register your models here.
class TemplateAdmin(admin.ModelAdmin):
  """docstring for PostAdmin"""

  list_display = ('title',)
  list_filter = ('title',)
  search_fields = ['title',]

admin.site.register(Template, TemplateAdmin)

class MaritalStatusAdmin(admin.ModelAdmin):
  """docstring for PostAdmin"""

  list_display = ('title',)
  list_filter = ('title',)
  search_fields = ['title',]

admin.site.register(MaritalStatus, MaritalStatusAdmin)

class IndustryAdmin(admin.ModelAdmin):
  """docstring for PostAdmin"""

  list_display = ('title',)
  list_filter = ('title',)
  search_fields = ['title',]
  prepopulated_fields = {'slug':('title',)}

admin.site.register(Industry, IndustryAdmin)

class PortfolioCategoryAdmin(admin.ModelAdmin):
  """docstring for CategoryAdmin"""
  list_display = ('title', 'slug', 'created_on')
  search_fields = ['title',]
  prepopulated_fields = {'slug':('title',)}
    
admin.site.register(PortfolioCategory, PortfolioCategoryAdmin)

class PortfolioInline(admin.StackedInline):
  model = Portfolio
  max_num = 10
  extra = 0

class WorkInline(admin.StackedInline):
  model = WorkExperience
  max_num = 2
  extra = 0

class ContactInline(admin.StackedInline):
  model = Contact
  max_num = 1
  extra = 0

class EducationInline(admin.StackedInline):
  model = Education
  max_num = 3
  extra = 0

class AchievementInline(admin.StackedInline):
  model = Achievement
  max_num = 4
  extra = 0

class ProfileAdmin(admin.ModelAdmin):
  """docstring for PostAdmin"""

  list_display = ('name', 'slug', 'email', 'position', 'industry', 'created_on')
  list_filter = ('industry',)
  search_fields = ['name', 'email', 'industry__title']
  prepopulated_fields = {'slug':('name',)}

  inlines = [ContactInline, PortfolioInline, WorkInline, EducationInline, AchievementInline]

admin.site.register(Profile, ProfileAdmin)

class ContactAdmin(admin.ModelAdmin):
  """docstring for PostAdmin"""

  list_display = ('address', 'email', 'phone', 'created_on')
  list_filter = ('created_on',)
  search_fields = ['email', 'phone']

# admin.site.register(Contact, ContactAdmin)