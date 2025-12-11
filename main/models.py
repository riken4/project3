from django.db import models

# Create your models here.



#************************************
# COMMON MODELS
#************************************
class CommonHeaderModel(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    image=models.ImageField(upload_to='common_header_images/',null=True,blank=True)

    class Meta:
        abstract = True
    
    def __str__ (self):
        return f'{{self.__class__.__name__}} - {{self.title}}'
    
    

#************************************
# Models for Index Page
#************************************
class IndexPage(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    image=models.ImageField(upload_to='index_images/')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class IndexPartner(models.Model):
    title=models.CharField(max_length=200,default="Our Valid Partners")
    description=models.TextField()


class IndexPartnerImages(models.Model):
    image=models.ImageField(upload_to='partner_images/')

    
class IndexHowitWorks(models.Model):
    title=models.CharField(max_length=200,default="How It Works")
    description=models.TextField()
    second_title=models.CharField(max_length=200,blank=True,null=True)
    secondary_description=models.TextField(blank=True,null=True)

class IndexHowitWorksObj(models.Model):
    howitwoeks_title=models.CharField(max_length=200,default="Step 1: Sign Up")
    howitwoeks_description=models.TextField()


class IndexWebStats(models.Model):
    title=models.CharField(max_length=200,default="Our Web Stats")
    description=models.TextField()
    happy_customers=models.IntegerField(default=0)
    total_services=models.IntegerField(default=0)
    reviews=models.FloatField(default=0)
    total_partners=models.IntegerField(default=0)

class IndexTestimonials(models.Model):
    title=models.CharField(max_length=200,default="What Our Customers Say")
    description=models.TextField()

class IndexTestimonialObj(models.Model):
    customer_name=models.CharField(max_length=200)
    customer_position=models.CharField(max_length=200,blank=True,null=True)
    testimonial=models.TextField()
    customer_image=models.ImageField(upload_to='testimonial_images/',blank=True,null=True)

    def __str__(self):
        return self.customer_name
    
class WhatOurCustomersSay(models.Model):
    title=models.CharField(max_length=200,default="What Our Customers Say")
    description=models.TextField(default="Our customers love us! Read what they have to say below.")

class WhatOurCustomersSayObj(models.Model):
    customer_name=models.CharField(max_length=200)
    customer_position=models.CharField(max_length=200,blank=True,null=True)
    testimonial=models.TextField()
    customer_image=models.ImageField(upload_to='customer_say_images/',blank=True,null=True)

    def __str__(self):
        return self.customer_name
    
class OrganizationSettings(models.Model):
    organization_name=models.CharField(max_length=200,default="My Organization")
    contact_email=models.EmailField()
    whatsapp_number=models.CharField(max_length=20,blank=True,null=True)
    facebook_link=models.URLField(blank=True,null=True)
    twitter_link=models.URLField(blank=True,null=True)
    linkedin_link=models.URLField(blank=True,null=True)
    instagram_link=models.URLField(blank=True,null=True)
    address=models.TextField(blank=True,null=True)



#************************************
# Models for Pricing Page
#************************************


class PricingPage(CommonHeaderModel):
    pass

class CommonPricingModel(CommonHeaderModel):
    price=models.FloatField()
    features=models.TextField()

    class Meta:
        abstract = True


class PricingOptionOne(CommonPricingModel):
    pass

class PricingOptionTwo(CommonPricingModel):
    pass

class PricingOptionThree(CommonPricingModel):
    pass
class PricingOptionFour(CommonPricingModel):
    pass

class AddonService(CommonHeaderModel):
    pass

class AddonServiceOption(CommonHeaderModel):
    price=models.FloatField()

class WhyChooseUs(CommonHeaderModel):
    pass

class WhatCustomersSay(CommonHeaderModel):
    address=models.CharField(max_length=20,blank=True,null=True)

#************************************
# Models for Team Page
#************************************

class TeamPage(CommonHeaderModel):
    pass

class TeamMember(CommonHeaderModel):
    position=models.CharField(max_length=200)
    facebook_link=models.URLField(blank=True,null=True)
    twitter_link=models.URLField(blank=True,null=True)
    linkedin_link=models.URLField(blank=True,null=True)
    instagram_link=models.URLField(blank=True,null=True)
    gmail=models.EmailField(blank=True,null=True)
    phone_number =models.CharField(max_length=20,blank=True,null=True)
    location=models.CharField(max_length=200,blank=True,null=True)

#************************************
# Models for Blogs Page
#************************************

class BlogPage(CommonHeaderModel):
    pass

class Blog(CommonHeaderModel):
    created_at=models.DateTimeField(auto_now_add=True)
    author=models.CharField(max_length=200)
    author_image=models.ImageField(upload_to='author_images/',blank=True,null=True)
    author_description=models.TextField(blank=True,null=True)

#************************************
# Models for Blogs Page
#************************************
class AboutUs(CommonHeaderModel):
    core_values_title=models.CharField(max_length=200)
    core_values_description=models.TextField(blank=True,null=True)


#************************************
# Models for FAQ Page
#************************************


class FAQPage(CommonHeaderModel):
    """Header section for FAQ page"""
    pass

class FAQ(models.Model):
    """Individual FAQ items"""
    question = models.CharField(max_length=500)
    answer = models.TextField()
    order = models.IntegerField(default=0, help_text="Display order (lower numbers appear first)")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'
    
    def __str__(self):
        return self.question[:50]
    
#************************************
# Models for Terms and Conditions
#************************************

from django.db import models

class CommonHeaderModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='common_header_images/', null=True, blank=True)

    class Meta:
        abstract = True
    
    def __str__(self):
        return f'{self.__class__.__name__} - {self.title}'


class TermsOfService(CommonHeaderModel):
    last_updated = models.DateField()
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0, help_text="Display order")

    class Meta:
        verbose_name = "Terms of Service"
        verbose_name_plural = "Terms of Service"
        ordering = ['order']

    def __str__(self):
        return f"Terms of Service - {self.title}"


class TermsSection(models.Model):
    terms = models.ForeignKey(TermsOfService, on_delete=models.CASCADE, related_name='sections')
    section_number = models.IntegerField()
    section_title = models.CharField(max_length=200)
    section_id = models.SlugField(max_length=100, help_text="Used for anchor links (e.g., 'acceptance')")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', 'section_number']
        verbose_name = "Terms Section"
        verbose_name_plural = "Terms Sections"

    def __str__(self):
        return f"{self.section_number}. {self.section_title}"


class TermsContent(models.Model):
    CONTENT_TYPE_CHOICES = [
        ('paragraph', 'Paragraph'),
        ('list_item', 'List Item'),
    ]

    section = models.ForeignKey(TermsSection, on_delete=models.CASCADE, related_name='contents')
    content_type = models.CharField(max_length=20, choices=CONTENT_TYPE_CHOICES, default='paragraph')
    text = models.TextField()
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Terms Content"
        verbose_name_plural = "Terms Contents"

    def __str__(self):
        return f"{self.section.section_title} - {self.content_type}"


class TermsContactInfo(models.Model):
    terms = models.OneToOneField(TermsOfService, on_delete=models.CASCADE, related_name='contact_info')
    organization_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    address = models.TextField()

    class Meta:
        verbose_name = "Terms Contact Information"
        verbose_name_plural = "Terms Contact Information"

    def __str__(self):
        return f"Contact Info for {self.terms.title}"
    






    

    
    