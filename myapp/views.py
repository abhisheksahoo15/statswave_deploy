from django.shortcuts import render

# Create your views here.


from django.shortcuts import render

def index(request):
    return render(request, 'myapp/index.html')

def career(request):
    return render(request, 'myapp/career.html')

def case_studies(request):
    return render(request, 'myapp/case_studies.html')

def certificate(request):
    return render(request, 'myapp/certificate.html')

def dashboard(request):
    return render(request, 'myapp/dashboard.html')

def pricing(request):
    return render(request, 'myapp/pricing.html')
