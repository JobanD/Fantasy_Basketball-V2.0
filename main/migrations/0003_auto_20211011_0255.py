# Generated by Django 3.2.6 on 2021-10-11 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20211011_0227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nba_players_20',
            name='age',
            field=models.FloatField(blank=True, default=None, verbose_name='age'),
        ),
        migrations.AlterField(
            model_name='nba_players_20',
            name='apg',
            field=models.FloatField(blank=True, default=None, verbose_name='apg'),
        ),
        migrations.AlterField(
            model_name='nba_players_20',
            name='astP',
            field=models.FloatField(blank=True, default=None, verbose_name='ast%'),
        ),
        migrations.AlterField(
            model_name='nba_players_20',
            name='bpg',
            field=models.FloatField(blank=True, default=None, verbose_name='bpg'),
        ),
        migrations.AlterField(
            model_name='nba_players_20',
            name='drtg',
            field=models.FloatField(blank=True, default=None, verbose_name='drtg'),
        ),
        migrations.AlterField(
            model_name='nba_players_20',
            name='efg',
            field=models.FloatField(blank=True, default=None, verbose_name='efg'),
        ),
        migrations.AlterField(
            model_name='nba_players_20',
            name='fga2',
            field=models.IntegerField(blank=True, default=None, verbose_name='fga2'),
        ),
        migrations.AlterField(
            model_name='nba_players_20',
            name='fga2P',
            field=models.FloatField(blank=True, default=None, verbose_name='fga2%'),
        ),
        migrations.AlterField(
            model_name='nba_players_20',
            name='fga3',
            field=models.IntegerField(blank=True, default=None, verbose_name='fga3'),
        ),
        migrations.AlterField(
            model_name='nba_players_20',
            name='fga3P',
            field=models.FloatField(blank=True, default=None, verbose_name='fga3%'),
        ),
        migrations.AlterField(
            model_name='nba_players_20',
            name='ftP',
            field=models.FloatField(blank=True, default=None, verbose_name='ft%'),
        ),
        migrations.AlterField(
            model_name='nba_players_20',
            name='fta',
            field=models.IntegerField(blank=True, default=None, verbose_name='fta'),
        ),
        migrations.AlterField(
            model_name='nba_players_20',
            name='gp',
            field=models.IntegerField(blank=True, default=None, verbose_name='gp'),
        ),
        migrations.AlterField(
            model_name='nba_players_20',
            name='minP',
            field=models.FloatField(blank=True, default=None, verbose_name='min%'),
        ),
        migrations.AlterField(
            model_name='nba_players_20',
            name='mpg',
            field=models.FloatField(blank=True, default=None, verbose_name='mpg'),
        ),
        migrations.AlterField(
            model_name='nba_players_20',
            name='ortg',
            field=models.FloatField(blank=True, default=None, verbose_name='ortg'),
        ),
        migrations.AlterField(
            model_name='nba_players_20',
            name='ppg',
            field=models.FloatField(blank=True, default=None, verbose_name='ppg'),
        ),
        migrations.AlterField(
            model_name='nba_players_20',
            name='rpg',
            field=models.FloatField(blank=True, default=None, verbose_name='rpg'),
        ),
        migrations.AlterField(
            model_name='nba_players_20',
            name='spg',
            field=models.FloatField(blank=True, default=None, verbose_name='spg'),
        ),
        migrations.AlterField(
            model_name='nba_players_20',
            name='toRate',
            field=models.FloatField(blank=True, default=None, verbose_name='to rate'),
        ),
        migrations.AlterField(
            model_name='nba_players_20',
            name='topg',
            field=models.FloatField(blank=True, default=None, verbose_name='topg'),
        ),
        migrations.AlterField(
            model_name='nba_players_20',
            name='trbP',
            field=models.FloatField(blank=True, default=None, verbose_name='trb%'),
        ),
        migrations.AlterField(
            model_name='nba_players_20',
            name='ts',
            field=models.FloatField(blank=True, default=None, verbose_name='ts'),
        ),
        migrations.AlterField(
            model_name='nba_players_20',
            name='usage',
            field=models.FloatField(blank=True, default=None, verbose_name='usage%'),
        ),
        migrations.AlterField(
            model_name='nba_players_20',
            name='viv',
            field=models.FloatField(blank=True, default=None, verbose_name='viv'),
        ),
        migrations.AlterField(
            model_name='nba_players_21',
            name='age',
            field=models.FloatField(blank=True, default=None, verbose_name='age'),
        ),
        migrations.AlterField(
            model_name='nba_players_21',
            name='apg',
            field=models.FloatField(blank=True, default=None, verbose_name='apg'),
        ),
        migrations.AlterField(
            model_name='nba_players_21',
            name='astP',
            field=models.FloatField(blank=True, default=None, verbose_name='ast%'),
        ),
        migrations.AlterField(
            model_name='nba_players_21',
            name='bpg',
            field=models.FloatField(blank=True, default=None, verbose_name='bpg'),
        ),
        migrations.AlterField(
            model_name='nba_players_21',
            name='drtg',
            field=models.FloatField(blank=True, default=None, verbose_name='drtg'),
        ),
        migrations.AlterField(
            model_name='nba_players_21',
            name='efg',
            field=models.FloatField(blank=True, default=None, verbose_name='efg'),
        ),
        migrations.AlterField(
            model_name='nba_players_21',
            name='fga2',
            field=models.IntegerField(blank=True, default=None, verbose_name='fga2'),
        ),
        migrations.AlterField(
            model_name='nba_players_21',
            name='fga2P',
            field=models.FloatField(blank=True, default=None, verbose_name='fga2%'),
        ),
        migrations.AlterField(
            model_name='nba_players_21',
            name='fga3',
            field=models.IntegerField(blank=True, default=None, verbose_name='fga3'),
        ),
        migrations.AlterField(
            model_name='nba_players_21',
            name='fga3P',
            field=models.FloatField(blank=True, default=None, verbose_name='fga3%'),
        ),
        migrations.AlterField(
            model_name='nba_players_21',
            name='ftP',
            field=models.FloatField(blank=True, default=None, verbose_name='ft%'),
        ),
        migrations.AlterField(
            model_name='nba_players_21',
            name='fta',
            field=models.IntegerField(blank=True, default=None, verbose_name='fta'),
        ),
        migrations.AlterField(
            model_name='nba_players_21',
            name='gp',
            field=models.IntegerField(blank=True, default=None, verbose_name='gp'),
        ),
        migrations.AlterField(
            model_name='nba_players_21',
            name='minP',
            field=models.FloatField(blank=True, default=None, verbose_name='min%'),
        ),
        migrations.AlterField(
            model_name='nba_players_21',
            name='mpg',
            field=models.FloatField(blank=True, default=None, verbose_name='mpg'),
        ),
        migrations.AlterField(
            model_name='nba_players_21',
            name='ortg',
            field=models.FloatField(blank=True, default=None, verbose_name='ortg'),
        ),
        migrations.AlterField(
            model_name='nba_players_21',
            name='ppg',
            field=models.FloatField(blank=True, default=None, verbose_name='ppg'),
        ),
        migrations.AlterField(
            model_name='nba_players_21',
            name='rpg',
            field=models.FloatField(blank=True, default=None, verbose_name='rpg'),
        ),
        migrations.AlterField(
            model_name='nba_players_21',
            name='spg',
            field=models.FloatField(blank=True, default=None, verbose_name='spg'),
        ),
        migrations.AlterField(
            model_name='nba_players_21',
            name='toRate',
            field=models.FloatField(blank=True, default=None, verbose_name='to rate'),
        ),
        migrations.AlterField(
            model_name='nba_players_21',
            name='topg',
            field=models.FloatField(blank=True, default=None, verbose_name='topg'),
        ),
        migrations.AlterField(
            model_name='nba_players_21',
            name='trbP',
            field=models.FloatField(blank=True, default=None, verbose_name='trb%'),
        ),
        migrations.AlterField(
            model_name='nba_players_21',
            name='ts',
            field=models.FloatField(blank=True, default=None, verbose_name='ts'),
        ),
        migrations.AlterField(
            model_name='nba_players_21',
            name='usage',
            field=models.FloatField(blank=True, default=None, verbose_name='usage%'),
        ),
        migrations.AlterField(
            model_name='nba_players_21',
            name='viv',
            field=models.FloatField(blank=True, default=None, verbose_name='viv'),
        ),
    ]
