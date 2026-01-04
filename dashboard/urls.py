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
    
    # pricing related start
    path('admin/price-info/', views.price_intro, name='price_info'),
    path('admin/update_price_intro/', views.update_price_intro, name='update_price_intro'),
    
    path('admin/add_package_plan/', views.add_package_plan, name='add_package_plan'),
    path('admin/update_package_plan/<int:id>/', views.update_package_plan, name='update_package_plan'),
    path('admin/delete_package_plan/<int:id>/', views.delete_package_plan, name='delete_package_plan'),

    path('admin/add_addon_services/', views.add_addon_services, name='add_addon_services'),
    path('admin/update_addon_services/<int:id>/', views.update_addon_services, name='update_addon_services'),
    path('admin/delete_addon_services/<int:id>/', views.delete_addon_services, name='delete_addon_services'),
    
    path('admin/add_why_choose_us/', views.add_why_choose_us, name='add_why_choose_us'),
    path('admin/update_why_choose_us/<int:id>/', views.update_why_choose_us, name='update_why_choose_us'),
    path('admin/delete_why_choose_us/<int:id>/', views.delete_why_choose_us, name='delete_why_choose_us'),
    
    path('admin/add-what-customers-say/', views.add_what_customers_say, name='add_what_customers_say'),
    path('admin/update-what-customers-say/<int:id>/', views.update_what_customers_say, name='update_what_customers_say'),
    path('admin/delete-what-customers-say/<int:id>/', views.delete_what_customers_say, name='delete_what_customers_say'),
    # pricing related end

    # about us related start
    path('about-header/', views.about_us_header_manage, name='about_header'),
    path('about-header/delete/<int:pk>/', views.delete_about_us, name='delete_about_us'),
    
    path('admin/add-core-values/', views.add_core_values, name='add_core_values'),
    path('admin/update-core-values/<int:id>/', views.update_core_values, name='update_core_values'),
    path('admin/delete-core-values/<int:id>/', views.delete_core_values, name='delete_core_values'),
    # about us related end
    
    # Team Member related start
    path('admin/team/', views.team_page, name='team_page'),
    path('admin/team/header/', views.manage_team_header, name='manage_team_header'),
    
    path('admin/add-team-member/', views.add_team_member, name='add_team_member'),
    path('admin/update-team-member/<int:id>/', views.update_team_member, name='update_team_member'),
    path('admin/delete-team-member/<int:id>/', views.delete_team_member, name='delete_team_member'),
    # Team Member related end
]