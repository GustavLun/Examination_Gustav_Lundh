from behave.api.pending_step import StepNotImplementedError
from behave import when, then, given
from playwright.sync_api import expect

titel = "Gäster"
författaren = "Edward Blom"

@given(u'att jag har öppnat lägg till bok')
def step_impl(context):
    context.page.get_by_test_id("add-book").click()



@when(u'jag fyller i titeln "Gäster" och författaren "Edward Blom"')
def step_impl(context):
    context.page.get_by_test_id("add-input-title").fill(titel)
    context.page.get_by_test_id("add-input-author").fill(författaren)


@when(u'jag trycker på lägg till en ny bok')
def step_impl(context):
    context.page.get_by_test_id("add-submit").click()


@then(u'ska boken "{titel}" finnas i katalogen')
def step_impl(context,titel):

    catalog = context.page.get_by_test_id("catalog")
    if catalog.is_enabled():
        catalog.click()
    book = context.page.locator(".catalog .book", has_text=titel)
    expect(book).to_be_visible()



@then(u'ska knappen lägg till ny bok vara inaktiv')
def step_impl(context):
    expect(context.page.get_by_test_id("add-submit")).to_be_disabled()




@then(u'ska knappen lägg till ny bok vara aktiv')
def step_impl(context):
    context.page.get_by_test_id("add-input-title").fill(titel)
    context.page.get_by_test_id("add-input-author").fill(författaren)
    expect(context.page.get_by_test_id("add-submit")).to_be_enabled()