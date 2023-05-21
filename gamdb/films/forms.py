from django import forms


class CustomRadioSelect(forms.RadioSelect):
    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option_attrs = attrs.copy() if attrs else {}
        option_attrs['class'] = f'radio-choice-{value}'
        return super().create_option(name, value, label, selected, index, subindex=subindex, attrs=option_attrs)

CHOICES = [('T','Rotten potato'),('F','Golden fries')]
class CommentForm(forms.Form):
    author = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Your name"}))
    text = forms.CharField(required=False, widget=forms.Textarea(attrs={"rows": 5, "class": "form-control"}))
    
    rating=forms.ChoiceField(widget=CustomRadioSelect(), choices=CHOICES, initial='T')
    #rating = forms.IntegerField(required=False)