from django.shortcuts import render,redirect,HttpResponse
from .models import project_details
import os
from django.conf import settings
from datetime import datetime
from django.contrib.auth import authenticate,login as auth_login , logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
period=0

# @login_required
def duration(date1,date2):
    date1 = datetime.strptime(date1,"%Y-%m-%d")
    date2 = datetime.strptime(date2,"%Y-%m-%d")

    start_month = date1.month
    # print(start_month)
    start_year = date1.year
    end_month = date2.month
    end_year = date2.year
    financial_year_start_index = start_year
    financial_year_end_index = end_year
    count = 0 
    if start_month < 4:
        count += 1 
        financial_year_start_index = start_year-1
    if end_month > 3:
        financial_year_end_index = end_year+1 
        count += 1

    count += (end_year - start_year)

    result = {
        'count':count,
        'financial_year_start_index':financial_year_start_index,
        'financial_year_end_index':financial_year_end_index,
        'start_month':start_month,
        'end_month':end_month
    }

    return result

import pickle
# @login_required
def createfile(Project_file_name,period_range):
    file_path = os.path.join(settings.BASE_DIR,os.path.join('project_files',f'{Project_file_name}.txt'))

    data={}
    for i in range(0,period_range):
        data[f"table_{i+1}"]={
            "one_Grant_Amount": "0",
            "one_Apr": "0",
            "one_May": "0",
            "one_Jun": "0",
            "one_Jul": "0",
            "one_Aug": "0",
            "one_Sep": "0",
            "one_Oct": "0",
            "one_Nov": "0",
            "one_Dec": "0",
            "one_Jan": "0",
            "one_Feb": "0",
            "one_Mar": "0",

            "two_Grant_Amount": "0",
            "two_Apr": "0",
            "two_May": "0",
            "two_Jun": "0",
            "two_Jul": "0",
            "two_Aug": "0",
            "two_Sep": "0",
            "two_Oct": "0",
            "two_Nov": "0",
            "two_Dec": "0",
            "two_Jan": "0",
            "two_Feb": "0",
            "two_Mar": "0",

            "three_Grant_Amount": "0",
            "three_Apr": "0",
            "three_May": "0",
            "three_Jun": "0",
            "three_Jul": "0",
            "three_Aug": "0",
            "three_Sep": "0",
            "three_Oct": "0",
            "three_Nov": "0",
            "three_Dec": "0",
            "three_Jan": "0",
            "three_Feb": "0",
            "three_Mar": "0",

            "four_Grant_Amount": "0",
            "four_Apr": "0",
            "four_May": "0",
            "four_Jun": "0",
            "four_Jul": "0",
            "four_Aug": "0",
            "four_Sep": "0",
            "four_Oct": "0",
            "four_Nov": "0",
            "four_Dec": "0",
            "four_Jan": "0",
            "four_Feb": "0",
            "four_Mar": "0",

            "five_Grant_Amount": "0",
            "five_Apr": "0",
            "five_May": "0",
            "five_Jun": "0",
            "five_Jul": "0",
            "five_Aug": "0",
            "five_Sep": "0",
            "five_Oct": "0",
            "five_Nov": "0",
            "five_Dec": "0",
            "five_Jan": "0",
            "five_Feb": "0",
            "five_Mar": "0",

            "six_Grant_Amount":"0",
            "six_Apr": "0",
            "six_May": "0",
            "six_Jun": "0",
            "six_Jul": "0",
            "six_Aug": "0",
            "six_Sep": "0",
            "six_Oct": "0",
            "six_Nov": "0",
            "six_Dec": "0",
            "six_Jan": "0",
            "six_Feb": "0",
            "six_Mar": "0",

            "seven_Grant_Amount": "0",
            "seven_Apr": "0",
            "seven_May": "0",
            "seven_Jun": "0",
            "seven_Jul": "0",
            "seven_Aug": "0",
            "seven_Sep": "0",
            "seven_Oct": "0",
            "seven_Nov": "0",
            "seven_Dec": "0",
            "seven_Jan": "0",
            "seven_Feb": "0",
            "seven_Mar": "0",
        }
    
    for table_name in data:
        data[table_name]["total_Grant_Amount"]="0"
        data[table_name]["total_Apr"] = "0"
        data[table_name]["total_May"] = "0"
        data[table_name]["total_Jun"] = "0"
        data[table_name]["total_Jul"] = "0"
        data[table_name]["total_Aug"] = "0"
        data[table_name]["total_Sep"] = "0"
        data[table_name]["total_Oct"] = "0"
        data[table_name]["total_Nov"] = "0"
        data[table_name]["total_Dec"] = "0"
        data[table_name]["total_Jan"] = "0"
        data[table_name]["total_Feb"] = "0"
        data[table_name]["total_Mar"] = "0"

    # print(data)

    with open(file_path, 'w') as file:
        json_data = json.dumps(data, indent=2,sort_keys=True)
        file.write(json_data)

