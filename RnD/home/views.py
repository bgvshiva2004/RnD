from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from .models import project_details
from django.conf import settings
from datetime import datetime
from django.contrib.auth import authenticate,login as auth_login , logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.db.models import Q
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from django.core.files.base import ContentFile
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from django.urls import reverse
import os
import json
import base64

period=0

# @login_required(login_url='/login/')
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

# import pickle
# @login_required(login_url='/login/')
# def createfile(Project_file_name,period_range):
#     # print('called create file')
#     file_path = os.path.join(settings.BASE_DIR,os.path.join('project_files',f'{Project_file_name}.txt'))

#     data={}
#     for i in range(0,period_range):
#         data[f"table_{i+1}"]={
#             "one_Grant_Amount": "0",
#             "one_Apr": "0",
#             "one_May": "0",
#             "one_Jun": "0",
#             "one_Jul": "0",
#             "one_Aug": "0",
#             "one_Sep": "0",
#             "one_Oct": "0",
#             "one_Nov": "0",
#             "one_Dec": "0",
#             "one_Jan": "0",
#             "one_Feb": "0",
#             "one_Mar": "0",

#             "two_Grant_Amount": "0",
#             "two_Apr": "0",
#             "two_May": "0",
#             "two_Jun": "0",
#             "two_Jul": "0",
#             "two_Aug": "0",
#             "two_Sep": "0",
#             "two_Oct": "0",
#             "two_Nov": "0",
#             "two_Dec": "0",
#             "two_Jan": "0",
#             "two_Feb": "0",
#             "two_Mar": "0",

#             "three_Grant_Amount": "0",
#             "three_Apr": "0",
#             "three_May": "0",
#             "three_Jun": "0",
#             "three_Jul": "0",
#             "three_Aug": "0",
#             "three_Sep": "0",
#             "three_Oct": "0",
#             "three_Nov": "0",
#             "three_Dec": "0",
#             "three_Jan": "0",
#             "three_Feb": "0",
#             "three_Mar": "0",

#             "four_Grant_Amount": "0",
#             "four_Apr": "0",
#             "four_May": "0",
#             "four_Jun": "0",
#             "four_Jul": "0",
#             "four_Aug": "0",
#             "four_Sep": "0",
#             "four_Oct": "0",
#             "four_Nov": "0",
#             "four_Dec": "0",
#             "four_Jan": "0",
#             "four_Feb": "0",
#             "four_Mar": "0",

#             "five_Grant_Amount": "0",
#             "five_Apr": "0",
#             "five_May": "0",
#             "five_Jun": "0",
#             "five_Jul": "0",
#             "five_Aug": "0",
#             "five_Sep": "0",
#             "five_Oct": "0",
#             "five_Nov": "0",
#             "five_Dec": "0",
#             "five_Jan": "0",
#             "five_Feb": "0",
#             "five_Mar": "0",

#             "six_Grant_Amount":"0",
#             "six_Apr": "0",
#             "six_May": "0",
#             "six_Jun": "0",
#             "six_Jul": "0",
#             "six_Aug": "0",
#             "six_Sep": "0",
#             "six_Oct": "0",
#             "six_Nov": "0",
#             "six_Dec": "0",
#             "six_Jan": "0",
#             "six_Feb": "0",
#             "six_Mar": "0",

#             "seven_Grant_Amount": "0",
#             "seven_Apr": "0",
#             "seven_May": "0",
#             "seven_Jun": "0",
#             "seven_Jul": "0",
#             "seven_Aug": "0",
#             "seven_Sep": "0",
#             "seven_Oct": "0",
#             "seven_Nov": "0",
#             "seven_Dec": "0",
#             "seven_Jan": "0",
#             "seven_Feb": "0",
#             "seven_Mar": "0",
#         }

#     for table_name in data:
#         data[table_name]["total_Grant_Amount"]="0"
#         data[table_name]["total_Apr"] = "0"
#         data[table_name]["total_May"] = "0"
#         data[table_name]["total_Jun"] = "0"
#         data[table_name]["total_Jul"] = "0"
#         data[table_name]["total_Aug"] = "0"
#         data[table_name]["total_Sep"] = "0"
#         data[table_name]["total_Oct"] = "0"
#         data[table_name]["total_Nov"] = "0"
#         data[table_name]["total_Dec"] = "0"
#         data[table_name]["total_Jan"] = "0"
#         data[table_name]["total_Feb"] = "0"
#         data[table_name]["total_Mar"] = "0"

