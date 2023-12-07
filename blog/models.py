from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок:')
    slug = models.SlugField()

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title.__str__()

    def get_absolute_url(self):
        return '/%s/' % self.slug


class Post(models.Model):
    ACTIVE = 'active'
    DRAFT = 'draft'

    CHOICES_STATUS = (
        (ACTIVE, 'Active'),
        (DRAFT, 'Draft')
    )

    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Заголовок:')
    slug = models.SlugField()
    intro = models.TextField(verbose_name="Вступление:")
    body = models.TextField(verbose_name="Содержимое:")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Созданно в:")
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=ACTIVE)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)

    class Meta():
        ordering = ('-created_at',)

    def __str__(self):
        return self.title.__str__()

    def get_absolute_url(self):
        return '/%s/%s/' % (self.category.slug, self.slug)



class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE, )
    name = models.CharField(max_length=255, verbose_name='Имя:')
    email = models.EmailField(verbose_name='Email:')
    body = models.TextField(verbose_name='Контент:')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Созданно в:")

    class Meta():
        ordering = ('-created_at',)

    def __str__(self):
        return self.email.__str__()