from django.core.exceptions import ObjectDoesNotExist
@login_required
def index(request):
    if request.method == "POST":
        Project_Fellowship_No =request.POST.get('Project_Fellowship_No')
        PI_of_Project = request.POST.get('PI_of_Project')
        Sanctioned_Date = request.POST.get('Sanctioned_Date')
        Project_Start_Date = request.POST.get('Project_Start_Date')
        Project_Closure_Date = request.POST.get('Project_Closure_Date')
        Title_of_Project = request.POST.get('Title_of_Project')

        Project_file_name = ''.join(letter for letter in Project_Fellowship_No if letter.isalnum())

        try:
            check = project_details.objects.get(Project_Fellowship_No=Project_Fellowship_No)
            return render(request,'index.html')
        except ObjectDoesNotExist:
            results = duration(Project_Start_Date,Project_Closure_Date)
            
            start_year=results['financial_year_start_index']
            closure_year=results['financial_year_end_index']
            period = results['count']
            start_month = results['start_month']
            end_month = results['end_month']

            details = project_details.objects.create(
                Project_Fellowship_No =Project_Fellowship_No,
                Project_file_name = Project_file_name,
                PI_of_Project = PI_of_Project,
                Sanctioned_Date = Sanctioned_Date,
                Project_Start_Date =Project_Start_Date, 
                Project_Closure_Date =Project_Closure_Date,
                Title_of_Project =Title_of_Project,
                project_duration = period,
                financial_year_start_index = start_year,
                financial_year_end_index = closure_year,
                start_month = start_month,
                end_month = end_month
            )

            details.save()

            

            period_range = range(0, period)

            createfile(Project_file_name,period)

            # print(period," ",period_range)
            context = {'period': period, 'period_range': period_range,'start_month':start_month,'end_month':end_month}
            years = {'start_year':start_year, 'closure_year':closure_year}

            years_dict = {'context':context, 'years':years, 'fellowship_no':Project_Fellowship_No,'title':Title_of_Project ,'id':details.id}

            # save_table_data(request,details.id)

            return render(request,'monthly.html',years_dict)
        
    return render(request,'index.html')

def homepage(request):
    return render(request, "homepage.html")         

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if user is not None and user.is_active:
            auth_login(request,user)
            return render(request,'homepage.html')
        else:
            messages.error(request,'Invalid Credentials')
    return render(request, "login.html")         

@login_required
def project_list(request):
    projects = project_details.objects.all()
    context = {'projects': projects}
    return render(request, 'project_list.html', context)

