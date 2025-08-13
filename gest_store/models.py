# models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class Utilisateur(AbstractUser):
    """Modèle utilisateur pour le système de centre commercial"""
    email = models.EmailField(unique=True)
    negociated_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de négociation/inscription")
    
    # Utiliser email comme identifiant principal
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    class Meta:
        db_table = 'utilisateurs'
        verbose_name = 'Utilisateur'
        verbose_name_plural = 'Utilisateurs'
    
    def __str__(self):
        return f"{self.username} ({self.email})"


class Categorie(models.Model):
    """Modèle pour les catégories d'articles"""
    name = models.CharField(max_length=100, verbose_name="Nom de la catégorie")
    description = models.TextField(blank=True, verbose_name="Description")
    
    class Meta:
        db_table = 'categories'
        verbose_name = 'Catégorie'
        verbose_name_plural = 'Catégories'
    
    def __str__(self):
        return self.name


class Shop(models.Model):
    """Modèle pour les magasins du centre commercial"""
    name = models.CharField(max_length=100, verbose_name="Nom du magasin")
    location = models.CharField(max_length=200, verbose_name="Localisation dans le centre")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    
    class Meta:
        db_table = 'shops'
        verbose_name = 'Magasin'
        verbose_name_plural = 'Magasins'
    
    def __str__(self):
        return f"{self.name} - {self.location}"


class Article(models.Model):
    """Modèle pour les articles"""
    name = models.CharField(max_length=100, verbose_name="Nom de l'article")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Prix")
    stock = models.IntegerField(default=0, verbose_name="Stock disponible")
    opened_at = models.DateTimeField(auto_now_add=True, verbose_name="Date d'ouverture/création")
    category = models.ForeignKey(
        Categorie, 
        on_delete=models.CASCADE,  # Un article appartient obligatoirement à une catégorie
        related_name='articles',
        verbose_name="Catégorie"
    )
    
    class Meta:
        db_table = 'articles'
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ['name']
    
    def __str__(self):
        return f"{self.name} - {self.price}€ (Cat: {self.category.name})"


class ShopArticle(models.Model):
    """Table de liaison entre Shop et Article - Un article peut être dans plusieurs magasins"""
    shop = models.ForeignKey(
        Shop, 
        on_delete=models.CASCADE, 
        related_name='shop_articles',
        verbose_name="Magasin"
    )
    article = models.ForeignKey(
        Article, 
        on_delete=models.CASCADE, 
        related_name='shop_articles',
        verbose_name="Article"
    )
    stock = models.IntegerField(default=0, verbose_name="Stock dans ce magasin")
    date_ajout = models.DateTimeField(auto_now_add=True, verbose_name="Date d'ajout dans le magasin")
    
    class Meta:
        db_table = 'shop_articles'
        verbose_name = 'Article en magasin'
        verbose_name_plural = 'Articles en magasin'
        unique_together = ['shop', 'article']  # Un article ne peut être référencé qu'une fois par magasin
    
    def __str__(self):
        return f"{self.shop.name} - {self.article.name} (Stock: {self.stock})"


class Transaction(models.Model):
    """Modèle pour les transactions - Plusieurs transactions par utilisateur, chaque transaction liée à un magasin"""
    client = models.ForeignKey(
        Utilisateur, 
        on_delete=models.CASCADE, 
        related_name='transactions',
        verbose_name="Client"
    )
    shop = models.ForeignKey(
        Shop, 
        on_delete=models.CASCADE, 
        related_name='transactions',
        verbose_name="Magasin"
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Montant total")
    transaction_date = models.DateTimeField(auto_now_add=True, verbose_name="Date de transaction")
    
    # Articles achetés dans cette transaction (Many-to-Many avec quantités)
    articles = models.ManyToManyField(
        Article,
        through='TransactionArticle',
        related_name='transactions'
    )
    
    class Meta:
        db_table = 'transactions'
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'
        ordering = ['-transaction_date']
    
    def __str__(self):
        return f"Transaction #{self.id} - {self.client.username} - {self.amount}€ - {self.shop.name}"


class TransactionArticle(models.Model):
    """Détails des articles dans une transaction (quantité, prix unitaire)"""
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    quantite = models.IntegerField(default=1, verbose_name="Quantité achetée")
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Prix unitaire au moment de l'achat")
    
    class Meta:
        db_table = 'transaction_articles'
        verbose_name = 'Article de transaction'
        verbose_name_plural = 'Articles de transaction'
        unique_together = ['transaction', 'article']
    
    def __str__(self):
        return f"Transaction #{self.transaction.id} - {self.article.name} x{self.quantite}"
    
    @property
    def sous_total(self):
        return self.quantite * self.prix_unitaire
    

    