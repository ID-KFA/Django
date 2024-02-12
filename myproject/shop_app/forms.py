from django import forms


class NewProduct(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.DecimalField(max_digits=8, decimal_places=2)
    amount = forms.IntegerField()
    product_image = forms.ImageField()

    def save(self):
        cleaned_data = self.cleaned_data

class ImageForm(forms.Form):
    image = forms.ImageField()
