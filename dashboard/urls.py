from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [

    path('', views.login_view, name='login'),             
    path('home/', views.dashboard, name='dashboard'),        
    path('logout/', views.logout_view, name='logout'),
    #path('change-password/', views.change_password, name='change_password'),

    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/update-index-page/', views.update_index_page, name='update_index_page'),
    path('admin/update-partners/', views.update_partners, name='update_partners'),
    path('admin/add-partner-image/', views.add_partner_image, name='add_partner_image'),
    path('admin/delete-partner-image/<int:id>/', views.delete_partner_image, name='delete_partner_image'),
    path('admin/update-howitworks/', views.update_howitworks, name='update_howitworks'),
    path('admin/add-howitworks-step/', views.add_howitworks_step, name='add_howitworks_step'),
    path('admin/update-howitworks-step/<int:id>/', views.update_howitworks_step, name='update_howitworks_step'),
    path('admin/delete-howitworks-step/<int:id>/', views.delete_howitworks_step, name='delete_howitworks_step'),
    path('admin/update-webstats/', views.update_webstats, name='update_webstats'),
    path('admin/update-testimonials/', views.update_testimonials, name='update_testimonials'),
    path('admin/add-testimonial/', views.add_testimonial, name='add_testimonial'),
    path('admin/update-testimonial/<int:id>/', views.update_testimonial, name='update_testimonial'),
    path('admin/delete-testimonial/<int:id>/', views.delete_testimonial, name='delete_testimonial'),



]