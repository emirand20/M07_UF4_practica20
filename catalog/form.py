from django.forms import ModelForm
from .models import Producto

class CatalogoForm(ModelForm):
    class Meta:

        model = Producto  
        exclude = ['fecha_creacion']