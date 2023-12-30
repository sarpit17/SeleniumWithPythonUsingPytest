import pytest

from PageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass
from TestData.testData import TestData

class TestHomepage(BaseClass):

    def test_homepage(self,getdata):
        log=self.get_logger()
        homepage_obj= HomePage(self.driver)
        homepage_obj.get_name().send_keys(getdata["name"])
        log.info("Name :" + getdata["name"])
        homepage_obj.get_mail().send_keys(getdata["mail"])
        log.info("Mail :" + getdata["mail"])
        homepage_obj.get_pass().send_keys(getdata["Pass"])
        log.info("Password :" + getdata["Pass"])
        homepage_obj.get_birth().send_keys(getdata["BD"])
        log.info("BirthDate :" + getdata["BD"])
        homepage_obj.get_gender(getdata["gender"])
        log.info("Gender :" + getdata["gender"])
        out=homepage_obj.submit("pos")
        if "Success" in out:
            log.info("Testcase Passed :" + out)
        else:
            log.error("Failed :" + out)
            assert "Success" in out
        self.driver.refresh()


    @pytest.fixture(params=TestData.testdata)
    def getdata(self, request):
        return request.param
