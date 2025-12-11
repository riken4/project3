from django.shortcuts import render
from .models import IndexPage, IndexPartner, IndexPartnerImages, IndexHowitWorks, IndexHowitWorksObj, IndexWebStats, IndexTestimonials, IndexTestimonialObj,OrganizationSettings
from .models import WhatOurCustomersSay,WhatOurCustomersSayObj
from .models import PricingPage, PricingOptionOne, PricingOptionTwo, PricingOptionThree, PricingOptionFour
from .models import AddonService,AddonServiceOption,WhyChooseUs,WhatCustomersSay,TeamPage,TeamMember,Blog,AboutUs,BlogPage
from django.shortcuts import render, get_object_or_404
from .models import FAQPage, FAQ
from .models import TermsOfService




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
    one=PricingOptionOne.objects.last()
    two=PricingOptionTwo.objects.last()
    three=PricingOptionThree.objects.last()
    four=PricingOptionFour.objects.last()
    servive_header=AddonService.objects.last
    service_option=AddonServiceOption.objects.all()
    why_choose_us=WhyChooseUs.objects.all()
    our_customers_say=WhatCustomersSay.objects.all()
    context ={
        'header': header,
        'one': one,
        'two': two,
        'three': three, 
        'four': four,
        'servive_header': servive_header,
        'service_option':service_option,
        'why_choose_us':why_choose_us,
        'our_customers_say':our_customers_say,
    }

    return render(request, 'price.html',context) 



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
#************************************
# Views for About
#************************************

def about(request):
    about_header=AboutUs.objects.last()
    about_content=AboutUs.objects.all()
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


