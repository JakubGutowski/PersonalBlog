from django import forms


class PostComent(forms.Form):
    nick = forms.CharField(label="nick", max_length=20)
    comment = forms.CharField(label="comment", max_length=140)
