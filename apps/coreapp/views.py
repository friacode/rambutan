from django.shortcuts import render
from PIL import Image

# Create your views here.
from apps.cart.models import Cart
from apps.category.models import Category
from apps.default_info.models import CurrencyType


def getCategory():
    category = Category.objects.all()
    return category


def getUserCartCount(request):
    if request.user.is_authenticated:
        cart_count = Cart.objects.filter(user=request.user).count()
    else:
        cart_count = 0

    return cart_count


def getCurrency():
    currency = CurrencyType.objects.get(status=True)
    return currency


def rescale(image, width):
    img = Image.open(image)

    src_width, src_height = img.size
    src_ratio = float(src_height) / float(src_width)
    dst_height = round(src_ratio * width)

    img = img.resize((width, dst_height), Image.LANCZOS)
    img.save(image.name, 'PNG')
    image.file = img

    # 이게 없으면 attribute error 발생
    image.file.name = image.name

    return image

