## Projet PythonAnywhere

Ce projet a été fait par **DAGNOL Loic** et **GONS SAIB Fatimah**.

### Que propose le site PythonAnywhere.com ?

Le site PythonAnywhere.com est un environnement de développement intégré en ligne ainsi qu’un service d’hébergement web basé sur le langage python. Il fournit des interfaces de ligne de commande en Python et en Bash.

#####  Qu'est ce que FLASK ? Quels sites connus utilisent Flask ?

Flask framework open source python et l’un des plus populaires. Il n'exige pas de dépendances, c’est au développeur de choisir les outils et librairies qu’il veut utiliser. Beaucoup d’extensions sont fournies par la communauté. Flask possède plusieurs fonctionnalités :

-   Contient un serveur de développement et un debugger
-   Supporte les tests unitaires
-   Utilise le moteur de template Jinja2 (un moteur de template est un outil de modèle structurel qui simplifie la syntaxe pour assurer une bonne maintenabilité du projet web, il permet de dissocier la partie vue de la partie programmation.
-   Compatible avec Web Server Gateway Interface 1.0 (c’est une spécification qui définit une interface entre les serveurs et des applications web pour le langage python)
-   Documentation complète
-   Possibilité de créer des extensions

#####  Les sites utilisant Flask :
Plusieurs sites connus utilisent Flask comme Netflix, Reddit ou encore Zalando.

### Description des actions réalisées

#####  Quelles étapes avez-vous suivi ?

Plusieurs étapes m'ont aidé à la réalisation du projet.
- Avec dans un premier temps, une phase de recherche sur les différentes technologies évoquées avec notamment **Flask** et **PythonAnywhere**. Cette partie m'a permis de comprendre à quoi servait ces deux outils et comment les manipuler. 
- Après cette phrase de recherche, je me suis créée un compte sur PythonAnywhere, je suis partie sur différents forums afin d'avoir plus d'informations sur la création d'une WebApp. 
- J'ai enfin pu avoir une application par défaut qui tourne sur PythonAnywhere. Après la phase d'installation terminée, j'ai commencé à explorer l'application fournie, à modifier mon application par défaut et à le remplacer par celle fournie. Je me suis intéressée au code de l'application, à tester les routes, à commencer à manipuler le code. J'ai ensuite lié mon compte avec github.
- La phase de test m'a permis de manipuler le code, de créer des routes, de voir comment toute l'application marchait et grâce à cela, j'ai pu mieux comprendre la logique de celle-ci.

#####  Quelles difficultés avez-vous rencontrées ?
Les erreurs de log ne sont pas toujours faciles à lire et à comprendre, c'était un peu complexe au début, mais après plus de pratiques on arrive mieux à comprendre d'où proviennent les erreurs. L'indentation était parfois difficile à mettre en place.

### Réflexions sur le projet

#####  Quels sont, selon vous, les aspects techniques limitants du projet FLGAZ dans l'état initial ? 
- L'application n'est pas en modèle MVC
- Toute l'application est centrée sur le fichier principal appelant toutes les routes
- Les routes ne sont pas sécurisées et accessibles par tous

#####  Quelles sont, selon vous, les menaces auxquelles un tel projet peut être soumis ?
Plusieurs menaces peuvent être détectées :
- Les attaques XSS
- l'injection de données en masse
- Les injections SQL
- Surcharger le serveur et le ralentir
