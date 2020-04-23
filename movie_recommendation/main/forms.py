from django import forms

class collab(forms.Form):
    u_id = forms.IntegerField(label="Input User ID  :", required=True)
    no_of_movie = forms.IntegerField(label="No. of movies :", required=True)


class cont(forms.Form):
    movie_name = forms.CharField(label="Movie name :", max_length=100, required=True)