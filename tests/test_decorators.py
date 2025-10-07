import allure
from selene import browser

repository_my = "YuliaEtm/QaGuru22_HW2"
issue_my = "Урок 10"


@allure.title('Проверка Issue')
@allure.description('Проверка наличия Issue в искомом репозитории')
@allure.feature("Github")
@allure.story("Issue")
def test_search_issue(browser_setup, github_page):

    open_browser(github_page)
    search_repository(github_page, repository_my)
    open_repository(github_page, repository_my)
    open_issues(github_page)
    check_issue(github_page, issue_my)


@allure.step('Открываем главную страницу GitHub')
def open_browser(github_page):
    github_page.open()


@allure.step(f'Ищем репозиторий {repository_my}')
def search_repository(github_page, repository):
    github_page.search_repository(repository)


@allure.step(f'Открываем репозиторий {repository_my}')
def open_repository(github_page, repository):
    github_page.open_repository(repository)


@allure.step('Заходим в Issues')
def open_issues(github_page):
    github_page.open_issues()


@allure.step('Проверяем существование Issue - Урок 10 ')
def check_issue(github_page, issue):
    github_page.issues_should_have_text(issue)
    screenshot = browser.driver.get_screenshot_as_png()
    allure.attach(
        screenshot,
        name="Результат выполнения теста",
        attachment_type=allure.attachment_type.PNG)
