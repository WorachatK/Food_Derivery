from re import T
from django.shortcuts import render,redirect
from .models import check_food, food, order_food,type_food
from django.contrib.auth.models import User, auth
from django.contrib import messages
from datetime import datetime,timedelta



#################### HOME #################################
def home(request):
    type_ob = type_food.objects.all

    type_all = []


    for types in type_ob():
        all_type = food.objects.filter(type=types)[0]
        type_all.append(all_type)

    return render(request,'home.html',{
        'random':type_all,
    })

#################### ABOUT #################################
def about(request):
    return render(request,'about.html')    

#################### food_page #################################

def food_page(request):
    
    return render(request,'food.html')

#################### foodmenu #################################    

def foodmenu(request):

    style_type = request.GET.get('style_type')
    name_food = request.GET.get('name_food')
    
    if style_type:
        food_type = type_food.objects.get(type=style_type)
        all_type = food.objects.filter(type=food_type)

        return render(request, 'menutype.html', {
         'foodtype': all_type,
         'type' :food_type,
    })   

    elif name_food:
        all_type = food.objects.get(name=name_food)

        return render(request, 'foodfood.html', {
         'foodfood': all_type,
        })

    foodshow = food.objects.all

    return render(request,'foodmenu.html',{
        'food': foodshow,} )        

#################### orderfood #################################           

def orderfood(request):
    food_food = request.GET.get('food_food')
    food_get = food.objects.get(name=food_food)
    
    return render(request,'orderfood.html',{
        'food_food':food_get,
    })

#################### register #################################      

def register(request):

    return render(request,'account/register.html' )        

#################### login_view #################################    

def login_view(request):

    return render(request,'account/login.html', )

#################### login #################################        

def login (request):
    username=request.POST['username']    
    password=request.POST['password']

    user = auth.authenticate(username=username,password=password)

    if user is not None:
        auth.login(request,user)
        return redirect('/')
    else :
        return redirect('/login_view')

#################### logout #################################            

def logout(request):
    auth.logout(request)
    return redirect('/')  

#################### add_user #################################              


def add_user(request):
    username=request.POST['username']
    firstname=request.POST['firstname']
    lastname=request.POST['lastname']
    email=request.POST['email']
    password=request.POST['password']
    re_password=request.POST['re-password']

    if password==re_password:
        if User.objects.filter(username=username).exists():
            messages.info(request,'UseraName มีคนใช้แล้ว')
            return redirect('/register') 

        elif User.objects.filter(email=email).exists():
            messages.info(request,'Emial alerydy have')    
            return redirect('/register') 

        else :
            user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=firstname,
            last_name=lastname,
            )
            user.save()    
            return redirect('/')  

    else :
        messages.info(request,'Password ไม่ตรงกัน')    
        return redirect('/register')        

#################### buynow #################################  

def buynow(request):
    food_food = request.POST.get('food_food')
    phone_number = request.POST.get('phone_number')
    ads_get = request.POST.get('address')

    datenow = datetime.today()
    date_now = datenow.strftime("%Y-%m-%d")
    
    getfood=food.objects.get(name=food_food)

    current_user = request.user
    print(current_user)
    
    users = order_food.objects.update_or_create(
        username=current_user,
        defaults={
            'phonenumber':phone_number,
            'address':ads_get,
        }     
    )

    f_food=check_food.objects.create(
        username=current_user,
        food=getfood,
        time=date_now,
    )


    return redirect('/services',)     

#################### SERVICES #################################  

def services(request):
    current_user = request.user
    food=check_food.objects.filter(username=current_user)



    return render(request,'service.html',{
        'food':food,
    })