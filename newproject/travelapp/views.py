from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Place2


# Create your views here.
def demo(request):
    obj = Place.objects.all()
    obj1 = Place2.objects.all()
    # name="india"
    return render(request, "index.html", {'result': obj,'result1':obj1})


# def demo1(request):
#     obj1 = Place1.objects.all()
#     # name="india"
#     return render(request, "index.html", {'result1': obj1})

# def addition(request):
#  x=int(request.GET['num1'])
# y=int(request.GET['num2'])
# res=x+y
# res1=x-y
# res2=x*y
# res3=x/y
# return render(request,"result.html",{'result':res,'result1':res1,'result2':res2,'result3':res3})
# def contact(request):
#   return HttpResponse("hello i am contact")
