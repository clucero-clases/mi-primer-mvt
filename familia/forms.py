from django import forms

class PersonaForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100)
    apellido = forms.CharField(label="Apellido", max_length=100)
    email = forms.EmailField(label="Email")
    # input_format hace que se pueda ingresar la fecha con el formato latino, dia/mes/año
    fecha_nacimiento = forms.DateField(label="fecha_nacimiento", input_formats=["%d/%m/%Y"],
    #widget es para poder agregar un tip para que el usuario sepa como ingresar la fecha
    widget=forms.TextInput(attrs={'placeholder': '30/12/1995'}))
    altura = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': "1.75 m"}))

class BuscarPersonasForm(forms.Form):
    palabra_a_buscar = forms.CharField(label="Buscar")

class DomicilioForm(forms.Form):
    calle = forms.CharField(label="Calle", max_length=50)
    numero = forms.IntegerField(label="Número")
    ciudad = forms.CharField(label="Ciudad", max_length=50)
    provincia = forms.CharField(label="Provincia", max_length=50)

class LaboralForm(forms.Form):
    actividad = forms.CharField(label="Actividad", max_length=30)
    antiguedad = forms.IntegerField(label="Antigüedad")
    