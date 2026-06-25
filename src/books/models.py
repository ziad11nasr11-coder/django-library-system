from django.db import models
from django.core.validators import MinValueValidator

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return self.name

class Book(models.Model):
    class Language(models.TextChoices):
        ENGLISH = 'EN', 'English'
        ARABIC = 'AR', 'Arabic'
        GERMAN = 'DE', 'German'
    class Status(models.TextChoices):
        AVAILABLE = 'AV', 'Available'
        SOLD = 'SO', 'Sold'
        RENTAL = 'RE', 'Rental'  
        
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    description = models.TextField()
    number_of_pages = models.IntegerField(validators=[MinValueValidator(1)])    
    language = models.CharField(max_length=2, choices=Language.choices, default=Language.ENGLISH)
    cover_image = models.ImageField(upload_to='covers/%Y/%m/%d/', blank=True, null=True)

    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])
    retail_price_day = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])
    retail_period = models.IntegerField(validators=[MinValueValidator(1)], blank=True, null=True)  

    published_date = models.DateField() # Book publication date
    updated_at = models.DateTimeField(auto_now=True)

    active = models.BooleanField(default=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.AVAILABLE, blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['slug', 'author'], name='unique_book_slug_author')]
        
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