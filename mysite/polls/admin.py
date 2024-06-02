from django.contrib import admin
from .models import Choice, Question

# Register your models here.
# Makes the poll app modifiable from the admin interface by registering our model here into the site
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3 # Adds three extra columns for our choices every time we access a question

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Add question", {"fields": ["question"]}),
        ("Date Information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)