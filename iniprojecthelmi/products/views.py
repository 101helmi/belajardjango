from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, CategoryProduct

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def product_create(request):
    choices = [(status.value, status.name) for status in CategoryProduct]

    if request.method == 'POST':
        name = request.POST['name']
        category = request.POST['category']
        price = request.POST['price']
        stock = request.POST['stock']
        description = request.POST.get('description', '')
        Product.objects.create(
            name=name,
            category=category,
            price=price,
            stock=stock,
            description=description
        )
        return redirect('product_list')

    return render(request, 'products/product_form.html', {
        'product': None,
        'category_choices': choices,
    })

def product_update(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        product.name = request.POST['name']
        product.category = request.POST['category']
        product.price = request.POST['price']
        product.stock = request.POST['stock']
        product.description = request.POST.get('description', '')
        product.save()
        return redirect('product_list')
    return render(request, 'products/product_form.html', {'product': product})

def product_delete(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'products/product_confirm_delete.html', {'product': product})