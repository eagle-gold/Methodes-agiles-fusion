Feature: US_0003 – Entraîner le CoachIA pour sélectionner les meilleures obligations

En tant que financier expérimenté souhaitant maximiser mes investissements,
Je veux qu’un CoachIA m’aide à choisir automatiquement les meilleures obligations en fonction du rendement,
Afin de constituer un portefeuille optimal tout en respectant mes contraintes de capital et de nombre de titres.


  Scenario Outline: Sélection des obligations par rendement décroissant
    Given un CoachIA dispose d'un capital de <capital> euros et souhaite acheter au plus <objectif> obligations
    And les obligations suivantes sont disponibles
      | nom  | maturite | taux   | nominal |
      | <nom1> | <mat1> | <taux1> | <nominal1> |
      | <nom2> | <mat2> | <taux2> | <nominal2> |
      | <nom3> | <mat3> | <taux3> | <nominal3> |
    When le CoachIA sélectionne les obligations
    Then il renvoie <attendu> obligation(s) triée(s) par rendement décroissant

    Examples:
      | capital | objectif | attendu | nom1 | mat1 | taux1 | nominal1 | nom2 | mat2 | taux2 | nominal2 | nom3 | mat3 | taux3 | nominal3 |
      | 4000    | 2        | 2       | SG   | 8    | 0.003 | 1500     | AXA  | 10   | 0.005 | 2000     | CA   | 6    | 0.002 | 1000     |
      | 1500    | 3        | 1       | SG   | 5    | 0.003 | 1500     | AXA  | 10   | 0.005 | 2000     | CA   | 6    | 0.002 | 1000     |

