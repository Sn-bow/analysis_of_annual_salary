import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import time
import re

load_dotenv()
URL = os.environ.get("START_URL")

# webdriver & driver url contect
driver = webdriver.Chrome()
driver.get(url=URL)

data_dic = {
    "id": [],
    "Major" : [],
    "Degree Type": [],
    "Early Career Pay": [],
    "Mid-Career Pay": [],
    "High Meaning %": []
}

money = pd.DataFrame(data_dic)
print(money)


while True:
    # BeautifulSoup & requests
    source = driver.page_source
    soup = BeautifulSoup(source, 'html.parser')
    # data 수집
    for el in soup.select(".data-table__row"):

        rank_data = re.findall("\d+[M]"," ".join(el.get_text().split("Rank:")))[0].replace("M", "")
        major_data = el.get_text().split("Degree Type:")[0].split("Rank:")[1].split("Major:")[1]
        degree_type_data = el.get_text().split("Early Career Pay:")[0].split("Degree Type:")[1]
        early_career_pay_data = el.get_text().split("Mid-Career Pay:")[0].split("Early Career Pay:$")[1]
        mid_career_pay_data = el.get_text().split("% High Meaning:")[0].split("Mid-Career Pay:$")[1]
        # 해당 부분 수정 필요 [] 로 감싸져서 나옴
        persent_high_meaning_data = "".join(re.findall("\d+",el.get_text().split("% High Meaning:")[1]))
        
        data_dic["id"].append(rank_data)
        data_dic["Major"].append(major_data)
        data_dic["Degree Type"].append(degree_type_data)
        data_dic["Early Career Pay"].append(early_career_pay_data)
        data_dic["Mid-Career Pay"].append(mid_career_pay_data)
        data_dic["High Meaning %"].append(persent_high_meaning_data)

    # page check
    page_num = driver.find_element(by="class name", value="pagination__btn--active")
    if page_num.text == "34" :
        break

    
    # next page click
    next_page_button = driver.find_element(by="class name", value="pagination__next-btn")
    next_page_button.click()
    time.sleep(2)

    


# csv file
major_early_df = pd.DataFrame(data_dic)
major_early_df.to_csv("./static/data/major_early_data.csv")
print(major_early_df)