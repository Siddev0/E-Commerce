from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=100,null=True)

    def __str__(self):
        return '{}'.format(self.name)


class Book(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField(null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    image=models.ImageField(upload_to='Book_image')

    def __str__(self):
        return '{}'.format(self.title)

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Book)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_items')
    quantity = models.PositiveIntegerField(default=1)
