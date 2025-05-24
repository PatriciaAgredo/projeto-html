from django import forms
from .models import CadastroFeirante

class CadastroFeiranteForm(forms.ModelForm):
    # Campos booleanos para sim/não
    disponibilidade_feira = forms.TypedChoiceField(
        coerce=lambda x: x == 'True',
        choices=[(True, 'Sim'), (False, 'Não')],
        widget=forms.RadioSelect,
        label="Tem disponibilidade de fazer feiras ao ar livre?"
    )
    tem_loja_fisica = forms.TypedChoiceField(
        coerce=lambda x: x == 'True',
        choices=[(True, 'Sim'), (False, 'Não')],
        widget=forms.RadioSelect,
        label="Tem loja física?"
    )

    class Meta:
        model = CadastroFeirante
        fields = '__all__'
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
            'objetos_a_vender': forms.Textarea(attrs={'rows': 4}),
        }
        labels = {
            'nome': 'Nome',
            'sobrenome': 'Sobrenome',
            'idade': 'Idade',
            'rua': 'Rua',
            'numero': 'Número',
            'complemento': 'Complemento',
            'bairro': 'Bairro',
            'cidade': 'Cidade',
            'tipo_artesanato': 'Tipo de Artesanato',
        }