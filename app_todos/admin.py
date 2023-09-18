from django.contrib import admin
from .models import Todos


# Register your models here.
# admin.site.register(Todos)
class TodosAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status')
    search_fields = ('title', 'description')
    list_filter = ['start_time', 'user']
admin.site.register(Todos, TodosAdmin)