#     with open(file_path, 'w') as file:
#         json_data = json.dumps(data)
#         file.write(json_data)

from django.core.exceptions import ObjectDoesNotExist
@login_required(login_url='/login/')
def index(request):
    if request.method == "POST":
        Project_Fellowship_No =request.POST.get('Project_Fellowship_No')
        PI_of_Project = request.POST.get('PI_of_Project')
        Sanctioned_Date = request.POST.get('Sanctioned_Date')
        Project_Start_Date = request.POST.get('Project_Start_Date')
        Project_Closure_Date = request.POST.get('Project_Closure_Date')
        Title_of_Project = request.POST.get('Title_of_Project')
        Co_PI_of_Project = request.POST.get('Co_PI_of_Project')
        funding_agency = request.POST.get('funding_agency')

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
                end_month = end_month,
                funding_agency= funding_agency,
                Co_PI_of_Project = Co_PI_of_Project
            )

            details.save()

            

            period_range = range(0, period)

            # createfile(Project_file_name,period)

            # print(period," ",period_range)
            context = {'period': period, 'period_range': period_range,'start_month':start_month,'end_month':end_month}
            years = {'start_year':start_year, 'closure_year':closure_year}

            years_dict = {'context':context, 'years':years, 'fellowship_no':Project_Fellowship_No,'title':Title_of_Project ,'id':details.id}


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


@login_required(login_url='/login/')
def project_list(request):
    projects = project_details.objects.all()
    filter_option = request.GET.get('filter')
    if filter_option == 'completed':
        projects = projects.filter(task='completed')
    elif filter_option == 'ongoing':
        projects = projects.filter(task='ongoing')
    context = {'projects': projects}
    return render(request, 'project_list.html', context)


@login_required(login_url='/login/')
def fill(request, project_id):
    try:
        project = project_details.objects.get(id = project_id)
        project_file_name = project.Project_file_name
        # print(project_file_name)
        # project_fellowship_no = project.Project_Fellowship_No
        file_path = f'project_files/{project_file_name}.txt'
        with open(file_path, 'r') as file:
            table_data1 = file.read()

        parsed_data = json.loads(table_data1)
        table_1_data = parsed_data["table_1"]
        your_data=parsed_data
        text_values_set = set()
    
# Loop through the outer dictionary
        for key, inner_dict in your_data.items():
                # Loop through the inner dictionary
                for inner_key, value in inner_dict.items():
                    # Check if the key ends with "_text"
                    if inner_key.endswith('_text'):
                        # Add the value to the set
                        text_values_set.add(value)
  
        budget_heads = list(text_values_set)
    
        # table_data={
        #     '1':table_1_data,
        #     '0':table_1_data
        # }

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
    
        parsed_data_json = json.dumps(parsed_data)
    
        return render(request, 'filling.html', {'budget_heads':budget_heads,'fellowship_no':project_id,'tablesdata': new_parsed_data,'range':range(0,5),'table_1_data':table_1_data,'parsed_data_json': parsed_data_json,'display':display})
    except Exception as e:
        return HttpResponse(e)



def ucr(request,project_id):
    project = project_details.objects.get(id = project_id)
    # Project_Fellowship_No = project.Project_Fellowship_No
    # PI_of_Project = project.PI_of_Project
    # Title_of_Project = project.Title_of_Project

    # data = {
    #     'project' : project,
    #     'Project_Fellowship_No' : Project_Fellowship_No,
    #     'PI_of_Project' : PI_of_Project,
    #     'Title_of_Project' :Title_of_Project,
    #     'project_id' : project_id
    # }
    data = {'project': project}

    return render(request, "ucr.html",data)


def ucnr(request,project_id):
    # existing_project = project_details.objects.get(id=project_id)
    
    return render(request, "ucnr.html",{'project_id':project_id})



# @login_required(login_url='/login/')
# def monthly(request):
    
