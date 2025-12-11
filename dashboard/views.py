from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from main.models import IndexPage, IndexPartner, IndexPartnerImages, IndexHowitWorks, IndexHowitWorksObj, IndexWebStats, IndexTestimonials, IndexTestimonialObj, WhatOurCustomersSay, WhatOurCustomersSayObj
from django.shortcuts import  get_object_or_404


# Create your views here.

def base(request):
    return render(request,'dashboard/admin_base/admin_base.html')

@login_required
def dashboard(request):
    return render(request,'dashboard/dashboard/dashboard.html')





def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user_obj = User.objects.get(email=email)
            user = authenticate(
                request,
                username=user_obj.username,
                password=password
            )
        except User.DoesNotExist:
            user = None

        if user is not None:
            login(request, user)
            return redirect('dashboard:dashboard')  
        else:
            messages.error(request, "Invalid email or password")

    return render(request, 'dashboard/login/login.html')




@login_required
def logout_view(request):
    logout(request)
    return redirect('dashboard:login')



@login_required
def admin_dashboard(request):
    context = {
        'index': IndexPage.objects.last(),
        'index_partners': IndexPartner.objects.last(),
        'index_partner_images': IndexPartnerImages.objects.all(),
        'index_howitworks': IndexHowitWorks.objects.last(),
        'index_howitworks_obj': IndexHowitWorksObj.objects.all(),
        'index_webstats': IndexWebStats.objects.last(),
        'index_testimonials': IndexTestimonials.objects.last(),
        'index_testimonial_obj': IndexTestimonialObj.objects.all(),
    }
    return render(request, 'dashboard/admin_home/home.html', context)

@login_required
def update_index_page(request):
    if request.method == 'POST':
        index = IndexPage.objects.last()
        if not index:
            index = IndexPage()
        index.title = request.POST.get('title')
        index.description = request.POST.get('description')
        if request.FILES.get('image'):
            index.image = request.FILES.get('image')
        index.save()
    return redirect('dashboard:admin_dashboard')

@login_required
def update_partners(request):
    if request.method == 'POST':
        partner = IndexPartner.objects.last()
        if not partner:
            partner = IndexPartner()
        partner.title = request.POST.get('title')
        partner.description = request.POST.get('description')
        partner.save()
    return redirect('dashboard:admin_dashboard')

@login_required
def add_partner_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        IndexPartnerImages.objects.create(image=request.FILES.get('image'))
    return redirect('dashboard:admin_dashboard')

@login_required
def delete_partner_image(request, id):
    if request.method == 'POST':
        image = get_object_or_404(IndexPartnerImages, id=id)
        image.delete()
    return redirect('dashboard:admin_dashboard')

@login_required
def update_howitworks(request):
    if request.method == 'POST':
        hiw = IndexHowitWorks.objects.last()
        if not hiw:
            hiw = IndexHowitWorks()
        hiw.title = request.POST.get('title')
        hiw.description = request.POST.get('description')
        hiw.second_title = request.POST.get('second_title')
        hiw.secondary_description = request.POST.get('secondary_description')
        hiw.save()
    return redirect('dashboard:admin_dashboard')

@login_required
def add_howitworks_step(request):
    if request.method == 'POST':
        IndexHowitWorksObj.objects.create(
            howitwoeks_title=request.POST.get('howitwoeks_title'),
            howitwoeks_description=request.POST.get('howitwoeks_description')
        )
    return redirect('dashboard:admin_dashboard')

@login_required
def update_howitworks_step(request, id):
    if request.method == 'POST':
        step = get_object_or_404(IndexHowitWorksObj, id=id)
        step.howitwoeks_title = request.POST.get('howitwoeks_title')
        step.howitwoeks_description = request.POST.get('howitwoeks_description')
        step.save()
    return redirect('dashboard:admin_dashboard')

@login_required
def delete_howitworks_step(request, id):
    if request.method == 'POST':
        step = get_object_or_404(IndexHowitWorksObj, id=id)
        step.delete()
    return redirect('dashboard:admin_dashboard')

@login_required
def update_webstats(request):
    if request.method == 'POST':
        stats = IndexWebStats.objects.last()
        if not stats:
            stats = IndexWebStats()
        stats.title = request.POST.get('title')
        stats.description = request.POST.get('description')
        stats.happy_customers = request.POST.get('happy_customers')
        stats.total_services = request.POST.get('total_services')
        stats.reviews = request.POST.get('reviews')
        stats.total_partners = request.POST.get('total_partners')
        stats.save()
    return redirect('dashboard:admin_dashboard')


@login_required
def admin_dashboard(request):
    context = {
        'index': IndexPage.objects.last(),
        'index_partners': IndexPartner.objects.last(),
        'index_partner_images': IndexPartnerImages.objects.all(),
        'index_howitworks': IndexHowitWorks.objects.last(),
        'index_howitworks_obj': IndexHowitWorksObj.objects.all(),
        'index_webstats': IndexWebStats.objects.last(),
        'index_testimonials': WhatOurCustomersSay.objects.last(),  # Changed
        'index_testimonial_obj': WhatOurCustomersSayObj.objects.all(),  # Changed
    }
    return render(request, 'dashboard/admin_home/home.html', context)

@login_required
def update_testimonials(request):
    if request.method == 'POST':
        testimonials = WhatOurCustomersSay.objects.last()  # Changed
        if not testimonials:
            testimonials = WhatOurCustomersSay()  # Changed
        testimonials.title = request.POST.get('title')
        testimonials.description = request.POST.get('description')
        testimonials.save()
    return redirect('dashboard:admin_dashboard')

@login_required
def add_testimonial(request):
    if request.method == 'POST':
        WhatOurCustomersSayObj.objects.create(  # Changed
            customer_name=request.POST.get('customer_name'),
            customer_position=request.POST.get('customer_position'),
            testimonial=request.POST.get('testimonial'),
            customer_image=request.FILES.get('customer_image')
        )
    return redirect('dashboard:admin_dashboard')

@login_required
def update_testimonial(request, id):
    if request.method == 'POST':
        testimonial = get_object_or_404(WhatOurCustomersSayObj, id=id)  # Changed
        testimonial.customer_name = request.POST.get('customer_name')
        testimonial.customer_position = request.POST.get('customer_position')
        testimonial.testimonial = request.POST.get('testimonial')
        if request.FILES.get('customer_image'):
            testimonial.customer_image = request.FILES.get('customer_image')
        testimonial.save()
    return redirect('dashboard:admin_dashboard')

@login_required
def delete_testimonial(request, id):
    if request.method == 'POST':
        testimonial = get_object_or_404(WhatOurCustomersSayObj, id=id)  
        testimonial.delete()
    return redirect('dashboard:admin_dashboard')