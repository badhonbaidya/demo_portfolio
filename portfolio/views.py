from django.http import HttpResponse
from django.shortcuts import render,redirect
from . models import About
from django.contrib import messages
import random
import re
from django.core.signing import Signer
from datetime import datetime
from django.core.mail import send_mail
from django.utils.html import format_html




# def home(request):

    # data = About.objects.first()
    # context_data = {'d':data}
    # print("this is root url function")

    # return render(request,'demo/portfolio.html',context_data)



# def login(request):
    # if 'user_id' in request.session.get('social_auth_google_oauth2')
    # if 'user_id' in request.session or google_data:
#     if 'user_id' in request.session:
#         return redirect('about')
#     else:
#         return render(request,'login.html')
# def logout(request):
#     request.session.flush()
#     return redirect('login')
    
    

# def login_admin(request):
#     email = request.POST.get('email')
#     password = request.POST.get('pass')
#     log_data = About.objects.get(email=email)

#     if(log_data.password==password and log_data.v_status=='1'):

#         request.session['user_id'] = log_data.id
#         request.session['user_name'] = log_data.U_name

#         return redirect('about')
#     else:
#         return redirect('login')


def about_index(request):
    # if 'user_id' in request.session.get('social_auth_google_oauth2')
    # if 'user_id' in request.session or google_data:
        all_data = About.objects.all()
        msg = messages.get_messages(request)
        # print(msg)
        data = {'d':all_data,'msg':msg}
        return render(request,'admin/about.html', data)
    # else:
    #     return redirect('logout')




def reg_confirm(request):
    return render(request,'reg_conf.html')

def email_verify(request,id):
    data = About.objects.get(v_c=id)
    bool_var = False
    if data.v_status=='0':
        bool_var = 0

        data.v_status = 1
        data.save()

        # bool_dic = {'d':bool_var}
        
        return redirect('about')
        # return HttpResponse("This is zero")
    else:
        bool_var = 1
         
        bool_dic = {'d':bool_var}
        return render (request,'success.html',bool_dic)
    
         

    # return redirect('about')

def about_insert(request):

    U_name=request.POST.get('U_name')
    dob=request.POST.get('dob')
    phone=request.POST.get('phone')
    email=request.POST.get('email')
    exp=request.POST.get('exp')
    no_cust=request.POST.get('no_cust')
    no_project_finished=request.POST.get('no_project_finished')
    no_of_awards=request.POST.get('no_of_awards')
    desc=request.POST.get('desc')
    current_datetime=datetime.now()
    formatted_datetime = current_datetime.strftime("%d %b %Y-%I:%M %p")
    password = request.POST.get('password')

    # pattern = r"^[a-zA-Z0-9_.]+@gmail/.com$"

    # Check if any of the required fields is empty
    # if not all ([U_name, dob, phone, email, exp, no_cust, no_project_finished,  no_of_awards, desc]):
    #     # messages.clear()
         
        
    #     messages.success(request,"the field can not be empty")
    #     return HttpResponse ("All fields are required.")
    # else:
#     if not re.match(pattern, email):
#         messages.success(request,"you email is not gmail")
# elif len(phone)!=11:
# messages.success(request,"your mobile Number must have 11 disit")

#     else:
#         data = about_objects.all()
#         len_data = len(data)
#         if (len_data>=1):
#              messages.success(request,"you can not entry more then onen data")
#         else:
    
    current_time = datetime.now().strftime("%H:%M:%S")
    print(current_time.split(':'))
    h, m, s = map(int,current_time.split(':'))
    t_s = h*3600+m*60+s
    random_number = random.choices('1234567890',k=4)
    random_number = ''.join(random_number)
    t_s = str(t_s)
    v_c = t_s + random_number
    signer = Signer()
    encrypted_value = signer.sign(v_c).split(":")[1]
    
    link = f"<p>congratulations Mr {U_name} ! For registering as a user in our portfolio System. to confirm the registration </p><a href='http://127.0.0.1:8000/admin/user/email_verification/"+encrypted_value+"'target='_blank'>please click this Activation link</a>"

    send_mail(f"Mr. {U_name} please confirm your Registration - portfolio panel",encrypted_value,'badhonbaidya2@gmail.com',[email],html_message=link)
    print(encrypted_value)

    about_obj = About()


    about_obj.U_name=U_name
    about_obj.dob=dob
    about_obj.phone=phone
    about_obj.email=email
    about_obj.no_exp=exp
    about_obj.no_happy_customers=no_cust
    about_obj.no_project_finished=no_project_finished
    about_obj.no_digital_awards=no_of_awards
    about_obj.description=desc
    about_obj.v_c = encrypted_value
    about_obj.v_status = 0
    about_obj.password = password
    about_obj.save()
     

    # formatted_datetime = current_datetime.strftime("%d %b %Y-%I:%M %p")

    # print ("this is root url function")
    return redirect('reg_conf')


def edit_index(request, id):
    allData = About.objects.get(id=id)
    dictn = {'data': allData}
    return render(request, 'admin/edit.html', dictn)


def about_edit(request):
    id = request.POST.get('id')
    U_name=request.POST.get('U_name')
    dob=request.POST.get('dob')
    phone=request.POST.get('phone')
    email=request.POST.get('email')
    exp=request.POST.get('exp')
    no_cust=request.POST.get('no_cust')
    no_project_finished=request.POST.get('no_project_finished')
    no_of_awards=request.POST.get('no_of_awards')
    desc=request.POST.get('desc')
    current_datetime=datetime.now()
    formatted_datetime = current_datetime.strftime("%d %b %Y-%I:%M %p")


    about_obj = About.objects.get(id=id)

    about_obj.U_name=U_name
    about_obj.dob=dob
    about_obj.phone=phone
    about_obj.email=email
    about_obj.no_exp=exp
    about_obj.no_happy_customers=no_cust
    about_obj.no_project_finished=no_project_finished
    about_obj.no_digital_awards=no_of_awards
    about_obj.description=desc
    about_obj.save()
     
    return redirect('about')




def delete_index(request,id):
    data1 = About.objects.get(id=id)
    data1.delete()
     
    return  redirect('about')
 


