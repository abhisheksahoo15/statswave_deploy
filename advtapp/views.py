from django.shortcuts import render

def index(request):
    return render(request, 'advtapp/index.html')

def career(request):
    return render(request, 'advtapp/career.html')

def case_studies(request):
    return render(request, 'advtapp/case_studies.html')

def certificate(request):
    return render(request, 'advtapp/certificate.html')

def dashboard(request):
    return render(request, 'advtapp/dashboard.html')

def pricing(request):
    return render(request, 'advtapp/pricing.html')
