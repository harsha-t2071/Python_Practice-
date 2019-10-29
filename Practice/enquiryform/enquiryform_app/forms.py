from django import forms
from multiselectfield import MultiSelectFormField


class EnquiryForm(forms.Form):
    name = forms.CharField(
        label='Enter Your Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Name'
            }
        )
    )

    email = forms.EmailField(
        label='Enter Your Email',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Email'
            }
        )
    )

    mobile = forms.IntegerField(
        label='Enter Your Number',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Number'
            }
        )
    )

    SKILL_CHOICES = (('py', 'PYTHON'),
                     ('dj', 'DJANGO'),
                     ('ra', 'RESTAPI'),
                     ('ui', 'UI')

                     )
    skills = MultiSelectFormField(max_length=100, choices=SKILL_CHOICES, label='Select Your Skill')

    LOCATION_CHOICES = (('hyd', 'Hyderabad'),
                        ('bang', 'Bangalore'),
                        ('che', 'Chennai'),
                        ('pun', 'Pune')

                        )
    location = MultiSelectFormField(max_length=100, choices=LOCATION_CHOICES, label='Select Your Location')

    GENDER_CHOICES = (('M', 'Male'),
                      ('F', 'Female'))
    gender = forms.ChoiceField(
        label="Select Your Gender",
        widget=forms.RadioSelect, choices=GENDER_CHOICES
    )

    y = range(2019, 2026)

    date = forms.DateField(
        label="Select Your Course Date",
        widget=forms.SelectDateWidget(years=y)
    )
