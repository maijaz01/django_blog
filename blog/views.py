from django.shortcuts import render
from django.http import HttpResponse
# from tempalet import temp_home	

# Create your views here.
def HomeMassage(request):
	context_dict = {'boldmessage': "I am bold font from the context"}
	return render(request,'Home_Page.html' ,context_dict)