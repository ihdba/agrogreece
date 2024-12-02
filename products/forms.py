from django import forms 


from .models import Producer, Product


class ProducerForm(forms.ModelForm):

    class Meta:
        model = Producer
        fields = '__all__'




class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'



class SearchForm(forms.Form):
    query = forms.CharField()