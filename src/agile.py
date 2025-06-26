from dataclasses import dataclass, field
class Obligation:
    def __init__(self, nom: str, maturite: int, taux: float, nominal: float):
        if maturite <= 0:
            raise ValueError("La maturité doit être positive")
        if taux < 0:
            raise ValueError("Le taux doit être positif")
        if nominal <= 0:
            raise ValueError("Le nominal doit être positif")
        self._nom = nom
        self._maturite = maturite
        self._taux = taux
        self._nominal = nominal
        self._rendement = 0


    def getNominal(self) -> float:

        return self.nominal

    def getTaux(self) -> float:
        return self.taux

    def getMaturite(self) -> int:
        return self.maturite

    def getNom(self) -> int:
        return self.nom

    def calculrendement(self) -> float:
        self._rendement = self._nominal * (1 + self._taux) ** self._maturite
        return self._rendement


class Portefeuille():
    def __init__(self, obligation: list[Obligation], annee: int):
        self.obligation = obligation
        self.annee = annee



    def getAnnee(self) -> int:

        return self.annee

    def getObligation(self) -> list[Obligation]:
        return self.obligation

    def computePosition(self) -> float:
        position = 0
        for i in range(len(self.obligation)):
            iterateur = self.obligation[i]
            nominal = iterateur.getNominal()
            taux = iterateur.getTaux()
            maturite = iterateur.getMaturite()
            if self.annee <= maturite:
                position += nominal*(1+taux)**self.annee
        return position


@dataclass
class Financier:
    obligation: Obligation | None = None
    boolean: bool = False