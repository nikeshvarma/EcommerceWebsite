from django.db import models


class CarouselImage(models.Model):
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='carousel_img')

    def __str__(self):
        return self.description

    class Meta:
        db_table = 'tbl_carousel_images'
