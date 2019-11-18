from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('email', 'name', 'text', 'company_nama', 'company_rating')
