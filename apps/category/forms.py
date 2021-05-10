from django.forms import ModelForm

from apps.category.models import Category


class CategoryCreationForm(ModelForm):

    class Meta:
        model = Category
        fields = ['name']