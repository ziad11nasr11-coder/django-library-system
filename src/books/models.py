from django.db import models
from django.core.validators import MinValueValidator

class Book(models.Model):
    class Language(models.TextChoices):
        ENGLISH = 'EN', 'English'
        ARABIC = 'AR', 'Arabic'
        GERMAN = 'DE', 'German'

    #author = models.ForeignKey('Author', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    description = models.TextField()
    number_of_pages = models.IntegerField(validators=[MinValueValidator(1)])
    published_date = models.DateField() # Book publication date
    updated_at = models.DateTimeField(auto_now=True)
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True)
    language = models.CharField(max_length=2, choices=Language.choices, default=Language.ENGLISH)

    class Meta:
        #constraints = [
        #   models.UniqueConstraint(fields=['slug', 'author'], name='unique_book_slug_author')]
        
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        ordering = ['title']
        indexes = [
            models.Index(fields=['title']),
            models.Index(fields=['published_date']),
            models.Index(fields=['language']),
            #models.Index(fields=['author']),

        ]
    def __str__(self):
        return self.title