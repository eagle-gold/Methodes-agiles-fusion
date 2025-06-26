Feature: US_0001 – Enregistrer les obligations

En tant que financier
Je veux enregistrer les différentes obligations avec leurs maturités, taux et nominals respectifs.
Ceci afin de développer la vision que j'ai de ma position.

  Scenario Outline: Calcul automatique du rendement à maturité
    Given l'enregistrement d'une obligation avec <nom1>, <maturite1>, <taux1>, <nominal1>
    When l'utilisateur la valide
    Then le <rendement1> est calculé

    Examples:
      | nom1  | maturite1 | taux1 | nominal1 | rendement1 |
      | SG    | 8         | 0.003 | 1500     | 1536.38    |



  Scenario Outline: Refus d'une obligation à maturité, taux ou nominal négatif
    Given l'enregistrement d'une obligation avec <nom1>, <maturite1>, <taux1>, <nominal1>
    When l'utilisateur valide
    Then le système la refuse <isBad>

    Examples:
    | nom1  | maturite1 | taux1 | nominal1 | isBad     |
    | SG    | 8         | -0.003| 1500     | True      |
