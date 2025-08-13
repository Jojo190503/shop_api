from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Utilisateur, Categorie, Shop, Article, ShopArticle, Transaction, TransactionArticle

# Enregistrement du modèle Utilisateur avec UserAdmin
admin.site.register(Utilisateur, UserAdmin)

# Enregistrement des autres modèles avec des configurations personnalisées
@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'created_at')
    search_fields = ('name', 'location')

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'category', 'opened_at')
    list_filter = ('category',)
    search_fields = ('name',)

@admin.register(ShopArticle)
class ShopArticleAdmin(admin.ModelAdmin):
    list_display = ('shop', 'article', 'stock', 'date_ajout')
    list_filter = ('shop', 'article')
    search_fields = ('shop__name', 'article__name')

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'shop', 'amount', 'transaction_date')
    list_filter = ('shop', 'transaction_date')
    search_fields = ('client__username', 'shop__name')

@admin.register(TransactionArticle)
class TransactionArticleAdmin(admin.ModelAdmin):
    list_display = ('transaction', 'article', 'quantite', 'prix_unitaire', 'sous_total')
    list_filter = ('transaction', 'article')
    search_fields = ('article__name',)