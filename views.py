from django.db import connection
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect


# Create your views here.

def login_home(request):
    return render(request,'login_home.html')

def login(request):
    if request.method == 'POST':
        idname = request.POST['name']
        password = request.POST['password']
        print(idname,password)

        cursor = connection.cursor()
        cursor.execute("select * from login where admin_id = '"+str(idname)+"' and password = '"+str(password)+"'")
        admin = cursor.fetchone()
        cursor.execute("select * from tour_agency where agency_id ='"+str(idname)+"' and password ='"+str(password)+"' and status = 'approved' ")
        tagency = cursor.fetchone()
        cursor.execute("select * from vehicle_agency where vehicle_agency_id ='"+str(idname)+"' and password ='"+str(password)+"' and status = 'approved' ")
        vagency = cursor.fetchone()
        if admin == None:
            if tagency == None:
                if vagency == None:
                    return HttpResponse("<script>alert('invalid login');window.location='../login';</script>")
                else:
                    request.session["vagencyid"] = idname
                    return redirect('vindex')
            else:
                request.session["tagencyid"] = idname
                return redirect('tindex')
        else:
            request.session["adminid"] = idname
            return redirect('adminindex')
    else:
        return render(request,'login.html')

def logout(request):
    return redirect('loginhome')

def admin_home(request):

    return render(request,'admin/index.html')
def t_home(request):
    d = request.session["tagencyid"]
    cursor = connection.cursor()
    cursor.execute("select name from tour_agency where agency_id ='"+str(d)+"' ")
    data = cursor.fetchone()
    data = list(data)
    return render(request,'tour/index.html',{'name':data[0]})
def v_home(request):
    d = request.session["vagencyid"]
    cursor = connection.cursor()
    cursor.execute("select name from vehicle_agency where vehicle_agency_id ='" + str(d) + "' ")
    data = cursor.fetchone()
    data = list(data)
    return render(request,'vehicle/index.html',{'name':data[0]})

def tagency_request(request):
    cursor = connection.cursor()
    cursor.execute("select * from tour_agency where status ='pending'")
    data = cursor.fetchall()
    return render(request, 'admin/tagency_request.html',{'data':data})

def view_tagency(request):
    cursor = connection.cursor()
    cursor.execute("select * from tour_agency where status ='approved'")
    data = cursor.fetchall()
    return render(request, 'admin/view_tagency.html',{'data':data})

def vagency_request(request):
    cursor = connection.cursor()
    cursor.execute("select * from vehicle_agency where status ='pending'")
    data = cursor.fetchall()
    return render(request, 'admin/vagency_request.html',{'data':data})

def approve_tagency(request,id):
    cursor = connection.cursor()
    cursor.execute("update tour_agency set status ='approved' where agency_id ='"+str(id)+"'")
    return redirect(tagency_request)

def approve_vagency(request,id):
    cursor = connection.cursor()
    cursor.execute("update vehicle_agency set status ='approved' where vehicle_agency_id ='"+str(id)+"'")
    return redirect(vagency_request)

def view_vagency(request):
    cursor = connection.cursor()
    cursor.execute("select * from vehicle_agency where status ='approved'")
    data = cursor.fetchall()
    return render(request, 'admin/view_vagency.html',{'data':data})

def view_user(request):
    cursor = connection.cursor()
    cursor.execute("select * from user_register ")
    data = cursor.fetchall()
    return render(request, 'admin/view_users.html',{'data':data})

def package_booked_user(request,id):
    cursor = connection.cursor()
    cursor.execute("select package_booking.*,package.* from package_booking join package where package_booking.user_id ='"+str(id)+"' and package_booking.idpackage = package.idpackage and package_booking.status = 'payed' ")
    data = cursor.fetchall()
    return render(request,'admin/view_upbookings.html',{'data':data})

def vehicle_booked_user(request,id):
    cursor = connection.cursor()
    cursor.execute("select vehicle_booking.*, vehicle_details.*, company.name from vehicle_booking join vehicle_details join company where vehicle_booking.user_id = '"+str(id)+"' and vehicle_details.idvehicle_details = vehicle_booking.idvehicle_detials  and vehicle_booking.status ='booked' and vehicle_details.company_id = company.companyid ")
    data = cursor.fetchall()
    return render(request,'admin/view_uvbookings.html',{'data':data})

def feedbacks(request):
    cursor = connection.cursor()
    cursor.execute("select feedback.*, user_register.name from feedback join user_register where feedback.user_id = user_register.user_id ")
    data = cursor.fetchall()
    return render(request, 'admin/feedbacks.html',{'data':data})

