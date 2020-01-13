
from pytest import mark
from termcolor import colored

from pages.telaviv.home_page_tel import HomePageTelAviv
from pages.telaviv.login_page import LoginTelAviv

MESSAGE_TEST_START_RUNNING = '\n===============| Test "%s" Started Running |==============='
MESSAGE_TEST_FINISHED_RUNNING = '===============| Test "%s" Finished Running |===============\n'

@mark.tel_aviv_login
def test_login_error(browser):
    home_page = HomePageTelAviv(driver=browser)
    login_page = LoginTelAviv(driver=browser)

    print(colored(MESSAGE_TEST_START_RUNNING % test_login_error.__name__, "green"))

    print(colored('Step 1: open {} ', 'blue').format(str(home_page.url)))
    home_page.go()

    print(colored('Step 2: Press on login button ', 'blue'))
    home_page.login_button.click()

    window_after = login_page.window_handles(1)
    login_page.switch_to(window_after, 2)

    print(colored('Step 3: Enter id ', 'blue'))
    login_page.id.type_text('201651593')

    print(colored('Step 4: Enter pass ', 'blue'))
    login_page.password.type_text('123456')

    print(colored('Step 5: Click enter button ', 'blue'))
    login_page.enter_button.click()

    error_text = login_page.error_text.text
    print(colored('Step 6: Verify if {} text display', 'blue').format(error_text))

    assert error_text == 'מספר הזהות או סיסמה אינם נכונים , אנא נסו שנית'

    print(colored(MESSAGE_TEST_FINISHED_RUNNING % test_login_error.__name__, "green"))






