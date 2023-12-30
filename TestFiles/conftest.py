import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    browser_name=request.config.getoption('browser')
    if browser_name=="chrome":
        service_obj = Service()
        driver=webdriver.Chrome(service = service_obj)
    elif browser_name=="firefox":
        service_obj = Service(executable_path="C:\\Gecko\\geckodriver-v0.33.0-win64\\geckodriver.exe")
        driver =webdriver.Firefox(service=service_obj)

    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver=driver
    yield
    driver.close()