#     if request.method == "POST":
#         Project_Fellowship_No = request.POST.get('Project_Fellowship_No')
#         PI_of_Project = request.POST.get('PI_of_Project')
#         Sanctioned_Date = request.POST.get('Sanctioned_Date')
#         Project_Start_Date = request.POST.get('Project_Start_Date')
#         Project_Closure_Date = request.POST.get('Project_Closure_Date')
#         Title_of_Project = request.POST.get('Title_of_Project')
#         Co_PI_of_Project = request.POST.get('Co_PI_of_Project')
#         funding_agency = request.POST.get('funding_agency')

#         start_year = Project_Start_Date[:4]
#         closure_year = Project_Closure_Date[:4]
#         period = int(closure_year) - int(start_year)

#         try:
#             # Try to get the existing project
#             existing_project = project_details.objects.get(Project_Fellowship_No=Project_Fellowship_No)

#             # If the project exists, update its fields
#             existing_project.PI_of_Project = PI_of_Project
#             existing_project.Sanctioned_Date = Sanctioned_Date
#             existing_project.Project_Start_Date = Project_Start_Date
#             existing_project.Project_Closure_Date = Project_Closure_Date
#             existing_project.Title_of_Project = Title_of_Project
#             existing_project.project_duration = period
#             existing_project.Co_PI_of_Project = Co_PI_of_Project
#             existing_project.funding_agency = funding_agency
#             existing_project.save()

#             start_year = int(start_year)
#             closure_year = int(closure_year)

#             period_range = range(0, period)
#             context = {'period': period, 'period_range': period_range}
#             years = {'start_year': start_year, 'closure_year': closure_year}

#             years_dict = {'context': context, 'years': years, 'fellowship_no': Project_Fellowship_No}
#             return redirect('fill',project_id=existing_project.id)
            

#         except project_details.DoesNotExist:
#             # If the project doesn't exist, create a new one
#             details = project_details.objects.create(
#                 Project_Fellowship_No=Project_Fellowship_No,
#                 PI_of_Project=PI_of_Project,
#                 Sanctioned_Date=Sanctioned_Date,
#                 Project_Start_Date=Project_Start_Date,
#                 Project_Closure_Date=Project_Closure_Date,
#                 Title_of_Project=Title_of_Project,
#                 project_duration=period,
#                 funding_agency = funding_agency,
#                 Co_PI_of_Project=Co_PI_of_Project
#             )

#             details.save()

#             start_year = int(start_year)
#             closure_year = int(closure_year)

#             period_range = range(0, period)
#             context = {'period': period, 'period_range': period_range}
#             years = {'start_year': start_year, 'closure_year': closure_year}

#             years_dict = {'context': context, 'years': years, 'fellowship_no': Project_Fellowship_No}

#             return render(request, 'monthly.html', years_dict)

#     return render(request, 'index.html')


from datetime import datetime
@login_required(login_url='/login/')
def mastersheet(request,project_id):
    # print("mastersheet called")
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
    file_path1 = os.path.join('commited', f'{existing_project.id}.txt')
    # print(file_path1)

    with open(file_path, 'r') as file:
        table_data1 = file.read()
    # print((table_data1))
    parsed_data = json.loads(table_data1)
    
    # table_1_data = parsed_data["table_1"]
    # print(table_1_data)

    # print(len(parsed_data))
    # table_data={
    #     '1':table_1_data,
    #     '0':table_1_data
    # }
    your_data=parsed_data
    text_values_set = set()
    
