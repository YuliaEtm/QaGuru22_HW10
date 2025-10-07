def test_issue(browser_setup, github_page):
    github_page.open()
    github_page.search_repository("YuliaEtm/QaGuru22_HW2")
    github_page.open_repository("YuliaEtm/QaGuru22_HW2")
    github_page.open_issues()

    github_page.issues_should_have_text("Урок 10")
