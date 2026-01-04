from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from main.models import IndexPage, IndexPartner, IndexPartnerImages, IndexHowitWorks, IndexHowitWorksObj, IndexWebStats, \
    IndexTestimonials, IndexTestimonialObj, WhatOurCustomersSay, WhatOurCustomersSayObj
from django.shortcuts import  get_object_or_404

from .decorators import superuser_required
from main.models import PricingPage, CommonPricingModel, AddonServiceOption, WhyChooseUs, WhatCustomersSay, AboutUs, \
    CoreValues, TeamMember, TeamPage
from .forms import PackagePlanForm, AddonServiceOptionForm, WhyChooseUsForm, WhatCustomersSayForm, AboutUsForm, \
    CoreValuesForm, TeamMemberForm, TeamPageForm
from django.urls import reverse
# Create your views here.

def base(request):
    return render(request,'dashboard/admin_base/admin_base.html')

@superuser_required
def dashboard(request):
    return render(request,'dashboard/dashboard/dashboard.html')





def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user_obj = User.objects.get(email=email)
            if not user_obj.is_superuser:
                messages.error(request, "You are not authorized to access the admin panel.")
                return render(request, 'dashboard/login/login.html')
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




@superuser_required
def logout_view(request):
    logout(request)
    return redirect('dashboard:login')



@superuser_required
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

@superuser_required
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

@superuser_required
def update_partners(request):
    if request.method == 'POST':
        partner = IndexPartner.objects.last()
        if not partner:
            partner = IndexPartner()
        partner.title = request.POST.get('title')
        partner.description = request.POST.get('description')
        partner.save()
    return redirect('dashboard:admin_dashboard')

@superuser_required
def add_partner_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        IndexPartnerImages.objects.create(image=request.FILES.get('image'))
    return redirect('dashboard:admin_dashboard')

@superuser_required
def delete_partner_image(request, id):
    if request.method == 'POST':
        image = get_object_or_404(IndexPartnerImages, id=id)
        image.delete()
    return redirect('dashboard:admin_dashboard')

@superuser_required
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

@superuser_required
def add_howitworks_step(request):
    if request.method == 'POST':
        IndexHowitWorksObj.objects.create(
            howitwoeks_title=request.POST.get('howitwoeks_title'),
            howitwoeks_description=request.POST.get('howitwoeks_description')
        )
    return redirect('dashboard:admin_dashboard')

@superuser_required
def update_howitworks_step(request, id):
    if request.method == 'POST':
        step = get_object_or_404(IndexHowitWorksObj, id=id)
        step.howitwoeks_title = request.POST.get('howitwoeks_title')
        step.howitwoeks_description = request.POST.get('howitwoeks_description')
        step.save()
    return redirect('dashboard:admin_dashboard')

@superuser_required
def delete_howitworks_step(request, id):
    if request.method == 'POST':
        step = get_object_or_404(IndexHowitWorksObj, id=id)
        step.delete()
    return redirect('dashboard:admin_dashboard')

@superuser_required
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

@superuser_required
def update_testimonials(request):
    if request.method == 'POST':
        testimonials = WhatOurCustomersSay.objects.last()  # Changed
        if not testimonials:
            testimonials = WhatOurCustomersSay()  # Changed
        testimonials.title = request.POST.get('title')
        testimonials.description = request.POST.get('description')
        testimonials.save()
    return redirect('dashboard:admin_dashboard')

@superuser_required
def add_testimonial(request):
    if request.method == 'POST':
        WhatOurCustomersSayObj.objects.create(  # Changed
            customer_name=request.POST.get('customer_name'),
            customer_position=request.POST.get('customer_position'),
            testimonial=request.POST.get('testimonial'),
            customer_image=request.FILES.get('customer_image')
        )
    return redirect('dashboard:admin_dashboard')

@superuser_required
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

@superuser_required
def delete_testimonial(request, id):
    if request.method == 'POST':
        testimonial = get_object_or_404(WhatOurCustomersSayObj, id=id)  
        testimonial.delete()
    return redirect('dashboard:admin_dashboard')


#************************************
# Pricing Section Viewsets
#************************************
def pricing_base_context():
    return {
        # lists
        'price_intro': PricingPage.objects.last(),
        'package_options': CommonPricingModel.objects.all(),
        'addon_services': AddonServiceOption.objects.all(),
        'why_choose_us': WhyChooseUs.objects.all(),
        'what_customers_say': WhatCustomersSay.objects.all(),
        
        # empty forms
        'package_plan_add_form': PackagePlanForm(),
        'package_plan_edit_form': None,
        'addon_services_add_form': AddonServiceOptionForm(),
        'addon_services_edit_form': None,
        'why_choose_us_add_form': WhyChooseUsForm(),
        'why_choose_us_edit_form': None,
        'what_customers_say_add_form': WhatCustomersSayForm(),
        'what_customers_say_edit_form': None,

        # flags (default OFF)
        'show_packageplan_addform': False,
        'show_packageplan_editform': False,
        'show_addonservice_addform': False,
        'show_addonservice_editform': False,
        'show_whychooseus_addform': False,
        'show_whychooseus_editform': False,
        'show_whatcustomersay_addform': False,
        'show_whatcustomersay_editform': False,
    }

