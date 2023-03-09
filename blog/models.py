from django.db import models


# Create your models here.
class Post(models.Model):
    """ Данные о статье """
    TOPIC_TYPES = [
        (1, 'Цветы комнатные'),
        (2, 'Цветы однолетние'),
        (3, 'Цветы многолетние'),
        (4, 'Декоративные кустарники'),
    ]
    title = models.CharField('Название статьи', max_length=150)
    text = models.TextField('Текст статьи')
    author = models.CharField('Автор', max_length=100)
    data = models.DateField('Дата публикации')
    img = models.ImageField('Изображение', upload_to='image/%Y')
    type = models.IntegerField(choices=TOPIC_TYPES)

    def __str__(self):
        return f'{self.title}, {self.author}'

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи сайта'


class Comments(models.Model):
    """Комментарии"""

    email = models.EmailField()
    name = models.CharField('Имя', max_length=50)
    text_comment = models.TextField('Текст комментария', max_length=1500)
    post = models.ForeignKey(Post, verbose_name='Статья', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.post}, {self.text_comment}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Likes(models.Model):
    """ Лайки для статьи """

    ip = models.CharField('IP-адрес', max_length=100)
    post_id = models.ForeignKey(Post, verbose_name='Статья', on_delete=models.CASCADE)
