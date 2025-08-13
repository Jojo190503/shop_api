from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import UtilisateurSerializer
from rest_framework import generics
from .models import Utilisateur, Categorie, Shop, Article, ShopArticle, Transaction, TransactionArticle
from .serializers import (
    UtilisateurSerializer, CategorieSerializer, ShopSerializer, 
    ArticleSerializer, ShopArticleSerializer, TransactionSerializer, TransactionArticleSerializer
)

class RegisterView(generics.CreateAPIView):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer
    permission_classes = [AllowAny]  # Tout le monde peut s'inscrire

    def perform_create(self, serializer):
        serializer.save()

class UtilisateurViewSet(viewsets.ModelViewSet):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer
    permission_classes = [permissions.IsAdminUser]  # Seuls les admins peuvent gérer les utilisateurs

class CategorieViewSet(viewsets.ModelViewSet):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Lecture publique, écriture authentifiée

class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ShopArticleViewSet(viewsets.ModelViewSet):
    queryset = ShopArticle.objects.all()
    serializer_class = ShopArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Associer l'utilisateur connecté comme client si non spécifié
        serializer.save(client=self.request.user)

    @action(detail=True, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def articles(self, request, pk=None):
        # Récupérer les articles d'une transaction spécifique
        transaction = self.get_object()
        transaction_articles = TransactionArticle.objects.filter(transaction=transaction)
        serializer = TransactionArticleSerializer(transaction_articles, many=True)
        return Response(serializer.data)

class TransactionArticleViewSet(viewsets.ModelViewSet):
    queryset = TransactionArticle.objects.all()
    serializer_class = TransactionArticleSerializer
    permission_classes = [permissions.IsAuthenticated]