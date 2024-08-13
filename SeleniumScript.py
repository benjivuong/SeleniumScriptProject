from selenium import webdriver
from selenium.webdriver.common.by import By

class AutomatedTester:
    driver = webdriver.Chrome()
    driver.get("http://sdetchallenge.fetch.com")
    driver.implicitly_wait(0.5)
    left0 = driver.find_element(by=By.ID, value="left_0")
    left1 = driver.find_element(by=By.ID, value="left_1")
    left2 = driver.find_element(by=By.ID, value="left_2")

    right0 = driver.find_element(by=By.ID, value="right_0")
    right1 = driver.find_element(by=By.ID, value="right_1")
    right2 = driver.find_element(by=By.ID, value="right_2")

    weighButton = driver.find_element(by=By.NAME, value="weigh")
    genericResetButtons = driver.find_elements(by=By.ID, value="reset")
    resetButton, resultButton = None, None
    for element in genericResetButtons:
        if element.is_enabled():
            resetButton = element
        else:
            resultButton = element

    def __init__(self) -> None:
        pass
    def click_reset(self):
        self.resetButton.click()
    def click_weigh(self):
        self.weighButton.click()
    def get_measurement_result(self):
        return self.resultButton.text
    def click_fake_bar_button(self, fakeBarValue):
        fakeBarButton = self.driver.find_element(by=By.ID, value="coin_" + fakeBarValue)
        fakeBarButton.click()
    def print_list(self):
        gameInfo = self.driver.find_element(by=By.CLASS_NAME, value="game-info")
        listOfWeighings = gameInfo.find_elements(by=By.TAG_NAME, value="li")
        for weighing in listOfWeighings:
            print(weighing)
    def run_algorithm(self):
        # First measure
        self.left0.send_keys("0")
        self.left1.send_keys("1")
        self.left2.send_keys("2")
        self.right0.send_keys("6")
        self.right1.send_keys("7")
        self.right2.send_keys("8")
        self.click_weigh()
        result = self.get_measurement_result()

        # Second measure
        self.click_reset()
        startAtNum = 0
        if result == '=':
            startAtNum = 3
        elif result == '>':
            startAtNum = 6
        self.left0.send_keys(startAtNum)
        self.right0.send_keys(startAtNum+1)
        self.click_weigh()

        result = self.get_measurement_result()
        fakeBarNum = startAtNum
        if result == '=':
            fakeBarNum = startAtNum + 2
            print(startAtNum + 2)
        elif result == '>':
            fakeBarNum = startAtNum + 1
            print(startAtNum + 1)
        else:
            print(startAtNum)

        self.click_fake_bar_button(fakeBarNum)
        alert = self.driver.switch_to.alert
        print(alert.text) # print the alert text
        print(2) # With this algorithm, the number of weighings is always 2
        self.print_list() # print the weighings list
        self.driver.quit()

test = AutomatedTester()
test.run_algorithm()