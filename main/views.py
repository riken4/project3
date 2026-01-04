from .models import IndexPage, IndexPartner, IndexPartnerImages, IndexHowitWorks, IndexHowitWorksObj, IndexWebStats, IndexTestimonials, IndexTestimonialObj,OrganizationSettings
from .models import WhatOurCustomersSay,WhatOurCustomersSayObj
from .models import PricingPage, CommonPricingModel
from .models import AddonService,AddonServiceOption,WhyChooseUs,WhatCustomersSay,TeamPage,TeamMember,Blog,AboutUs,BlogPage, \
    CoreValues
from django.shortcuts import render, get_object_or_404, redirect
from .models import FAQPage, FAQ
from .models import TermsOfService

from .models import CommonPricingModel, SubscriptionPlan, UserSubscription
from .utils import get_active_subscription
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import SignupForm, LoginForm
from django.contrib import messages

from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.utils import timezone
from datetime import timedelta
import json


#************************************
# Views for Payment
#************************************
def checkout(request, pk):
    # import ipdb;ipdb.set_trace()
    if not request.user.is_authenticated:
        messages.warning(request, "Please login first to continue.")
        return redirect(f"/price_detail/{pk}/")

    pricing = get_object_or_404(CommonPricingModel, pk=pk)
    plan = get_object_or_404(SubscriptionPlan, pricing=pricing, is_active=True)
    
    existing_subscription = get_active_subscription(request.user, plan)

    if existing_subscription and existing_subscription.is_valid():
        messages.info(
            request,
            "You have already paid for this service. No need to pay again."
        )
        return redirect(f"/price_detail/{pk}/")

    context = {
        "option": pricing,
        "paypal_client_id": settings.PAYPAL_CLIENT_ID,
    }

    return render(request, "checkout.html", context)

@csrf_exempt
def payment_success(request, pk):
    pricing = get_object_or_404(CommonPricingModel, pk=pk)
    plan = get_object_or_404(SubscriptionPlan, pricing=pricing)
    if request.method == "POST":
        data = json.loads(request.body)
        paypal_id = data.get("id")

        # Prevent duplicate activation
        if UserSubscription.objects.filter(
            payment_id=paypal_id
        ).exists():
            return redirect(f"/price_detail/{pk}/")

        # Calculate end date
        end_date = None
        if plan.plan_type != "one_time":
            end_date = timezone.now() + timedelta(days=plan.duration_days)

        # Deactivate old subscriptions of same plan
        UserSubscription.objects.filter(
            user=request.user,
            plan=plan,
            is_active=True
        ).update(is_active=False)

        # Create new subscription
        UserSubscription.objects.create(
            user=request.user,
            plan=plan,
            start_date=timezone.now(),
            end_date=end_date,
            is_active=True,
            payment_id=paypal_id
        )
        return redirect("main:payment_success", pk=pk)
    ctx = {
        "option": pricing,
    }
    return render(request, "payment_success.html", ctx)


def payment_failed(request, pk):
    option = get_object_or_404(CommonPricingModel, pk=pk)
    context = {
        "option": option,
    }
    return render(request, "payment_failed.html", context)


#************************************
# Views for Index Page
#************************************
def home(request):
    index=IndexPage.objects.last()
    index_partners=IndexPartner.objects.last()
    latest_images = IndexPage.objects.order_by('-created_at')[:3]
    index_partner_images=IndexPartnerImages.objects.all()
    index_howitworks=IndexHowitWorks.objects.last()
    index_howitworks_obj=IndexHowitWorksObj.objects.all()
    index_webstats=IndexWebStats.objects.last()
    customers_say=WhatOurCustomersSay.objects.last()
    customers_say_obj=WhatOurCustomersSayObj.objects.all()
    org =OrganizationSettings.objects.last()
    context={
        'index':index,
        'index_partners':index_partners,
        'index_partner_images':index_partner_images,
        'index_howitworks':index_howitworks,
        'index_howitworks_obj':index_howitworks_obj,
        'index_webstats':index_webstats,    
        'customers_say':customers_say,
        'latest_images':latest_images,
        'customers_say_obj':customers_say_obj,
        'org':org,
    }
    return render(request, 'home.html',context)


