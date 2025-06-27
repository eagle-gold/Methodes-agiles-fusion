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
Enfin, nous utilisons nos méthodes de la classe Obligation afin de calculer le rendement de notre portefeuille.

![image](https://github.com/user-attachments/assets/007c633d-7b39-4ab3-b9c8-23d0d368305a)




Nous pouvons maintenant  créer une nouvelle méthode de test sur la méthode CalculRendement de la classe Portefeuille. 

![image](https://github.com/user-attachments/assets/0ca2afeb-f8b3-4e04-a3ee-573f88af3843)




Maintenant nous pouvons sauvegarder nos instances dans la fixture de la classe test.

![image](https://github.com/user-attachments/assets/bc847f0d-5349-484c-bf56-6f58c55ffff4)


Nous allons créer une classe PortefeuilleTemps, constituée d’une collection de portefeuille. Tous contiennent la même obligation mais à des instants différents.

![image](https://github.com/user-attachments/assets/38b054db-7e4d-4b05-94af-97c5f8550c44)

Accompagnée de sa classe de test : 

![image](https://github.com/user-attachments/assets/39f4cfde-ad4b-4d19-aae0-d917ab3b82c2)

![image](https://github.com/user-attachments/assets/e778b435-771c-4921-a4cf-2a5ed146606b)


Pour finir la classe Position, composé d'une collection de PortefeuilleTemps




![image](https://github.com/user-attachments/assets/920ffb4e-05ef-4cba-9279-9489df580400)

![image](https://github.com/user-attachments/assets/719b2218-fbbb-48a6-85b4-9212cc8df57f)

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

