from django.forms import ModelForm
from django import forms
from apps.products.models import Product, ProductImage
from apps.category.models import Category
from apps.brand.models import Brand

TYPES = (('CP', '소모품'), ('SP', '서비스 상품'), ('IP', '재고관리 상품'),)
OPTION = (('NR', '할인 없음'), ('FA', '고정 금액 할인'), ('DR', '할인율'),)
CATEGORY = Category.objects.all()
BRAND = Brand.objects.all()


class ProductCreationForm(ModelForm):
    types = forms.CharField(label='상품타입', widget=forms.Select(choices=TYPES, attrs={'class': 'form-control'}))
    category = forms.ModelChoiceField(label='카테고리', queryset=CATEGORY, widget=forms.Select(attrs={'class': 'form-control'}))
    brand = forms.ModelChoiceField(label='상품 브랜드', queryset=BRAND, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Product
        fields = ['name', 'summary', 'description', 'types', 'category', 'brand', 'price', 'saleOption',
                  'salePrice', 'inventory', 'sale_ok']