# Loop through the outer dictionary
    for key, inner_dict in your_data.items():
        # Loop through the inner dictionary
        for inner_key, value in inner_dict.items():
            # Check if the key ends with "_text"
            if inner_key.endswith('_text'):
                # Add the value to the set
                text_values_set.add(value)

    # Print the resulting set
    # print(type(text_values_set))
    # print(type(budget_heads))
    text_values_list = list(text_values_set)
    budget_heads=text_values_list
    # print(parsed_data)
    # for table_key, table_data in parsed_data.items():
    #     print(table_key)

    # years = {'start_year':2023, 'closure_year':2027}
    # for i in parsed_data.items():
    #     print('parsed data',i)
        
    new_parsed_data = {int(key.split('_')[1]): value for key, value in parsed_data.items()}

    # print(new_parsed_data)
    # parsed_data_json = json.dumps(parsed_data)

    period_range =range(1,len(text_values_set)+1)
    zipped_data = zip(period_range, budget_heads)

    # zipped_data1 = zip(range(1,len(financial_years)+1), financial_years)
    if os.path.exists(file_path1):
        with open(file_path1, 'r') as file:
         table_data2 = file.read()
        parsed_data2 = json.loads(table_data2)
    else:
        parsed_data2 = "null"
    data={
        'financial_years':financial_years,
        'period_range' :period_range,
        'period_range1' :range(0,7),
        'budget_heads':budget_heads,
        'zipped_data':zipped_data,
        'zipped_data1':zipped_data,
        'l':len(financial_years)+1,
        'tablesdata':new_parsed_data,
        'tablesdata1':new_parsed_data,
        'existing_project':existing_project,
        'parsed_data2':parsed_data2,
        'project_id':project_id
        }
    
    # for table_key,total_sum in new_parsed_data.items():
    #     print('table key',table_key)
    #     print('total sum',total_sum)
    
    # print("zipped data",new_parsed_data)
    return render(request,'mastersheet.html',data)


def get_monthewise_exp(project_id,financialYearStartYear,start_year1):
    try:
        project = project_details.objects.get(id=project_id)

        file_path = os.path.join(settings.BASE_DIR,os.path.join('project_files',f'{project.Project_file_name}.txt'))
        with open(file_path,'r') as file:
            data = json.load(file)

        table_1_data = data.get(f'table_{financialYearStartYear-start_year1 +1}',{})
        total_Apr = table_1_data.get('total_Apr','')
        total_May = table_1_data.get('total_May','')
        total_Jun = table_1_data.get('total_Jun','')
        total_Jul = table_1_data.get('total_Jul','')
        total_Aug = table_1_data.get('total_Aug','')
        total_Sep = table_1_data.get('total_Sep','')
        total_Oct = table_1_data.get('total_Oct','')
        total_Nov = table_1_data.get('total_Nov','')
        total_Dec = table_1_data.get('total_Dec','')
        total_Jan = table_1_data.get('total_Jan','')
        total_Feb = table_1_data.get('total_Feb','')
        total_Mar = table_1_data.get('total_Mar','')
        total_expenses = table_1_data.get('total_expenses','')

        monthwise_exp ={
            'total_Apr':total_Apr,
            'total_May':total_May,
            'total_Jun':total_Jun,
            'total_Jul':total_Jul,
            'total_Aug':total_Aug,
            'total_Sep':total_Sep,
            'total_Oct':total_Oct,
            'total_Nov':total_Nov,
            'total_Dec':total_Dec,
            'total_Jan':total_Jan,
            'total_Feb':total_Feb,
            'total_Mar':total_Mar,
            'total_expenses':total_expenses
        }

        return monthwise_exp

    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})


def get_sanctions(project_id):
    try:
        project = project_details.objects.get(id=project_id)
        duration = project.project_duration
        # print('duration',duration)
        file_path = os.path.join(settings.BASE_DIR,os.path.join('project_files',f'{project.Project_file_name}.txt'))
        with open(file_path,'r') as file:
            data = json.load(file)
        

        total_sanctions = []

        
        for i in range(1,duration+1):
            table_data = data.get(f'table_{i}',{})
            total_Sanctioned_Amount = table_data.get('total_Sanctioned_Amount','')

            total_sanctions.append(total_Sanctioned_Amount)

        return total_sanctions
        

    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})




def SOE_navigation(request,project_id):

    existing_project = project_details.objects.get(id=project_id)
    
    start_year1 = existing_project.financial_year_start_index
    end_year1 = existing_project.financial_year_end_index

    financial_years = [f"{year}-{year+1}" for year in range(start_year1, end_year1)]
    

    data={
        'financial_years':financial_years,  
        'project_id':project_id
    }

    return render(request,'SOE_navigation.html',data)


