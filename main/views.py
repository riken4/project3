from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html') 

def price(request):
    return render(request, 'price.html') 

def price_detail(request):
    return render(request, 'price_detail.html') 

def register_agent(request):
    return render(request, 'register_agent.html') 

def company_formation(request):
    return render(request, 'company_formation.html') 

def ein_registration(request):
    return render(request, 'ein_registration.html') 

def annual_report_filing(request):
    return render(request, 'annual_report_filing.html') 

def expert_taxes(request):
    return render(request, 'expert_taxes.html') 

def file_your_own_taxes(request):
    return render(request, 'file_your_own_taxes.html') 

def refund_advance(request):
    return render(request, 'refund_advance.html') 

def flex_advance(request):
    return render(request, 'flex_advance.html') 

def account(request):
    return render(request, 'account.html') 

def about(request):
    return render(request, 'nav info/about.html') 

def blog(request):
    return render(request, 'nav info/blog.html') 


def blog_detail(request):
    return render(request, 'blog_detail.html') 

def team(request):
    return render(request, 'nav info/team.html') 


def faq(request):
    return render(request, 'nav info/faq.html') 


def privacy_policy(request):
    return render(request, 'nav info/privacy_policy.html') 


def term_of_services(request):
    return render(request, 'nav info/term_of_services.html') 

def company_formation_info(request):
    return render(request, 'company_formation_info.html')

def order_summary(request):
    return render(request, 'order_summary.html')

def services(request):
    return render(request, 'services.html')

def annual_report_cart(request):
    return render(request, 'annual_report_cart.html')