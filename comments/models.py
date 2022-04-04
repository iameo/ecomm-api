from unicodedata import name
from django.contrib.auth import get_user_model

from django.db import models

from services.models import Product



# Create your models here.
class Comment(models.Model):

    review_on = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_discussed')
    commenter = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='user_comment')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'auth_comments'
        ordering = ['created_on']

    def dp(self):
        return self.commenter.display_photo

    def __str__(self):
        return 'Comment ({} by {})'.format(self.body[:20], self.commenter.full_name)