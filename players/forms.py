# File to hold forms in players app

class statForm(forms.Form):
    ppgCheck = forms.BooleanField(required=False)
    apgCheck = forms.BooleanField(required=False)
    rpgCheck = forms.BooleanField(required=False)
    spgCheck = forms.BooleanField(required=False)
    bpgCheck = forms.BooleanField(required=False)
    topgCheck = forms.BooleanField(required=False)
    fgCheck = forms.BooleanField(required=False)
    ftCheck = forms.BooleanField(required=False)
    threesCheck = forms.BooleanField(required=False)