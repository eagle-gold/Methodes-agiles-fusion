Feature: US_0002 – Calcul de position à un instant donné

  En tant que financier
  Je veux enregistrer plusieurs obligations dans un portefeuille
  Afin de calculer leur position future

  Scenario: Création d’un portefeuille avec plusieurs obligations
    Given les obligations suivantes sont enregistrées
      | nom | maturite | taux  | nominal |
      | SG  | 8        | 0.003 | 1500    |
      | BNP | 7        | 0.005 | 2000    |
    And le portefeuille est créé pour l’année 2
    When je calcule la position du portefeuille
    Then la position obtenue est 3529.06













