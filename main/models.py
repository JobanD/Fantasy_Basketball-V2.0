from django.db import models
from django.utils.translation import gettext as _

import pandas as pd
import numpy as np
import scipy.stats as stats

# Create your models here.

class nba_players_21 (models.Model):
    fullName = models.CharField(_("full_name"), max_length=100)
    team = models.CharField(_("team"), max_length=5)
    position = models.CharField(_("position"), max_length=15)
    age = models.FloatField(_("age"), blank=True, default=None)
    gp = models.IntegerField(_("gp"), blank=True, default=None)
    mpg = models.FloatField(_("mpg"), blank=True, default=None)
    minP = models.FloatField(_("min%"), blank=True, default=None)        # Percentage of team minutes used by a player while he was on the floor
    usage = models.FloatField(_("usage%"), blank=True, default=None)     # usage percentage is an estimate of the percentage of team plays used by a player while he was on the floor
    toRate = models.FloatField(_("to rate"), blank=True, default=None)   # estimates the number of turnovers a player commits per 100 possessions
    fta = models.IntegerField(_("fta"), blank=True, default=None)
    ftP = models.FloatField(_("ft%"), blank=True, default=None)
    fga2 = models.IntegerField(_("fga2"), blank=True, default=None)                           # 2 point field goals attempted
    fga2P = models.FloatField(_("fga2%"), blank=True, default=None)                           # % made of two point field goals attempted
    fga3 = models.IntegerField(_("fga3"), blank=True, default=None)                           # 3 point field goals attempted
    fga3P = models.FloatField(_("fga3%"), blank=True, default=None)                           # % made of 3 point field goals attempted
    efg = models.FloatField(_("efg"), blank=True, default=None)                               # eFG% Formula=(FGM+ (0.5 x 3PM))/FGA
    ts = models.FloatField(_("ts"), blank=True, default=None)                                 # ts formula = pts/ (2 * (fga + 0.44*fta))
    ppg = models.FloatField(_("ppg"), blank=True, default=None)
    rpg = models.FloatField(_("rpg"), blank=True, default=None)
    trbP = models.FloatField(_("trb%"), blank=True, default=None)         # estimated percentage of available rebounds grabbed by the player while the player is on the court.
    apg = models.FloatField(_("apg"), blank=True, default=None)
    astP = models.FloatField(_("ast%"), blank=True, default=None)         # estimated percentage of teammate field goals a player assisted while the player is on the court
    spg = models.FloatField(_("spg"), blank=True, default=None)
    bpg = models.FloatField(_("bpg"), blank=True, default=None)
    topg = models.FloatField(_("topg"), blank=True, default=None)
    viv = models.FloatField(_("viv"), blank=True, default=None)           # measures a player’s ability to produce in points, assists, and rebounds. The average player will score around a five on the index
    ortg = models.FloatField(_("ortg"), blank=True, default=None)         # points produced by a player per 100 total individual possessions.
    drtg = models.FloatField(_("drtg"), blank=True, default=None)         # points saved by a player per 100 total possessions

