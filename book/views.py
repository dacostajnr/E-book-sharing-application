from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from django.db.models import Q
from .models import Year,Semester,Book,Other
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt


def home(request):	
	# get all books 
	books = Book.objects.all()
	return render(request,"book/index.html",{"books":books})   	


def semester_detail(request,year_id,semester_id):

	# get year 
	year = Year.objects.get(id=year_id)	
	print(year.name)
	#get semester
	semester = year.sems.get(id=semester_id)
	# get books of sem
	books = semester.books.all()	
	return render(request,"book/semester_detail.html",{"year":year,"semester":semester,"books":books})



def search(request):
	# get all books with query 
	books = Book.objects.all()  
	others = Other.objects.all()
	query = request.GET.get("q") 
	
	if (query!=""):
		books =books.filter(Q(name__icontains=query))
	return render(request,"book/index.html",{"books":books})
	#return render(request,"book/index.html",{"books":books})   	



def upload(request):	
	# get name
	name  = request.POST.get("name")	
	
	# get year 
	year  = request.POST.get("year") 	
	# get the sem  
	sem   = request.POST.get("sem")	
	
	# get sem of year 
	semester = Year.objects.get(name=(year)).sems.get(cumm_name=(sem))
	
	# get file = 
	file = request.FILES.get("file")
	# create object 
	book = Book()
	book.semester = semester 
	book.name = name 
	book.file = file
	book.save()
	# save object in db	
	return redirect("book:home")




def about(request):
	return render(request,"book/about.html",{})


def others(request):
	books = Other.objects.all() 
	return render(request,"book/others.html",{"books":books})




def upload_other(request):
	name = request.POST.get("name")
	file = request.FILES.get("file") 
	print (file)
	book = Other()
	book.name = name 
	book.file = file 
	book.save()
	return redirect("book:others")