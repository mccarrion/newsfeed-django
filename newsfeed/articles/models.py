from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from easy_thumbnails.fields import ThumbnailerImageField
from hitcount.models import HitCount, HitCountMixin


class Article(models.Model, HitCountMixin):
    """
    This is the model for all of the articles that will be written in the news
    website. For an attribute with multiple constraints, each constraint is put
    on its own line. Way more readable.
    """
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=128)
    thumbnail = ThumbnailerImageField(
        upload_to='thumbnail', 
        blank=True,
        null=True, 
        resize_source=dict(size=(150, 150), crop="True"), 
        max_length=255
    )
    author = models.ManyToManyField('users.User')
    image = models.ImageField(
        upload_to='articles', 
        blank=True,
        null=True, 
        max_length=255
    )
    body = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(max_length=128, unique=True, blank=True)

    # This is for displaying the most popular articles
    hit_count_generic = GenericRelation(
        HitCount,
        object_id_field='object_pk',
        related_query_name='hit_count_generic_relation'
    )

    # This list will be used to break up the news website into subsections
    # based on what subjects the publisher decides to include
    TECH = 'tech'
    BUSINESS = 'business'
    WORLD = 'world'
    SCIENCE = 'science'

    # Using an array of tuples to allow publisher to define subjects
    # to include in their news website.
    SUBJECT_CHOICES = (
        (TECH, 'Tech'),
        (BUSINESS, 'Business'),
        (WORLD, 'World'),
        (SCIENCE, 'Science'),
    )

    subject = models.CharField(
        max_length=9,
        choices=SUBJECT_CHOICES,
        default='science'
    )

    #TODO: Add a check for uniqueness
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    This model stores the user's comments.
    """
    body = models.TextField(max_length=1024)
    date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    article = models.ForeignKey('articles.Article', on_delete=models.CASCADE)
