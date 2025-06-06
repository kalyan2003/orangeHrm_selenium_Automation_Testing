from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Lauching Chrome browser....")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Lauching FireFox browser....")
    else:
        driver = webdriver.Chrome()
        print("Lauching chrome......")
    return driver



def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


####### PyTest Html Report ######
def pytest_configure(config):
    if hasattr(config, '_metadata'):
        config._metadata['Project Name'] = 'nop commerce'
        config._metadata['Module Name'] = 'Customers'
        config._metadata['Tester'] = 'Pavan'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)



