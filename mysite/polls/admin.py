from django.contrib import admin
from .models import Question

# Register your models here.
# Makes the poll app modifiable from the admin interfae by registering our model here into the site
admin.site.register(Question)