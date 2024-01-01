from django.http import HttpResponse
from django.shortcuts import render


def demo(request):

    # print("this is root url function")
    return HttpResponse("this is root url function")
def demo(request):
    title="this is a demo html"
    name="badhon"
    product_name=['p1','p2','p3',]
    data={"t":title,'name':name,'prod':product_name}

    return render(request,'demo/portfolio.html',data)

def emptyview():
    pass