from django.core.management.base import BaseCommand
from django.utils import timezone
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        channel_layer = get_channel_layer()
        print("hello")
        async_to_sync(channel_layer.group_send)("chat_first", {
                    'type': 'chat_message',
                    'message': "notification",
                    })