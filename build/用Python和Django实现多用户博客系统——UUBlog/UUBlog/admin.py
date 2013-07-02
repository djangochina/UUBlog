from django.contrib import admin
from UUBlog.models import Category, Article

class CategoryInline(admin.TabularInline):
    model = Category
    extra = 3

class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title']}),
        (None,               {'fields': ['content']}),
        (None,               {'fields': ['category']}),
        #('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

    inlines = [CategoryInline]
    list_display = ('title', 'createtime')
    #list_filter = ['pub_date']
    #search_fields = ['question']
    #date_hierarchy = 'pub_date'

admin.site.register(Article, ArticleAdmin)