@superuser_required
def price_intro(request):
    ctx = pricing_base_context()
    return render(request, 'dashboard/pricings/pricing.html', ctx)

@superuser_required
def update_price_intro(request):
    if request.method == 'POST':
        pricingpage = PricingPage.objects.last()
        if not pricingpage:
            pricingpage = PricingPage()
        pricingpage.title = request.POST.get('title')
        pricingpage.description = request.POST.get('description')
        if request.FILES.get('image'):
            pricingpage.image = request.FILES.get('image')
        pricingpage.save()
    return redirect('dashboard:price_info')

@superuser_required
def add_package_plan(request):
    ctx = pricing_base_context()

    if request.method == 'POST':
        form = PackagePlanForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/admin/price-info/?section=packageplan')

        ctx['package_plan_add_form'] = form
        ctx['show_packageplan_addform'] = True

    return render(request, 'dashboard/pricings/pricing.html', ctx)

@superuser_required
def update_package_plan(request, id):
    instance = get_object_or_404(CommonPricingModel, id=id)
    ctx = pricing_base_context()

    if request.method == 'POST':
        form = PackagePlanForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/admin/price-info/?section=packageplan')
    else:
        form = PackagePlanForm(instance=instance)

    ctx['package_plan_edit_form'] = form
    ctx['show_packageplan_editform'] = True

    return render(request, 'dashboard/pricings/pricing.html', ctx)



@superuser_required
def delete_package_plan(request, id):
    package = get_object_or_404(CommonPricingModel, id=id)

    if request.method == 'POST':
        package.delete()

    return redirect('/dashboard/admin/price-info/?section=packageplan')

@superuser_required
def add_addon_services(request):
    ctx = pricing_base_context()

    if request.method == 'POST':
        form = AddonServiceOptionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/admin/price-info/?section=addonservices')

        ctx['addon_services_add_form'] = form
        ctx['show_addonservice_addform'] = True

    return render(request, 'dashboard/pricings/pricing.html', ctx)


@superuser_required
def update_addon_services(request, id):
    instance = get_object_or_404(AddonServiceOption, id=id)
    ctx = pricing_base_context()

    if request.method == 'POST':
        form = AddonServiceOptionForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/admin/price-info/?section=addonservices')
    else:
        form = AddonServiceOptionForm(instance=instance)

    ctx['addon_services_edit_form'] = form
    ctx['show_addonservice_editform'] = True

    return render(request, 'dashboard/pricings/pricing.html', ctx)



@superuser_required
def delete_addon_services(request, id):
    package = get_object_or_404(AddonServiceOption, id=id)

    if request.method == 'POST':
        package.delete()

    return redirect('/dashboard/admin/price-info/?section=addonservices')


@superuser_required
def add_why_choose_us(request):
    ctx = pricing_base_context()

    if request.method == 'POST':
        form = WhyChooseUsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/admin/price-info/?section=whychooseus')

    ctx['why_choose_us_add_form'] = form
    ctx['show_whychooseus_addform'] = True

    return render(request, 'dashboard/pricings/pricing.html', ctx)


@superuser_required
def update_why_choose_us(request, id):
    instance = get_object_or_404(WhyChooseUs, id=id)
    ctx = pricing_base_context()

    if request.method == 'POST':
        form = WhyChooseUsForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/admin/price-info/?section=whychooseus')
    else:
        form = WhyChooseUsForm(instance=instance)

    ctx['why_choose_us_edit_form'] = form
    ctx['show_whychooseus_editform'] = True

    return render(request, 'dashboard/pricings/pricing.html', ctx)


@superuser_required
def delete_why_choose_us(request, id):
    package = get_object_or_404(WhyChooseUs, id=id)

    if request.method == 'POST':
        package.delete()

    return redirect('/dashboard/admin/price-info/?section=whychooseus')


@superuser_required
def add_what_customers_say(request):
    ctx = pricing_base_context()

    if request.method == 'POST':
        form = WhatCustomersSayForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/admin/price-info/?section=whatcustomersay')

        ctx['what_customers_say_add_form'] = form
        ctx['show_whatcustomersay_addform'] = True

    return render(request, 'dashboard/pricings/pricing.html', ctx)


@superuser_required
def update_what_customers_say(request, id):
    instance = get_object_or_404(WhatCustomersSay, id=id)
    ctx = pricing_base_context()

    if request.method == 'POST':
        form = WhatCustomersSayForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/admin/price-info/?section=whatcustomersay')
    else:
        form = WhatCustomersSayForm(instance=instance)

    ctx['what_customers_say_edit_form'] = form
    ctx['show_whatcustomersay_editform'] = True

    return render(request, 'dashboard/pricings/pricing.html', ctx)


