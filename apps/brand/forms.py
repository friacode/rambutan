from django.forms import ModelForm

from apps.brand.models import Brand


class BrandCreationForm(ModelForm):

    class Meta:
        model = Brand
        fields = ['name']