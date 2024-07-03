from django.forms import ModelForm, forms

from catalog.models import Product


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