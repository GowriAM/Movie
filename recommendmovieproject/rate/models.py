from django.db import models
from book.models import Product

# Create your models here.
class Rate(models.Model):
    DoesNotExist = None
    objects = None
    rate_id=models.CharField(max_length=250,blank=True)
    date_added=models.DateField(auto_now_add=True)

    class Meta:
        db_table='Rate'
        ordering=['date_added']
    def __str__(self):
        return '{}'.format(self.rate_id)
class RateMovie(models.Model):
        DoesNotExist = None
        product=models.ForeignKey(Product,on_delete=models.CASCADE)
        rate=models.ForeignKey(Rate,on_delete=models.CASCADE)
        # quantity=models.IntegerField()
        active=models.BooleanField(default=True)
        class Meta:
            db_table='RateMovie'
        # def sub_total(self):
        #     return self.product.price * self.quantity
        def __str__(self):
            return '{}'.format(self.product)
