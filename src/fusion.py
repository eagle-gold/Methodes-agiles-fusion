
from __future__ import annotations
from dataclasses import dataclass, field
from typing import List


@dataclass(order=True)
class Obligation:
    nom: str
    maturite: int
    taux: float
    nominal: float
    rendement: float = field(init=False, repr=False, compare=False)

    def __post_init__(self) -> None:
        if self.maturite <= 0:
            raise ValueError("La maturité doit être positive")
        if self.taux < 0:
            raise ValueError("Le taux doit être positif")
        if self.nominal <= 0:
            raise ValueError("Le nominal doit être positif")


        self.rendement = self.nominal * (1 + self.taux) ** self.maturite
    def getNominal(self) -> float:

        return self.nominal

    def getTaux(self) -> float:
        return self.taux

    def getMaturite(self) -> int:
        return self.maturite

    def getNom(self) -> int:
        return self.nom


    def calcul_rendement(self) -> float:
        self.rendement = self.nominal * (1 + self.taux) ** self.maturite
        return self.rendement



@dataclass
class Portefeuille:
    obligations: List[Obligation]
    annee: int


@dataclass
class Financier:
    obligation: Obligation | None = None
    boolean: bool = False


class CoachIA:

    def __init__(self, obligations: List[Obligation], capital: float, nombre: int):
        self.obligations = obligations
        self.capital = capital
        self.nombre = nombre

    def entrainer_coach(self) -> List[Obligation]:

        candidates = sorted(self.obligations, key=lambda ob: ob.rendement, reverse=True)

        selection: List[Obligation] = []
        solde = self.capital


        for ob in candidates:
            if len(selection) >= self.nombre:
                break
            if ob.nominal <= solde:
                selection.append(ob)
                solde -= ob.nominal

        return selection


