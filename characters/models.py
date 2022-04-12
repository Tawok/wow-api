from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from wow import settings


class Character(models.Model):
    """Database model for characters"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=10, unique=True)

    MALE = 'male'
    FEMALE = 'female'

    GENDER_CHOICES = [
        (MALE, 'male'),
        (FEMALE, 'female')
    ]

    gender = models.CharField(
        max_length=6, choices=GENDER_CHOICES, blank=False)

    HORDE = 'horde'
    ALLIANCE = 'alliance'
    NEUTRAL = 'neutral'

    FACTION_CHOICES = [
        (HORDE, 'horde'),
        (ALLIANCE, 'alliance'),
        (NEUTRAL, 'neutral')
    ]

    faction = models.CharField(
        max_length=8, choices=FACTION_CHOICES, blank=False)

    HUMAN = 'human'
    DWARF = 'dwarf'
    NIGHT_ELF = 'night elf'
    GNOME = 'gnome'
    DRAENEI = 'draenei'
    WORGEN = 'worgen'
    VOID_ELF = 'void Elf'
    LIGHTFORGED_DRAENEI = 'lightforged draenei'
    DARK_IRON_DWARF = 'dark iron dwarf'
    KULTIRAN = 'kultiran'
    MECHAGNOME = 'mechagnome'
    ORC = 'orc'
    UNDEAD = 'undead'
    TAUREN = 'tauren'
    TROLL = 'troll'
    BLOODELF = 'blood elf'
    GOBLIN = 'goblin'
    NIGHTBORNE = 'nightborne'
    HIGHMOUNTAIN_TAUREN = 'highmountain tauren'
    MAGHAR_ORC = "maghar orc"
    ZANDALARI_TROLL = 'zandalari troll'
    VULPERA = 'vulpera'
    PANDAREN = 'pandaren'

    RACE_CHOICES = [
        (HUMAN, 'human'),
        (DWARF, 'dwarf'),
        (NIGHT_ELF, 'night elf'),
        (GNOME, 'gnome'),
        (WORGEN, 'worgen'),
        (VOID_ELF, 'void elf'),
        (LIGHTFORGED_DRAENEI, 'lightforged draenei'),
        (DARK_IRON_DWARF, 'dark iron dwarf'),
        (KULTIRAN, 'kultiran'),
        (MECHAGNOME, 'mechagnome'),
        (ORC, 'orc'),
        (UNDEAD, 'undead'),
        (TAUREN, 'tauren'),
        (TROLL, 'troll'),
        (BLOODELF, 'blood elf'),
        (GOBLIN, 'goblin'),
        (NIGHTBORNE, 'nightborne'),
        (HIGHMOUNTAIN_TAUREN, 'highmountain tauren'),
        (MAGHAR_ORC, "maghar orc"),
        (ZANDALARI_TROLL, 'zandalari troll'),
        (VULPERA, 'vulpera'),
        (PANDAREN, 'pandaren')
    ]

    race = models.CharField(max_length=21, choices=RACE_CHOICES, blank=False)

    WARRIOR = 'warrior'
    HUNTER = 'hunter'
    MAGE = 'mage'
    ROGUE = 'rogue'
    PRIEST = 'priest'
    WARLOCK = 'warlock'
    PALADIN = 'paladin'
    DRUID = 'druid'
    SHAMAN = 'shaman'
    MONK = 'monk'
    DEMON_HUNTER = 'demon hunter'
    DEATH_KNIGHT = 'death knight'

    CLASS_CHOICES = [
        (WARRIOR, 'warrior'),
        (HUNTER, 'hunter'),
        (MAGE, 'mage'),
        (ROGUE, 'rogue'),
        (PRIEST, 'priest'),
        (WARLOCK, 'warlock'),
        (PALADIN, 'paladin'),
        (DRUID, 'druid'),
        (SHAMAN, 'shaman'),
        (MONK, 'monk'),
        (DEMON_HUNTER, 'demon hunter'),
        (DEATH_KNIGHT, 'death knight')

    ]

    job = models.CharField(max_length=12, choices=CLASS_CHOICES, blank=False)

    age = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100000)])

    description = models.TextField(max_length=280, blank=True)

    def __str__(self):
        """Displays the name of the character"""
        return f'{self.name}'
