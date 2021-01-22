from django import forms


class ContactForm(forms.Form):
    #name = forms.CharField()
    fullname = forms.CharField(widget = forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Name", 'name': 'fullname'
                }))
    email = forms.EmailField(required=True,
                widget = forms.EmailInput(attrs={
                'class': 'form-control', 'placeholder': "Your Email", 'name': 'Email'
                }))
    message = forms.CharField(widget=forms.Textarea(attrs=
        {'class': 'form-control'}))

    # def clean_email(self):
    #     """
    #     To only allow emails from gmail
    #     """
    #     email = self.cleaned_data.get("email")
    #     if not "gmail.com" in email:
    #         raise forms.ValidationError("Email has to be gmail.com")
    #     return email
