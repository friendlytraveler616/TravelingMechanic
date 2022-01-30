from django import forms
from .models import review, Commission

class createReview(forms.ModelForm):
    class Meta:
        model = review
        fields = ['stars', 'description', 'target', 'image', 'author']
        widgets = {'author':forms.HiddenInput()}

# class takerForm(forms.ModelForm):
#     class Meta:
#         model = Commission
#         fields = ['pknum']
#         widgets = {
#             'pknum': forms.textInput(attrs={
#                 'id': 'pknum',
#                 'required': True
#             }),
#         }