class nba_players_20 (models.Model):
    fullName = models.CharField(_("full_name"), max_length=100)
    team = models.CharField(_("team"), max_length=5)
    position = models.CharField(_("position"), max_length=15)
    age = models.FloatField(_("age"), blank=True, default=None)
    gp = models.IntegerField(_("gp"), blank=True, default=None)
    mpg = models.FloatField(_("mpg"), blank=True, default=None)
    minP = models.FloatField(_("min%"), blank=True, default=None)        # Percentage of team minutes used by a player while he was on the floor
    usage = models.FloatField(_("usage%"), blank=True, default=None)     # usage percentage is an estimate of the percentage of team plays used by a player while he was on the floor
    toRate = models.FloatField(_("to rate"), blank=True, default=None)   # estimates the number of turnovers a player commits per 100 possessions
    fta = models.IntegerField(_("fta"), blank=True, default=None)
    ftP = models.FloatField(_("ft%"), blank=True, default=None)
    fga2 = models.IntegerField(_("fga2"), blank=True, default=None)                           # 2 point field goals attempted
    fga2P = models.FloatField(_("fga2%"), blank=True, default=None)                           # % made of two point field goals attempted
    fga3 = models.IntegerField(_("fga3"), blank=True, default=None)                           # 3 point field goals attempted
    fga3P = models.FloatField(_("fga3%"), blank=True, default=None)                           # % made of 3 point field goals attempted
    efg = models.FloatField(_("efg"), blank=True, default=None)                               # eFG% Formula=(FGM+ (0.5 x 3PM))/FGA
    ts = models.FloatField(_("ts"), blank=True, default=None)                                 # ts formula = pts/ (2 * (fga + 0.44*fta))
    ppg = models.FloatField(_("ppg"), blank=True, default=None)
    rpg = models.FloatField(_("rpg"), blank=True, default=None)
    trbP = models.FloatField(_("trb%"), blank=True, default=None)         # estimated percentage of available rebounds grabbed by the player while the player is on the court.
    apg = models.FloatField(_("apg"), blank=True, default=None)
    astP = models.FloatField(_("ast%"), blank=True, default=None)         # estimated percentage of teammate field goals a player assisted while the player is on the court
    spg = models.FloatField(_("spg"), blank=True, default=None)
    bpg = models.FloatField(_("bpg"), blank=True, default=None)
    topg = models.FloatField(_("topg"), blank=True, default=None)
    viv = models.FloatField(_("viv"), blank=True, default=None)           # measures a player’s ability to produce in points, assists, and rebounds. The average player will score around a five on the index
    ortg = models.FloatField(_("ortg"), blank=True, default=None)         # points produced by a player per 100 total individual possessions.
    drtg = models.FloatField(_("drtg"), blank=True, default=None)         # points saved by a player per 100 total possessions

class nba_players_19 (models.Model):
    fullName = models.CharField(_("full_name"), max_length=100)
    team = models.CharField(_("team"), max_length=5)
    position = models.CharField(_("position"), max_length=15)
    age = models.FloatField(_("age"), blank=True, default=None)
    gp = models.IntegerField(_("gp"), blank=True, default=None)
    mpg = models.FloatField(_("mpg"), blank=True, default=None)
    minP = models.FloatField(_("min%"), blank=True, default=None)        # Percentage of team minutes used by a player while he was on the floor
    usage = models.FloatField(_("usage%"), blank=True, default=None)     # usage percentage is an estimate of the percentage of team plays used by a player while he was on the floor
    toRate = models.FloatField(_("to rate"), blank=True, default=None)   # estimates the number of turnovers a player commits per 100 possessions
    fta = models.IntegerField(_("fta"), blank=True, default=None)
    ftP = models.FloatField(_("ft%"), blank=True, default=None)
    fga2 = models.IntegerField(_("fga2"), blank=True, default=None)                           # 2 point field goals attempted
    fga2P = models.FloatField(_("fga2%"), blank=True, default=None)                           # % made of two point field goals attempted
    fga3 = models.IntegerField(_("fga3"), blank=True, default=None)                           # 3 point field goals attempted
    fga3P = models.FloatField(_("fga3%"), blank=True, default=None)                           # % made of 3 point field goals attempted
    efg = models.FloatField(_("efg"), blank=True, default=None)                               # eFG% Formula=(FGM+ (0.5 x 3PM))/FGA
    ts = models.FloatField(_("ts"), blank=True, default=None)                                 # ts formula = pts/ (2 * (fga + 0.44*fta))
    ppg = models.FloatField(_("ppg"), blank=True, default=None)
    rpg = models.FloatField(_("rpg"), blank=True, default=None)
    trbP = models.FloatField(_("trb%"), blank=True, default=None)         # estimated percentage of available rebounds grabbed by the player while the player is on the court.
    apg = models.FloatField(_("apg"), blank=True, default=None)
    astP = models.FloatField(_("ast%"), blank=True, default=None)         # estimated percentage of teammate field goals a player assisted while the player is on the court
    spg = models.FloatField(_("spg"), blank=True, default=None)
    bpg = models.FloatField(_("bpg"), blank=True, default=None)
    topg = models.FloatField(_("topg"), blank=True, default=None)
    viv = models.FloatField(_("viv"), blank=True, default=None)           # measures a player’s ability to produce in points, assists, and rebounds. The average player will score around a five on the index
    ortg = models.FloatField(_("ortg"), blank=True, default=None)         # points produced by a player per 100 total individual possessions.
    drtg = models.FloatField(_("drtg"), blank=True, default=None)         # points saved by a player per 100 total possessions