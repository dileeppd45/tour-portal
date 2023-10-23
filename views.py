from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect
from django.db import connection
from django.contrib import messages
from . import views

# Create your views here.



def login(request):
    if request.method == "POST":
        userid = request.POST['userid']
        password = request.POST['password']
        cursor = connection.cursor()
        cursor.execute("select * from login where admin_id= '" + userid + "' AND password = '" + password + "'")
        admin = cursor.fetchone()
        if admin == None:
            return render(request, "login.html")
        else:
            return redirect("admin_home")

    return render(request, "login.html")

def admin_home(request):
    return render(request, "admin_home.html")



def pending_reg(request):#pending_taxi
    cursor = connection.cursor()
    cursor.execute("select * from taxi_registration where status='pending'")
    cdata = cursor.fetchall()
    table0 = list(cdata)
    length = len(table0)
    if length == 0:
        val = "pending taxis"
        return render(request, "ptano_carts.html", {"val": val})
    else:
        return render(request, "pending_reg.html",  {'cdata': cdata})

def pending_view_taxi(request,id):
    cursor=connection.cursor()
    cursor.execute("select taxi_registration.idtaxi_registration,taxi_registration.taxi_number,taxi_registration.adhar_number,taxi_registration.owner_name,taxi_registration.address,taxi_registration.phone,taxi_registration.status,place.place_name,district.name from taxi_registration join place join district ON taxi_registration.idplace = place.idplace and place.iddistrict = district.iddistrict  and taxi_registration.iddistrict = district.iddistrict where idtaxi_registration ='"+str(id)+"' ")
    data=cursor.fetchone()
    return render(request,"view_taxi.html",{"data":data})

def pending_approve_taxi(request,id):
    cursor=connection.cursor()
    cursor.execute("update taxi_registration set status='approved' where idtaxi_registration ='"+str(id)+"'")
    return redirect('pending_reg')

def pending_reject_taxi(request,id):
    cursor=connection.cursor()
    cursor.execute("update taxi_registration set status='rejected' where idtaxi_registration ='"+str(id)+"'")
    return redirect('pending_reg')




def approved_reg(request):#approved taxi
    cursor=connection.cursor()
    cursor.execute("select * from taxi_registration where status='approved'")
    cdata = cursor.fetchall()
    table0 = list(cdata)
    length = len(table0)
    if length == 0:
        val = "Approved Taxis"
        return render(request, "atano_carts.html", {"val": val})
    else:
        return render(request, "approved_reg.html", {'cdata': cdata})

def approve_view_taxi(request,id):
    cursor=connection.cursor()
    cursor.execute("select taxi_registration.idtaxi_registration,taxi_registration.taxi_number,taxi_registration.adhar_number,taxi_registration.owner_name,taxi_registration.address,taxi_registration.phone,taxi_registration.status,place.place_name,district.name from taxi_registration join place join district ON taxi_registration.idplace = place.idplace and place.iddistrict = district.iddistrict  and taxi_registration.iddistrict = district.iddistrict where idtaxi_registration ='"+str(id)+"' ")
    data=cursor.fetchone()
    return render(request,"approved_view_taxi.html",{"data":data})

def approve_delete_taxi(request,id):
    cursor=connection.cursor()
    cursor.execute("delete from taxi_registration where idtaxi_registration ='"+str(id)+"'")
    return redirect('approved_reg')

def approve_reject_taxi(request,id):#pending taxi
    cursor=connection.cursor()
    cursor.execute("update taxi_registration set status='rejected' where idtaxi_registration ='"+str(id)+"'")
    return redirect('approved_reg')





def rejected_reg(request):#regected taxi
    cursor = connection.cursor()
    cursor.execute("select * from taxi_registration where status='rejected'")
    cdata = cursor.fetchall()
    table0 = list(cdata)
    length = len(table0)
    if length == 0:
        val = "Rejected Taxis"
        return render(request, "rtano_carts.html", {"val": val})
    else:
        return render(request, "rejected_reg.html", {'cdata': cdata})

def reject_view_taxi(request,id):
    cursor=connection.cursor()
    cursor.execute("select taxi_registration.idtaxi_registration,taxi_registration.taxi_number,taxi_registration.adhar_number,taxi_registration.owner_name,taxi_registration.address,taxi_registration.phone,taxi_registration.status,place.place_name,district.name from taxi_registration join place join district ON taxi_registration.idplace = place.idplace and place.iddistrict = district.iddistrict  and taxi_registration.iddistrict = district.iddistrict where idtaxi_registration ='"+str(id)+"' ")
    data=cursor.fetchone()
    return render(request,"rejected_view_taxi.html",{"data":data})

def reject_approve_taxi(request,id):
    cursor=connection.cursor()
    cursor.execute("update taxi_registration set status='approved' where idtaxi_registration ='"+str(id)+"'")
    return redirect('rejected_reg')

def reject_delete_taxi(request,id):
    cursor=connection.cursor()
    cursor.execute("delete from taxi_registration where idtaxi_registration ='"+str(id)+"'")
    return redirect('rejected_reg')