def register_t(request):
    if request.method == 'POST':
        tid = request.POST['tid']
        name = request.POST['name']
        address = request.POST['address']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        # longitude = request.POST['longitude']
        cursor = connection.cursor()
        cursor.execute("select * from login where admin_id ='"+str(tid)+"' ")
        admin = cursor.fetchone()
        cursor.execute("select * from tour_agency where agency_id ='" + str(tid) + "' ")
        tour = cursor.fetchone()
        cursor.execute("select * from vehicle_agency where vehicle_agency_id ='" + str(tid) + "' ")
        vehicle = cursor.fetchone()
        if admin == None:
            if tour == None:
                if vehicle == None:
                    cursor.execute("insert into tour_agency values('"+str(tid)+"','"+name+"','"+address+"','"+phone+"','"+email+"','"+password+"','pending')")
                    return HttpResponse("<script>alert('Registration complete');window.location='../login';</script>")
                else:
                    return HttpResponse("<script>alert('the name you entered is already taken please use unique one ');window.location='../login';</script>")
            else:
                return HttpResponse("<script>alert('the name you entered is already taken please use unique one ');window.location='../login';</script>")
        else:
            return HttpResponse("<script>alert('the name you entered is already taken please use unique one ');window.location='../login';</script>")

    else:
        return render(request,'register_t.html')

def register_v(request):
    if request.method == 'POST':
        vid = request.POST['vid']
        name = request.POST['name']
        address = request.POST['address']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        # longitude = request.POST['longitude']
        cursor = connection.cursor()
        cursor.execute("select * from login where admin_id ='"+str(vid)+"' ")
        admin = cursor.fetchone()
        cursor.execute("select * from tour_agency where agency_id ='" + str(vid) + "' ")
        tour = cursor.fetchone()
        cursor.execute("select * from vehicle_agency where vehicle_agency_id ='" + str(vid) + "' ")
        vehicle = cursor.fetchone()
        if admin == None:
            if tour == None:
                if vehicle == None:
                    cursor.execute("insert into vehicle_agency values('"+str(vid)+"','"+name+"','"+address+"','"+phone+"','"+email+"','"+password+"','pending')")
                    return HttpResponse("<script>alert('Registration complete');window.location='../login';</script>")
                else:
                    return HttpResponse("<script>alert('the name you entered is already taken please use unique one ');window.location='../login';</script>")
            else:
                return HttpResponse("<script>alert('the name you entered is already taken please use unique one ');window.location='../login';</script>")
        else:
            return HttpResponse("<script>alert('the name you entered is already taken please use unique one ');window.location='../login';</script>")

    else:
        return render(request,'register_v.html')

def admin_logout(request):
    return render(request,'admin/LogOut.html')
def t_logout(request):
    return render(request,'tour/LogOut.html')
def v_logout(request):
    return render(request,'vehicle/LogOut.html')

def add_vehicle_type(request):
    if request.method == 'POST':
        vtype = request.POST['vtype']
        # address = request.POST['address']
        # phone = request.POST['phone']
        # exp = request.POST['experience']
        cursor = connection.cursor()
        cursor.execute("insert into vehicle_type values(null,'"+vtype+"')")
        return redirect(add_vehicle_type)
    else:
        return render(request,'admin/add_vehicle_type.html')

def vehicle_type(request):
    cursor = connection.cursor()
    cursor.execute("select * from vehicle_type ")
    data = cursor.fetchall()
    return render(request, 'admin/vehicle_type.html',{'data':data})

def add_company(request, id):
    if request.method == 'POST':
        company = request.POST['company']
        # address = request.POST['address']
        # phone = request.POST['phone']
        # exp = request.POST['experience']
        cursor = connection.cursor()
        cursor.execute("insert into company values(null,'"+company+"','"+str(id)+"')")
        return redirect('add_company', id=id)
    else:
        return render(request,'admin/add_company.html')

def view_company(request,id):
    cursor = connection.cursor()
    cursor.execute("select * from company where id_vehicle_type ='"+str(id)+"' ")
    data = cursor.fetchall()
    return render(request, 'admin/view_company.html',{'data':data})

def view_packages(request,id):
    cursor = connection.cursor()
    cursor.execute("select * from package where agency_id='"+str(id)+"' ")
    data = cursor.fetchall()
    return render(request, 'admin/view_packages.html', {'data': data})

