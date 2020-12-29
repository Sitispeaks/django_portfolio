from django.shortcuts import render

# Create your views here.
def services(request):
    context={"servi":"active"}
    return render(request,'services/serv.html',context)