def soe(request,project_id,period):

    # print("period: ",period)

    years = period.split('-')
    fist_year_check = years[0]
    # print("first year",fist_year_check)

    first_years = fist_year_check.split('=')
    first_year = int(first_years[1])

    # print("first year",first_year)
    # print("first year type", type(first_year))

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
    file_path1 = os.path.join('commited', f'{existing_project.id}.txt')
    # print(file_path1)
    with open(file_path, 'r') as file:
        table_data1 = file.read()
    # print((table_data1))
    parsed_data = json.loads(table_data1)
    table_1_data = parsed_data["table_1"]
    # print(table_1_data)
    # print(len(parsed_data))
    # table_data={
    #     '1':table_1_data,
    #     '0':table_1_data
    # }
    # print(parsed_data)
    your_data=parsed_data
    text_values_set = set()
    
# Loop through the outer dictionary
    for key, inner_dict in your_data.items():
        # Loop through the inner dictionary
        for inner_key, value in inner_dict.items():
            # Check if the key ends with "_text"
            if inner_key.endswith('_text'):
                # Add the value to the set
                text_values_set.add(value)

    # Print the resulting set
    # print(type(text_values_set))
    # print(type(budget_heads))
    text_values_list = list(text_values_set)
    budget_heads=text_values_list
    # print(parsed_data)
    # for table_key, table_data in parsed_data.items():
    #     print(table_key)

    # years = {'start_year':2023, 'closure_year':2027}
    new_parsed_data = {int(key.split('_')[1]): value for key, value in parsed_data.items()}

    # print(new_parsed_data)
    parsed_data_json = json.dumps(parsed_data)

    period_range =range(1,len(text_values_set)+1)
    zipped_data = zip(period_range, budget_heads)
    # zipped_data1 = zip(range(1,len(financial_years)+1), financial_years)
    if os.path.exists(file_path1):
        with open(file_path1, 'r') as file:
         table_data2 = file.read()
        parsed_data2 = json.loads(table_data2)
    else:
        parsed_data2 = "null"

    # current_month = datetime.now().month
    # current_year = datetime.now().year

    # print("current year type", type(current_year))
    # print("current year", current_year)

    # if(current_month >=3):
    financialYearStartYear = first_year
    # else:
    #     financialYearStartYear = current_year-1

    monthwise_exp = {}
    monthwise_exp = get_monthewise_exp(project_id,financialYearStartYear,start_year1)

    total_sanctions = []
    total_sanctions = get_sanctions(project_id)

    # for i in total_grants:
    #     print(i)

    zipped_data_2 = zip(financial_years,total_sanctions)

    data={
        'financial_years':financial_years,  
        'period_range' :period_range,
        'period_range1' :range(0,7),
        'budget_heads':budget_heads,
        'zipped_data':zipped_data,
        'zipped_data1':zipped_data,
        'l':len(financial_years)+1,
        'tablesdata':new_parsed_data,
        'tablesdata1':new_parsed_data,
        'existing_project':existing_project,
        'parsed_data2':parsed_data2,
        'project_id':project_id,
        'financialYearStartYear':financialYearStartYear,
        'monthwise_exp':monthwise_exp,
        # 'total_grants':total_grants
        'zipped_data_2':zipped_data_2
    }
    # print("zipped data",new_parsed_data.items())
    # print("total sanctions",total_sanctions)


    return render(request,'soe_copy.html',data)



@csrf_exempt
@require_POST
def save_table_data(request, project_id):
    try:
        project = project_details.objects.get(id=project_id)
        file_path = os.path.join(settings.BASE_DIR,os.path.join('project_files',f'{project.Project_file_name}.txt'))

        # Decode and save the JSON data to the file
        with open(file_path, 'w') as file:
            json_data = json.loads(request.body)
            json.dump(json_data, file)
        
        return JsonResponse({'success': True})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})


# def count_keys(d):
#     if not isinstance(d, dict):
#         return 1
#     return sum(count_keys(v) for v in d.values())


@csrf_exempt
@require_POST
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
    

# @require_POST
# def save_table_data_to_file(request):
#     try:
#         data = json.loads(request.body.decode('utf-8'))['tableData']
#         # print(data)
#         # print(1)
#         # Process and save the data to the 'files.txt' file
#         file_path = 'home/te.txt'
#         with open(file_path, 'w') as file:
#             for row in data:
#                 file.write(','.join(row) + '\n')

