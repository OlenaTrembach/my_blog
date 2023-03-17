from django.db.models.signals import post_save
from django.dispatch import receiver
import telegram
from blog.models import Post
import re
from io import BytesIO
from django.core.files.images import ImageFile

@receiver(post_save, sender=Post)
def send_article_to_telegram(sender, instance, **kwargs):
    cleaned_text = re.sub('<[^<]+?>', '', instance.text)
    trimmed_text = cleaned_text[:300]
    image = ImageFile(instance.img).file.read()
    image_bytes = BytesIO(image)
    bot = telegram.Bot(token='6218436186:AAF6HyIiFFd0DsQRZVzO1gGpRdRPzPtgNhY')
    chat_id = '-938036438'
    message = f'Новая статья: {instance.title}\n\n{trimmed_text}...\n\n Полная версия уже на нашем сайте!'
    bot.send_photo(chat_id=chat_id, photo=image_bytes, caption=message)
