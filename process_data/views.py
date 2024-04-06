from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth, User
import pandas as pd
from .models import process_data
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('upload')
        else:
            messages.info(request, "invalid creditionals")
            return redirect('login')

    else:
        return render(request, 'login.html')


def upload(request):
    if request.method == 'POST':
        global df, records_data
        BatchD = request.FILES.getlist('xlsx')
        if len(BatchD) == 1:
            for listoffilesgiven in BatchD:
                if listoffilesgiven.name.endswith('xlsx'):
                    df = pd.read_excel(listoffilesgiven)
                    # print(df)

                elif listoffilesgiven.name.endswith('csv'):
                    df = pd.read_csv(listoffilesgiven)
                    # print(df)
                else:
                    messages.info(request,
                                  "File extention need to be 'xlsx' or 'csv,"
                                  " Please upload files with 'xlsx' extention files")
                    return redirect("upload")
        else:
            messages.info(request,
                          "Only one csv or xlsx file should be uploaded.")
            return redirect("upload")
        records_data = []
        for i, data in enumerate(df.values.tolist()):
            # print(data)
            row_value = process_data(id=data[0], organization_name=data[1], domain=data[2], year_founded=data[3],
                                     industry_type=data[4],
                                     size_range=data[5], locality=data[6], country=data[7], link_url=data[8],
                                     current_employee_estimate=data[9],
                                     total_employee_estimate=data[10])
            records_data.append(row_value)
        process_data.objects.bulk_create(records_data)
        messages.info(request, f"Total {len(records_data)} records are updated")

    return render(request, "upload.html")


@api_view(['POST', 'GET'])
def count_records(request):
    if request.method == 'POST':
        year_founded_value = request.POST.get('year_founded_value')
        industry_types = request.POST.get('industry_types')
        locality_value = request.POST.get('locality_value')

        # Assuming you have a model named 'Record' to query
        records_count = process_data.objects.filter(year_founded=year_founded_value, industry_type=industry_types,
                                                    locality=locality_value).count()

        if year_founded_value:
            messages.info(request, f"Total records fetch are : {records_count}")
        values = process_data.objects.all().values_list('year_founded', 'industry_type',
                                                                                  'locality',
                                                                                  'organization_name').distinct()
        values2 = process_data.objects.filter(year_founded=year_founded_value, industry_type=industry_types,
                                              locality=locality_value).values_list('year_founded', 'industry_type',
                                                                                   'locality',
                                                                                   'organization_name').distinct()

        return render(request, "view.html", {'datalist': values, 'return_records': values2})
    values = process_data.objects.all().values_list('year_founded', 'industry_type', 'locality').distinct()
    return render(request, "view.html", {'datalist': values})


def user_list(request):
    if request.method == 'POST':
        # If the form is submitted, create a new user
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        User.objects.create_user(username=username, email=email, password=password)
        return redirect('user_list')  # Redirect to the same page to refresh the user list

    users = User.objects.all()  # Fetch all users from the database
    return render(request, 'user_creation.html', {'users': users})


def logout(request):
    # print(user)
    User.objects.filter(username=request.user)
    auth.logout(request)
    return redirect('/login')