def view_vehtypes(request,id):
    cursor = connection.cursor()
    cursor.execute("select idvehicle_type from vehicle_details where vehicle_agency_id ='"+str(id)+"'")
    mata =cursor.fetchone()
    if mata == None:
        return HttpResponse("<script>alert('No Vehicles');window.location='../adminindex';</script>")
    cursor.execute("select idvehicle_type from vehicle_details where vehicle_agency_id ='" + str(id) + "'")
    data = cursor.fetchall()
    l= []

    data = set(data)
    data = list(data)
    for i in data:
        print(i[0])
        l.append(i[0])
    print(l)
    li =[]
    n = int(0)
    for i in l:
        n = n+1
        cursor.execute("select name from vehicle_type where idvehicle_type ='"+str(i)+"' ")
        data = cursor.fetchone()
        li.append(data[0])
    m = {}
    m = set(m)
    for i in range(n):
        s = (l[i],li[i])
        m.add(s)
    print(m)
    request.session["vaid"] = id
    return render(request,'admin/view_vehtypes.html',{'data': m})

def view_vehicles(request,id):
    vaid = request.session["vaid"]
    cursor = connection.cursor()
    cursor.execute("select vehicle_details.* ,company.name from vehicle_details join company where vehicle_details.vehicle_agency_id ='"+str(vaid)+"' and vehicle_details.idvehicle_type ='"+str(id)+"' and company.companyid = vehicle_details.company_id")
    data = cursor.fetchall()
    return render(request,'admin/view_vehicles.html',{'data':data})

def view_vbookings(request,id):
    cursor = connection.cursor()
    cursor.execute("select vehicle_booking.* ,user_register.* from vehicle_booking join user_register where vehicle_booking.idvehicle_detials ='"+str(id)+"' and vehicle_booking.user_id = user_register.user_id ")
    data = cursor.fetchall()
    cursor.execute("select vehicle_no,vehicle_image from vehicle_details where idvehicle_details = '"+str(id)+"' ")
    vn = cursor.fetchone()
    vno = vn[0]
    vimg = vn[1]
    print(vno)
    return render(request,'admin/view_vbookings.html',{'data':data,'vno':vno,'vimg':vimg})

def view_vvbookings(request,id):
    cursor = connection.cursor()
    cursor.execute("select vehicle_booking.* ,user_register.* from vehicle_booking join user_register where vehicle_booking.idvehicle_detials ='"+str(id)+"' and vehicle_booking.user_id = user_register.user_id ")
    data = cursor.fetchall()
    cursor.execute("select vehicle_no,vehicle_image from vehicle_details where idvehicle_details = '"+str(id)+"' ")
    vn = cursor.fetchone()
    vno = vn[0]
    vimg = vn[1]
    print(vno)
    return render(request,'vehicle/view_vbookings.html',{'data':data,'vno':vno,'vimg':vimg})

def view_pbookings(request,id):
    cursor = connection.cursor()
    cursor.execute("select package_booking.* ,user_register.* from package_booking join user_register where package_booking.idpackage ='"+str(id)+"' and package_booking.user_id = user_register.user_id and package_booking.status ='paid' ")
    data = cursor.fetchall()
    cursor.execute("select package_description,place_image from package where idpackage = '"+str(id)+"' ")
    vn = cursor.fetchone()
    vno = vn[0]
    vimg = vn[1]
    print(vno)
    return render(request,'admin/view_pbookings.html',{'data':data,'vno':vno,'vimg':vimg})


def tview_packages(request):
    cursor = connection.cursor()
    id = request.session["tagencyid"]
    # cursor.execute("select agency_id from tour_agency where name='"+str(id)+"'")
    # name = cursor.fetchone()
    cursor.execute("select * from package where agency_id='"+str(id)+"' ")
    data = cursor.fetchall()
    return render(request, 'tour/view_packages.html', {'data': data})

def add_package(request):
    if request.method == 'POST':
        cursor = connection.cursor()
        id = request.session["tagencyid"]
        # cursor.execute("select agency_id from tour_agency where name='" + str(id) + "'")
        # name = cursor.fetchone()
        package = request.POST['package']
        place = request.POST['place']
        description = request.POST['description']
        days = request.POST['days']
        rate = request.POST['rate']
        cursor.execute("insert into package values(null,'"+place+"','"+str(description)+"','"+package+"','"+str(days)+"','"+rate+"','"+str(id)+"','pending')")
        return redirect(add_package)
    else:
        return render(request,'tour/add_package.html')

