from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import HttpResponseRedirect
from products.models import ProductCategory, Product, Basket
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.db.models.query import QuerySet



class IndexView(TemplateView):
    template_name = 'products/index.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super(IndexView, self).get_context_data()
        context['title'] = 'Store'
        return context


class ProducsListView(ListView):
    model = Product
    template_name = 'products/products.html'
    paginate_by = 3

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super(ProducsListView, self).get_context_data()
        context['title'] = 'Store - Каталог'
        context['categories'] = ProductCategory.objects.all()
        return context

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super(ProducsListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset


@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])