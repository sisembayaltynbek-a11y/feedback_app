from django.db import models


class ReviewTable(models.Model):
    user_name = models.CharField(max_length=100)
    review_text = models.CharField(max_length=1000)
    rate = models.IntegerField()
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.user_name} {self.rate}'