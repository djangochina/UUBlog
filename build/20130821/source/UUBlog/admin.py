from django.contrib import admin
from UUBlog.models import *
from django.contrib import admin
from django import forms

class CategoryAdmin(admin.ModelAdmin):
  
    list_display = ('name', 'alias','articles')
    #list_filter = ['pub_date']
    #search_fields = ['question']
    #date_hierarchy = 'pub_date'

admin.site.register(Category, CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
  
    list_display = ('title', 'category','views','createtime')
    #list_filter = ['pub_date']
    #search_fields = ['question']
    #date_hierarchy = 'pub_date'

admin.site.register(Post, PostAdmin)

class NavigateAdmin(admin.ModelAdmin):
  
    list_display = ('name', 'alias','position','url','target')
    #list_filter = ['pub_date']
    #search_fields = ['question']
    #date_hierarchy = 'pub_date'

admin.site.register(Navigate, NavigateAdmin)

class MyWidgetAdmin(admin.ModelAdmin):
  
    list_display = ('widget', 'title')
    #list_filter = ['pub_date']
    #search_fields = ['question']
    #date_hierarchy = 'pub_date'
    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(MyWidgetAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'params' or db_field.name == 'data':
            formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
            #formfield.widget = forms.Textarea(attrs={'cols': 80, 'rows': 20})
        return formfield

admin.site.register(MyWidget, MyWidgetAdmin)

class WidgetAdmin(admin.ModelAdmin):
  
    list_display = ('name', 'title')
    #list_filter = ['pub_date']
    #search_fields = ['question']
    #date_hierarchy = 'pub_date'
    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(WidgetAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'params' or db_field.name == 'data':
            formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
            #formfield.widget = forms.Textarea(attrs={'cols': 80, 'rows': 20})
        return formfield

admin.site.register(Widget, WidgetAdmin)