from django.contrib import admin

# Register your models here.
from conversations.models import Conversations, Message


@admin.register(Conversations)
class ConversationsAdmin(admin.ModelAdmin):
    """Conversations Admin Definition"""

    list_display = ("__str__", "count_messages", "count_participants")


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    """Message Admin Definition"""

    list_display = ("__str__", "created")