from . import views
from django.urls import path

urlpatterns = [
    path('login',views.login,name="login"),
    path('',views.login_home,name="loginhome"),
    path('loginhome',views.login_home,name="loginhome"),
    path('adminindex',views.admin_home,name="adminindex"),
    path('adminlogout', views.admin_logout, name='admin_logout'),
    path('tlogout', views.t_logout, name='tlogout'),
    path('vlogout', views.v_logout, name='vlogout'),
    path('register_t', views.register_t, name='register_t'),
    path('register_v', views.register_v, name='register_v'),
    path('tindex',views.t_home,name="tindex"),
    path('vindex',views.v_home,name="vindex"),
    path('tagency_request',views.tagency_request,name="tagency_request"),
    path('view_tagency',views.view_tagency,name="view_tagency"),
    path('vagency_request',views.vagency_request,name="vagency_request"),
    path('view_vagency',views.view_vagency, name="view_vagency"),
    path('approve_tagency/<str:id>',views.approve_tagency,name="approve_tagency"),
    path('approve_vagency/<str:id>', views.approve_vagency, name="approve_vagency"),
    path('view_user', views.view_user, name='view_user'),
    path('feedbacks', views.feedbacks, name='feedbacks'),
    path('add_vehicle_type', views.add_vehicle_type, name="add_vehicle_type"),
    path('vehicle_type', views.vehicle_type, name="vehicle_type"),
    path('add_company/<str:id>', views.add_company, name='add_company'),
    path('view_company/<str:id>', views.view_company, name='view_company'),
    path('view_packages/<str:id>', views.view_packages, name='view_packages'),
    path('view_vehtypes/<str:id>', views.view_vehtypes, name='view_vehtypes'),
    path('view_vehicles/<str:id>', views.view_vehicles, name='view_vehicles'),
    path('view_vbookings/<str:id>', views.view_vbookings, name='view_vbookings'),
    path('view_pbookings/<str:id>', views.view_pbookings, name='view_pbookings'),
    path('vehicle_booked_uer/<str:id>', views.vehicle_booked_user, name='vehicle_booked_user'),
    path('package_booked_user/<str:id>', views.package_booked_user, name='package_booked_user'),









    path('tview_packages', views.tview_packages, name='tview_packages'),
    path('add_package',views.add_package, name='add_package'),
    path('edit_package/<str:id>',views.edit_package, name='edit_package'),
    path('delete_package/<str:id>',views.delete_package, name='delete_package'),
    path('package_requests/<str:id>',views.package_requests, name='package_requests'),
    path('approve_prequest/<str:id>', views.approve_prequest, name='approve_prequest'),
    path('package_bookedp/<str:id>', views.package_bookedp, name='package_bookedp'),






    path('vview_vehtypes', views.vview_vehtypes, name='vview_vehtypes'),
    path('select_company/<str:id>', views.select_company, name='select_company'),
    path('add_vehicle/<str:id>',views.add_vehicle, name='add_vehicle'),
    path('vview_vehicles', views.vview_vehicles, name='vview_vehicles'),
    path('vview_vehicless/<str:id>', views.vview_vehicless, name='vview_vehicless'),
    path('upload_pimage/<str:id>', views.upload_pimage, name='upload_pimage'),
    path('upload_vimage/<str:id>', views.upload_vimage, name='upload_vimage'),
    path('edit_vehicle/<str:id>', views.edit_vehicle, name='edit_vehicle'),
    path("delete_vehicle/<str:id>", views.delete_vehicle, name='delete_vehicle'),
    path("make_available/<str:id>", views.make_available, name='make_available'),
    path('view_vvbookings/<str:id>', views.view_vvbookings, name="view_vvbookings"),







    #
    # path('adminprofile', views.admin_profile, name='admin_profile'),
    # path('update_profile', views.update_profile, name='update_profile'),
    # path('change_password', views.change_password, name='change_password'),

    #
    # path('add_route', views.add_route, name='add_route'),
    # path('view_route', views.view_route, name='view_route'),
    # path('add_route_signal/<str:id>', views.add_signal, name='add_signal'),
    # path('view_route_signal/<str:id>', views.view_signal, name='view_signal'),
    # path('add_staff', views.add_staff, name='add_staff'),
    # path('view_staff', views.view_staff, name='view_staff'),
    # path('update_staff/<str:id>', views.update_staff, name='update_staff'),
    # path('delete_staff/<str:id>', views.delete_staff, name='delete_staff'),
    # path('allocate_staff/<str:id>', views.allocate_staff, name='allocate_staff'),
    # path('view_allocated_staff/<str:id>', views.allocated_staff, name='allocated_staff'),
    # path('remove_staff/<str:id>', views.remove_staff, name='remove_staff'),
    # path('adminlogout',views.admin_logout,name="adminlogout"),
    # path('tlogout',views.t_logout,name="tlogout"),
    # path('vlogout',views.v_logout,name="vlogout"),
    # path('add_fine', views.add_user_fine, name='add_fine'),
    # path('view_fine', views.view_fine, name='view_fine'),
]