from django.db import models
import uuid


class Music(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    album = models.ForeignKey('Album',on_delete=models.CASCADE, null=True, blank=True)
    band = models.ForeignKey('Band',on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.title


class Album(models.Model):
    title = models.CharField(max_length=200)
    prefix = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=200)
    slug = models.SlugField()
    band = models.ForeignKey('Band',on_delete=models.CASCADE, null=True, blank=True)
    label = models.ForeignKey('Label', on_delete=models.CASCADE, null=True, blank=True)
    asin = models.UUIDField(unique=True, default=uuid.uuid4)
    release_date = models.DateField()
    cover_image = models.ImageField(upload_to='musicapp/static/images',null=True,blank=True)
    genre = models.ManyToManyField('Genre')

    def __str__(self):
        """String for representing the Model object."""
        return self.title


class Genre(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        """String for representing the Model object."""
        return self.title


class Label(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        """String for representing the Model object."""
        return self.title


class Band(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        """String for representing the Model object."""
        return self.title
