
#from webscrape_lib import webscr

import json
import time
import xlwt
import pickle
import numpy as np
import pandas as pd
from datetime import date
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

start_time = time.time()

# Get URL from JSON file
f = open('input.json',)
data = json.load(f)
url = data.get('url')
url

#def webscr1(url, start_time):
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

# Initialisation
company = []
links = []

# GET THE SOUP - (GRAB THE CONTENTS)
for i in range(25):
    print(f"Count {i}")

    content = driver.page_source
    soup = BeautifulSoup(content,features="html.parser")

    # COLLECT URLS

    items = soup.find_all('div', class_ ='sabai-directory-title')
    len(items)
    items[0].find('a')['title']

    for item in items:
        links.append(item.find('a')['href'])
        company.append(item.find('a')['title'])

    # GO TO NEXT PAGE
    time.sleep(3)
    elem=driver.find_element_by_class_name("sabai-pagination.sabai-btn-group")
    b=elem.find_elements_by_tag_name('a')

    b[-1].click()

# Close the browser
driver.close()
links = links[30:] # origial list has double copy of first page
company = company[30:]

links.remove('https://team.org.my/directory/listing/classics-living-furniture-m-sdn-bhd')


ind1 = links.index('https://team.org.my/directory/listing/classics-living-furniture-m-sdn-bhd')
del(links[ind1])
del(company[ind1])

ind2 = links.index('https://team.org.my/directory/listing/durga-timber-traders')
del(links[ind2])
del(company[ind2])

ind3 = links.index('https://team.org.my/directory/listing/foretask-resources-sdn-bhd')
del(links[ind3])
del(company[ind3])

ind4 = links.index('https://team.org.my/directory/listing/heseh-wood-sdn-bhd-1')
del(links[ind4])
del(company[ind4])

ind5 = links.index('https://team.org.my/directory/listing/hi-mac-resources-sdn-bhd')
del(links[ind5])
del(company[ind5])

ind6 = links.index('https://team.org.my/directory/listing/jq-timber-sdn-bhd')
del(links[ind6])
del(company[ind6])

ind7 = links.index('https://team.org.my/directory/listing/k-l-sumber-sejati-enterprise')
del(links[ind7])
del(company[ind7])

ind7 = links.index('https://team.org.my/directory/listing/ka-solution-sdn-bhd')
del(links[ind7])
del(company[ind7])

ind8 = links.index('https://team.org.my/directory/listing/kian-seng-timber-sdn-bhd-1')
del(links[ind8])
del(company[ind8])

ind9 = links.index('https://team.org.my/directory/listing/kihuat-timber-m-sdn-bhd-1')
del(links[ind9])
del(company[ind9])

ind10 = links.index('https://team.org.my/directory/listing/mammoet-romstar-sdn-bhd')
del(links[ind10])
del(company[ind10])

ind11 = links.index('https://team.org.my/directory/listing/medan-agresif-sdn-bhd-1')
del(links[ind11])
del(company[ind11])

ind12 = links.index('https://team.org.my/directory/listing/n-j-international-sdn-bhd-1')
del(links[ind12])
del(company[ind12])

ind13 = links.index('https://team.org.my/directory/listing/n-s-landmark-m-sdn-bhd')
del(links[ind13])
del(company[ind13])

ind14 = links.index('https://team.org.my/directory/listing/prent-malaysia-sdn-bhd')
del(links[ind14])
del(company[ind14])

ind15 = links.index('https://team.org.my/directory/listing/r-jie-wood-trading')
del(links[ind15])
del(company[ind15])

ind16 = links.index('https://team.org.my/directory/listing/samudaya-phita-enterprise')
del(links[ind16])
del(company[ind16])

ind17 = links.index('https://team.org.my/directory/listing/se-agro-industries-sdn-bhd')
del(links[ind17])
del(company[ind17])

ind18 = links.index('https://team.org.my/directory/listing/shen-foong-trading-sdn-bhd-1')
del(links[ind18])
del(company[ind18])

ind19 = links.index('https://team.org.my/directory/listing/sukana-jaya-sdn-bhd-1')
del(links[ind19])
del(company[ind19])

ind20 = links.index('https://team.org.my/directory/listing/thiam-bee-timber-processing-sdn-bhd')
del(links[ind20])
del(company[ind20])



