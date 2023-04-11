from django.db import models

def synonyms_default():
    return {"synonims":[]}

# Create your models here.
class Location(models.Model):
    title = models.TextField(max_length=100,blank=False, verbose_name="Местоположение")
    gpostCode = models.IntegerField(blank=False,null=False, verbose_name="код страны для почты Грузии")
    postcodeFormat = models.TextField(max_length=20,blank=True, verbose_name="Формат индекса")
    phoneLength = models.IntegerField(default=10, verbose_name="Длина номера телефона без кода")
    countryPhoneCode = models.TextField(max_length=5,blank=False, verbose_name="Телефонный код страны")
    isEU = models.BooleanField(default=True, verbose_name="Входит в ЕС")
    synonims = models.JSONField(default=synonyms_default, verbose_name="синонимы")

    def __str__(self):
        return self.title

class Address(models.Model):
    postCode = models.TextField(max_length=10, null=False, blank=False, verbose_name="Индекс")
    city = models.TextField(max_length=100, null=False, blank=False, verbose_name="Населенный пункт")
    addressLine = models.TextField(max_length=200, null=False, blank=False, verbose_name="Строка адреса")
    firstName = models.TextField(max_length=100, null=False, blank=False, verbose_name="Имя")
    lastName = models.TextField(max_length=100, null=False, blank=False, verbose_name="Фамилия")
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.location.__str__() + " " + self.city + " " + self.addressLine + " " + self.postCode + " " + self.firstName + " " + self.lastName

class BillingAddress(models.Model):
    postCode = models.TextField(max_length=10, null=False, blank=False, verbose_name="Индекс")
    city = models.TextField(max_length=100, null=False, blank=False, verbose_name="Населенный пункт")
    addressLine = models.TextField(max_length=200, null=False, blank=False, verbose_name="Строка адреса")
    firstName = models.TextField(max_length=100, null=False, blank=False, verbose_name="Имя")
    lastName = models.TextField(max_length=100, null=False, blank=False, verbose_name="Фамилия")
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.location.__str__() + " " + self.city + " " + self.addressLine + " " + self.postCode + " " + self.firstName + " " + self.lastName