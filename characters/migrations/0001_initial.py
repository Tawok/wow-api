# Generated by Django 4.0.3 on 2022-04-03 22:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True)),
                ('gender', models.CharField(choices=[('Male', 'male'), ('Female', 'female')], max_length=6)),
                ('faction', models.CharField(choices=[('Horde', 'horde'), ('Alliance', 'alliance'), ('Neutral', 'neutral')], max_length=8)),
                ('race', models.CharField(choices=[('Human', 'Human'), ('Dwarf', 'Dwarf'), ('Night Elf', 'Night Elf'), ('Gnome', 'Gnome'), ('Worgen', 'Worgen'), ('Void Elf', 'Void Elf'), ('Lightforged Draenei', 'Lightforged Draenei'), ('Dark Iron Dwarf', 'Dark Iron Dwarf'), ('Kultiran', 'Kultiran'), ('Mechagnome', 'Mechagnome'), ('ORC', 'Orc'), ('Undead', 'Undead'), ('Tauren', 'Tauren'), ('Troll', 'Troll'), ('Blood Elf', 'Blood Elf'), ('Goblin', 'Goblin'), ('Nightborne', 'Nightborne'), ('Highmountain Tauren', 'Highmountain Tauren'), ("Mag'har Orc", "Mag'har Orc"), ('Zandalari Troll', 'Zandalari Troll'), ('Vulpera', 'Vulpera'), ('Pandaren', 'Pandaren')], max_length=21)),
                ('job', models.CharField(choices=[('Warrior', 'Warrior'), ('Hunter', 'Hunter'), ('Mage', 'Mage'), ('Rogue', 'Rogue'), ('Priest', 'Priest'), ('Warlock', 'Warlock'), ('Paladin', 'Paladin'), ('Druid', 'Druid'), ('Shaman', 'Shaman'), ('Monk', 'Monk'), ('Demon Hunter', 'Demon Hunter'), ('Death Knight', 'Death Knight')], max_length=12)),
                ('age', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100000)])),
                ('description', models.TextField(blank=True, max_length=280)),
            ],
        ),
    ]