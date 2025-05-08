from django import forms
from .models import Book

class BookCreationForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'isbn', 'pages']
        widgets = {
            'published_date' : forms.DateInput(attrs={'type':'date', 'class':'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(BookCreationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = f'Enter {field.label}'
    
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if Book.objects.filter(title=title).exists():
            raise forms.ValidationError("A book with this title already exists.")
        return title

class UserFeedbackForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email Address')
    age = forms.IntegerField(label='Age', min_value=18, max_value=100)
    message = forms.CharField(label='Message', widget=forms.Textarea)

    #email custom validation to only accept @gmail.com emails only
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@gmail.com'):
            raise forms.ValidationError('Email must be from the domain @gmail.com')
        return email
    
    #multiple form fields validation (age & message fields)
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        if email:
            domain = email.split('@')[-1]
            if domain != 'gmail.com':
                #raise forms.ValidationError('Email must be an @gmail.com address.')
                self.add_error('email', 'Email must be an @gmail.com address.')

        message = cleaned_data.get('message')
        if message and len(message)<10: #check if message is entered, and if its length is >10
            #raise forms.ValidationError('Message must be at least 10 characters!')
            self.add_error('message', 'Message must be at least 10 characters')
        
        age = cleaned_data.get('age')
        if age is not None and (age<18 or age>100): #chacks if age is entered, and if its in the range 18-100
            #raise forms.ValidationError('Age must be in the range 18 - 100 only')
            self.add_error('age', 'Age must be in the range 18-100')
        
        return cleaned_data