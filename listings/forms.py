from django import forms

from listings.models import Listing
from realtors.models import Realtor
class NewListingForm(forms.ModelForm):


    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control form-group',
        }
    ))
    address = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control form-group',
        }
    ))
    city = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control form-group',
        }
    ))
    state = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control form-group',

        }
    ))
    zipcode = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control form-group',
        }
    ))
    description = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control form-group',
            'rows': 4,
        }
    ))
    price = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control form-group',
        }
    ))
    bedrooms = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control form-group',
        }
    ))
    bathrooms = forms.DecimalField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control form-group',

        }
    ))
    garage = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control form-group',
        }
    ))
    sqft = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control form-group',
        }
    ))
    lot_size = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control form-group',
        }
    ))
    # photo_main = forms.ImageField(widget=forms.ClearableFileInput(
    #     attrs={
    #         'class': 'form-control form-group',

    #     }
    # ))
    # photo_1 = forms.ImageField(widget=forms.ClearableFileInput(
    #     attrs={
    #         'class': 'form-control form-group',

    #     }
    # ))
    # photo_2 = forms.ImageField(widget=forms.ClearableFileInput(
    #     attrs={
    #         'class': 'form-control form-group',

    #     }
    # ))
    # photo_3 = forms.ImageField(widget=forms.ClearableFileInput(
    #     attrs={
    #         'class': 'form-control form-group',

    #     }
    # ))
    # photo_4 = forms.ImageField(widget=forms.ClearableFileInput(
    #     attrs={
    #         'class': 'form-control form-group',

    #     }
    # ))
    # photo_5 = forms.ImageField(widget=forms.ClearableFileInput(
    #     attrs={
    #         'class': 'form-control form-group',

    #     }
    # ))
    # photo_6 = forms.ImageField(widget=forms.ClearableFileInput(
    #     attrs={
    #         'class': 'form-control form-group',

    #     }
    # ))
    class Meta:
        model = Listing
        fields = ('realtor','title','address','city','state','zipcode','description','price','bedrooms','bathrooms','garage','sqft',
        'lot_size','photo_main','photo_1','photo_2','photo_3','photo_4','photo_5','photo_6')

        # widget = {
                
                # 'title': forms.TextInput(attrs={'class':'form-control form-group', 'placeholder':'Input title'}),
                # 'address': forms.TextInput(attrs={'class':'form-control form-group'}),
                # 'city': forms.TypedMultipleChoiceField(attrs={'class':'form-control form-group'}),
                # 'state':
                # 'zipcode':
                # 'description':
                # 'price':
                # 'bedrooms':
                # 'bathrooms':
                # 'garage':
                # 'sqft':
                # 'lot_size':
                # 'photo_main':
                # 'photo_1':
                # 'photo_2':
                # 'photo_3':
                # 'photo_4':
                # 'photo_5':
                # 'photo_6':

        # }