@login_required
def monthly(request):
    
    if request.method == "POST":
        Project_Fellowship_No = request.POST.get('Project_Fellowship_No')
        PI_of_Project = request.POST.get('PI_of_Project')
        Sanctioned_Date = request.POST.get('Sanctioned_Date')
        Project_Start_Date = request.POST.get('Project_Start_Date')
        Project_Closure_Date = request.POST.get('Project_Closure_Date')
        Title_of_Project = request.POST.get('Title_of_Project')

        start_year = Project_Start_Date[:4]
        closure_year = Project_Closure_Date[:4]
        period = int(closure_year) - int(start_year)

        try:
            # Try to get the existing project
            existing_project = project_details.objects.get(Project_Fellowship_No=Project_Fellowship_No)

            # If the project exists, update its fields
            existing_project.PI_of_Project = PI_of_Project
            existing_project.Sanctioned_Date = Sanctioned_Date
            existing_project.Project_Start_Date = Project_Start_Date
            existing_project.Project_Closure_Date = Project_Closure_Date
            existing_project.Title_of_Project = Title_of_Project
            existing_project.project_duration = period
            existing_project.save()

            start_year = int(start_year)
            closure_year = int(closure_year)

            period_range = range(0, period)
            context = {'period': period, 'period_range': period_range}
            years = {'start_year': start_year, 'closure_year': closure_year}

            years_dict = {'context': context, 'years': years, 'fellowship_no': Project_Fellowship_No}
            return redirect('fill',project_id=existing_project.id)
            

        except project_details.DoesNotExist:
            # If the project doesn't exist, create a new one
            details = project_details.objects.create(
                Project_Fellowship_No=Project_Fellowship_No,
                PI_of_Project=PI_of_Project,
                Sanctioned_Date=Sanctioned_Date,
                Project_Start_Date=Project_Start_Date,
                Project_Closure_Date=Project_Closure_Date,
                Title_of_Project=Title_of_Project,
                project_duration=period
            )

            details.save()

            start_year = int(start_year)
            closure_year = int(closure_year)

            period_range = range(0, period)
            context = {'period': period, 'period_range': period_range}
            years = {'start_year': start_year, 'closure_year': closure_year}

            years_dict = {'context': context, 'years': years, 'fellowship_no': Project_Fellowship_No}

            return render(request, 'monthly.html', years_dict)

    return render(request, 'index.html')


from datetime import datetime
@login_required
def mastersheet(request,project_id):
    print("mastersheet called")
    existing_project = project_details.objects.get(id=project_id)
    start_year1 = existing_project.financial_year_start_index
    end_year1 = existing_project.financial_year_end_index

    financial_years = [f"{year}-{year+1}" for year in range(start_year1, end_year1)]
    budget_heads = [
    'Equipment',
    'Manpower',
    'Contingency',
    'Consumables',
    'Travel',
    'Overhead',
    'SSR',

]
    file_path = os.path.join('project_files', f'{existing_project.Project_file_name}.txt')
    with open(file_path, 'r') as file:
        table_data1 = file.read()
    # print((table_data1))
    parsed_data = json.loads(table_data1)
    table_1_data = parsed_data["table_1"]
    # print(table_1_data)
    # print(len(parsed_data))
    table_data={
        '1':table_1_data,
        '0':table_1_data
    }
    # print(parsed_data)
    # for table_key, table_data in parsed_data.items():
    #     print(table_key)

    # years = {'start_year':2023, 'closure_year':2027}
    new_parsed_data = {int(key.split('_')[1]): value for key, value in parsed_data.items()}

    # print(new_parsed_data)
    parsed_data_json = json.dumps(parsed_data)

    period_range =range(0,8)
    zipped_data = zip(period_range, budget_heads)
    # zipped_data1 = zip(range(1,len(financial_years)+1), financial_years)
    data={
        'financial_years':financial_years,
        'period_range' :range(0,8),
        'period_range1' :range(0,7),
        'budget_heads':budget_heads,
        'zipped_data':zipped_data,
        'zipped_data1':zipped_data,
        'l':len(financial_years)+1,
        'tablesdata':new_parsed_data,
        'existing_project':existing_project,
        'project_id':project_id
        }
    print("zipped data",new_parsed_data)
    return render(request,'mastersheet.html',data)


import json
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json
from django.http import JsonResponse
from django.views.decorators.http import require_POST


                

    

