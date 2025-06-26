import unittest
from src.fusion import Obligation, Portefeuille, CoachIA

class TestObligation(unittest.TestCase):

    def test_rendement_valide(self):
        ob = Obligation("SG", 5, 0.01, 1000)
        self.assertAlmostEqual(ob.calcul_rendement(), 1051.01, places=2)

    def test_maturite_negative(self):
        with self.assertRaises(ValueError):
            Obligation("SG", -2, 0.01, 1000)

    def test_taux_negatif(self):
        with self.assertRaises(ValueError):
            Obligation("SG", 5, -0.01, 1000)

    def test_nominal_zero(self):
        with self.assertRaises(ValueError):
            Obligation("SG", 5, 0.01, 0)

class TestPortefeuille(unittest.TestCase):

    def test_compute_position(self):
        ob1 = Obligation("A", 5, 0.01, 1000)
        ob2 = Obligation("B", 3, 0.02, 1000)
        pf = Portefeuille([ob1, ob2], annee=2)
        expected = 1000 * (1 + 0.01)**2 + 1000 * (1 + 0.02)**2
        self.assertAlmostEqual(pf.compute_position(), expected, places=2)

class TestCoachIA(unittest.TestCase):

    def test_selection_rendement(self):
        ob1 = Obligation("A", 5, 0.01, 1000)
        ob2 = Obligation("B", 5, 0.03, 1000)
        ob3 = Obligation("C", 5, 0.02, 1000)
        coach = CoachIA([ob1, ob2, ob3], capital=2000, nombre=2)
        result = coach.entrainer_coach()
        noms = [ob.nom for ob in result]
        self.assertEqual(noms, ["B", "C"])

    def test_selection_budget_limite(self):
        ob1 = Obligation("A", 5, 0.03, 3000)
        ob2 = Obligation("B", 5, 0.02, 1000)
        coach = CoachIA([ob1, ob2], capital=1500, nombre=2)
        result = coach.entrainer_coach()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].nom, "B")

if __name__ == "__main__":
    unittest.main()
