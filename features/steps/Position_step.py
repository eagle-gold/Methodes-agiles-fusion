from behave import given, when, then
from src.fusion import Obligation, Portefeuille
import math

@given("les obligations suivantes sont enregistrées")
def step_given_obligations(context):
    context.obligations = []
    for row in context.table:
        obl = Obligation(
            nom=row["nom"],
            maturite=int(row["maturite"]),
            taux=float(row["taux"]),
            nominal=float(row["nominal"]),
        )
        context.obligations.append(obl)

@given("le portefeuille est créé pour l’année {annee:d}")
def step_given_portefeuille(context, annee):
    context.portefeuille = Portefeuille(
        obligations=context.obligations,
        annee=annee
    )

@when("je calcule la position du portefeuille")
def step_when_calcul_position(context):
    context.resultat = context.portefeuille.compute_position()

@then("la position obtenue est {valeur:f}")
def step_then_resultat(context, valeur):
    assert math.isclose(context.resultat, valeur, rel_tol=1e-2), (
        f"Attendu {valeur}, obtenu {context.resultat}"
    )
