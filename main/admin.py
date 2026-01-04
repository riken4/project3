from django.contrib import admin
from .models import IndexPage, IndexPartner, IndexPartnerImages, IndexHowitWorks, IndexHowitWorksObj, IndexWebStats, IndexTestimonials, IndexTestimonialObj,PricingPage
from .models import OrganizationSettings, WhatOurCustomersSay,WhatOurCustomersSayObj,BlogPage,Blog
from .models import CommonPricingModel,AddonService,AddonServiceOption,WhyChooseUs,WhatCustomersSay, TeamPage, TeamMember,AboutUs, CoreValues
from .models import FAQPage, FAQ
from .models import SubscriptionPlan, UserSubscription
# Register your models here.
admin.site.register(IndexPage)
admin.site.register(IndexPartner)
admin.site.register(IndexPartnerImages)
admin.site.register(IndexHowitWorks)
admin.site.register(IndexHowitWorksObj)
admin.site.register(IndexWebStats)
admin.site.register(IndexTestimonials)
admin.site.register(IndexTestimonialObj)
admin.site.register(OrganizationSettings)
admin.site.register(WhatOurCustomersSay)
admin.site.register(WhatOurCustomersSayObj)

admin.site.register(CommonPricingModel)
admin.site.register(PricingPage)

admin.site.register(AddonService)
admin.site.register(AddonServiceOption)
admin.site.register(WhyChooseUs)
admin.site.register(WhatCustomersSay)

admin.site.register(TeamPage)
admin.site.register(TeamMember)

admin.site.register(BlogPage)

admin.site.register(Blog)
admin.site.register(AboutUs)
admin.site.register(CoreValues)


admin.site.register(FAQPage)
admin.site.register(FAQ)

admin.site.register(UserSubscription)
admin.site.register(SubscriptionPlan)



from django.contrib import admin
from .models import TermsOfService, TermsSection, TermsContent, TermsContactInfo


class TermsContentInline(admin.TabularInline):
    model = TermsContent
    extra = 1
    fields = ['content_type', 'text', 'order']


class TermsSectionInline(admin.StackedInline):
    model = TermsSection
    extra = 0
    fields = ['section_number', 'section_title', 'section_id', 'order']
    show_change_link = True


class TermsContactInfoInline(admin.StackedInline):
    model = TermsContactInfo
    extra = 0
    max_num = 1
    fields = ['organization_name', 'email', 'phone', 'address']


@admin.register(TermsOfService)
class TermsOfServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'last_updated', 'is_active', 'order']
    list_filter = ['is_active', 'last_updated']
    search_fields = ['title', 'description']
    inlines = [TermsContactInfoInline, TermsSectionInline]
    fieldsets = (
        ('Header Information', {
            'fields': ('title', 'description', 'image')
        }),
        ('Settings', {
            'fields': ('last_updated', 'is_active', 'order')
        }),
    )


@admin.register(TermsSection)
class TermsSectionAdmin(admin.ModelAdmin):
    list_display = ['section_number', 'section_title', 'terms', 'order']
    list_filter = ['terms']
    search_fields = ['section_title']
    inlines = [TermsContentInline]
    fieldsets = (
        (None, {
            'fields': ('terms', 'section_number', 'section_title', 'section_id', 'order')
        }),
    )


@admin.register(TermsContent)
class TermsContentAdmin(admin.ModelAdmin):
    list_display = ['section', 'content_type', 'text_preview', 'order']
    list_filter = ['content_type', 'section']
    search_fields = ['text']
    
    def text_preview(self, obj):
        return obj.text[:50] + '...' if len(obj.text) > 50 else obj.text
    text_preview.short_description = 'Content Preview'


@admin.register(TermsContactInfo)
class TermsContactInfoAdmin(admin.ModelAdmin):
    list_display = ['organization_name', 'email', 'phone']
    search_fields = ['organization_name', 'email']






