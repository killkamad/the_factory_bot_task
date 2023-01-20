from django.db.models.signals import post_save
from django.dispatch import receiver
from core.celery_tasks import send_telegram_message
from core.models import Messages


@receiver(post_save, sender=Messages)
def send_message_to_telegram(sender, instance, *args, **kwargs):
    send_telegram_message.delay(instance.id)
