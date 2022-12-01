from django import forms
class Formularipaciente(forms.Form):

    TipoAfiliado=(
        (1,'Cotizante'),
        (2,'Beneficario')
       
    )
    Regimen=(
        (1,'Contributivo'),
        (2, 'Subsidiado')
    )
    Grupo_ingresos=(
        (1,'A'),
        (2,'B'),
        (3,'C'),
        (4,'D')
    )

    nombrepaciente=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=15
    ) 
    apellidosPaciente=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=35
    )
    cedulaPaciente=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=10
    )
    
    TipoAfiliado=forms.ChoiceField(
        widget=forms.Select(attrs={"class":"form-select mb-3"}),
        required=True,
        choices=TipoAfiliado
    )
    Regimen=forms.ChoiceField(
        widget=forms.Select(attrs={"class":"form-select mb-3"}),
        required=True,
        choices=Regimen
    )
    
    Grupo_ingresos =forms.ChoiceField(
        widget=forms.Select(attrs={"class":"form-select mb-3"}),
        required=True,
        choices=Grupo_ingresos
    ) 