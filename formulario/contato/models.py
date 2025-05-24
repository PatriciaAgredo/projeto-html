from django.db import models

class CadastroFeirante(models.Model):
    TIPO_ARTESANATO_CHOICES = [('ceramica', 'Cerâmica'),
        ('costura', 'costura'),
        ('cozinha', 'Cozinha'),
        ('pintura_tecido', 'Pintura em Tecido'),
        ('pintura', 'Pintura'),
        ('comidas', 'Comidas'),
        ('outro', 'Outro'),]
    nome = models.CharField(max_length=100, verbose_name="Nome")
    sobrenome = models.CharField(max_length=100, verbose_name="Sobrenome")
    idade = models.IntegerField(verbose_name="Idade")
    data_nascimento = models.DateField(verbose_name="Data de Nascimento")
    rua = models.CharField(max_length=200, verbose_name="Rua")
    numero = models.CharField(max_length=10, verbose_name="Número")
    complemento = models.CharField(max_length=100, blank=True, null=True, verbose_name="Complemento")
    bairro = models.CharField(max_length=100, verbose_name="Bairro")
    cidade = models.CharField(max_length=100, verbose_name="Cidade")
    disponibilidade_feira = models.BooleanField(verbose_name="Tem disponibilidade de fazer feiras ao ar livre?")
    tem_loja_fisica = models.BooleanField(verbose_name="Tem loja física?")
    tipo_artesanato = models.CharField(
        max_length=20,
        choices=TIPO_ARTESANATO_CHOICES,
        verbose_name="Tipo de Artesanato"
    )
    objetos_a_vender = models.TextField(verbose_name="Objetos a Vender")

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"

