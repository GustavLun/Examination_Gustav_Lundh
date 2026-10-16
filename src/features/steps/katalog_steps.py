import re
from behave.api.pending_step import StepNotImplementedError
from behave import when, then, given
from playwright.sync_api import expect

BOOK_TITLE = "The Pragmatic Procrastinator"
SELECTED = re.compile(r"\bselected\b")

@when(u'jag trycker på katalog')
def step_impl(context):
    context.page.get_by_test_id("catalog") # Click skippas då det är det första syns på sidan vilket täck äav common steps.



@then(u'ska en lista med böcker visas')
def step_impl(context):
        books = context.page.locator(".catalog .book")
        assert books.count() > 0

def get_star(context):
    return context.page.get_by_test_id(f"star-{context.book_title}")

@when(u'jag trycker på hjärtat vid en bok')
def step_impl(context):
    context.book_title = BOOK_TITLE
    get_star(context).click()


@then(u'ska boken vara favoritmarkerad')
def step_impl(context):
    expect(get_star(context)).to_have_class(SELECTED)



@given(u'att jag favoritmarkerat en bok')
def step_impl(context):
    context.book_title = BOOK_TITLE
    get_star(context).click()
    expect(get_star(context)).to_have_class(SELECTED)



@when(u'Jag trycker på hjärtat igen')
def step_impl(context):
    context.book_title = BOOK_TITLE
    get_star(context).click()


@then(u'ska boken inte längre vara favoritmarkerad')
def step_impl(context):
    expect(get_star(context)).to_have_class(re.compile(r"^star$"))