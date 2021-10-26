from django.shortcuts import render

# Create your views here.

# def test_view(request):
#     return HttpResponse("I am a very nice view!")

# def homepage(request):
#     return HttpResponse("Welcome to the homepage")   

def test_view(request):
    
    return render(request, 'test.html')