from django.http import JsonResponse
import json
import os
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from home.models import project_details
from django.conf import settings

@csrf_exempt
@require_POST
# @login_required
def save_table_data(request, project_id):
    try:
        project = project_details.objects.get(id=project_id)
        print(f"project id: ",project_id)
        file_path = os.path.join(settings.BASE_DIR,os.path.join('project_files',f'{project.Project_file_name}.txt'))
        # Decode and save the JSON data to the file
        with open(file_path, 'w') as file:
            json_data = json.loads(request.body)
            json.dump(json_data, file)
        
        # print('data',json_data)

        return JsonResponse({'success': True})
    except Exception as e:
        # print(e)
        return JsonResponse({'success': False, 'error': str(e)})

@login_required
def fill(request, project_id):
    try:
        # project_id = project_id.replace('/','_')
        project = project_details.objects.get(id = project_id)
        project_file_name = project.Project_file_name
        # project_fellowship_no = project.Project_Fellowship_No
        file_path = f'project_files/{project_file_name}.txt'
        with open(file_path, 'r') as file:
            table_data1 = file.read()

        parsed_data = json.loads(table_data1)
        table_1_data = parsed_data["table_1"]
    
        table_data={
            '1':table_1_data,
            '0':table_1_data
        }
    

        new_parsed_data = {int(key.split('_')[1]): value for key, value in parsed_data.items()}

        display_id = project.Project_Fellowship_No
        display_name = project.Title_of_Project
        start_year = project.financial_year_start_index
        end_year = project.financial_year_end_index
        start_month = project.start_month
        end_month = project.end_month

        display = {
            'display_id':display_id,
            'display_name':display_name,
            'start_year':start_year,
            'end_year':end_year,
            'start_month':start_month,
            'end_month':end_month
        }

        print(start_year)
    
        parsed_data_json = json.dumps(parsed_data)
    
        return render(request, 'filling.html', {'fellowship_no':project_id,'tablesdata': new_parsed_data,'range':range(0,5),'table_1_data':table_1_data,'parsed_data_json': parsed_data_json,'display':display})
    except Exception as e:
        print(e)
        return HttpResponse(e)

def count_keys(d):
    if not isinstance(d, dict):
        return 1
    return sum(count_keys(v) for v in d.values())


@csrf_exempt
@require_POST
# @login_required
def save_tables_to_file(request, project_id):
    try:
        project = get_object_or_404(project_details, id=project_id)
        file_path = os.path.join('project_files', f'{project.Project_file_name}.txt')

        # Decode and save the JSON data to the file
        with open(file_path, 'w') as file:
            json_data = json.loads(request.body)
            json.dump(json_data, file)

        return JsonResponse({'success': True})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})
    
from django.views.decorators.http import require_POST

@require_POST
# @login_required
def save_table_data_to_file(request):
    try:
        data = json.loads(request.body.decode('utf-8'))['tableData']  # Assuming the data is sent as an array
        # print(data)
        # print(1)
        # Process and save the data to the 'files.txt' file
        file_path = 'home/te.txt'
        with open(file_path, 'w') as file:
            for row in data:
                file.write(','.join(row) + '\n')

        return JsonResponse({'success': True})
    except Exception as e:
        print(f'Error saving file: {e}')
        return JsonResponse({'success': False, 'error': str(e)})
    
# @login_required
def save_data_to_file(request):
    if request.method == 'POST':
        try:
            # Parse the JSON data from the request
            json_data = json.loads(request.body.decode('utf-8'))
            # print(json_data)

            # Convert the JSON data to a text format (e.g., newline-separated)
            text_data = '\n'.join([f"{key}: {value}" for key, value in json_data.items()])

            # Overwrite the file with the new data
            with open('home/2.txt', 'w') as file:
                file.write(text_data)

            return JsonResponse({'status': 'success'})
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON data'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
    

def logout(request):
    auth_logout(request)
    return render(request,'homepage.html')