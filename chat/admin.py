
from django.contrib import admin
from chat.models import message

class MessageAdmin(admin.ModelAdmin):
    pass

admin.site.register(message, MessageAdmin)