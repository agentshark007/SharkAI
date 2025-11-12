from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def generate(iterations):
    print("Loading website...")

    driver = webdriver.Safari()
    driver.get("https://baturin.org/tools/bnfgen/")
    time.sleep(0.5)

    print("Website loaded.")

    def generate_single():
        driver.find_element(By.CSS_SELECTOR, 'input[value="Generate"]').click()
        time.sleep(0.1)
        return driver.find_element(By.ID, "output").text

    print("Generating...")

    output = ""
    for _ in range(iterations):
        print(f"Iteration {_ + 1}/{iterations}")
        output += generate_single()

    print("Done generating.")

    driver.quit()
    return output

if __name__ == "__main__":
    result = generate(5000)
    print(result)
    with open("data_retreived.txt", "w") as file:
        file.write(result)
