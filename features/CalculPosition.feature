Feature: US_0002 Calcul position à un instant donné
En tant que financier
Je veux après avoir enregistré les différentes obligations avec leurs maturités, taux et nominals respectifs. Je souhaite calculer ma position au cours du temps.
Ceci afin de développer mes perspectives d'investissements.

  Scenario Outline: Création d'un portefeuille avec plusieurs obligations
    Given des obligations avec <nom>, <maturite>, <taux>, <nominal>
      | nom   | maturite  | taux  | nominal  |
      | SG    | 8         | 0.003 | 1500     |
      | BNP   | 7         | 0.005 | 2000     |

    When l'utilisateur la valide
    Then le système enregistre deux obligations <obligation1> <obligation2> dans le portefeuille <portefeuille1>

    Examples:

    | portefeuille1  | obligation1 | obligation2  |
    | myportefeuille | obligationSG| obligationBNP|














