from django import forms


class CreateTweetForm(forms.Form):
    title = forms.CharField(max_length=40)
    body = forms.CharField(widget=forms.Textarea, max_length=140)
