
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import Company
import csv
from django.db import transaction
from io import StringIO
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .forms import UploadFileForm
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def login_view(request):
    if request.method == 'POST':
        # Get the username and password from the form
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('query_builder')  # Redirect to a page after successful login
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')


# Logout view
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login after logout


@login_required
def user_list_view(request):
    users = User.objects.all()  # Use Django's built-in User model

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = CustomUserCreationForm()

    return render(request, 'user_list.html', {'users': users, 'form': form})

@login_required
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return redirect('user_list')


@login_required
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            process_csv_file(uploaded_file)
            return render(request, 'upload_success.html')  # Render a custom success page

    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

@login_required
def query_builder_view(request):
    results = None
    count = 0

    if request.method == 'POST':
        # Get form data
        keyword = request.POST.get('keyword', '')
        industry = request.POST.get('industry', '')
        year_founded = request.POST.get('year_founded', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        country = request.POST.get('country', '')
        employees_from = request.POST.get('employees_from', '')
        employees_to = request.POST.get('employees_to', '')
        domain = request.POST.get('domain', '')

        # Build a query set filtering the Company model
        query = Company.objects.all()

        if keyword:
            query = query.filter(name__icontains=keyword)
        if industry:
            query = query.filter(industry__icontains=industry)
        if year_founded:
            query = query.filter(year_founded=year_founded)
        if city:
            query = query.filter(locality__icontains=city)
        if state:
            query = query.filter(locality__icontains=state)
        if country:
            query = query.filter(country__icontains=country)
        if employees_from:
            query = query.filter(current_employee_estimate__gte=employees_from)
        if employees_to:
            query = query.filter(current_employee_estimate__lte=employees_to)
        if domain:
            query = query.filter(domain__icontains=domain)

        results = query
        count = results.count()

    return render(request, 'query_builder.html', {'results': results, 'count': count})

@api_view(['GET'])
def query_companies(request):
    companies = Company.objects.all()
    return Response({'count': companies.count()})

def process_csv_file(uploaded_file):
    try:
        file_content = StringIO(uploaded_file.read().decode('utf-8'))
        reader = csv.DictReader(file_content)
        companies = []

        for row in reader:
            try:
                company = Company(
                    id=row['id'],
                    name=row['name'],
                    domain=row['domain'],
                    year_founded=int(row['year founded']) if row['year founded'] else None,
                    industry=row['industry'],
                    locality=row['locality'],
                    country=row['country'],
                    linkedin_url=row['linkedin url'],
                    current_employee_estimate=int(row['current employee estimate']) if row['current employee estimate'] else None,
                    total_employee_estimate=int(row['total employee estimate']) if row['total employee estimate'] else None,
                )
                companies.append(company)
            except KeyError as e:
                print(f"CSV parsing error - missing column {e}")

        with transaction.atomic():
            Company.objects.bulk_create(companies)

    except Exception as e:
        print(f"Error processing file: {e}")

