from django.contrib import admin
from app.models import Author, JobPost,Location, Skill

class JobAdmin(admin.ModelAdmin):
    list_display = ('__str__','title', 'date', 'expiry_date', 'salary', 'slug')
    list_filter = ('date', 'expiry_date', 'salary')
    search_fields = ('title', 'description')
    search_help_text = 'Search by title or description'
    #fields= (('title', 'description'),'expiry_date',)
    #exclude = ('slug',)  # Exclude slug from the form
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', ('expiry_date', 'salary'))
        }),
        ('Advanced options', {
            'classes': ('collapse','wide'),
            'fields': ('slug',)
        }),
    )
# Register your models here.
admin.site.register(JobPost)
admin.site.register(Location)
admin.site.register(Author)
admin.site.register(Skill)

