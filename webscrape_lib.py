
import json
import time
import pandas as pd
from datetime import date
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def webscr(url, start_time):
    options = Options()
    options.headless = False

    if options.headless == True:
        print ("Headless Chrome Initialized on Linux")
        options.add_argument('--disable-gpu')
    else:
        pass
    print('headless')
    print(time.time() - start_time)

    # chrome_driver = r"C:\Users\User\Documents\virtual\webscsrape_indianoil\chromedriver.exe"

    # Opens url, options is for headless chrome
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    # driver = webdriver.Chrome(chrome_driver, options=options)
    driver.get(url)
    print('open url')
    print(time.time() - start_time)

    # Wait until all is loaded
    # cur = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.CLASS_NAME,'current-value')))

    print('webdriverwait')
    print(time.time() - start_time)
    # Grab the Contents
    content = driver.page_source
    soup = BeautifulSoup(content,features="html.parser")
    # print(soup.prettify())
    print('soup')
    print(time.time() - start_time)

    # Close the browser
    driver.close()
    print('driver close')
    print(time.time() - start_time)

    # Initialisation
    datey = date.today().strftime("%d/%b/%Y")            # Date of request
    print(datey)
    print(time.time() - start_time)


    # Scraping
    product_name = soup.find('h1',class_ = "module-pdp-title").get_text()
    print(product_name)
    print(time.time() - start_time)

    competitor_price = soup.find_all(class_="pre-inquiry-price")[-1].get_text()
    print(competitor_price)
    print(time.time() - start_time)

    # currency = soup.find_all('label',class_= "ellipsis")[-1].get_text().split(" - ")[-1]
    currency = 'USD'
    print(currency)
    print(time.time() - start_time)

    uom = soup.find_all('span',class_= "ma-quantity-range")[-1].get_text().split(" ")[-1]
    print(uom)

    comp_name = soup.find('a',class_ = "company-name company-name-lite-vb").get_text()
    print(comp_name)

    for item in soup.find_all('dl',class_ = "do-entry-item"):
        #print(item.get_text())

        if 'Place of Origin:' in item.get_text():
            country = item.get_text().split(':')[-1].split(", ")[-1]
            print(country)

        elif 'Model Number:' in item.get_text():
            grade = item.get_text().split(':')[-1].replace(' grade','')
            print(grade)

        elif 'Package:' in item.get_text():
            package = item.get_text().split(':')[-1].split('/')[0]
            print(package)

        elif 'Payment term:' in item.get_text():
            payment_term = item.get_text().split(':')[-1]
            print(payment_term)

        else:
            pass

    # Save to dataframe and excel
    # df = pd.DataFrame({
    #     'Product Name': [product_name],
    #     'Product Grade': [grade],
    #     'Company Name': [comp_name],
    #     'Country': [country],
    #     'Competitor price': [competitor_price],
    #     'Currency': [currency],
    #     'UOM': [uom],
    #     'Packaging': [package]
    #     })

    # df.to_excel('products1.xls', index=False, encoding='utf-8')
    # os.system("start EXCEL.EXE products1.xls")
    # df_json = json.loads(df.to_json(orient='records'))
    df_json = {
        'Product Name': [product_name],
        'Product Grade': [grade],
        'Company Name': [comp_name],
        'Country': [country],
        'Competitor price': [competitor_price],
        'Currency': [currency],
        'UOM': [uom],
        'Packaging': [package]
        }
    return df_json
