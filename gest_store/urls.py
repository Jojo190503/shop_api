from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UtilisateurViewSet, CategorieViewSet, ShopViewSet, 
    ArticleViewSet, ShopArticleViewSet, TransactionViewSet, TransactionArticleViewSet
)

router = DefaultRouter()
router.register(r'utilisateurs', UtilisateurViewSet)
router.register(r'categories', CategorieViewSet)
router.register(r'shops', ShopViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'shop-articles', ShopArticleViewSet)
router.register(r'transactions', TransactionViewSet)
router.register(r'transaction-articles', TransactionArticleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UtilisateurViewSet, CategorieViewSet, ShopViewSet, 
    ArticleViewSet, ShopArticleViewSet, TransactionViewSet, 
    TransactionArticleViewSet, RegisterView
)

router = DefaultRouter()
router.register(r'utilisateurs', UtilisateurViewSet)
router.register(r'categories', CategorieViewSet)
router.register(r'shops', ShopViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'shop-articles', ShopArticleViewSet)
router.register(r'transactions', TransactionViewSet)
router.register(r'transaction-articles', TransactionArticleViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
]