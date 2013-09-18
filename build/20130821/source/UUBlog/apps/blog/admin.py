#-*- coding:utf-8 -*-

from django.contrib import admin
from django import forms


from UUBlog.apps.blog.models import *

#文章管理
class ArticleAdmin(admin.ModelAdmin):
    list_display=("title","username","views","comments","createtime")

admin.site.register(Article,ArticleAdmin)


#频道管理
class ChannelAdmin(admin.ModelAdmin):
    list_display=("id","parent_id","name","sortnum")

admin.site.register(Channel,ChannelAdmin)

#------begin 碎片管理--------


#碎片分类
class BlockCategoryAdmin(admin.ModelAdmin):
    list_display=("id","namecn")
admin.site.register(BlockCategory,BlockCategoryAdmin)

#碎片管理
class BlockAdmin(admin.ModelAdmin):
    list_display=("id","name","namecn","type","createtime")
admin.site.register(Block,BlockAdmin)


#代码碎片
class Block1Admin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "block":
            kwargs["queryset"] = Block.objects.filter(type=1)
        return super(Block1Admin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    list_display=("id","block","createtime")
admin.site.register(Block1,Block1Admin)

#静态碎片
class Block2Admin(admin.ModelAdmin):
    #外键选择
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "block":
            kwargs["queryset"] = Block.objects.filter(type=2)
        return super(Block2Admin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(Block2Admin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'summary':
            formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
            #formfield.widget = forms.Textarea(attrs={'cols': 80, 'rows': 20})
        return formfield

    list_display=("id","block","title","createtime")
admin.site.register(Block2,Block2Admin)
#---------end 碎片管理-----------



#Widget管理
class WidgetAdmin(admin.ModelAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(WidgetAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'render':
            formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
            #formfield.widget = forms.Textarea(attrs={'cols': 80, 'rows': 20})
        return formfield
    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(WidgetAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'attdef' or db_field.name == 'jsondef' or db_field.name == 'defaultdata' or db_field.name == 'render':
            formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
            #formfield.widget = forms.Textarea(attrs={'cols': 80, 'rows': 20})
        return formfield

    list_display=("name","title","datafrom","issys")
admin.site.register(Widget,WidgetAdmin)

#from UUBlog.models import Category, Article

#class CategoryInline(admin.TabularInline):
#    model = Category
#    extra = 3

#class ArticleAdmin(admin.ModelAdmin):
#    fieldsets = [
#        (None,               {'fields': ['title']}),
#        (None,               {'fields': ['content']}),
#        (None,               {'fields': ['blogpubcategory']}),
#        #('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#    ]

#    inlines = [CategoryInline]
#    list_display = ('title', 'createtime')
#    #list_filter = ['pub_date']
#    #search_fields = ['question']
#    #date_hierarchy = 'pub_date'

