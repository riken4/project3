from django import forms
from main.models import CommonPricingModel, AddonServiceOption, WhyChooseUs, WhatCustomersSay, AboutUs, CoreValues, \
    TeamMember, TeamPage
from django.core.exceptions import ValidationError

class PackagePlanForm(forms.ModelForm):
    class Meta:
        model = CommonPricingModel
        fields = [
            'title',
            'description',
            'image',
            'price',
            'features',
            'submit_text',
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter package title'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Enter package description',
                'rows': 3
            }),
            'price': forms.NumberInput(attrs={
                'placeholder': 'Enter price'
            }),
            'features': forms.Textarea(attrs={
                'placeholder': 'Enter package features',
                'rows': 4
            }),
            'submit_text': forms.TextInput(attrs={
                'placeholder': 'Button text (e.g. Buy Now)'
            }),
        }

class AddonServiceOptionForm(forms.ModelForm):
    description = forms.CharField(
        required=False,  # makes it optional
        widget=forms.Textarea(attrs={
            'placeholder': 'Enter addon description',
            'rows': 3
        })
    )
    class Meta:
        model = AddonServiceOption
        fields = ['title', 'description', 'image', 'price']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter addon title'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
            'price': forms.NumberInput(attrs={
                'placeholder': 'Enter price',
                'step': '0.01'
            }),
        }

class WhyChooseUsForm(forms.ModelForm):
    description = forms.CharField(
        required=False,  # optional description
        widget=forms.Textarea(attrs={
            'placeholder': 'Enter description',
            'rows': 3
        })
    )

    class Meta:
        model = WhyChooseUs
        fields = ['title', 'description', 'image']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter title'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }

class WhatCustomersSayForm(forms.ModelForm):
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'placeholder': 'Customer feedback',
            'rows': 3
        })
    )

    class Meta:
        model = WhatCustomersSay
        fields = ['title', 'description', 'image', 'address']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Customer Name'
            }),
            'address': forms.TextInput(attrs={
                'placeholder': 'City / Country'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }

class AboutUsForm(forms.ModelForm):
    class Meta:
        model = AboutUs
        fields = ['title', 'description', 'image', 'display_in_banner']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'class': 'form-input', 'rows': 4}),
            'display_in_banner': forms.CheckboxInput(attrs={'class': 'form-checkbox'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].required = True
        self.fields['display_in_banner'].label = "Show in Hero Banner / Top Section"

    def clean(self):
        cleaned_data = super().clean()
        display_in_banner = cleaned_data.get('display_in_banner')

        # Query all existing AboutUs objects excluding current instance if editing
        qs = AboutUs.objects.all()
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)

        total_existing = qs.count()
        hero_exists = qs.filter(display_in_banner=True).exists()
        normal_exists = qs.filter(display_in_banner=False).exists()

        # Case 1: Creating new object
        if not self.instance.pk:
            if display_in_banner:
                if hero_exists:
                    raise ValidationError("There is already a hero About Us. Only one allowed. Please edit the existing ones or delete and then create.")
            else:
                if normal_exists:
                    raise ValidationError("There is already a normal About Us. Only one allowed. Please edit the existing ones or delete and then create.")

        # Case 2: Updating existing object
        else:
            if display_in_banner:
                if hero_exists:
                    raise ValidationError("Another About Us is already marked as hero. Only one hero About Us Allowed")
            else:
                if normal_exists:
                    raise ValidationError("Another About Us is already marked as normal. Only one normal About Us Allowed")

        return cleaned_data


class CoreValuesForm(forms.ModelForm):
    class Meta:
        model = CoreValues
        fields = [
            'core_values_title',
            'core_values_description',
            
        ]


class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = [
            'title',
            'position',
            'description',
            'image',
            'facebook_link',
            'twitter_link',
            'linkedin_link',
            'instagram_link',
            'gmail',
            'phone_number',
            'location',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Full Name'}),
            'position': forms.TextInput(attrs={'placeholder': 'Job Position'}),
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Short bio'}),
            'facebook_link': forms.URLInput(attrs={'placeholder': 'Facebook URL'}),
            'twitter_link': forms.URLInput(attrs={'placeholder': 'Twitter URL'}),
            'linkedin_link': forms.URLInput(attrs={'placeholder': 'LinkedIn URL'}),
            'instagram_link': forms.URLInput(attrs={'placeholder': 'Instagram URL'}),
            'gmail': forms.EmailInput(attrs={'placeholder': 'Email Address'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
            'location': forms.TextInput(attrs={'placeholder': 'Location'}),
        }


class TeamPageForm(forms.ModelForm):
    class Meta:
        model = TeamPage
        fields = ['title', 'description', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Our Team'}),
            'description': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Short description for team section'
            }),
        }

    def clean(self):
        """
        Allow ONLY ONE TeamPage object
        """
        cleaned_data = super().clean()

        if not self.instance.pk and TeamPage.objects.exists():
            raise forms.ValidationError(
                "Only one Team Header is allowed."
            )

        return cleaned_data
