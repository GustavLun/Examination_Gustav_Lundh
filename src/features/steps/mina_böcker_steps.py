from behave import when, then, given
from playwright.sync_api import expect
from behave.api.pending_step import StepNotImplementedError

BOOK_TITLE = "Ormar på ett plan: En Python-berättelse"

@given(u'att jag har favoritmarkerat en bok')
def step_impl(context):
    context.page.get_by_text(BOOK_TITLE).click(but)

@when(u'jag öppnar Mina böcker')
def step_impl(context):
    context.page.get_by_test_id("favorites").click()


@then(u'ska boken finnas i Mina böcker')
def step_impl(context):
    expect.contains(BOOK_TITLE)


@when(u'jag öppnar mina böcker')
def step_impl(context):
    raise StepNotImplementedError(u'When jag öppnar mina böcker')


@then(u'ska information om att listan är tom visas')
def step_impl(context):
    raise StepNotImplementedError(u'Then ska information om att listan är tom visas')