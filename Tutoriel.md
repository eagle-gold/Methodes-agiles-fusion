# Tutoriel : La programmation orientée-objet pour financiers très très motivés

## Courte histoire pour une mise en jambe efficace

Pierre , financier expert sur le marché des obligations, en avait marre de jongler avec ses tableurs excel chargés de formules et illisibles. Un soir, après un énième café, il se dit : “Stop, j'en peux plus, il me faut un truc qui calcul tout, tout le temps et à ma place !”. Il se rendit sur internet, à la recherche d'un tutoriel qui le ménera vers un avenir radieux. "Très bien, il me suffit d'apprendre à coder, ça ne devrait pas être si difficile" pensa t-il à haute voix.
"Mais comment m'assurer que mon code fonctionne, je pourrais perdre des millions d'euros et finir par vendre des paninis à chateaurou" s'inquiéta t-il.
Après des heures de recherches, au bord de l'abandon, il découvrit une vidéo youtube lui introduisant le principe des tests Junit, fonctionnels et l'IA.
"Eureka !" s'écriat-il.
Après une bonne nuit de sommeil, une tasse de café à la main, il s'attela à sa formation.

## Le tutoriel avec BlueJ
Nous commençons par créer une classe obligation qui représente un actif financier possédant une maturité, un nominal et un taux.
![image](https://github.com/user-attachments/assets/f0ca2f5f-8ae9-4fdc-b42f-d3b8d1cc355d)

Nous pouvons la compiler et l’instancier même sans schéma clair de sa constitution.
![image](https://github.com/user-attachments/assets/05f16ef3-72d2-410a-a4b2-e5898da8e958)


![image](https://github.com/user-attachments/assets/5cc0d42b-a0a7-4351-9b45-1ddfb06a9b7e)

Commençons à mieux définir notre classe.
![image](https://github.com/user-attachments/assets/83026085-bd9c-4f56-98c7-bef28e3930c1)



![image](https://github.com/user-attachments/assets/43be6376-f8b7-40a3-9524-7ba26a5a8cd1)


 



 
Instancions notre classe et essayons nos méthodes GetTaux. getNominal et getMaturite




Maintenant pour notre premier test nous créons une classe test, nous la compilons, nous définissons notre première méthode de test pour la méthode GetTaux.

![image](https://github.com/user-attachments/assets/0bc4235b-a376-4237-94cb-a6823fb2be0f)

![image](https://github.com/user-attachments/assets/3d1cc12e-2745-4654-ab37-7181751f6820)



Maintenant nous créons une nouvelle classe Portefeuille, qui va contenir une obligation à un instant t.

![image](https://github.com/user-attachments/assets/cd014480-bc50-4d98-8471-48a651bd0115)


Nous allons poursuivre le développement en suivant le pattern strategy, commençons par réaliser notre classe interface StrategieRendement

![image](https://github.com/user-attachments/assets/e5214024-4720-45b0-8e18-a0af0dd76f67)

Puis la classe RendementTauxFixe qui l'implèmente

![image](https://github.com/user-attachments/assets/9c73fec4-05e5-4b91-9c7a-27aa35eab482)

Notre Facotry d'obligation 

![image](https://github.com/user-attachments/assets/c4a4b2e5-3491-4fa4-9721-295a3dd5f4e3)

Et enfin notre Coach IA, si précieux pour développer les meilleures stratégies d'investissement

![image](https://github.com/user-attachments/assets/3f5f0b50-158c-496a-a92d-fd0e02105733)

Dorénavement, réalisons des tests JUnit sur notre solution

Des Tests sur Obligation
![image](https://github.com/user-attachments/assets/e3eb84e9-eb80-4635-83ad-52bb64cab5c2)

Des Tests sur Portefeuille
![image](https://github.com/user-attachments/assets/ebbef7b8-2487-4038-a3ef-78b17512bf6c)

Des Tests sur ObligationFactory
![image](https://github.com/user-attachments/assets/b1e3fb77-ff05-47cf-b314-19b236cee2b0)

Des Tests sur RendementTauxFixe
![image](https://github.com/user-attachments/assets/95e58456-2c58-4c6e-aea6-ff2533d7e14d)


Des Tests sur CoachIA
![image](https://github.com/user-attachments/assets/de1098d1-45c6-4e4b-ba0e-0482a531a709)

Il suffit de cliquer sur "Executer les tests" et avec beaucoup d'espoir, tout devrait être vert !

![image](https://github.com/user-attachments/assets/e6f04081-610c-4f07-bb02-af92cb3ede16)



## Behave et PyCharm
Il s'agit ici d'implémenter nos classes de BlueJ en Python, pour cela nous allons utiliser l'IDE PyCharm.

![image](https://github.com/user-attachments/assets/c46f9d41-9507-4d6f-8235-459320bf5810)

![image](https://github.com/user-attachments/assets/ff07760c-ff02-42fa-bcf9-076cef9707f4)



Dorénavant nous allons effectuer des tests fonctionnels dits de Behavior-Driven Development 

Pour cela nous posons une première feature, enregistrer des obligations.
Nous y voyons deux scénarios, le premier est le calcul automatique du rendement d'une obligation à maturité, l'autre est une vérification de la validité e l'obligation.

![image](https://github.com/user-attachments/assets/2824c19f-d025-4505-bf48-223ab54025db)


Il s'agit de faire passer à notre solution un test d'acceptance. Développons un step programme 

![image](https://github.com/user-attachments/assets/29cbf304-9558-47c7-b30d-03d63cfeeed0)

![image](https://github.com/user-attachments/assets/3f8b5767-0e04-4c4b-bded-300b80fac603)


Il nous suffit d'exécuter notre feature, avec un peu de chance tout sera au vert :)

![image](https://github.com/user-attachments/assets/153048e6-eecd-459b-94a3-06b5a04542b8)

On est bon !

