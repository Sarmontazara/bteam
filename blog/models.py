from django.db import models
from django.utils import timezone


class Status(models.Model):
    name = models.CharField(max_length=200, verbose_name=u'Статус', )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'Статус'
        verbose_name_plural = u'Статусы'


class Post(models.Model):
    author = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE,
        verbose_name=u'Пользователь',
    )
    title = models.CharField(max_length=200, verbose_name=u'Заголовок', )
    shorttext = models.TextField(verbose_name=u'Превью')
    fulltext = models.TextField(verbose_name=u'Текст')
    created_date = models.DateTimeField(
        default=timezone.now,
        verbose_name=u'Дата создания', )
    published_date = models.DateTimeField(
        blank=True, null=True, verbose_name=u'Дата публикации')
    artimgurl = models.CharField(max_length=200, verbose_name=u'Адрес картинки', blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = u'Статья'
        verbose_name_plural = u'Статьи'


class Order(models.Model):
    page = models.CharField(
        verbose_name=u'Страница',
        max_length=1024,
    )
    name = models.CharField(
        verbose_name=u'Имя',
        max_length=200,
    )
    email = models.EmailField(
        verbose_name=u'Почта',
        max_length=255,
    )
    date_created = models.DateTimeField(
        verbose_name=u'Дата создания',
        auto_now_add=True,
    )
    price = models.PositiveIntegerField(
        verbose_name=u'Цена',
    )
    zstatus = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name=u'Статус заявки', )

    sale = models.BooleanField(verbose_name=u'Акционная заявка', )

    def __str__(self):
        return (self.name + ' ' + self.email)

    class Meta:
        verbose_name = u'Заявка'
        verbose_name_plural = u'Заявки'
