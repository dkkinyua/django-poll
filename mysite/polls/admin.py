from django.contrib import admin
from .models import Question

# Register your models here.
# Makes the poll app modifiable from the admin interface by registering our model here into the site
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Add question", {"fields": ["question"]}),
        ("Date Information", {"fields": ["pub_date"]})
    ]

admin.site.register(Question, QuestionAdmin)