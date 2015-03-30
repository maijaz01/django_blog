from django.shortcuts import render
from django.http import HttpResponse	
from blog.models import Category
from blog.models import Page

# Create your views here.
def HomeMassage(request):
	# import pdb;pdb.set_trace()
	category_list = Category.objects.order_by('id')[1:]
	context_dict = {'categories': category_list}
	# context_dict = {'boldmessage': "I am bold font from the context"}
	return render(request,'Home_Page.html' ,context_dict)

def category(request, category_name):
	context_dict = {}
	# import pdb;pdb.set_trace()
	category = Category.objects.get(name=category_name)
	category_name=category.name
	category_id=category.id
	context_dict['category_name'] = category.name
	pages = Page.objects.filter(category_id=category_id)
	# Adds our results list to the template context under name pages.
	context_dict['pages'] = pages
	context_dict['category'] = category

	return render(request, 'category.html', context_dict)