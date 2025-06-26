from behave import given, when, then
from src.fusion import CoachIA, Obligation


def _to_float(txt: str) -> float:
    return float(txt.replace(",", "."))

@given("un CoachIA dispose d'un capital de {capital:d} euros et souhaite acheter au plus {objectif:d} obligations")
def given_coach_params(context, capital, objectif):
    context.capital = float(capital)
    context.objectif = int(objectif)
    context.obligations = []

@given("les obligations suivantes sont disponibles")
def given_obligations_table(context):
    for row in context.table:
        context.obligations.append(
            Obligation(
                nom=row["nom"],
                maturite=int(row["maturite"]),
                taux=_to_float(row["taux"]),
                nominal=_to_float(row["nominal"]),
            )
        )

@when("le CoachIA sélectionne les obligations")
def when_coach_selects(context):
    coach = CoachIA(context.obligations, context.capital, context.objectif)
    context.selection = coach.entrainer_coach()

@then("il renvoie {attendu:d} obligation(s) triée(s) par rendement décroissant")
def then_verify_selection(context, attendu):
    assert len(context.selection) == attendu, (
        f"Le CoachIA devait renvoyer {attendu} obligation(s), "
        f"mais en a renvoyé {len(context.selection)}."
    )
    rendements = [obl.rendement for obl in context.selection]
    assert rendements == sorted(rendements, reverse=True), (
        f"Les obligations ne sont pas triées par rendement décroissant : {rendements}"
    )
