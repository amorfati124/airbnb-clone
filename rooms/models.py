from django.db import models
from django_countries.fields import CountryField
from core import models as core_models


# Create your models here.


class AbstractItem(core_models.TimesStampedModel):

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):

    """Rooms time object definition"""

    class Meta:
        verbose_name = "Room Types"


class Amenity(AbstractItem):

    """Amenity model definition"""

    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):

    """ Facilitys model definition"""

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRules(AbstractItem):

    """House Rules """

    class Meta:
        verbose_name = "House Rules"


class Photo(core_models.TimesStampedModel):

    """ photo model definition """

    caption = models.CharField(max_length=80)
    file = models.ImageField()
    room = models.ForeignKey("Room", on_delete=models.CASCADE)


class Room(core_models.TimesStampedModel):
    """Rooms app"""

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    chech_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room_type = models.ForeignKey("RoomType", on_delete=models.SET_NULL, null=True)
    amenity = models.ManyToManyField("Amenity", blank=True,)
    facility = models.ManyToManyField("Facility", blank=True)
    house_rules = models.ManyToManyField("HouseRules", blank=True)

    def __str__(self):
        return self.name