#         return JsonResponse({'success': True})
#     except Exception as e:
#         # print(f'Error saving file: {e}')
#         return JsonResponse({'success': False, 'error': str(e)})
    
# @login_required(login_url='/login/')
# def save_data_to_file(request):
#     if request.method == 'POST':
#         try:
#             # Parse the JSON data from the request
#             json_data = json.loads(request.body.decode('utf-8'))
#             # print(json_data)

#             # Convert the JSON data to a text format (e.g., newline-separated)
#             text_data = '\n'.join([f"{key}: {value}" for key, value in json_data.items()])

#             # Overwrite the file with the new data
#             with open('home/2.txt', 'w') as file:
#                 file.write(text_data)

#             return JsonResponse({'status': 'success'})
#         except json.JSONDecodeError:
#             return JsonResponse({'status': 'error', 'message': 'Invalid JSON data'})
#     else:
#         return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
    

def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return render(request,'homepage.html')

def save_table_data1(request,project_id):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        
            file_path = os.path.join('commited', f'{project_id}.txt')

            with open(file_path, 'w') as file:
                file.write(json.dumps(data, indent=2))
            return JsonResponse({'success': True})
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': 'Invalid JSON data'})

    return JsonResponse({'success': False, 'error': 'Invalid request method'})    


def project_search(request):
    query = request.GET.get('q')

   
    if query:
     projects = project_details.objects.filter(
        (
            Q(Project_Fellowship_No__icontains=query) |
            Q(PI_of_Project__icontains=query) |
            Q(Title_of_Project__icontains=query) | 
            Q(funding_agency__icontains=query) | 
            Q(Co_PI_of_Project__icontains=query)
        ) &
        Q(task='ongoing')
    )
    else:
     projects = project_details.objects.filter(task='ongoing')    

    context = {
        'projects': projects,
        'query': query,
    }

    return render(request, 'project_list.html', context)



def complete_task(request,project_id):
    
    project = get_object_or_404(project_details, id=project_id)
    
    project.task = 'completed'
    project.save()
    
    return redirect('project_listwise')
    # return render(request,'project_listwise.html')


def project_listwise(request):

    projects =  project_details.objects

    filter_option = request.GET.get('filter')

    if filter_option == 'ongoing':
        projects = projects.filter(task='ongoing')
    elif filter_option == 'completed':
        projects = projects.filter(task='completed')

    sort_by = request.GET.get('sortBy', 'Title_of_Project')
    sort_order = request.GET.get('sortOrder', 'asc')

    if sort_order == 'asc':
        projects = projects.order_by(sort_by)
    else:
        projects = projects.order_by(f'-{sort_by}')

    context = {'projects': projects}
    return render(request, 'project_listwise.html', context)


# from django.template.loader import render_to_string


# from django.templatetags.static import static


def save_as_pdf(request):
    if request.method == 'POST':
        try:
            # print("save as pdf called")
            data = json.loads(request.body)
            image_data = data.get('imageData')

            # Convert base64 image data to binary
            binary_data = base64.b64decode(image_data.split(',')[1])

            # Save the image temporarily
            fs = FileSystemStorage(location=settings.MEDIA_ROOT)
            image_path = fs.save('temp_image.png', ContentFile(binary_data))

            # Generate PDF
            pdf_buffer = BytesIO()
            pdf = canvas.Canvas(pdf_buffer, pagesize=letter)
            pdf.drawInlineImage(image_path, 0, 0, width=letter[0], height=letter[1])
            pdf.showPage()
            pdf.save()

            # Remove the temporary image
            fs.delete(image_path)

            # Save the generated PDF temporarily
            pdf_path = fs.save('temp_pdf.pdf', ContentFile(pdf_buffer.getvalue()))
            pdf_buffer.close()

            # Provide the download link using reverse
            download_link = reverse('download_pdf') + f'?path={pdf_path}'

            return JsonResponse({'downloadLink': download_link})
        except Exception as e:
            print(e)
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=400)


import io
import json
import base64
import os
from django.http import JsonResponse, HttpResponse
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import xlsxwriter

