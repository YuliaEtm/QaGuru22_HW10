from selene import browser, have, by, be


class GithubPage:

    def open(self):
        browser.open('/')
        return self

    def search_repository(self, repository):
        browser.element('.search-input').click()
        browser.element('#query-builder-test').type(repository).press_enter()
        return self

    def open_repository(self, repository):
        browser.element(f'[href="/{repository}"]').click()
        return self

    def open_issues(self):
        browser.element('#issues-tab').click()
        return self

    def issues_should_have_text(self, value):
        browser.element('html').should(have.text(value))
        return self
