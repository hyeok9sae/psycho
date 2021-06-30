from django.db import models


class Store(models.Model):
    id = models.IntegerField(primary_key=True)
    tel = models.CharField(max_length=20, null=True)
    address1 = models.CharField(max_length=200, null=True)
    address2 = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=10, null=True)
    pos_x = models.FloatField(max_length=10, null=True)
    pos_y = models.FloatField(max_length=10, null=True)

    def __str__(self):
        return [self.id, self.address1, self.name, self.category, self.pos_x, self.pos_y]


class Hotel(models.Model):
    id = models.IntegerField(primary_key=True)
    tel = models.CharField(max_length=15, default=False)
    address1 = models.CharField(max_length=100, default=False)
    address2 = models.CharField(max_length=100, default=False)
    name = models.CharField(max_length=50, default=False)
    pos_x = models.FloatField(max_length=10, null=True)
    pos_y = models.FloatField(max_length=10, null=True)

    def __str__(self):
        return [self.id, self.tel, self.address1, self.name, self.pos_x, self.pos_y]


class District(models.Model):
    sido = models.CharField(max_length=20, default=False)
    gugun = models.CharField(max_length=20, default=False)
    dong = models.CharField(max_length=20, default=False)
    payment_count = models.BigIntegerField(max_length=20, default=False)

    def __str__(self):
        return [self.sido, self.gugun, self.dong]
