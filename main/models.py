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
    age = models.FloatField(_("age"), blank=True)
    gp = models.IntegerField(_("gp"), blank=True)
    mpg = models.FloatField(_("mpg"), blank=True)
    minP = models.FloatField(_("min%"), blank=True)        # Percentage of team minutes used by a player while he was on the floor
    usage = models.FloatField(_("usage%"), blank=True)     # usage percentage is an estimate of the percentage of team plays used by a player while he was on the floor
    toRate = models.FloatField(_("to rate"), blank=True)   # estimates the number of turnovers a player commits per 100 possessions
    fta = models.IntegerField(_("fta"), blank=True)
    ftP = models.FloatField(_("ft%"), blank=True)
    fga2 = models.IntegerField(_("fga2"), blank=True)                           # 2 point field goals attempted
    fga2P = models.FloatField(_("fga2%"), blank=True)                           # % made of two point field goals attempted
    fga3 = models.IntegerField(_("fga3"), blank=True)                           # 3 point field goals attempted
    fga3P = models.FloatField(_("fga3%"), blank=True)                           # % made of 3 point field goals attempted
    efg = models.FloatField(_("efg"), blank=True)                               # eFG% Formula=(FGM+ (0.5 x 3PM))/FGA
    ts = models.FloatField(_("ts"), blank=True)                                 # ts formula = pts/ (2 * (fga + 0.44*fta))
    ppg = models.FloatField(_("ppg"), blank=True)
    rpg = models.FloatField(_("rpg"), blank=True)
    trbP = models.FloatField(_("trb%"), blank=True)         # estimated percentage of available rebounds grabbed by the player while the player is on the court.
    apg = models.FloatField(_("apg"), blank=True)
    astP = models.FloatField(_("ast%"), blank=True)         # estimated percentage of teammate field goals a player assisted while the player is on the court
    spg = models.FloatField(_("spg"), blank=True)
    bpg = models.FloatField(_("bpg"), blank=True)
    topg = models.FloatField(_("topg"), blank=True)
    viv = models.FloatField(_("viv"), blank=True)           # measures a player’s ability to produce in points, assists, and rebounds. The average player will score around a five on the index
    ortg = models.FloatField(_("ortg"), blank=True)         # points produced by a player per 100 total individual possessions.
    drtg = models.FloatField(_("drtg"), blank=True)         # points saved by a player per 100 total possessions
    
    # Z score values below based off other fields
    # pointZ = models.FloatField(_("pointZ"), blank=True)
    # assistZ = models.FloatField(_("pointZ"), blank=True)
    # reboundZ = models.FloatField(_("pointZ"), blank=True)
    # stealZ = models.FloatField(_("pointZ"), blank=True)
    # blockZ = models.FloatField(_("pointZ"), blank=True)
    # turnoverZ = models.FloatField(_("pointZ"), blank=True)
    # fgZ = models.FloatField(_("pointZ"), blank=True)
    # ftZ = models.FloatField(_("pointZ"), blank=True)
    # threeZ = models.FloatField(_("pointZ"), blank=True)

    # def save(self):
        