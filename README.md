# 💊 Pharmacy - Système de Gestion de Pharmacie

**Système complet de gestion de pharmacie - Développé par Hiba Bourzgui , benchahid basma , hammouda imane**

_Votre solution intelligente pour la gestion pharmaceutique_ 💊🏥

## 📋 Table des Matières
- [🌟 Aperçu du Projet](#-aperçu-du-projet)
- [🎯 Fonctionnalités Avancées](#-fonctionnalités-avancées)
- [🏗️ Architecture Technique](#️-architecture-technique)
- [💻 Stack Technologique](#-stack-technologique)
- [🚀 Guide d'Installation](#-guide-dinstallation)
- [📊 Structure des Données](#-structure-des-données)
- [🔐 Système de Sécurité](#-système-de-sécurité)
- [📱 Interface Utilisateur](#-interface-utilisateur)
- [🔄 Workflows Métier](#-workflows-métier)
- [🧪 Tests & Qualité](#-tests--qualité)
- [📈 Performance](#-performance)
- [🌐 Déploiement](#-déploiement)
- [🤝 Contribution](#-contribution)
- [📄 Licence & Contact](#-licence--contact)

## 🌟 Aperçu du Projet

**Pharmacy** est une solution complète et professionnelle de gestion de pharmacie, conçue et développée par ** Bourzgui,benchahid basma , hammouda imane**. Cette application web moderne offre une plateforme intuitive pour la gestion des médicaments, des stocks, des ventes et des utilisateurs.

### ✨ Points Forts
- ✅ **Interface utilisateur moderne et responsive**
- ✅ **Gestion complète des médicaments et stocks**
- ✅ **Système de vente intégré**
- ✅ **Tableau de bord analytique en temps réel**
- ✅ **Gestion multi-utilisateurs**
- ✅ **Export de rapports et données**

## 🎯 Fonctionnalités Avancées

### 👥 Module Utilisateur
| Fonctionnalité | Description | Statut |
|---|---|---|
| **Inscription Intelligente** | Validation en temps réel, vérification d'email | ✅ |
| **Gestion de Profil** | Historique complet, documents numérisés | ✅ |
| **Tableau de Bord** | KPI en temps réel, graphiques interactifs | ✅ |
| **Notifications** | Rappels, confirmations, alertes | ✅ |

### 💊 Module Médicaments
| Fonctionnalité | Description | Statut |
|---|---|---|
| **Catalogue Dynamique** | Filtres avancés, recherche en temps réel | ✅ |
| **Gestion Stock** | Suivi en temps réel, alertes de rupture | ✅ |
| **Import/Export CSV** | Importation massive, export de données | ✅ |
| **Historique Mouvements** | Traçabilité complète des entrées/sorties | ✅ |

### 📊 Module Ventes
| Fonctionnalité | Description | Statut |
|---|---|---|
| **Enregistrement Ventes** | Processus optimisé, interface intuitive | ✅ |
| **Calcul Automatique** | TVA, remises, prix, stocks | ✅ |
| **Facturation** | Génération PDF, historique des factures | ✅ |
| **Rapports Analytiques** | Statistiques détaillées, export Excel | ✅ |

### 📊 Tableau de Bord Analytique
```javascript
// Exemple de métriques suivies
const analyticsMetrics = {
  revenue: {
    daily: 25000,
    monthly: 750000,
    yearly: 9000000,
    growth: "+12.5%"
  },
  products: {
    total: 350,
    lowStock: 12,
    expiring: 8
  },
  sales: {
    today: 145,
    monthly: 3240,
    averageCart: 520
  },
  customers: {
    active: 278,
    newThisMonth: 45,
    retentionRate: "82%"
  }
};
┌─────────────────────────────────────────────────────────────┐
│                     COUCHE PRÉSENTATION                      │
├─────────────────────────────────────────────────────────────┤
│  HTML5 │ CSS3 │ Bootstrap 5 │ JavaScript │ Responsive       │
└─────────────────────────────────────────────────────────────┘
                                  │
┌─────────────────────────────────────────────────────────────┐
│                    COUCHE LOGIQUE MÉTIER                     │
├─────────────────────────────────────────────────────────────┤
│  Django │ Python │ Modèles MVC │ Gestion des vues           │
└─────────────────────────────────────────────────────────────┘
                                  │
┌─────────────────────────────────────────────────────────────┐
│                    COUCHE PERSISTANCE                        │
├─────────────────────────────────────────────────────────────┤
│        SQLite │ Django ORM │ JSON / CSV Export             │
└─────────────────────────────────────────────────────────────┘

# Navigateurs supportés
- Chrome 90+ (Recommandé)
- Firefox 88+
- Safari 14+
- Edge 90+

# Configuration minimale
- RAM: 2 GB
- Stockage: 100 MB
- Python 3.8+
- Django 3.2+

# 1. Cloner le dépôt
git clone https://github.com/BOURZGUI/pharmacy.git
cd pharmacy

# 2. Créer un environnement virtuel
python -m venv venv

# 3. Activer l'environnement virtuel
# Sur Windows:
venv\Scripts\activate
# Sur macOS/Linux:
source venv/bin/activate

# 4. Installer les dépendances
pip install -r requirements.txt

# 5. Appliquer les migrations
python manage.py makemigrations
python manage.py migrate

# 6. Créer un superutilisateur
python manage.py createsuperuser

# 7. Charger les données initiales
python manage.py loaddata medicaments.json

# 8. Lancer le serveur de développement
python manage.py runserver

# 9. Accéder à l'application
# Ouvrir http://localhost:8000 dans votre navigateur

# settings.py - Configuration principale
DJANGO_SETTINGS = {
    'DEBUG': True,
    'ALLOWED_HOSTS': ['localhost', '127.0.0.1'],
    'INSTALLED_APPS': [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'pharmacie',  # Application principale
        'users',      # Gestion des utilisateurs
        'stock',      # Gestion des stocks
        'ventes',     # Gestion des ventes
        'dashboard',  # Tableau de bord
    ],
    'LANGUAGE_CODE': 'fr-fr',
    'TIME_ZONE': 'UTC',
    'STATIC_URL': '/static/',
    'MEDIA_URL': '/media/',
    'MEDIA_ROOT': os.path.join(BASE_DIR, 'media'),
}

# Fichier de configuration
REQUIREMENTS = {
    'django': '3.2.25',
    'pillow': '9.5.0',
    'reportlab': '4.0.4',
    'openpyxl': '3.1.2'
}


{
  "admin": {
    "username": "admin",
    "email": "admin@pharmacy.com",
    "password": "Admin123!",
    "role": "ADMIN"
  },
  "pharmacien": {
    "username": "pharmacien",
    "email": "pharmacien@pharmacy.com",
    "password": "Pharmacien123!",
    "role": "PHARMACIEN"
  },
  "assistant": {
    "username": "assistant",
    "email": "assistant@pharmacy.com",
    "password": "Assistant123!",
    "role": "ASSISTANT"
  }
}

# models.py - Modèles Django
class Medicament(models.Model):
    code = models.CharField(max_length=50, unique=True)
    nom = models.CharField(max_length=200)
    description = models.TextField()
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True)
    prix_achat = models.DecimalField(max_digits=10, decimal_places=2)
    prix_vente = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    stock_min = models.IntegerField(default=5)
    date_peremption = models.DateField()
    fournisseur = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.code} - {self.nom}"

    def en_rupture(self):
        return self.stock <= 0

    def stock_critique(self):
        return 0 < self.stock <= self.stock_min

class Vente(models.Model):
    reference = models.CharField(max_length=20, unique=True)
    medicament = models.ForeignKey(Medicament, on_delete=models.PROTECT)
    quantite = models.IntegerField()
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    date_vente = models.DateTimeField(auto_now_add=True)
    client = models.CharField(max_length=200, blank=True)
    utilisateur = models.ForeignKey(User, on_delete=models.PROTECT)

class MouvementStock(models.Model):
    TYPES = (
        ('ENTREE', 'Entrée'),
        ('SORTIE', 'Sortie'),
        ('AJUSTEMENT', 'Ajustement'),
    )
    medicament = models.ForeignKey(Medicament, on_delete=models.PROTECT)
    type = models.CharField(max_length=20, choices=TYPES)
    quantite = models.IntegerField()
    date_mouvement = models.DateTimeField(auto_now_add=True)
    note = models.TextField(blank=True)
    utilisateur = models.ForeignKey(User, on_delete=models.PROTECT)

┌─────────────┐      ┌─────────────┐      ┌─────────────┐
│   CATÉGORIES│◄────┤ MÉDICAMENTS │◄────┤    VENTES   │
└─────────────┘      └─────────────┘      └─────────────┘
      │                     │                     │
      │ 1:N                 │ 1:N                 │ N:1
      ▼                     ▼                     ▼
┌─────────────┐      ┌─────────────┐      ┌─────────────┐
│  FOURNISSEURS│◄────┤    STOCK    │◄────┤  UTILISATEURS│
└─────────────┘      └─────────────┘      └─────────────┘


# security.py - Gestion de sécurité
class SecurityManager:
    def __init__(self):
        self.session_timeout = 3600  # 1 heure

    def hash_password(self, password):
        return make_password(password)

    def verify_password(self, password, hashed):
        return check_password(password, hashed)

    def create_session(self, user):
        session = {
            'user_id': user.id,
            'username': user.username,
            'role': user.role,
            'created_at': datetime.now().isoformat(),
            'expires_at': (datetime.now() + timedelta(hours=1)).isoformat()
        }
        return session

    def has_permission(self, user, permission):
        permissions = {
            'ADMIN': ['ALL'],
            'PHARMACIEN': ['VIEW_MEDICAMENTS', 'MANAGE_STOCK', 'CREATE_VENTES'],
            'ASSISTANT': ['VIEW_MEDICAMENTS', 'VIEW_STOCK']
        }
        return permission in permissions.get(user.role, []) or 'ALL' in permissions.get(user.role, [])

# Validation des données
class DataValidator:
    @staticmethod
    def validate_medicament(data):
        errors = []
        if not data.get('nom'):
            errors.append("Le nom du médicament est obligatoire")
        if not data.get('code'):
            errors.append("Le code du médicament est obligatoire")
        if data.get('prix_vente', 0) <= 0:
            errors.append("Le prix de vente doit être supérieur à 0")
        if data.get('stock', 0) < 0:
            errors.append("Le stock ne peut pas être négatif")
        return {
            'is_valid': len(errors) == 0,
            'errors': errors
        }

/* Variables CSS - Design System */
:root {
  /* Couleurs principales */
  --primary-color: #2E86C1;
  --secondary-color: #27AE60;
  --accent-color: #F39C12;
  --danger-color: #E74C3C;
  --success-color: #2ECC71;
  --info-color: #3498DB;
  --warning-color: #F39C12;

  /* Typographie */
  --font-primary: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;

  /* Espacements */
  --spacing-xs: 0.25rem;
  --spacing-sm: 0.5rem;
  --spacing-md: 1rem;
  --spacing-lg: 1.5rem;
  --spacing-xl: 2rem;

  /* Ombres */
  --shadow-sm: 0 2px 4px rgba(0,0,0,0.1);
  --shadow-md: 0 4px 8px rgba(0,0,0,0.15);
  --shadow-lg: 0 8px 16px rgba(0,0,0,0.2);

  /* Bordures */
  --border-radius: 8px;
  --border-radius-lg: 12px;
}

graph TD
    A[Client arrive] --> B[Recherche médicament]
    B --> C{Vérification stock}
    C -->|Disponible| D[Validation prescription]
    C -->|Non disponible| E[Proposition alternative]
    D --> F[Enregistrement vente]
    F --> G[Mise à jour stock automatique]
    G --> H[Génération facture]
    H --> I[Paiement]
    I --> J[Confirmation client]
    J --> K[Vente finalisée]
<img width="1751" height="3699" alt="deepseek_mermaid_20260620_0cc605" src="https://github.com/user-attachments/assets/f3ebfcb4-ede4-4477-bbfb-45f69db918d2" />


class StockManager:
    def update_stock(self, medicament_id, quantite, type_mouvement):
        medicament = Medicament.objects.get(id=medicament_id)
        ancien_stock = medicament.stock
        if type_mouvement == 'ENTREE':
            medicament.stock += quantite
        elif type_mouvement == 'SORTIE':
            if medicament.stock < quantite:
                raise ValueError("Stock insuffisant")
            medicament.stock -= quantite
        elif type_mouvement == 'AJUSTEMENT':
            medicament.stock = quantite
        medicament.save()

        # Enregistrement du mouvement
        MouvementStock.objects.create(
            medicament=medicament,
            type=type_mouvement,
            quantite=quantite,
            ancien_stock=ancien_stock,
            nouveau_stock=medicament.stock
        )

    def detect_stock_critique(self):
        medicaments_critiques = Medicament.objects.filter(
            stock__lte=models.F('stock_min')
        )
        if medicaments_critiques.exists():
            # Envoyer alerte
            self.send_alert(medicaments_critiques)

# tests.py - Tests automatisés
from django.test import TestCase

class MedicamentModelTest(TestCase):
    def test_creation_medicament(self):
        medicament = Medicament.objects.create(
            code="MED001",
            nom="Paracétamol",
            prix_vente=5.50,
            stock=100
        )
        self.assertEqual(medicament.code, "MED001")
        self.assertEqual(medicament.nom, "Paracétamol")
        self.assertEqual(medicament.stock, 100)

    def test_stock_critique(self):
        medicament = Medicament.objects.create(
            code="MED002",
            nom="Ibuprofène",
            prix_vente=8.00,
            stock=3,
            stock_min=5
        )
        self.assertTrue(medicament.stock_critique())

class VenteModelTest(TestCase):
    def test_creation_vente(self):
        medicament = Medicament.objects.create(
            code="MED003",
            nom="Amoxicilline",
            prix_vente=12.00,
            stock=50
        )
        vente = Vente.objects.create(
            medicament=medicament,
            quantite=5,
            prix_unitaire=12.00,
            total=60.00
        )
        self.assertEqual(vente.total, 60.00)
        self.assertEqual(medicament.stock, 45)  # Stock mis à jour
# tests.py - Tests automatisés
from django.test import TestCase

class MedicamentModelTest(TestCase):
    def test_creation_medicament(self):
        medicament = Medicament.objects.create(
            code="MED001",
            nom="Paracétamol",
            prix_vente=5.50,
            stock=100
        )
        self.assertEqual(medicament.code, "MED001")
        self.assertEqual(medicament.nom, "Paracétamol")
        self.assertEqual(medicament.stock, 100)

    def test_stock_critique(self):
        medicament = Medicament.objects.create(
            code="MED002",
            nom="Ibuprofène",
            prix_vente=8.00,
            stock=3,
            stock_min=5
        )
        self.assertTrue(medicament.stock_critique())

class VenteModelTest(TestCase):
    def test_creation_vente(self):
        medicament = Medicament.objects.create(
            code="MED003",
            nom="Amoxicilline",
            prix_vente=12.00,
            stock=50
        )
        vente = Vente.objects.create(
            medicament=medicament,
            quantite=5,
            prix_unitaire=12.00,
            total=60.00
        )
        self.assertEqual(vente.total, 60.00)
        self.assertEqual(medicament.stock, 45)  # Stock mis à jour
class PerformanceOptimizer:
    def __init__(self):
        self.cache = {}
        self.query_timeout = 5

    # Cache des requêtes fréquentes
    @cache_page(60 * 15)  # 15 minutes
    def get_medicaments_populaires(self):
        return Medicament.objects.annotate(
            total_ventes=Sum('vente__quantite')
        ).order_by('-total_ventes')[:10]

    # Optimisation des requêtes
    def get_medicaments_avec_stock(self):
        return Medicament.objects.select_related('categorie').prefetch_related('mouvementstock_set')

    # Pagination des listes
    def paginate_medicaments(self, page=1, per_page=20):
        medicaments = Medicament.objects.all().order_by('nom')
        paginator = Paginator(medicaments, per_page)
        return paginator.get_page(page)

class PerformanceOptimizer:
    def __init__(self):
        self.cache = {}
        self.query_timeout = 5

    # Cache des requêtes fréquentes
    @cache_page(60 * 15)  # 15 minutes
    def get_medicaments_populaires(self):
        return Medicament.objects.annotate(
            total_ventes=Sum('vente__quantite')
        ).order_by('-total_ventes')[:10]

    # Optimisation des requêtes
    def get_medicaments_avec_stock(self):
        return Medicament.objects.select_related('categorie').prefetch_related('mouvementstock_set')

    # Pagination des listes
    def paginate_medicaments(self, page=1, per_page=20):
        medicaments = Medicament.objects.all().order_by('nom')
        paginator = Paginator(medicaments, per_page)
        return paginator.get_page(page)

# settings_production.py
import os
import dj_database_url

DEBUG = False
ALLOWED_HOSTS = ['pharmacy.com', 'www.pharmacy.com']

# Base de données PostgreSQL
DATABASES = {
    'default': dj_database_url.config(
        default='postgresql://user:password@localhost/pharmacy'
    )
}

# Fichiers statiques
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Caching
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

# Sécurité
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Guide de Contribution pour Pharmacy

## 1. Workflow Git
- Branche `main` : Production
- Branche `develop` : Développement
- Branches `feature/*` : Nouvelles fonctionnalités
- Branches `hotfix/*` : Corrections urgentes

## 2. Convention de commits
<type>(<scope>): <description>

Types:
- feat: Nouvelle fonctionnalité
- fix: Correction de bug
- docs: Documentation
- style: Formatage
- refactor: Refactoring
- test: Tests

Exemple: feat(ventes): ajout de l'export PDF des factures

## 3. Revue de code
- Toutes les PR doivent être revues par au moins un développeur
- Les tests doivent passer avant le merge
- Respect des conventions PEP 8
- Documentation mise à jour

MIT License

Copyright (c) 2026  Bourzgui , Benchahid basma , Hammouda imane 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
const team_emotion = {
    name: "Pharmacy Team",
    members: [" ", "Basma ", "Imane "],
    mission: "Améliorer les soins de santé grâce à la technologie",
    values: ["Innovation", "Qualité", "Empathie", "Excellence"],
    emotion: ",
    status: "Passionnément engagées"
};

console.log(" Pharmacy - Là où la technologie rencontre la santé avec passion!");
console.log(" Codé avec  par Hiba, Basma & Imane");
console.log(" Ensemble pour un meilleur avenir pharmaceutique!");

