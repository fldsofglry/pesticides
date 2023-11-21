from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    
    # implement later
    # street1 = models.CharField(max=200)
    # street2 = models.CharField(max=100)
    # city = models.CharField(max_length=100)
    # state = models.CharField(max_length=2)
    # zip = models.CharField(max_length=20)

    def __str__(self):
        return self.name

# these are additives to make pesticide formulas more effective
class Adjuvant(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    epa_number = models.CharField(max_length=25, blank=True) 
    manufacturer = models.ForeignKey(Manufacturer, null=True, on_delete=models.SET_NULL, blank=True)
    # formulas = models.ManyToManyField(Pesticide, through='Formula')
    def __str__(self):
        return self.name
    
class Pesticide(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    epa_number = models.CharField(max_length=25)
    manufacturer = models.ForeignKey(Manufacturer, null=True, blank=True, on_delete=models.SET_NULL)
    formulas = models.ManyToManyField(Adjuvant, through='Formula')

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
        (ACTIVE, "Active"),
    ] 
    status = models.CharField(
        max_length = 1,
        choices=STATUS_CHOICES,
        default=ACTIVE,
    )

    def __str__(self):
        return self.name

class Formula(models.Model):
     # using concentrations as choices, but could conceivably use this 
    # as an enum type where. I am hesistant to use enum, because 
    # python assigned the label automatically
    PERCENT_CONCENTRATION = 'P'
    GALLON_CONCENTATION = 'G'
    
    CONCENTRATION_CHOICES = [
        (PERCENT_CONCENTRATION, "%"),
        (GALLON_CONCENTATION, "/gallon")
    ]

    name = models.CharField(max_length=200, blank=False, null=False)
    pesticide = models.ForeignKey(Pesticide, on_delete=models.CASCADE)
    adjuvant = models.ForeignKey(Adjuvant, on_delete=models.CASCADE)
    pesticide_amount = models.DecimalField(max_length=20,
                                 max_digits=6,
                                 decimal_places=3,
                                 null=True
                                )
    
    concentration = models.CharField(
        max_length=2, 
        choices=CONCENTRATION_CHOICES, 
        default=PERCENT_CONCENTRATION
    )

    adjuvant_amount = models.DecimalField(max_length=20,
                                 max_digits=4,
                                 decimal_places=3,
                                 null=True
                                )
   
    adjuvant_concentration = models.CharField(
        max_length=2, 
        choices=CONCENTRATION_CHOICES, 
        default=PERCENT_CONCENTRATION
    )

    def __str__(self):
        return self.name

class Region(models.Model):
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )
    abbreviation = models.CharField(
        max_length=20,
    )

    def __str__(self):
        return self.name

class Park(models.Model):
    name = models.CharField(
        max_length=200,
        null=False,
        blank=False,
    )
    abbreviation = models.CharField(
        max_length=10,
        null=True,
        blank=True
    )
    region = models.ForeignKey(Region, models.SET_NULL, blank=True,null=True)

    def __str__(self):
        return self.name

class Applicator(models.Model):
    first_name = models.CharField(
        max_length=200,
        null=False,
        blank=False,
    )
    last_name = models.CharField(
        max_length=200,
    )
    applicator_number = models.CharField(
        max_length=20,
        null=True,
        blank=True,
    )
    home_park = models.ForeignKey(Park, models.SET_NULL, blank=True,null=True)   

    def __str__(self):
        return self.first_name + " " + self.last_name

class Record(models.Model):
    applicator = models.ForeignKey(Applicator, models.DO_NOTHING)
    park = models.ForeignKey(Park, models.DO_NOTHING)
    formula = models.ForeignKey(Formula, models.DO_NOTHING)
    area_size = models.CharField(max_length=100) 
    date = models.DateTimeField()
    targeted_species = models.CharField(max_length=200,null=False)
    weather = models.CharField(
        max_length=200,
        null=False,
        blank=False,
    )

    # expected input is 5 mph West for speed and direction 
    wind = models.CharField
    
    #still need to figure out how I want to handle total amount applied
    # due to having multiple pesticides in the formula
    # total_amount_applied
    def __str__(self):
        summary = str(self.formula) + " " + str(self.park) + " " + str(self.date) 
        return summary