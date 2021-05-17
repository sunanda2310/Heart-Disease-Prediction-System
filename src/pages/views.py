from django.conf import settings
from django.conf.urls.static import static

from django.shortcuts import render
from django.http import HttpResponse
from .models import userModel, userInfoModel
from .forms import UserForm, UserInfoForm
import pickle
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import redirect


# Create your views here.

def home_view(request, *args, **kwargs):
    print("static url=", settings.STATIC_URL)
    return render(request, 'home.html', {}) #string of html code

def user_heart_info_view(request, *args, **kwargs):
    return render(request, 'user_heart_info.html', {})

def about_view(request, *args, **kwargs):
    return render(request, 'about.html', {})

def contact_view(request, *args, **kwargs):
    return render(request, 'contact.html', {})

def footer_view(request, *args, **kwargs):
    return render(request, 'footer.html', {})

def login_view(request, *args, **kwargs):
    return render(request, 'login.html', {})

def login_failure_view(request, *args, **kwargs):
    return render(request, 'login_failure.html', {})

def login_validation_view(request, *args, **kwargs):
    # dictionary for initial data with
    # field names as keys
    if request.method == 'POST':
        context = {}
        values = []
        username1 = request.POST.get('username')
        password1 = request.POST.get('password')
        print("username = ", username1)
        context = {"name": username1}
        # add the dictionary during initialization
        try:
            values = userModel.objects.get(username=username1, password=password1)
        except:
            context = { "validation": False }

        print("VAlues=", values)
        
        if values:
            context = { "validation": True, "user": username1 }
            return render(request, 'profile.html', context)
        else:
            print("error")
            return render(request, 'login_failure.html', context)

def header_view(request, *args, **kwargs):
    return render(request, 'header.html', {})

def registration_view(request, *args, **kwargs):
    return render(request, 'register.html', {})

def profile_view(request, *args, **kwargs):
    values = request.POST
    my_form = UserForm()
    if request.method == "POST":
        my_form = UserForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            my_form.save()
        else:
            print(my_form.errors)

    context = {
        "form": my_form,
        "data": values
    }
    return render(request, 'login.html', {})


def get_predictions(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):
    with open('model_pickle', 'rb') as f:
        mp = pickle.load(f)
    # patient1 = mp.predict([[39, 0, 1, 135, 208, 0, 0, 171, 0, 1.5, 2, 0, 2]])
    # print(patient1[0])
    prediction = mp.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

    if prediction[0] == 0:
        return 'no'
    elif prediction[0] == 1:
        return 'yes'
    else:
        return 'error'


def prediction_page_view(request, *args, **kwargs):
    my_form = UserInfoForm()
    if request.method == 'POST':
        my_form = UserInfoForm(request.POST)
        values = request.POST
        age = int(request.POST['age'])
        sex = int(request.POST['sex'])
        cp = int(request.POST['cp'])
        trestbps = int(request.POST['trestbps'])
        chol = int(request.POST['chol'])
        fbs = int(request.POST['fbs'])
        restecg = int(request.POST['restecg'])
        thalach = int(request.POST['thalach'])
        exang = int(request.POST['exang'])
        oldpeak = float(request.POST['oldpeak'])
        slope = int(request.POST['slope'])
        ca = int(request.POST['ca'])
        thal = int(request.POST['thal'])

    result = get_predictions(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)
    print("result=", result)
    context = {
        'obj': result,
        'object': values
    }
    return render(request, 'prediction.html', context)


def user_info_view(request, *args, **kwargs):
    username = request.GET.get('user')
    print("username =", username)
    #context = { "user_name": username}
    try:
            values = userInfoModel.objects.get(user = username)
            context = {"object": values, "user": username}

    except:
            context = { "user": username, "object": "" }
    
    return render(request, "user_Details.html", context)

def user_heart_info_save_display_view(request, *args, **kwargs):
    user = request.GET.get('user')
    context = {'user': user}
    return render(request, 'user_heart_info_save_display.html', context)

def user_heart_info_save_view(request, *args, **kwargs):
    values = ""
    result = ""
    username = request.GET.get('user')
    print("username =", username)
    my_form = UserInfoForm()
    my_form = UserInfoForm(request.POST)
    try:

        values = userInfoModel.objects.get(user = username)
        context = {"object": values, "user": username}

    except:

        context = { "object": False, "user": username }

    if values:
        userInfoModel.objects.filter(user = username).delete()
        my_form.save()
        values = userInfoModel.objects.get(user = username)
        result = get_predictions(values.age, values.sex, values.cp, values.trestbps, values.chol, values.fbs, values.restecg, values.thalach, values.exang, values.oldpeak, values.slope, values.ca, values.thal)
        print("result=", result)
        context = {
            'obj': result,
            'object': values
        }
        
    else:
        my_form.save()
    
    return render(request, 'user_info_page_show_record.html', context)

def change_password_view(request, *args, **kwargs):
    username = request.GET.get('user')
    context = {"object": username}
    return render(request, 'change_password.html', context)

def change_password_view_record(request, *args, **kwargs):
    #context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print("username and pwd=", username, password)
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            userModel.objects.filter(username=username).update(password=password)
            
    return render(request, 'login.html', {})