len(links)
len(company)


with open('test.pickle', 'wb') as f:
    pickle.dump([links, company], f)


with open('test.pickle', 'rb') as f:
    links,company = pickle.load(f)


# SCRAPING SUB-LINKS ###################

options = Options()
options.headless = True

if options.headless == True:
    print ("Headless Chrome Initialized on Linux")
    options.add_argument('--disable-gpu')
else:
    pass

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)


n_list = np.arange(630,700,30).tolist()
n_list

for n in n_list:

    # INITIALISATION
    i=0
    address = []
    telephone = []
    email = []
    city = []
    contact_person = []
    memberID = []
    postcode = []
    state = []
    #url1 = links[0]

    url1 = 'https://team.org.my/directory/listing/kihuat-timber-m-sdn-bhd-1'


    for url1 in links[n:n+30]:
        print('========================================================\n')
        #print(f"URL{i}")
        print(url1)
        #time.sleep(2)
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        driver.get(url1)

        content1 = driver.page_source
        soup1 = BeautifulSoup(content1,features="html.parser")
        #print(soup1.prettify())
        driver.close()

        subdir_contact = soup1.find('div', {"class" :"sabai-directory-contact"})
        #telephone.append('-')
        #email.append('-')

        telephone.append(subdir_contact.find('span',{"class" :"sabai-hidden-xs"}).text)
        email.append(subdir_contact.find('div',{"class" :"sabai-directory-contact-email"}).text)


        # print(soup.find('div',class_ ='postcontent').text)
        subdir_field = soup1.find('div', {"class" :'sabai-directory-custom-fields'})
        #print(subdir_field.prettify())


        labels = subdir_field.find_all('div', {"class":"sabai-field-label"})
        values = subdir_field.find_all('div', {"class":"sabai-field-value"})
        labels[0].text

        df = pd.DataFrame([[a.text,b.text] for a,b in zip(labels,values)])
        df.columns = ['Key','Value']

        # Changing all keys with address to 'Address'
        df.loc[df['Key'].str.contains('Address'), 'Key'] = 'Address'

        combined_df = df.groupby(['Key'], as_index = False).agg({'Value': ' '.join})

        MID = '-'
        ADD = '-'
        CT = '-'
        CON = '-'
        POST = '-'
        ST = '-'
        memberID.append('-')
        address.append('-')
        city.append('-')
        contact_person.append('-')
        postcode.append('-')
        state.append('-')

        for _, row in combined_df.iterrows():
            #print(index)
            #print(row['Key'])
            #print(row['Value'])

            if "Member ID" in row['Key']:
                #memberID.append(row['Value'])
                memberID[-1] = row['Value']
                print(f"Member{len(memberID)}")

            elif "Address" in row['Key']:
                #address.append(row['Value'])
                address[-1] = row['Value']
                print(f"Address{len(address)}")

            elif "City" in row['Key']:
                #city.append(row['Value'])
                city[-1] = row['Value']
                print(f"City{len(city)}")

            elif "Contact Person" in row['Key']:
                #contact_person.append(row['Value'])
                contact_person[-1] = row['Value']
                print(f"contact person{len(contact_person)}")

            elif "Postcode" in row['Key']:
                #postcode.append(row['Value'])
                postcode[-1] = row['Value']
                print(f"postcode{len(postcode)}")

            elif "State" in row['Key']:
                #state.append(row['Value'])
                state[-1] = row['Value']
                print(f"state{len(state)}")

            else:
                pass

        i+=1


    len(address)
    len(email)
    len(contact_person)
    len(company[n:n+30])
    len(links[n:n+30])
    len(state)
    len(postcode)
    len(telephone)
    len(city)


    df_ex = pd.DataFrame({
    'Company': company[n:n+30],
    'Contact Person': contact_person,
    'E-mail': email,
    'Telephone': telephone,
    'Address': address,
    'City':city,
    'Postcode':postcode,
    'State': state,
    'URL': links[n:n+30]
    #'url':links
    })#, 'Product Keyword': searched_keyword})



    df_ex.to_excel(f'timber{int(n/30 +1)}.xls', index=False, encoding='utf-8')
#retJson = webscr1(url, start_time)
#print(retJson)
