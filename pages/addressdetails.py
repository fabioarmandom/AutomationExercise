from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import Select
import time 


class Address:
    def __init__(self, driver):
        self.driver = driver
        self.SIGNUP_LOGIN_BTN = (By.XPATH, "//a[@href='/login'][contains(.,'Signup / Login')]")
        self.USERNAME_INPUT = (By.XPATH, "//input[contains(@data-qa,'signup-name')]")
        self.EMAIL_INPUT = (By.XPATH, "//input[contains(@data-qa,'signup-email')]")
        self.BTN_SIGN_UP = (By.XPATH, "//button[@type='submit'][contains(.,'Signup')]")
        self.BTN_MR = (By.XPATH, "//input[@type='radio'][contains(@id,'gender1')]")
        self.PASSWORD_INPUT = (By.XPATH, "//input[contains(@id,'password')]")
        self.DAY_DROPDOWN = (By.ID, 'days')
        self.MONTH_DROPDOWN = (By.ID, 'months')
        self.YEAR_DROPDOWN = (By.ID, 'years')
        self.COUNTRY = (By.ID, 'country')
        self.BOX1 = (By.XPATH, "//input[contains(@id,'newsletter')]")
        self.BOX2 = (By.XPATH, "//input[contains(@id,'optin')]")
        self.FIRSTNAME_INPUT = (By.XPATH, "//input[contains(@id,'first_name')]")
        self.LASTNAME_INPUT = (By.XPATH, "//input[contains(@data-qa,'last_name')]")
        self.COMPANY_INPUT = (By.XPATH, "//input[contains(@data-qa,'company')]")
        self.ADDRESS_INPUT = (By.XPATH, "//input[@data-qa='address']")
        self.ADDRESS2_INPUT = (By.XPATH, "//input[contains(@data-qa,'address2')]")
        self.COUNTRY = (By.ID, 'country')
        self.STATE_INPUT = (By.XPATH, "//input[contains(@data-qa,'state')]")
        self.CITY_INPUT = (By.XPATH, "//input[contains(@data-qa,'city')]")
        self.ZIPCODE_INPUT = (By.XPATH, "//input[contains(@data-qa,'zipcode')]")
        self.MOBILENUMBER_INPUT = (By.XPATH, "//input[@type='text'][contains(@id,'number')]")
        self.COUNTRY = (By.ID, 'country')
        self.CREATE_ACCOUNT = (By.XPATH, "//button[contains(@data-qa,'create-account')]")
        self.BTN_CONTINUE = (By.XPATH, "//a[@href='/'][contains(.,'Continue')]")
        self.ACCOUNT_CREATED_B = (By.XPATH, "//b[contains(.,'Account Created!')]")
        self.BTN_CONTINUE = (By.XPATH, "//a[@href='/'][contains(.,'Continue')]")
        self.LOGGED_AS = (By.XPATH, "//a[contains(.,'Logged in as Fabio Armando')]")
        self.HOME_BTN = (By.XPATH, "//a[@href='/'][contains(.,'Home')]")
        self.PRODUCT_01 = (By.XPATH, "/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/a")
        self.PRODUCT_02 = (By.XPATH, "/html/body/section[2]/div/div/div[2]/div/div[3]/div/div[1]/div[1]/a")
        self.CONTINUE_BTN = (By.XPATH, "//button[contains(.,'Continue Shopping')]")
        self.CART_BTN = (By.XPATH, "//i[contains(@class,'fa fa-shopping-cart')]")
        self.CHECKOUT_BTN = (By.XPATH, "//a[contains(@class,'btn btn-default check_out')]")
        self.delivery_address_element = (By.ID, "address_delivery")
        self.registered_address_element = (By.ID, "address_invoice")
        self.DELETE_ACCT = (By.XPATH, "//a[@href='/delete_account']")
        self.ACCT_DELETED = (By.XPATH, "//b[contains(.,'Account Deleted!')]")

    def btn_delete_acct(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.DELETE_ACCT)).click()
        except (NoSuchElementException, TimeoutException):
            print("Error: First btn sign up not found")
            return False
        
    def get_deleted_message(self):
        try:
           create_text = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.ACCT_DELETED)).text
        except(NoSuchElementException, TimeoutException):
            print("Error: No text found!")
            return False
        assert create_text == "ACCOUNT DELETED!", f"Expected 'ACCOUNT DELETED!' but got '{create_text}'"


    def get_delivery_address(self):
        delivery_address = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.delivery_address_element)).text.lstrip()
        return delivery_address.split('\n')[1:]
    
    def get_registered_address(self):
        registered_address = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.registered_address_element)).text.lstrip()
        return registered_address.split('\n')[1:]
    
    def verify_delivery_address(self):
        delivery_address = self.get_delivery_address()
        registered_address = self.get_registered_address()
        print(delivery_address) 
        print(registered_address)
        assert delivery_address == registered_address, "Delivery address does not match the registered address"
        print("Delivery address matches the registered address:", delivery_address)
        


    def scroll_by_amount(self, x_pixels, y_pixels):
        """Scroll the window by the given amount."""
        scroll_script = f"window.scrollBy({x_pixels}, {y_pixels})"
        self.driver.execute_script(scroll_script)

    def signup_login_btn(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.SIGNUP_LOGIN_BTN)).click()
        except (NoSuchElementException, TimeoutException):
            print("Error: First btn products not found")
            return False
        
    def credentials(self, username, email):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.USERNAME_INPUT)).send_keys(username)
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.EMAIL_INPUT)).send_keys(email)
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.BTN_SIGN_UP)).click()
        except (NoSuchElementException, TimeoutException):
            print("Error: Username input not found")
            return False
        
    def btn_mr(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.BTN_MR)).click()
        except (NoSuchElementException, TimeoutException):
            print("Error: First btn sign up not found")
            return False
    
    def enter_password(self, password):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.PASSWORD_INPUT)).send_keys(password)
        except (NoSuchElementException, TimeoutException):
            print("Error: password space no found")
            return False
        
    def select_date_of_birth(self, day, month, year):
        Select(self.driver.find_element(*self.DAY_DROPDOWN)).select_by_index(day)
        Select(self.driver.find_element(*self.MONTH_DROPDOWN)).select_by_index(month)
        Select(self.driver.find_element(*self.YEAR_DROPDOWN)).select_by_value(year)

    def select_country(self, state):
        Select(self.driver.find_element(*self.COUNTRY)).select_by_value(state)

    def check_box(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.BOX1)).click()
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.BOX2)).click()
        except (NoSuchElementException, TimeoutException):
            print("Error: check box not found")
            return False
      
    def address_information(self, first_name, last_name, company, address, address2, state, city, zipcode, mobile_number):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.FIRSTNAME_INPUT)).send_keys(first_name)
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.LASTNAME_INPUT)).send_keys(last_name)
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.COMPANY_INPUT)).send_keys(company)
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.ADDRESS_INPUT)).send_keys(address)
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.ADDRESS2_INPUT)).send_keys(address2)
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.STATE_INPUT)).send_keys(state)
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.CITY_INPUT)).send_keys(city)
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.ZIPCODE_INPUT)).send_keys(zipcode)
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.MOBILENUMBER_INPUT)).send_keys(mobile_number)
        except (NoSuchElementException, TimeoutException):
            print("Error: Username input not found")
            return False
        
    def select_country(self, state):
        Select(self.driver.find_element(*self.COUNTRY)).select_by_value(state)

    def create_btn(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.CREATE_ACCOUNT)).click()
        except (NoSuchElementException, TimeoutException):
            print("Error: Acct btn sign up not found")
            return False
        
    def get_create_message(self):
        try:
           create_text = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.ACCOUNT_CREATED_B)).text
        except(NoSuchElementException, TimeoutException):
            print("Error: No text found!")
            return False
        assert create_text == "ACCOUNT CREATED!", f"Expected 'ACCOUNT CREATED!' but got '{create_text}'"

    def continue_btn(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.BTN_CONTINUE)).click()
        except (NoSuchElementException, TimeoutException):
            print("Error: First btn sign up not found")
            return False
        
    def get_logged_as(self):
        try:
           logged_text = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.LOGGED_AS)).text
        except(NoSuchElementException, TimeoutException):
            print("Error: No text found!")
            return False
        assert logged_text == "Logged in as Fabio Armando", f"Expected 'Logged in as Fabio Armando' but got '{logged_text}'"
    
    def home_btn(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.HOME_BTN)).click()
        except (NoSuchElementException, TimeoutException):
            print("Error: First btn products not found")
            return False
        
    def selecting_products(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.PRODUCT_01)).click()
            time.sleep(2)
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.CONTINUE_BTN)).click()

            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.PRODUCT_02)).click()
            time.sleep(2)
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.CONTINUE_BTN)).click()
        except (NoSuchElementException, TimeoutException):
            print("Error: First btn products not found")
            return False
        
    def cart_btn(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.CART_BTN)).click()
        except (NoSuchElementException, TimeoutException):
            print("Error: First btn products not found")
            return False
        
    def checkout_btn(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.CHECKOUT_BTN)).click()
        except (NoSuchElementException, TimeoutException):
            print("Error: First btn products not found")
            return False