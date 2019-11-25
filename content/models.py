from django.db import models
from django.contrib.auth.models import User


class SnAlbumType(models.Model):
    album_type = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.album_type


class SnContentType(models.Model):
    content_type = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.content_type


class VisibilityMode(models.Model):
    visibility_mode = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.visibility_mode


class SnAlbum(models.Model):
    album_name = models.CharField(max_length=100, blank=False, default="Gallery")
    album_type = models.ForeignKey(SnAlbumType, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album_date = models.DateTimeField(blank=False, auto_now=True)

    def __str__(self):
        return self.album_name


class SnContentDetail(models.Model):
    content_type = models.ForeignKey(SnContentType, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album = models.ForeignKey(SnAlbum, on_delete=models.CASCADE)
    is_featured = models.BooleanField(default=False, blank=False)
    is_captcha = models.BooleanField(default=False, blank=False)
    post = models.ForeignKey('timeline.Post', on_delete=models.CASCADE, related_name='post_content_reverse')
    file = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.file)
