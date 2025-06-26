from behave import given, when, then
import typing
from src.fusion import *
from dataclasses import dataclass, field

import math




@given("l'enregistrement d'une obligation avec {nom1}, {maturite1:d}, {taux1:g}, {nominal1:g}")
def step_given_obligation(context, nom1, maturite1, taux1, nominal1):

    context.financier = Financier()
    if maturite1 > 0 and taux1 > 0 and nominal1 > 0:
        context.financier.boolean = True

    if context.financier.boolean:
        context.financier.obligation = Obligation(
            nom=nom1, maturite=maturite1, taux=taux1, nominal=nominal1
        )

@when("l'utilisateur la valide")
def step_when_valide(context):

    pass

@then("le {rendement1:g} est calculé")
def step_then_rendement(context, rendement1):

    assert context.financier.boolean, "L'obligation n'a pas été acceptée"
    rendu = context.financier.obligation.calculrendement()
    assert math.isclose(rendu, rendement1, rel_tol=1e-4), (
        f"Attendu {rendement1}, obtenu {rendu}"
    )

@given(
    "l'enregistrement d'une obligation avec {nom1}, {maturite1:d} ans, {taux1:g}, {nominal1:g}"
)
def step_given_obligation_invalide(context, nom1, maturite1, taux1, nominal1):

    context.financier = Financier()

    try:

        context.financier.obligation = Obligation(
            nom=nom1,
            maturite=maturite1,
            taux=taux1,
            nominal=nominal1,
        )

        context.financier.boolean = False
    except ValueError:

        context.financier.boolean  = True
@when("l'utilisateur valide")
def step_when_valide(context):

    pass

@then("le système la refuse {isBad:w}")
def step_then_refus(context, isBad):

    attendu = False
    assert context.financier.boolean  == attendu, (
        f"Attendu refus={attendu}, obtenu refus={context.financier.boolean}"
    )