def edit_package(request,id):
    if request.method == 'POST':
        cursor = connection.cursor()
        package = request.POST['package']
        place = request.POST['place']
        description = request.POST['description']
        days = request.POST['days']
        rate = request.POST['rate']
        cursor.execute("update package set place ='"+place+"',place_description ='"+str(description)+"',package_description ='"+package+"',no_of_days= '"+str(days)+"', rate ='"+rate+"' where idpackage ='"+str(id)+"'")
        return redirect(tview_packages)
    else:
        cursor = connection.cursor()
        cursor.execute("select * from package where idpackage ='"+str(id)+"' ")
        data = cursor.fetchone()
        return render(request,'tour/edit_package.html',{'data':data})
def delete_package(request,id):
    cursor = connection.cursor()
    cursor.execute("delete from package where idpackage ='"+str(id)+"' ")
    return redirect(tview_packages)

def package_requests(request,id):
    cursor = connection.cursor()
    cursor.execute("select package_booking.*, user_register.* from package_booking join user_register where package_booking.status ='pending' and package_booking.idpackage='"+str(id)+"' and package_booking.user_id = user_register.user_id")
    data = cursor.fetchall()
    cursor.execute("select package_description,place_image from package where idpackage = '" + str(id) + "' ")
    vn = cursor.fetchone()
    vno = vn[0]
    vimg = vn[1]
    print(vno)
    return render(request,'tour/package_request.html',{'data': data, 'vno': vno, 'vimg': vimg})

def approve_prequest(request,id):
    cursor = connection.cursor()
    cursor.execute("update package_booking set status = 'approved' where idpackage_booking ='"+str(id)+"' ")
    return redirect(tview_packages)

def package_bookedp(request,id):
    cursor = connection.cursor()
    cursor.execute("select package_booking.*, user_register.* from package_booking join user_register where package_booking.status ='paid' and package_booking.idpackage='"+str(id)+"' and package_booking.user_id = user_register.user_id")
    data = cursor.fetchall()
    cursor.execute("select package_description,place_image from package where idpackage = '" + str(id) + "' ")
    vn = cursor.fetchone()
    vno = vn[0]
    vimg = vn[1]
    print(vno)
    return render(request,'tour/package_booked.html',{'data': data, 'vno': vno, 'vimg': vimg})



def vview_vehtypes(request):
    cursor = connection.cursor()
    cursor.execute("select * from vehicle_type ")
    data = cursor.fetchall()
    return render(request,'vehicle/vview_vehtypes.html', {'data':data})

def select_company(request,id):
    cursor = connection.cursor()
    cursor.execute("select * from company where id_vehicle_type ='"+str(id)+"'")
    data = cursor.fetchall()
    return render(request,'vehicle/select_company.html',{'data':data})

def add_vehicle(request,id):
    if request.method == 'POST':
        cursor = connection.cursor()
        cursor.execute("select id_vehicle_type from company where companyid ='"+str(id)+"' ")
        data = cursor.fetchone()
        vid = request.session["vagencyid"]
        # cursor.execute("select vehicle_agency_id from vehicle_agency where name='" + str(vid) + "'")
        # name = cursor.fetchone()
        vehno = request.POST['vehno']
        model = request.POST['model']
        rent = request.POST['rent']
        cursor.execute("insert into vehicle_details values(null,'"+vehno+"','"+str(id)+"','"+model+"','"+str(rent)+"','"+str(vid)+"','"+str(data[0])+"','available','null')")
        return redirect('add_vehicle', id=id)
    else:
        return render(request,'vehicle/add_vehicle.html')


def vview_vehicles(request):
    cursor = connection.cursor()
    vid = request.session["vagencyid"]
    cursor.execute("select vehicle_agency_id from vehicle_agency where name='" + str(vid) + "'")
    name = cursor.fetchone()
    cursor.execute("select idvehicle_type from vehicle_details where vehicle_agency_id ='"+str(vid)+"'")
    mata =cursor.fetchone()
    if mata == None:
        return HttpResponse("<script>alert('No Vehicles');window.location='../vindex';</script>")
    cursor.execute("select idvehicle_type from vehicle_details where vehicle_agency_id ='" + str(vid) + "'")
    data = cursor.fetchall()
    l= []

    data = set(data)
    data = list(data)
    for i in data:
        print(i[0])
        l.append(i[0])
    print(l)
    li =[]
    n = int(0)
    for i in l:
        n = n+1
        cursor.execute("select name from vehicle_type where idvehicle_type ='"+str(i)+"' ")
        data = cursor.fetchone()
        li.append(data[0])
    m = {}
    m = set(m)
    for i in range(n):
        s = (l[i],li[i])
        m.add(s)
    print(m)
    return render(request,'vehicle/view_vehtypes.html',{'data': m})