def save_as_excel(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            html_content = data.get('htmlContent')

            # Convert HTML content to Excel
            output = io.BytesIO()
            workbook = xlsxwriter.Workbook(output, {'in_memory': True})
            worksheet = workbook.add_worksheet()

            # Parse HTML content and write to Excel
            rows = html_content.split('</tr>')
            for i, row in enumerate(rows):
                columns = row.split('</th>') + row.split('</td>')
                for j, column in enumerate(columns[:-1]):
                    text = column.split('>')[-1]
                    worksheet.write(i, j, text)

            workbook.close()

            # Save the Excel file temporarily
            fs = FileSystemStorage(location=settings.MEDIA_ROOT)
            excel_path = fs.save('temp_excel.xlsx', ContentFile(output.getvalue()))
            print(excel_path)
            output.close()

            # Provide the download link
            download_link = reverse('download_excel') + f'?path={excel_path}'
            print(download_link)
            return JsonResponse({'downloadLink': download_link})
        except Exception as e:
            print(e)
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=400)




def download_pdf(request):
    # print("download pdf called")
    pdf_path = request.GET.get('path')
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{os.path.basename(pdf_path)}"'

    with open(pdf_path, 'rb') as pdf_file:
        response.write(pdf_file.read())

    return response

def download_excel(request):
    # print("download excel called")
    excel_path = request.GET.get('path')
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="{os.path.basename(excel_path)}"'

    with open(excel_path, 'rb') as excel_file:
        response.write(excel_file.read())

    return response




def submit_project_data(request, project_id):

    if request.method == 'POST':
        try:
            project = project_details.objects.get(id=project_id)
            
            # project.Title_of_Project = request.POST.get('Title_of_Project')
            # project.Project_Fellowship_No = request.POST.get('Project_Fellowship_No')
            project.Category = request.POST.get('Category')
            project.Country = request.POST.get('Country')
            project.Country_Involved = request.POST.get('Country_Involved')
            project.task = request.POST.get('task')
            # project.PI_of_Project = request.POST.get('PI_of_Project')
            # project.Co_PI_of_Project = request.POST.get('Co_PI_of_Project')
            project.Department = request.POST.get('Department')
            # project.Project_Start_Date = request.POST.get('Project_Start_Date')
            # project.Project_Closure_Date = request.POST.get('Project_Closure_Date')
            # project.Sanctioned_Date = request.POST.get('Sanctioned_Date')
            # project.Project_file_name = request.POST.get('Project_file_name')
            # project.project_duration = request.POST.get('project_duration')
            # project.financial_year_start_index = request.POST.get('financial_year_start_index')
            # project.financial_year_end_index = request.POST.get('financial_year_end_index')
            # project.start_month = request.POST.get('start_month')
            # project.end_month = request.POST.get('end_month')
            # project.funding_agency = request.POST.get('funding_agency')
            project.Details_of_Donors = request.POST.get('Details_of_Donors')
            project.remark = request.POST.get('remark')
            project.scheme_name = request.POST.get('scheme_name')
            project.scheme_code = request.POST.get('scheme_code')
            project.received_amount = request.POST.get('received_amount')
            # project.date_of_receipt_amount = request.POST.get('date_of_receipt_amount')
            project.provisional_uc = request.POST.get('provisional_uc')
            project.audited_uc = request.POST.get('audited_uc')
            project.link_uc = request.POST.get('link_uc')
            project.sanction_letters_link = request.POST.get('sanction_letters_link')
            project.total_project_cost = request.POST.get('total_project_cost')
            project.fellowship_type = request.POST.get('fellowship_type')

            project.save()
        
            return redirect('project_listwise')
        except Exception as e:
            return HttpResponse("Failed to submit form. Error: " + str(e), status=500)

    return redirect('project_list')



# @require_POST
def delete_project(request,project_id):
    # print(project_id)
    existing_project = project_details.objects.get(id=project_id)
    # print(existing_project.Title_of_Project)
    existing_project.delete()
    # print('deleted')

    projects = project_details.objects.all()
    filter_option = request.GET.get('filter')
    
    # Apply filtering if a filter option is selected
    if filter_option == 'ongoing':
        projects = projects.filter(task='ongoing')
    elif filter_option == 'completed':
        projects = projects.filter(task='completed')
    context = {'projects': projects}

    return render(request,'project_list.html', context)


