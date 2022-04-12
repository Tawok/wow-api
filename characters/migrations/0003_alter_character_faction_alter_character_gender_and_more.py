# Generated by Django 4.0.3 on 2022-04-10 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='faction',
            field=models.CharField(choices=[('horde', 'horde'), ('alliance', 'alliance'), ('neutral', 'neutral')], max_length=8),
        ),
        migrations.AlterField(
            model_name='character',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=6),
        ),
        migrations.AlterField(
            model_name='character',
            name='job',
            field=models.CharField(choices=[('warrior', 'warrior'), ('hunter', 'hunter'), ('mage', 'mage'), ('rogue', 'rogue'), ('priest', 'priest'), ('warlock', 'warlock'), ('paladin', 'paladin'), ('druid', 'druid'), ('shaman', 'shaman'), ('monk', 'monk'), ('demon hunter', 'demon hunter'), ('death knight', 'death knight')], max_length=12),
        ),
        migrations.AlterField(
            model_name='character',
            name='race',
            field=models.CharField(choices=[('human', 'human'), ('dwarf', 'dwarf'), ('night elf', 'night elf'), ('gnome', 'gnome'), ('worgen', 'worgen'), ('void Elf', 'void elf'), ('lightforged draenei', 'lightforged daenei'), ('dark iron dwarf', 'dark iron dwarf'), ('kultiran', 'kultiran'), ('mechagnome', 'mechagnome'), ('orc', 'orc'), ('undead', 'undead'), ('tauren', 'tauren'), ('troll', 'troll'), ('blood elf', 'blood elf'), ('goblin', 'goblin'), ('nightborne', 'nightborne'), ('highmountain tauren', 'highmountain tauren'), ('maghar orc', 'maghar orc'), ('zandalari troll', 'zandalari troll'), ('vulpera', 'vulpera'), ('pandaren', 'pandaren')], max_length=21),
        ),
    ]
