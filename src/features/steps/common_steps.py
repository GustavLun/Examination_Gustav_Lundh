from behave import given

URL = "https://tap-vt26-testautomatisering.github.io/exam/"

@given("att jag har öppnat läslistan")
def step_open_app(context):
    context.page.goto(URL)