@superuser_required
def delete_what_customers_say(request, id):
    obj = get_object_or_404(WhatCustomersSay, id=id)

    if request.method == 'POST':
        obj.delete()

    return redirect('/dashboard/admin/price-info/?section=whatcustomersay')


#************************************
# About Us Section Viewsets
#************************************
def core_values_base_context():
    return {
        'core_values': CoreValues.objects.all().order_by('id'),

        'core_values_add_form': CoreValuesForm(),
        'core_values_edit_form': None,

        'show_corevalues_addform': False,
        'show_corevalues_editform': False,
    }


@superuser_required
def about_us_header_manage(request):
    # Get all AboutUs objects, hero first
    about_us_list = AboutUs.objects.all().order_by('-display_in_banner')

    # Check if editing
    edit_id = request.GET.get('edit_id')
    if edit_id:
        about_instance = get_object_or_404(AboutUs, pk=edit_id)
        about_form = AboutUsForm(request.POST or None, request.FILES or None, instance=about_instance)
    else:
        about_form = AboutUsForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if about_form.is_valid():
            about_form.save()
            return redirect('/dashboard/about-header/?section=aboutheader')

    # Use your base context for consistency
    ctx = core_values_base_context()
    ctx['about_us_list'] = about_us_list
    ctx['about_header_form'] = about_form
    ctx['edit_id'] = edit_id
    return render(request, 'dashboard/About_us/about_us.html', ctx)


@superuser_required
def delete_about_us(request, pk):
    about_obj = get_object_or_404(AboutUs, pk=pk)
    about_obj.delete()
    messages.success(request, "About Us entry deleted successfully.")
    return redirect('/dashboard/about-header/?section=aboutheader')


@superuser_required
def add_core_values(request):
    ctx = core_values_base_context()

    if request.method == 'POST':
        form = CoreValuesForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to About Us page with corevalues tab
            return redirect('/dashboard/about-header/?section=corevalues')

        # If form invalid, show the add form again with errors
        ctx['core_values_add_form'] = form
        ctx['show_corevalues_addform'] = True

    return render(request, 'dashboard/About_us/about_us.html', ctx)


@superuser_required
def update_core_values(request, id):
    instance = get_object_or_404(CoreValues, id=id)
    ctx = core_values_base_context()

    if request.method == 'POST':
        form = CoreValuesForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/about-header/?section=corevalues')
    else:
        form = CoreValuesForm(instance=instance)

    ctx['core_values_edit_form'] = form
    ctx['show_corevalues_editform'] = True

    return render(request, 'dashboard/About_us/about_us.html', ctx)


@superuser_required
def delete_core_values(request, id):
    obj = get_object_or_404(CoreValues, id=id)

    if request.method == 'POST':
        obj.delete()

    return redirect('/dashboard/about-header/?section=corevalues')


#************************************
# Team Section Viewsets
#************************************
#************************************
# Team Section Base Context
#************************************
def team_member_base_context():
    team_header = TeamPage.objects.first()
    return {
        'team_header': team_header,
        'team_header_form': TeamPageForm(instance=team_header),
        'show_teamheader_form': False,

        'team_members': TeamMember.objects.all().order_by('id'),
        'team_add_form': TeamMemberForm(),
        'team_edit_form': None,
        'show_team_addform': False,
        'show_team_editform': False,
    }


@superuser_required
def add_team_member(request):
    ctx = team_member_base_context()

    if request.method == 'POST':
        form = TeamMemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/admin/add-team-member/?section=ourteam')

        ctx['team_add_form'] = form
        ctx['show_team_addform'] = True

    return render(request, 'dashboard/team/team.html', ctx)


@superuser_required
def update_team_member(request, id):
    instance = get_object_or_404(TeamMember, id=id)
    ctx = team_member_base_context()

    if request.method == 'POST':
        form = TeamMemberForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/admin/add-team-member/?section=ourteam')
    else:
        form = TeamMemberForm(instance=instance)

    ctx['team_edit_form'] = form
    ctx['show_team_editform'] = True

    return render(request, 'dashboard/team/team.html', ctx)


@superuser_required
def delete_team_member(request, id):
    member = get_object_or_404(TeamMember, id=id)

    if request.method == 'POST':
        member.delete()

    return redirect('/dashboard/admin/add-team-member/?section=ourteam')


@superuser_required
def team_page(request):
    ctx = team_member_base_context()
    return render(request, 'dashboard/team/team.html', ctx)


@superuser_required
def manage_team_header(request):
    ctx = team_member_base_context()
    team_header = TeamPage.objects.first()

    if request.method == 'POST':
        form = TeamPageForm(
            request.POST,
            request.FILES,
            instance=team_header
        )
        if form.is_valid():
            form.save()
            return redirect('/dashboard/admin/team/?section=teamheader')

        ctx['team_header_form'] = form
        ctx['show_teamheader_form'] = True
    else:
        ctx['show_teamheader_form'] = True

    return render(request, 'dashboard/team/team.html', ctx)