def admin_pending_complaint(request):
    cursor = connection.cursor()
    cursor.execute("select * from complaint where reply = 'no reply' ")
    table = cursor.fetchall()
    table0 = list(table)
    length = len(table0)
    if length == 0:
        val = "complaints"
        return render(request, "pcano_carts.html", {"val": val})
    else:
        return render(request, "admin_pending_complaint.html", {"table": table})

def admin_replied_complaints(request):
    cursor = connection.cursor()
    cursor.execute("select * from complaint where reply != 'no reply' ")
    table = cursor.fetchall()
    table0 = list(table)
    length = len(table0)
    if length == 0:
        val = "replys"
        return render(request, "rcano_carts.html", {"val": val})
    else:
        return render(request, "admin_replied_complaint.html", {"table": table})

def reply_complaints(request, id):
    cursor = connection.cursor()
    cursor.execute("select * from complaint where idcomplaint ='" + str(id) + "'")
    row = cursor.fetchone()
    return render(request, "reply_form.html", {"data": row})

def edit_reply_complaints(request, id):
    cursor = connection.cursor()
    cursor.execute("select * from complaint where idcomplaint ='" + str(id) + "' ")
    row = cursor.fetchone()
    return render(request, "edit_reply_form.html", {"data": row})

def reply_submit(request,id):
    if request.method == "POST":
        reply = request.POST['reply']
        cursor = connection.cursor()
        cursor.execute(" update complaint set reply='" + str(reply) + "' where idcomplaint='" + str(id) + "' ")
        return redirect(admin_pending_complaint)

def edit_reply_submit(request,id):
    if request.method == "POST":
        reply = request.POST['reply']
        cursor = connection.cursor()
        cursor.execute(" update complaint set reply='" + str(reply) + "' where idcomplaint='" + str(id) + "' ")
        return redirect(admin_replied_complaints)


def view_district(request):
    cursor = connection.cursor()
    cursor.execute("select * from district ")
    row = cursor.fetchall()
    return render(request, "view_district.html", {"data": row})

def view_places(request,id):
    cursor = connection.cursor()
    cursor.execute("select * from place where iddistrict ='"+str(id)+"' ")
    data = cursor.fetchall()
    return  render(request,'view_places.html',{'data':data})

def add_place(request,id):
    if request.method == "POST":
        place = request.POST['pn']
        cursor = connection.cursor()
        cursor.execute(" insert into place values(null,'"+str(id)+"','"+str(place)+"') ")
        return redirect(add_place,id)
    return render(request,'add_place.html')

def update_place(request,id):
    cursor = connection.cursor()
    if request.method == "POST":
        place = request.POST['pn']
        cursor = connection.cursor()
        cursor.execute("select iddistrict from place where idplace ='"+str(id)+"' ")
        data = cursor.fetchone()
        data = list(data)
        data = data[0]
        cursor.execute(" update place set place_name ='"+str(place)+"' where idplace ='"+str(id)+"' ")
        return redirect(view_places,id = str(data))
    cursor.execute("select * from place where idplace = '"+str(id)+"' ")
    data = cursor.fetchone
    return render(request,'update_place.html',{'data':data})

def delete_place(request,id):
    cursor = connection.cursor()
    cursor.execute("select iddistrict from place where idplace ='" + str(id) + "' ")
    data = cursor.fetchone()
    data = list(data)
    data = data[0]
    cursor.execute("delete from place where idplace ='"+str(id)+"' ")
    return redirect(view_places, id =str(data))

def problems(request):
    cursor = connection.cursor()
    cursor.execute("select * from problem_place ")
    data = cursor.fetchall()
    return render(request, 'problems.html', {'data': data})

def add_problem(request):
    if request.method == "POST":
        title = request.POST['title']
        details = request.POST['details']
        lat = request.POST['lat']
        lon = request.POST['lon']
        cursor = connection.cursor()
        cursor.execute(" insert into problem_place values(null,'"+str(title)+"','"+str(details)+"','"+str(lat)+"','"+str(lon)+"', curdate() )")
        return redirect(problems)
    return render(request,'add_problem.html')

def update_problem(request,id):
    if request.method == "POST":
        title = request.POST['title']
        details = request.POST['details']
        lat = request.POST['lat']
        lon = request.POST['lon']
        cursor = connection.cursor()
        cursor.execute(" update problem_place set title ='"+str(title)+"', details ='"+str(details)+"', latitude ='"+str(lat)+"', longitude ='"+str(lon)+"', date_post = curdate() where idproblem_place ='"+str(id)+"' ")
        return redirect(problems)
    cursor = connection.cursor()
    cursor.execute("select * from problem_place where idproblem_place ='"+str(id)+"' ")
    data = cursor.fetchone()
    return render(request,'update_problem.html',{'data':data})

def delete_problem(request,id):
    cursor = connection.cursor()
    cursor.execute("delete from problem_place where idproblem_place ='"+str(id)+"' ")
    return redirect(problems)
