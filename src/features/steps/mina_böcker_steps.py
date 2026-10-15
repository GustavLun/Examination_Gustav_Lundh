import re
from behave import when, then, given
from playwright.sync_api import expect
from behave.api.pending_step import StepNotImplementedError

from src.features.steps.katalog_steps import SELECTED

BOOK_TITLE = "Ormar på ett plan: En Python-berättelse"
SELECTED = re.compile(r"\bselected\b")


@when(u'jag öppnar mina böcker')
def step_impl(context):
    context.page.get_by_test_id("favorites").click()


@then(u'ska boken finnas i Mina böcker')
def step_impl(context):
    expect(context.page.get_by_text(context.book_title)).to_be_visible()



@then(u'ska information om att listan är tom visas')
def step_impl(context):
    expect(context.page.get_by_text(" När du valt, kommer dina favoritböcker att visas här. ")).to_be_visible()