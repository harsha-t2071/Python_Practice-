from django import forms


class Empform(forms.Form):
    name = forms.CharField(
        label="Enter your Name :",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Name'
            }
        )
    )

    salary = forms.IntegerField(
        label="Enter Your Salary :",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Salary'
            }
        )
    )

    email = forms.EmailField(
        label="Enter your Email :",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Email'
            }
        )
    )

    location = forms.CharField(
        label="Enter your Location :",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Location'
            }
        )
    )