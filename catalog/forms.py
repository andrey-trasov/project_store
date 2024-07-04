from django.forms import ModelForm, forms, BooleanField

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = 'form-check-input'
            else:
                fild.widget.attrs['class'] = 'form-control'


class ProductForm(ModelForm):
    forbidden_words = ['казино',
                       'криптовалюта',
                       'крипта',
                       'биржа',
                       'дешево',
                       'бесплатно',
                       'обман',
                       'полиция',
                       'радар']
    class Meta:
        model = Product
        fields = '__all__'    #выводим все поля модели

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')
        for forbidden_word in self.forbidden_words:
            if forbidden_word in cleaned_data.lower():
                raise forms.ValidationError('Присутствует запрещенное слово')

        return cleaned_data

class VersionForm(ModelForm):
    class Meta:
        model = Version
        fields = '__all__'