def vview_vehicless(request,id):
    cursor = connection.cursor()
    vid = request.session["vagencyid"]
    # cursor.execute("select vehicle_agency_id from vehicle_agency where name='" + str(vid) + "'")
    # name = cursor.fetchone()
    cursor.execute("select vehicle_details.* ,company.name from vehicle_details join company where vehicle_details.vehicle_agency_id ='" +str(vid)+"' and vehicle_details.idvehicle_type ='" + str(
            id) + "' and company.companyid = vehicle_details.company_id")
    data = cursor.fetchall()
    return render(request, 'vehicle/view_vehicles.html', {'data': data})

def make_available(request,id):
    cursor = connection.cursor()
    cursor.execute("update vehicle_details set status = 'available' where idvehicle_details = '"+str(id)+"'")
    return redirect(vview_vehicles)

def upload_pimage(request,id):
    return render(request,'tour/upload_pimage.html',{'id':id})

def upload_vimage(request,id):
    return render(request,'vehicle/upload_vimage.html',{'id':id})

def edit_vehicle(request,id):
    if request.method == 'POST':
        cursor = connection.cursor()
        cursor.execute("select id_vehicle_type from company where companyid ='"+str(id)+"' ")
        data = cursor.fetchone()
        vid = request.session["vagencyid"]
        cursor.execute("select vehicle_agency_id from vehicle_agency where name='" + str(vid) + "'")
        name = cursor.fetchone()
        vehno = request.POST['vehno']
        model = request.POST['model']
        rent = request.POST['rent']
        cursor.execute("update vehicle_details set vehicle_no ='"+vehno+"', model ='"+model+"', daily_rent ='"+str(rent)+"' where idvehicle_details ='"+str(id)+"' ")
        return redirect(vview_vehicles)
    else:
        cursor = connection.cursor()
        cursor.execute("select * from vehicle_details where idvehicle_details ='"+str(id)+"'")
        data = cursor.fetchone()
        return render(request,'vehicle/edit_vehicle.html', {'data':data})

def delete_vehicle(request,id):
    cursor = connection.cursor()
    cursor.execute("delete from vehicle_details where idvehicle_details ='"+str(id)+"' ")
    return redirect(vview_vehicles)


































