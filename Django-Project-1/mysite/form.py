from django import forms

class login(forms.Form):
	user    = forms.CharField()
	pwd 	= forms.CharField(
		widget=forms.TextInput(
        attrs={
          'type':'password',}
          )
        )
	
