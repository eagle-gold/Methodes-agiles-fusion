from behave import given, when, then
from src.fusion import Obligation, Financier
import math

@given("l'enregistrement d'une obligation avec {nom1}, {maturite1:d}, {taux1:g}, {nominal1:g}")
def step_given_obligation(context, nom1, maturite1, taux1, nominal1):
    context.financier = Financier()
    try:
        obligation = Obligation(
            nom=nom1,
            maturite=maturite1,
            taux=taux1,
            nominal=nominal1
        )
        context.financier.obligation = obligation
        context.financier.boolean = True
    except ValueError:
        context.financier.boolean = False

@when("l'utilisateur la valide")
def step_when_valide(context):
    pass

@when("l'utilisateur valide")
def step_when_valide_short(context):
    pass

@then("le {rendement1:g} est calculé")
def step_then_rendement(context, rendement1):
    assert context.financier.boolean, "L'obligation n'a pas été acceptée"
    rendu = context.financier.obligation.calcul_rendement()
    assert math.isclose(rendu, rendement1, rel_tol=1e-2), (
        f"Attendu {rendement1}, obtenu {rendu}"
    )

@then("le système la refuse {isBad:w}")
def step_then_refus(context, isBad):
    attendu = isBad.lower() == "true"
    assert context.financier.boolean != attendu, (
        f"Refus attendu : {attendu}, mais reçu : {not context.financier.boolean}"
    )
