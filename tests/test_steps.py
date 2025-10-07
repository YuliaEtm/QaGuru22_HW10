import allure
from selene import browser

repository = "YuliaEtm/QaGuru22_HW2"


@allure.title('Проверка Issue')
@allure.description('Проверка наличия Issue в искомом репозитории')
@allure.feature("Github")
@allure.story("Issue")
def test_search_issue(browser_setup, github_page):
    with allure.step('Открываем главную страницу GitHub'):
        github_page.open()

    with allure.step(f'Ищем репозиторий {repository}'):
        github_page.search_repository(repository)

    with allure.step(f'Открываем репозиторий {repository}'):
        github_page.open_repository(repository)

    with allure.step('Заходим в Issues'):
        github_page.open_issues()

    with allure.step('Проверяем существование Issue - Урок 10 '):
        github_page.issues_should_have_text("Урок 10")
        screenshot = browser.driver.get_screenshot_as_png()
        allure.attach(
            screenshot,
            name="Результат test_search_issue",
            attachment_type=allure.attachment_type.PNG)
