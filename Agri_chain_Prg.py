#Problem 1:
#Program for following:
#Given a string, find the length of the longest substring without repeating characters. For example, the
#longest substring without repeating letters for "abcabcbb" is "abc", for which the length is 3. For
#"bbbbb" the longest substring is "b", with the length of 1

#Solution - 

def find_longest_unique_substring_length(input_string: str) -> int:
    char_last_seen_at = {}         
    substring_start_index = 0      
    max_length = 0                 

    for current_index, current_char in enumerate(input_string):
        # The character is exist and inside the current substring window
        if current_char in char_last_seen_at and char_last_seen_at[current_char] >= substring_start_index:
            # to avoid duplicates chars
            substring_start_index = char_last_seen_at[current_char] + 1

        # Update the last seen index of the current character
        char_last_seen_at[current_char] = current_index

        # Calculate the length of the current substring window
        current_length = current_index - substring_start_index + 1

        # Update max_length if the current window is longer than all previously found windows
        max_length = max(max_length, current_length)

    return max_length

#Examples of Usage
print(find_longest_unique_substring_length("abcabcbb"))  # Output: 3
print(find_longest_unique_substring_length("bbbbb"))     # Output: 1



#Problem 2:
#Assume there is a website https://agrichain.com which does exactly the same thing as
#problem 1, it takes the input on home page and then on click of submit button, it navigates to
#different page where it prints the output for longest substring without repeating letters.

#Solution by using pytest

##home_page.py`

from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.input_field = (By.ID, "inputString")     # Locator for input field
        self.submit_button = (By.ID, "submitButton")  # Locator for submit button

    def enter_input(self, text):
        self.driver.find_element(*self.input_field).clear()      # Clear any existing input
        self.driver.find_element(*self.input_field).send_keys(text)  # Enter the input text

    def click_submit(self):
        self.driver.find_element(*self.submit_button).click()  # Click the submit button

## result_page.py
from selenium.webdriver.common.by import By

class ResultPage:
    def __init__(self, driver):
        self.driver = driver
        self.result_text = (By.ID, "result")  # Locator for the result element

    def get_result(self):
        return self.driver.find_element(*self.result_text).text  # Return the result text from the page

## main.py

from selenium import webdriver
from pages.home_page import HomePage
from pages.result_page import ResultPage
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_longest_substring():
    options = Options()
    options.add_argument("--start-maximized")  # Start browser maximized
    service = Service()  # You can specify path to chromedriver here if needed

    driver = webdriver.Chrome(service=service, options=options)  # Launch Chrome browser
    driver.get("https://agrichain.com")  # Open the website

    home = HomePage(driver)  # Create HomePage object
    home.enter_input("abcabcbb")  # Enter test string
    home.click_submit()  # Submit the input

    # Wait until result is visible on result page (maximum wait: 10 seconds)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "result")))

    result = ResultPage(driver)  # Create ResultPage object
    output = result.get_result()  # Get the output string from the page
    print("Output from agrichain.com:", output)  # Print the result

    driver.quit()  # Close the browser window

# Run the test
test_longest_substring()

