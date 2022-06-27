from multiprocessing import context
from unicodedata import category
from urllib import request
from django import views
from django.shortcuts import render
from django.views import View

from customer.models import MenuItem

class Index(View):
    def get(self, request,*args, **kwargs):
        return render(request, 'customer/index.html')

class About(View):
    def get ( self,request, *args , **kwargs):
        return render(request, 'customer/about.html')

class Order(View):
    def get(self, request, *args, **kwargs):
        #get every item from each category
        fastfood = MenuItem.objects.filter(category__name__contains='fastfood')
        drinks = MenuItem.objects.filter(category__name__contains='drinks')
        meals = MenuItem.objects.filter(category__name__contains='meals')
        hardmeals = MenuItem.objects.filter(category__name__contains='hardmeals')

        #pass into context
        context={
            'fastfood': fastfood,
            'drinks': drinks,
            'meals': meals,
            'hardmeals' : hardmeals,
        }
    #render the template
        return render (request, 'customer/order.html', context)

class Menu(View):
    def get (self, request, *args,**kwargs):
        return render (request, 'customer/menu.html')
#    def post (self, request, *args,**kwargs):
#        order_items ={
#            'items' : []
#        }
#        items = request.post.getlist('items[]')
#        for item in items:
#            menu_item = MenuItem.objects.get(pk=int(item))
#            item_date = {
#                'id': menu_item.pk,
#                'name': menu_item.name,
#                'price' : menu_item.price,
#            }
#            order_items['items'].append(item_data)
#
#