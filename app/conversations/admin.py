from django.contrib import admin

# Register your models here.
from conversations.models import Conversations, Message


@admin.register(Conversations)
class ConversationsAdmin(admin.ModelAdmin):
    """Conversations Admin Definition"""
    pass


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    """Message Admin Definition"""
    pass
