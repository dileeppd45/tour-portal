from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login, name="login"),
    path('login', views.login, name="login"),

    path('admin_home', views.admin_home, name='admin_home'),

    path('pending_reg', views.pending_reg, name='pending_reg'),
    path('approved_reg', views.approved_reg, name='approved_reg'),
    path('rejected_reg', views.rejected_reg, name='rejected_reg'),

    path('pending_view_taxi/<int:id>', views.pending_view_taxi, name='pending_view_taxi'),
    path('reject_view_taxi/<int:id>', views.reject_view_taxi, name='reject_view_taxi'),
    path('approve_view_taxi/<int:id>', views.approve_view_taxi, name='approve_view_taxi'),

    path('pending_approve_taxi/<int:id>', views.pending_approve_taxi, name='pending_approve_taxi'),
    path('reject_approve_taxi/<int:id>', views.reject_approve_taxi, name='reject_approve_taxi'),


    path('pending_reject_taxi/<int:id>', views.pending_reject_taxi, name='pending_reject_taxi'),
    path('approve_reject_taxi/<int:id>', views.approve_reject_taxi, name='approve_reject_taxi'),

    path('reject_delete_taxi/<int:id>', views.reject_delete_taxi, name='reject_delete_taxi'),
    path('approve_delete_taxi/<int:id>', views.approve_delete_taxi, name='approve_delete_taxi'),


    path('admin_pending_complaint',views.admin_pending_complaint,name='admin_pending_complaint'),
    path('admin_replied_complaints',views.admin_replied_complaints, name='admin_replied_complaints'),

    path('reply_complaints/<int:id>', views.reply_complaints, name='reply_complaints'),
    path('edit_reply_complaints/<int:id>', views.edit_reply_complaints, name='edit_reply_complaints'),

    path('reply_submit/<int:id>',views.reply_submit, name='reply_submit'),
    path('edit_reply_submit/<int:id>',views.edit_reply_submit, name='edit_reply_submit'),
    path('problems', views.problems, name='problems'),
    path('add_problem', views.add_problem, name='add_problem'),
    path('update_problem/<str:id>', views.update_problem, name='update_problem'),
    path('delete_problem/<str:id>', views.delete_problem, name='delete_problem'),
    path('view_district', views.view_district, name='view_district'),
    path('add_place/<str:id>', views.add_place, name='add_place'),
    path('view_places/<str:id>', views.view_places, name='view_places'),
    path('update_place/<str:id>', views.update_place, name='update_place'),
    path('delete_place/<str:id>', views.delete_place, name='delete_place'),


]