from django.db import models

from django.utils.translation import gettext as _

# Create your models here.

class Squirrel(models.Model):


    AM = 'AM'
    PM = 'PM'

    ADULT = 'ADULT'
    JUVENILE = 'JUVENILE'

    Gray = 'GRAY'
    Cinnamon = 'CINAMMON'
    Black = 'BLACK'


    AGE_CHOICES = (
            (ADULT, 'ADULT'),
            (JUVENILE, 'JUVENILE'),
        )

    TIME_CHOICES = (
            (AM, 'AM'),
            (PM, 'PM'),
        )

    X = models.DecimalField(
            help_text=_('Add the longitude of where the squirrel appears'),
            max_digits=50,
            decimal_places=30,
            blank = True,
        )

    Y = models.DecimalField(
            help_text=_('Add the latitude of where the squirrel appears'),
            max_digits =50,
            decimal_places = 30,
            blank = True,
        )
    

    Shift = models.CharField(
            help_text=_('Choose AM or PM'),
            max_length=10,
            choices=TIME_CHOICES,
            blank = True,
        )
    Date = models.IntegerField(
            help_text=_('When did the sighting happen?'),
            null = True,
            blank = True,
        )
    Unique_squirrel_ID = models.CharField(
            help_text=_('What is the unique_squirrel_ID?'),
            max_length=20,
            primary_key = True,
        )

    Age = models.CharField(
            help_text=_('Either Adult or Juvenile'),
            max_length=15,
            choices=AGE_CHOICES,
            blank=True,
        )

    COLOR_CHOICES = (
            (Gray, 'GRAY'),
            (Cinnamon, 'CINNAMON'),
            (Black, 'BLACK'),
        )

    Primary_Fur_Color = models.CharField(
            help_text=_('Either Gray,Cinnamon or Black'),
            max_length = 10,
            choices = COLOR_CHOICES,
            blank = True,
        )


    GROUND_PLANE = 'Ground Plane'
    ABOVE_GROUND = 'Above Ground'

    LOCATION= (
            (GROUND_PLANE,' Ground Plane'),
            (ABOVE_GROUND, 'Above Ground'),
        )

    Location = models.CharField(
            help_text=_('Either Ground Plane or Above Ground'),
            choices = LOCATION,
            blank = True,
            max_length = 20,
        )

    Specific_Location = models.CharField(
            help_text=_('Leave your comment about the location'),
            blank = True,
            max_length = 100,
        )

    Running = models.BooleanField(
            help_text=_('Either True or False'),
            default=False,
        )

    Chasing = models.BooleanField(
            help_text=_('Either True or False'),
            default=False,
         )
    Climbing = models.BooleanField(
            help_text=_('Either True or False'),
            default=False,
        )
    Eating = models.BooleanField(
            help_text=_('Either True or False'),
            default=False,
        )
     
    Foraging = models.BooleanField(
            help_text=_('Either True or False'),
            default=False,
        )
     
    Other_Activities = models.CharField(
            help_text=_('What other activities is the squirrel doing?'),
            blank=True,
            max_length = 100,
        )
            
    Kuks = models.BooleanField(
            help_text=_('Either True or False'),
            default=False,
        )
    

    Quaas = models.BooleanField(
            help_text=_('Either True or False'),
            default=False,
        )
     
    Moans = models.BooleanField(
            help_text=_('Either True or False'),
            default=False,
        )
            
    Tail_flags = models.BooleanField(
            help_text=_('Either True or False'),
            default=False,
        )
            
    Tail_twitching = models.BooleanField(
            help_text=_('Either True or False'),
            default=False,
        )
            
    Approaches = models.BooleanField(
        help_text=_('Either True or  False'),
        default=False,
        )
            
    Indifferent = models.BooleanField(
            help_text=_('Either True or  False'),
            default=False,
        )
    Runs_from = models.BooleanField(
            help_text=_('Either True or False'),
            default=False,
        )

    def __str__(self):
        return self.Unique_squirrel_ID
            














            
