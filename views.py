from django.shortcuts import render
from django.http import HttpResponse,Http404
# Create your views here.
def home(request):
    return render(request, 'home.html')
def demo(request):
    return render(request, 'demo.html')
def juan(request):
    context={}
    context['name']='娟娟'
    return render(request,'juan.html',context)
def page1(request):
    context={"name":"juanjuan"}
    return render(request, 'page1.html',context)
def page(request,num):
    try:
        num=int(num)
        return render(request, 'demo.html')
    except:
        raise Http404
def sonpage(request):
    return render(request, 'Subpage.html')
