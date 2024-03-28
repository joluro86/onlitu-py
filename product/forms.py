from django import forms
from .models import Producto, ProductGender, Gender

class ProductoForm(forms.ModelForm):
    gender = forms.ModelMultipleChoiceField(
        queryset=Gender.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Producto
        fields = ['name', 'description', 'price', 'category', 'gender', 'imagen']

    def __init__(self, *args, **kwargs):
        if kwargs.get('instance'):
            initial = kwargs.setdefault('initial', {})
            initial['gender'] = [g.gender_id for g in kwargs['instance'].productgender_set.all()]
        forms.ModelForm.__init__(self, *args, **kwargs)

    def save(self, commit=True):
        instance = forms.ModelForm.save(self, commit)
        if commit:
            instance.productgender_set.all().delete()
            genders = self.cleaned_data['gender']
            for gender in genders:
                ProductGender.objects.create(product=instance, gender=gender)
        return instance