#************************************
# Views for Pricing Page
#************************************


def price(request):
    header=PricingPage.objects.last()
    pricing_options = CommonPricingModel.objects.all()
    servive_header=AddonService.objects.last
    service_option=AddonServiceOption.objects.all()
    why_choose_us=WhyChooseUs.objects.all()
    our_customers_say=WhatCustomersSay.objects.all()
    context ={
        'header': header,
        'pricing_option': pricing_options,
        'servive_header': servive_header,
        'service_option':service_option,
        'why_choose_us':why_choose_us,
        'our_customers_say':our_customers_say,
    }

    return render(request, 'price.html',context) 



def price_detail(request, pk):
    option = get_object_or_404(CommonPricingModel, pk=pk)
    context = {
        'option': option,
    }
    return render(request, 'price_detail.html', context) 

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
    active_tab = "login"
    signup_form = SignupForm()
    login_form = LoginForm()

    if request.method == "POST":
        if "signup_request" in request.POST:
            active_tab = "signup"
            signup_form = SignupForm(request.POST)
            if signup_form.is_valid():
                user = User.objects.create_user(
                    email=signup_form.cleaned_data["email"],
                    password=signup_form.cleaned_data["password"],
                    username=signup_form.cleaned_data["full_name"]
                )
                return redirect("/")
        elif "login_request" in request.POST:
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                email = login_form.data.get("email")
                password = login_form.cleaned_data["password"]
                user = authenticate(email=email, password=password)
                if user:
                    login(request, user)
                    return redirect("/")
                return redirect("/")

    return render(request, "account.html", {
        "active_tab": active_tab,
        "signup_form": signup_form,
        "login_form": login_form,
    })

def user_logout(request):
    logout(request)
    return redirect("/")

#************************************
# Views for About
#************************************

def about(request):
    about_header=AboutUs.objects.last()
    about_content=CoreValues.objects.all()
    index_webstats=IndexWebStats.objects.last()
    members=TeamMember.objects.all()
  
    context={
        'about_header':about_header,
        'about_content':about_content,
        'index_webstats':index_webstats,
        'members':members,
        

    }
    return render(request, 'nav info/about.html',context) 


#************************************
# Views for Blog
#************************************

def blog(request):
    blog =Blog.objects.all()
    blog_page=BlogPage.objects.last()
    context ={
        'blog':blog,
        'blog_page':blog_page,

    }
    return render(request, 'nav info/blog.html',context) 


def blog_detail(request, id):
    # Get the specific blog post by ID
    blog_post = get_object_or_404(Blog, id=id)
    
    # Get other blogs excluding the current one
    other_blogs = Blog.objects.exclude(id=id).order_by('-created_at')
    
    context = {
        'blog_post': blog_post,
        'other_blogs': other_blogs,
    }
    return render(request, 'blog_detail.html', context)

#************************************
# Views Team Page
#************************************

def team(request):
    page=TeamPage.objects.last()
    members=TeamMember.objects.all()
    context={
        'page':page,
        'members':members,
    }
    return render(request, 'nav info/team.html',context) 




def faq(request):
    faq_page = FAQPage.objects.last()
    faqs = FAQ.objects.filter(is_active=True)
    
    context = {
        'faq_page': faq_page,
        'faqs': faqs,
    }
    return render(request, 'nav info/faq.html', context)


def privacy_policy(request):
    return render(request, 'nav info/privacy_policy.html') 

#************************************
# Views Terms and Condition Page
#************************************


def term_of_services(request):
    terms = get_object_or_404(TermsOfService)
    
    context = {
        'terms': terms,
    }
    
    return render(request, 'nav info/term_of_services.html', context)


def company_formation_info(request):
    return render(request, 'company_formation_info.html')

def order_summary(request):
    return render(request, 'order_summary.html')

def services(request):
    return render(request, 'services.html')

def annual_report_cart(request):
    return render(request, 'annual_report_cart.html')

def ein_payment(request):
    return render(request, 'ein_payment.html')

def irs_tax_filling(request):
    return render(request, 'irs_tax_filling.html')