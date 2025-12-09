from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'), 
    path('price/', views.price, name='price'),
    path('price_detail/', views.price_detail, name='price_detail'),
    path('register_agent/', views.register_agent, name='register_agent'),
    path('company_formation/', views.company_formation, name='company_formation'),
    path('ein_registration/', views.ein_registration, name='ein_registration'),
    path('annual_report_filing/', views.annual_report_filing, name='annual_report_filing'),
    path('expert_taxes/', views.expert_taxes, name='expert_taxes'),
    path('file_your_own_taxes/', views.file_your_own_taxes, name='file_your_own_taxes'),
    path('refund_advance/', views.refund_advance, name='refund_advance'),
    path('flex_advance/', views.flex_advance, name='flex_advance'),
    path('account/', views.account, name='account'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('blog_detail/', views.blog_detail, name='blog_detail'),
    path('team/', views.team, name='team'),
    path('faq/', views.faq, name='faq'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('term_of_services/', views.term_of_services, name='term_of_services'),
    path('company_formation_info/', views.company_formation_info, name='company_formation_info'),
    path('order_summary/', views.order_summary, name='order_summary'),
    path('services/', views.services, name='services'),
    path('annual_report_cart/', views.annual_report_cart, name='annual_report_cart'),



]