#
# def admin_profile(request):
#     cursor = connection.cursor()
#     cursor.execute("select * from login")
#     data = cursor.fetchone()
#     return render(request, 'traffic/admin_profile.html', {'data':data})
# def update_profile(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         address = request.POST['address']
#         email = request.POST['email']
#         cursor = connection.cursor()
#         cursor.execute("update login set name ='"+str(name)+"', address ='"+str(address)+"', email ='"+str(email)+"' where admin_id ='admin' ")
#         return redirect(admin_profile)
#     else:
#         cursor = connection.cursor()
#         cursor.execute("select * from login")
#         data = cursor.fetchone()
#         return render(request, 'traffic/update_profile.html',{'data':data})
#
# def change_password(request):
#     if request.method == 'POST':
#         old = request.POST['old_password']
#         new = request.POST['new_password']
#         conform = request.POST['conform_password']
#         # longitude = request.POST['longitude']
#         cursor = connection.cursor()
#         cursor.execute("select password from login where admin_id = 'admin' ")
#         password =cursor.fetchone()
#         print(password[0])
#         if password[0] == old:
#             if new == conform:
#                 cursor.execute("update login set password ='"+str(conform)+"' where admin_id ='admin' ")
#                 return redirect(admin_profile)
#             else:
#                 return HttpResponse("<script>alert('please enter same new password  in conform password');window.location='../adminprofile';</script>")
#         else:
#             return HttpResponse("<script>alert('incorrect password please validate ');window.location='../adminprofile';</script>")
#
#
#     else:
#         return render(request,'traffic/change_password.html')
#
# def add_user_fine(request):
#     if request.method == 'POST':
#         veh_no = request.POST['veh_no']
#         amount = request.POST['amount']
#
#         # latitude = request.POST['latitude']
#         # longitude = request.POST['longitude']
#         cursor = connection.cursor()
#         cursor.execute("insert into user_fine values(null,'"+veh_no+"','"+amount+"',curdate() )")
#         return redirect(add_user_fine)
#     else:
#         return render(request,'traffic/add_fine.html')
#
# def view_fine(request):
#     cursor = connection.cursor()
#     cursor.execute("select * from user_fine ")
#     fine = cursor.fetchall()
#     return render(request, 'traffic/view_fine.html', {'data': fine})
#
# def add_route(request):
#     if request.method == 'POST':
#         place = request.POST['start_place']
#         destination = request.POST['destination']
#         # latitude = request.POST['latitude']
#         # longitude = request.POST['longitude']
#         cursor = connection.cursor()
#         cursor.execute("insert into route values(null,'"+place+"','"+destination+"')")
#         return redirect(add_route)
#     else:
#         return render(request,'traffic/add_route.html')
#
#
# def view_route(request):
#     cursor = connection.cursor()
#     cursor.execute("select * from route ")
#     route = cursor.fetchall()
#     return render(request,'traffic/view_route.html',{'data':route})
#
# def add_signal(request,id):
#     if request.method == 'POST':
#         place = request.POST['place']
#         # destination = request.POST['destination']
#         # latitude = request.POST['latitude']
#         # longitude = request.POST['longitude']
#         cursor = connection.cursor()
#         cursor.execute("insert into route_signal values(null,'"+id+"','"+place+"')")
#         return redirect('add_signal', id=id)
#     else:
#         return render(request,'traffic/add_route_signal.html')
#
# def view_signal(request,id):
#     cursor = connection.cursor()
#     cursor.execute("select * from route_signal where idroute ='"+id+"' ")
#     signal = cursor.fetchall()
#     return render(request,'traffic/view_route_signal.html',{'data':signal})
#
# def add_staff(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         address = request.POST['address']
#         phone = request.POST['phone']
#         exp = request.POST['experience']
#         cursor = connection.cursor()
#         cursor.execute("insert into traffic_staff values(null,'"+name+"','"+address+"','"+phone+"','"+exp+"','null','pending')")
#         return redirect(add_staff)
#     else:
#         return render(request,'traffic/add_staff.html')
# def view_staff(request):
#     cursor = connection.cursor()
#     cursor.execute("select * from traffic_staff ")
#     route = cursor.fetchall()
#     return render(request,'traffic/view_staff.html',{'data':route})
#
# def update_staff(request,id):
#     if request.method == 'POST':
#         name = request.POST['name']
#         address = request.POST['address']
#         phone = request.POST['phone']
#         exp = request.POST['experience']
#         cursor = connection.cursor()
#         cursor.execute("update traffic_staff set name ='" + name + "', address ='" + address + "',phone ='" + phone + "',work_experience ='" + exp + "' where idtraffic_staff ='"+str(id)+"' ")
#         return redirect(view_staff)
#     else:
#         cursor = connection.cursor()
#         cursor.execute("select * from traffic_staff where idtraffic_staff ='"+str(id)+"' ")
#         data = cursor.fetchone()
#         return render(request, 'traffic/update_staff.html',{'data':data})
#
# def delete_staff(request,id):
#     cursor = connection.cursor()
#     cursor.execute("delete from traffic_staff where idtraffic_staff ='"+str(id)+"'")
#     return redirect(view_staff)
#
# def allocate_staff(request,id):
#     if request.method == 'POST':
#         sid = request.POST['staffid']
#         # address = request.POST['address']
#         # phone = request.POST['phone']
#         # exp = request.POST['experience']
#         cursor = connection.cursor()
#         cursor.execute("update traffic_staff set idroute_signal ='" + id + "', allocation_date = curdate() where idtraffic_staff ='"+str(sid)+"' ")
#         return redirect('allocate_staff',id=id)
#     else:
#         cursor = connection.cursor()
#         cursor.execute("select * from traffic_staff where idroute_signal ='null' ")
#         data = cursor.fetchall()
#         return render(request, 'traffic/allocate_staff.html',{'data':data})
#
# def allocated_staff(request,id):
#     cursor = connection.cursor()
#     cursor.execute("select * from traffic_staff where idroute_signal ='"+str(id)+"'")
#     data = cursor.fetchall()
#     return render(request, 'traffic/allocated_staff.html',{'data':data})
#
# def remove_staff(request,id):
#     cursor =connection.cursor()
#     cursor.execute("update traffic_staff set idroute_signal ='null' where idtraffic_staff ='"+str(id)+"' ")
#     return redirect(view_route)




