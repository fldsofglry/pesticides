from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    
    # implement later
    # street1 = models.CharField(max=200)
    # street2 = models.CharField(max=100)
    # city = models.CharField(max_length=100)
    # state = models.CharField(max_length=2)
    # zip = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Pesticide(models.Model):
    name = models.CharField(max_length=100)
    epa_number = models.CharField(max_length=25)
    manufacturer = models.ForeignKey(Manufacturer, null=True, blank=True, on_delete=models.SET_NULL)
    # using non-standard abbreviations for signal words for enum
    # just because I need something for the tuple
    CAUTION = "C"
    DANGER = "D"
    WARNING = "W"

    SIGNAL_WORD_CHOICES = [
        (CAUTION, "Caution"),
        (DANGER, "Danger"),
        (WARNING, "Warning"),
    ]
    
    signal_word = models.CharField(
        max_length=2,
        choices=SIGNAL_WORD_CHOICES,
    )

    INACTIVE = "I"
    TRIAL = "T"
    RETIRED = "R"
    ACTIVE = "A"

    STATUS_CHOICES = [
        (INACTIVE, "Inactive"),
        (TRIAL, "Trial"),
        (RETIRED, "Retired"),
        (INACTIVE, "Inactive"),
    ] 
    status = models.CharField(
        max_length = 1,
        choices=STATUS_CHOICES,
        default=ACTIVE,
    )

    def __str__(self):
        return self.name
