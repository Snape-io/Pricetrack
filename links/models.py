from django.db import models
from .utlis import link_data

class Link(models.Model):
    productname = models.CharField(max_length=220, blank=True)
    url = models.URLField()
    current_price = models.FloatField(blank=True)
    old_price = models.FloatField(default=0)
    price_diff = models.FloatField(default=0)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.productname)

    class Meta:
        ordering = ('price_diff', '-created')

    def save(self, *args, **kwargs):
        productname, price = link_data(self.url)
        old_price = self.current_price
        if self.current_price:
            if price != old_price:
                price_diff = price - old_price
                self.price_diff = price_diff
                self.old_price = old_price
        else:
            self.old_price = 0
            self.price_diff = 0
        
        self.productname = productname
        self.current_price = price
        
        super().save(*args, **kwargs)

