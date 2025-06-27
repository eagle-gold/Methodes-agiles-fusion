from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Protocol

class StrategieRendement(Protocol):
    def calculer(self, obligation: Obligation) -> float:
        ...

class RendementTauxFixe:
    def calculer(self, obligation: Obligation) -> float:
        return obligation.nominal * (1 + obligation.taux) ** obligation.maturite

@dataclass(order=True)
class Obligation:
    nom: str
    maturite: int
    taux: float
    nominal: float
    strategie_rendement: StrategieRendement = field(default_factory=RendementTauxFixe, repr=False, compare=False)
    rendement: float = field(init=False, repr=False, compare=False)

    def __post_init__(self) -> None:
        if self.maturite <= 0:
            raise ValueError("La maturité doit être positive")
        if self.taux < 0:
            raise ValueError("Le taux doit être positif")
        if self.nominal <= 0:
            raise ValueError("Le nominal doit être positif")
        self.rendement = self.calcul_rendement()

    def calcul_rendement(self) -> float:
        self.rendement = self.strategie_rendement.calculer(self)
        return self.rendement

@dataclass
class Portefeuille:
    obligations: List[Obligation]
    annee: int

    def compute_position(self) -> float:
        total = 0
        for obl in self.obligations:
            if self.annee <= obl.maturite:
                total += obl.strategie_rendement.calculer(
                    Obligation(obl.nom, self.annee, obl.taux, obl.nominal, obl.strategie_rendement)
                )
        return total

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
