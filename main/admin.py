from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django import forms
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import nba_players_21

## To add in a new dataset follow these steps
# 1. Create new model with the same fields as listed here
# 2. Ensure dataset is cleaned with header row removed
# 2. Change name inside the for loop to match new model
# 3. Register it at the bottom of this page

# Creating upload form field on admin page
class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()

# Handling csv uploads on admin page which populate django model
class nbaAdmin(admin.ModelAdmin):
    list_display = ('fullName','team','position','age','gp','mpg','minP','usage','toRate','fta',
    'ftP','fga2','fga2P','fga3','fga3P','efg','ts','ppg','rpg','trbP','apg','astP','spg','bpg','topg','viv','ortg','drtg')

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls

    def upload_csv(self, request):

        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]

            # Error handling
            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'Wrong file type, please try again with a csv')
                return HttpResponseRedirect(request.path_info)

            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")            # split by lines (each player)

            # loop through the points in each line seperating by comma (each player's stats)
            for x in csv_data:
                fields = x.split(",")
                created = nba_players_21.objects.update_or_create(
                    fullName = fields[0],
                    team = fields[1],
                    position = fields[2],
                    age = fields[3],
                    gp = fields[4],
                    mpg = fields[5],
                    minP = fields[6],
                    usage = fields[7],
                    toRate = fields[8],
                    fta = fields[9],
                    ftP = fields[10],
                    fga2 = fields[11],
                    fga2P = fields[12],
                    fga3 = fields[13],
                    fga3P = fields[14],
                    efg = fields[15],
                    ts = fields[16],
                    ppg = fields[17],
                    rpg = fields[18],
                    trbP = fields[19],
                    apg = fields[20],
                    astP = fields[21],
                    spg = fields[22],
                    bpg = fields[23],
                    topg = fields[24],
                    viv = fields[25],
                    ortg = fields[26],
                    drtg = fields[27]
                )
            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data = {"form": form}

        return render(request, "admin/csv_upload.html", data)


admin.site.register(nba_players_21, nbaAdmin)
