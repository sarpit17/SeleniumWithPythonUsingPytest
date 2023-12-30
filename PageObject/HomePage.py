from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class HomePage:
    name = (By.CSS_SELECTOR, "form div input[name='name']")
    email = (By.NAME, "email")
    password = (By.CSS_SELECTOR, "#exampleInputPassword1")
    option = (By.CSS_SELECTOR, "#exampleCheck1")
    gender = (By.CSS_SELECTOR, "#exampleFormControlSelect1")
    eployment = (By.CSS_SELECTOR, "#inlineRadio2")
    birth = (By.NAME, "bday")
    check = (By.CSS_SELECTOR, ".btn-success")

    def __init__(self, driver):
        self.driver = driver

    def get_name(self):
        return self.driver.find_element(*HomePage.name)

    def get_mail(self):
        return self.driver.find_element(*HomePage.email)

    def get_pass(self):
        return self.driver.find_element(*HomePage.password)

    def get_gender(self, gen):
        Gender = Select(self.driver.find_element(*HomePage.gender))
        Gender.select_by_visible_text(gen)

    def get_birth(self):
        return self.driver.find_element(*HomePage.birth)

    def submit(self, scenario):
        self.driver.find_element(*HomePage.check).click()
        if scenario == "pos" or "":
            return self.driver.find_element(By.CSS_SELECTOR, ".alert-success").text
