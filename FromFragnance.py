from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import re
from selenium.common.exceptions import NoSuchElementException
from urllib import request
import csv
from datetime import date
import os.path
from os import path

class GUI(Tk):
    def __init__(self):
        super(GUI,self).__init__()
        self.title("Fragnance")
        self.minsize(300,200)
        self.initUI()

    def clicked(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        element = ''

        driver = webdriver.Chrome('C:\Python\chromedriver.exe',options=options)
        siteID = self.siteid.get()
        gender = self.gender.get()
        type = self.type.get()
        print(self.siteid.get())
        if(self.siteid.get()=='Fragnancex'):
            if(not(os.path.isfile('products.csv'))):
                row = ['Prod_id','Prod_Brand','Prod_Name','Prod_Type', 'Gender', 'Category','Reg_Price','Disc_Price','Site_ID','Date','Image URL']
                with open('products.csv', 'a',newline='') as csvFile:
                    writer = csv.writer(csvFile)
                    writer.writerow(row)
                csvFile.close()
                
            driver.get('https://www.fragrancex.com')
            if(self.gender.get()=='Men'):
                men = driver.find_element_by_xpath('//*[@id="header"]/nav/div[1]/div[3]/div/div/ul[1]/li[3]/a')
                men.click()
            if(self.gender.get()=='Women'):
                women = driver.find_element_by_xpath('//*[@id="header"]/nav/div[1]/div[3]/div/div/ul[1]/li[2]/a')
                women.click()
            if(self.gender.get()=='Unisex'):
                driver.get('https://www.fragrancex.com/products/top_selling_perfumes.html')
                unisex = driver.find_element_by_xpath('//*[@id="gender_3"]')
                unisex.click()
            if(self.type.get()==''):
                if(self.gender.get()=='Men'):
                    type='Colonge'
                if(self.gender.get()=='Women'):
                    type='Perfume'
                
            if(self.type.get()=='Testers'):
                tester = driver.find_element_by_xpath('//*[@id="subcat_1"]')
                tester.click()
            if(self.type.get()=='Travel Minis'):
                travelMinis = driver.find_element_by_xpath('//*[@id="subcat_2"]')
                travelMinis.click()
            if(self.type.get()=='Samples'):
                samples = driver.find_element_by_xpath('//*[@id="subcat_3"]')
                samples.click()
            if(self.type.get()=='Gift Sets'):
                giftSets = driver.find_element_by_xpath('//*[@id="subcat_4"]')
                giftSets.click()
            if(self.type.get()=='Hard To Find'):
                hardToFind = driver.find_element_by_xpath('//*[@id="subcat_5"]')
                hardToFind.click()
            if(self.type.get()=='New Arrivals'):
                newArrivals = driver.find_element_by_xpath('//*[@id="subcat_6"]')
                newArrivals.click()
            if(self.type.get()=='Celebrity Scents'):
                celebrityScents = driver.find_element_by_xpath('//*[@id="subcat_7"]')
                celebrityScents.click()
            if(self.type.get()=='Body Lotion'):
                bodyLotion = driver.find_element_by_xpath('//*[@id="subcat_8"]')
                bodyLotion.click()
            if(self.type.get()=='Deodorant'):
                element = driver.find_element_by_xpath('//*[@id="SearchBlockAsyncForm"]/div/div/div/div/div/div/div[2]/div[2]/div[3]/div/div[23]/a')
                element.click()
                time.sleep(1)
                deodorant = driver.find_element_by_xpath('//*[@id="subcat_9"]')
                deodorant.click()
            if(self.type.get()=='After Shave'):
                element = driver.find_element_by_xpath('//*[@id="SearchBlockAsyncForm"]/div/div/div/div/div/div/div[2]/div[2]/div[3]/div/div[23]/a')
                element.click()
                time.sleep(1)
                afterShave = driver.find_element_by_xpath('//*[@id="subcat_10"]')
                afterShave.click()
            if(self.type.get()=='Shower Gel'):
                element = driver.find_element_by_xpath('//*[@id="SearchBlockAsyncForm"]/div/div/div/div/div/div/div[2]/div[2]/div[3]/div/div[23]/a')
                element.click()
                time.sleep(1)
                showerGel = driver.find_element_by_xpath('//*[@id="subcat_11"]')
                showerGel.click()
            if(self.type.get()=='After Shave Balm'):
                element = driver.find_element_by_xpath('//*[@id="SearchBlockAsyncForm"]/div/div/div/div/div/div/div[2]/div[2]/div[3]/div/div[23]/a')
                element.click()
                time.sleep(1)
                afterShaveBalm = driver.find_element_by_xpath('//*[@id="subcat_12"]')
                afterShaveBalm.click()
            if(self.type.get()=='Body Cream'):
                element = driver.find_element_by_xpath('//*[@id="SearchBlockAsyncForm"]/div/div/div/div/div/div/div[2]/div[2]/div[3]/div/div[23]/a')
                element.click()
                time.sleep(1)
                bodyCream = driver.find_element_by_xpath('//*[@id="subcat_13"]')
                bodyCream.click()
            if(self.type.get()=='Pure Perfume'):
                element = driver.find_element_by_xpath('//*[@id="SearchBlockAsyncForm"]/div/div/div/div/div/div/div[2]/div[2]/div[3]/div/div[23]/a')
                element.click()
                time.sleep(1)
                purePerfume = driver.find_element_by_xpath('//*[@id="subcat_14"]')
                purePerfume.click()
            if(self.type.get()=='Body Powder'):
                element = driver.find_element_by_xpath('//*[@id="SearchBlockAsyncForm"]/div/div/div/div/div/div/div[2]/div[2]/div[3]/div/div[23]/a')
                element.click()
                time.sleep(1)
                bodyPowder = driver.find_element_by_xpath('//*[@id="subcat_15"]')
                bodyPowder.click()
            if(self.type.get()=='Soap'):
                element = driver.find_element_by_xpath('//*[@id="SearchBlockAsyncForm"]/div/div/div/div/div/div/div[2]/div[2]/div[3]/div/div[23]/a')
                element.click()
                time.sleep(1)
                soap = driver.find_element_by_xpath('//*[@id="subcat_16"]')
                soap.click()
            if(self.type.get()=='Bath Oil'):
                element = driver.find_element_by_xpath('//*[@id="SearchBlockAsyncForm"]/div/div/div/div/div/div/div[2]/div[2]/div[3]/div/div[23]/a')
                element.click()
                time.sleep(1)
                bathOil = driver.find_element_by_xpath('//*[@id="subcat_17"]')
                bathOil.click()
            if(self.type.get()=='Accessories'):
                element = driver.find_element_by_xpath('//*[@id="SearchBlockAsyncForm"]/div/div/div/div/div/div/div[2]/div[2]/div[3]/div/div[23]/a')
                element.click()
                time.sleep(1)
                accessories = driver.find_element_by_xpath('//*[@id="subcat_18"]')
                accessories.click()
            if(self.type.get()=='Talc'):
                element = driver.find_element_by_xpath('//*[@id="SearchBlockAsyncForm"]/div/div/div/div/div/div/div[2]/div[2]/div[3]/div/div[23]/a')
                element.click()
                time.sleep(1)
                talc = driver.find_element_by_xpath('//*[@id="subcat_19"]')
                talc.click()
            if(self.type.get()=='Solid Perfume'):
                element = driver.find_element_by_xpath('//*[@id="SearchBlockAsyncForm"]/div/div/div/div/div/div/div[2]/div[2]/div[3]/div/div[23]/a')
                element.click()
                time.sleep(1)
                solidPerfume = driver.find_element_by_xpath('//*[@id="subcat_20"]')
                solidPerfume.click()
                driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
                time.sleep(1)
            if(self.type.get()=='Shampoo'):
                element = driver.find_element_by_xpath('//*[@id="SearchBlockAsyncForm"]/div/div/div/div/div/div/div[2]/div[2]/div[3]/div/div[23]/a')
                element.click()
                time.sleep(1)
                shampoo = driver.find_element_by_xpath('//*[@id="subcat_21"]')
                shampoo.click()
                driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
                time.sleep(1)
            if(self.type.get()=='Candles'):
                element = driver.find_element_by_xpath('//*[@id="SearchBlockAsyncForm"]/div/div/div/div/div/div/div[2]/div[2]/div[3]/div/div[23]/a')
                element.click()
                time.sleep(1)
                candles = driver.find_element_by_xpath('//*[@id="subcat_22"]')
                candles.click()
                driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
                time.sleep(1)
            time.sleep(2)

            element = driver.find_element_by_xpath('//*[@id="SearchBlockAsyncForm"]/div/div/div/div/div/div/div[1]/div[1]')
            text = element.text
            print(text)
            if(text[0]=='0'):
                self.exit()
            text = text.split()
            results = text[4]
            results = int(results)
            print(results)
            l=1
            time.sleep(2)
            for i in range(1,results+1):
                print('Value of l is '+str(l))
                time.sleep(2)
                element = driver.find_element_by_xpath('//*[@id="search_result_content"]/div[2]/div/div['+str(l)+']/p[1]/span[1]/span/a')
                brand = element.text
                print(brand)
                element = driver.find_element_by_xpath('//*[@id="search_result_content"]/div[2]/div/div['+str(l)+']/h2/a[2]/span')
                productname = element.text
                element.click()
                time.sleep(2)
                count = driver.find_elements_by_xpath('//*[@id="products_page"]/div/section/div/div/div/div[2]/div/ul/li')
                print('The number of elements in the list are'+str(len(count))) 
                j=1
                while j<len(count)+1:
                    try:
                        print('Value of j in loop is '+str(j))
                        element = driver.find_element_by_xpath('//*[@id="products_page"]/div/section/div/div/div/div[2]/div/ul/li['+str(j)+']/div[1]/ul/li/div/div[2]/div[1]/h2')
                        productType = element.text
                        element = driver.find_element_by_xpath('//*[@id="products_page"]/div/section/div/div/div/div[2]/div/ul/li['+str(j)+']/div[1]/ul/li/div/div[2]/div[1]/p')
                        productId = element.text
                        productId = productId.split()
                        productId = productId[1]
                        productId = productId[1:]
                        src = driver.current_url
                        time.sleep(1)
                        element = driver.find_element_by_xpath('//*[@id="products_page"]/div/section/div/div/div/div[2]/div/ul/li['+str(j)+']/div[1]/ul/li/div/div[2]/div[2]/a')
                        element.click()
                        time.sleep(2)
                        element = driver.find_element_by_xpath('//*[@id="CartQuantityAsyncForm"]/table/tbody/tr/td[1]/div/div/h2/a')
                        description = element.text
                        element = driver.find_element_by_xpath('//*[@id="CartQuantityAsyncForm"]/table/tbody/tr/td[2]/div[2]')
                        regularPrice = element.text
                        element = driver.find_element_by_xpath('//*[@id="CartQuantityAsyncForm"]/table/tbody/tr/td[2]/div[4]')
                        aftercouponprice = element.text
                        element = driver.find_element_by_xpath('//*[@id="CartQuantityAsyncForm"]/table/tbody/tr/td[1]/div/a/div/img')
                        element = driver.find_element_by_xpath('//*[@id="CartQuantityAsyncForm"]/table/tbody/tr/td[1]/div/div/a')
                        element.click()
                        today = str(date.today())
                        row = [productId,brand,productname,productType,gender,type, regularPrice, aftercouponprice,siteID,today,src]
                        with open('products.csv', 'a',newline='') as csvFile:
                            writer = csv.writer(csvFile)
                            writer.writerow(row)
                        csvFile.close()
                        time.sleep(2)
                        driver.execute_script("window.history.go(-1)")
                        j+=1
                    except NoSuchElementException as n:
                        print('Value of j after exception '+str(j))
                        print('Please check your internet connection')
                    except Exception as e :
                        print('Your internet Connection is either blocked or not working')

                time.sleep(2)
                driver.execute_script("window.history.go(-1)")
                time.sleep(2)
                print('go back')
                if(l%40==0):
                    element = driver.find_element_by_xpath('//*[@id="search_result_content"]/div[3]/div/div/div/div/a')
                    element.click()
                    l=0
                    time.sleep(2)
                l = l+1
                    
        print('You have successfully Scraped all data')
            

            


    def initUI(self):
        self.siteid = StringVar()
        self.combobox = ttk.Combobox(self,state="readonly",width=15,textvariable=self.siteid)
        self.combobox['values']= ('Fragnancex')
        self.combobox.grid(column=1,row=1)
        self.label = ttk.Label(self,text="Select your Site ID")
        self.label.grid(column=0,row=1)
        self.combobox.current(0)

        self.gender = StringVar()
        self.combobox = ttk.Combobox(self,state="readonly",width=15,textvariable=self.gender)
        self.combobox['values']= ('Men','Women','Unisex')
        self.combobox.grid(column=1,row=2)
        self.label = ttk.Label(self,text="Select your gender category")
        self.label.grid(column=0,row=2)
        self.combobox.current(0)

        self.type = StringVar()
        self.combo2 = ttk.Combobox(self,state="readonly",width=15,textvariable=self.type)
        self.combo2['values']= ('Testers','Travel Minis','Samples','Gift Sets','Hard To Find','New Arrivals','Celebrity Scents','Body Lotion','Deodorant','After Shave','Shower Gel','After Shave Balm','Body Cream','Pure Perfume','Body Powder','Soap','Bath Oil','Accessories','Talc','Solid Perfume','Shampoo','Candles')
        self.combo2.grid(column=1,row=3)
        self.label = ttk.Label(self,text="Select your type category")
        self.label.grid(column=0,row=3)

        self.button = ttk.Button(self,text="Start",command= self.clicked)
        self.button.grid(column=1,row=4)

    def exit(self):
        print('No any results found')
        exit()

     
    


if __name__ == '__main__':
    wind = GUI()
    wind.mainloop()
