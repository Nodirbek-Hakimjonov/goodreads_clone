from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import CustomUser
# from users.tasks import send_email

# @receiver(post_save,sender=CustomUser)
# def send_welcome_email(sender,instance,created,**kwargs):
#     if created:
#         send_email.delay(
#                 "Welcome to GoodReads clone",
#                 f"hi, {instance.username}. Welcome to GoodReads clone. Enjoy the books and reviews ",
#                 [instance.email]
#             )
@receiver(post_save, sender=CustomUser)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        send_mail(
            f"You have been successfuly registered!",
            f"Salom {instance.username}\n\nGoodReadsga xush kelibsiz! Ro'yxatdan o'tish jarayonini muvoffaqiyatli tugallandi.\n\nAgar sizning boshqa savollar yoki takliflaringiz bo'lsa https://t.me/javohirtwits kanal izohlariga yozishingiz mumkin.\n\nYana bir bor bizni tanlaganingiz uchun rahmat!\n\nHurmat bilan,\n\n{instance.first_name}\n\nGoodReads Jamoasi\n\n",
            "coderjek@gmail.com",
            [instance.email],
        )