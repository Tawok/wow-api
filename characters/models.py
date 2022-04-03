from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from wow import settings

class Character(models.Model):
    """Database model for characters"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name    = models.CharField(max_length =10, unique=True)

    MALE    = 'Male'
    FEMALE  = 'Female'
    
    GENDER_CHOICES  = [
        (MALE, 'male'),
        (FEMALE, 'female')
    ]

    gender  = models.CharField(max_length= 6, choices= GENDER_CHOICES, blank=False)

    HORDE   = 'Horde'
    ALLIANCE= 'Alliance'
    NEUTRAL = 'Neutral'
    
    FACTION_CHOICES = [
        (HORDE, 'horde'),
        (ALLIANCE, 'alliance'),
        (NEUTRAL, 'neutral')
    ]

    faction = models.CharField(max_length= 8, choices= FACTION_CHOICES, blank=False)

    HUMAN               = 'Human'
    DWARF               = 'Dwarf'
    NIGHT_ELF           = 'Night Elf'
    GNOME               = 'Gnome'
    DRAENEI             = 'Draenei'
    WORGEN              = 'Worgen'
    VOID_ELF            = 'Void Elf'
    LIGHTFORGED_DRAENEI = 'Lightforged Draenei'
    DARK_IRON_DWARF     = 'Dark Iron Dwarf'
    KULTIRAN            = 'Kultiran'
    MECHAGNOME          = 'Mechagnome'
    ORC                 = 'ORC'
    UNDEAD              = 'Undead'
    TAUREN              = 'Tauren'
    TROLL               = 'Troll'
    BLOODELF            = 'Blood Elf'
    GOBLIN              = 'Goblin'
    NIGHTBORNE          = 'Nightborne'
    HIGHMOUNTAIN_TAUREN = 'Highmountain Tauren'
    MAGHAR_ORC          = "Mag'har Orc"
    ZANDALARI_TROLL     = 'Zandalari Troll'
    VULPERA             = 'Vulpera'
    PANDAREN            = 'Pandaren'
    
    RACE_CHOICES = [
        (HUMAN, 'Human'),
        (DWARF, 'Dwarf'),
        (NIGHT_ELF, 'Night Elf'),
        (GNOME, 'Gnome'),
        (WORGEN, 'Worgen'),
        (VOID_ELF, 'Void Elf'),
        (LIGHTFORGED_DRAENEI, 'Lightforged Draenei'),
        (DARK_IRON_DWARF, 'Dark Iron Dwarf'),
        (KULTIRAN, 'Kultiran'),
        (MECHAGNOME, 'Mechagnome'),
        (ORC, 'Orc'),
        (UNDEAD, 'Undead'),
        (TAUREN, 'Tauren'),
        (TROLL, 'Troll'),
        (BLOODELF, 'Blood Elf'),
        (GOBLIN, 'Goblin'),
        (NIGHTBORNE, 'Nightborne'),
        (HIGHMOUNTAIN_TAUREN, 'Highmountain Tauren'),
        (MAGHAR_ORC, "Mag'har Orc"),
        (ZANDALARI_TROLL, 'Zandalari Troll'),
        (VULPERA, 'Vulpera'),
        (PANDAREN, 'Pandaren')
    ]

    race = models.CharField(max_length=21, choices=RACE_CHOICES, blank=False)

    WARRIOR         = 'Warrior'
    HUNTER          = 'Hunter'
    MAGE            = 'Mage'
    ROGUE           = 'Rogue'
    PRIEST          = 'Priest'
    WARLOCK         = 'Warlock'
    PALADIN         = 'Paladin'
    DRUID           = 'Druid'
    SHAMAN          = 'Shaman'
    MONK            = 'Monk'
    DEMON_HUNTER    = 'Demon Hunter'
    DEATH_KNIGHT    = 'Death Knight'

    CLASS_CHOICES = [
        (WARRIOR, 'Warrior'),
        (HUNTER, 'Hunter'),
        (MAGE, 'Mage'),
        (ROGUE, 'Rogue'),
        (PRIEST, 'Priest'),
        (WARLOCK, 'Warlock'),
        (PALADIN, 'Paladin'),
        (DRUID, 'Druid'),
        (SHAMAN, 'Shaman'),
        (MONK, 'Monk'),
        (DEMON_HUNTER, 'Demon Hunter'),
        (DEATH_KNIGHT, 'Death Knight')

    ]

    job = models.CharField(max_length=12, choices=CLASS_CHOICES, blank=False)

    age = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100000)])

    description = models.TextField(max_length=280, blank=True)

    def __str__(self):
        return f'{self.name}'  
