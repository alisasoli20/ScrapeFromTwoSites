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
        print('clicked')

    def initUI(self):
        self.siteid = StringVar()
        self.combobox = ttk.Combobox(self,state="readonly",width=15,textvariable=self.siteid)
        self.combobox['values']= ('fragrancenet')
        self.combobox.grid(column=1,row=1)
        self.label = ttk.Label(self,text="Select your Site ID")
        self.label.grid(column=0,row=1)
        self.combobox.current(0)

        self.gender = StringVar()
        self.combobox = ttk.Combobox(self,state="readonly",width=15,textvariable=self.gender)
        self.combobox['values']= ('Women','Men','Shop')
        self.combobox.grid(column=1,row=2)
        self.label = ttk.Label(self,text="Select category")
        self.label.grid(column=0,row=2)
        self.combobox.current(0)

        if(self.gender.get()=='Women'):
            print(self.gender.get())
            self.womenType = StringVar()
            self.combo2 = ttk.Combobox(self,state="readonly",width=15,textvariable=self.womenType)
            self.combo2['values']= ('Perfume','Bath & Body')
            self.combo2.grid(column=1,row=3)
            self.label = ttk.Label(self,text="Select sub category")
            self.label.grid(column=0,row=3)
            self.combo2.current(0)
            self.combo2.bind('<<ComboboxSelected>>', lambda event:self.callback)

        self.button = ttk.Button(self,text="Start",command= self.clicked)
        self.button.grid(column=1,row=4)

        def callback(self,eventObject):
            print('--- callback ---')

if __name__ == '__main__':
    wind = GUI()
    wind.mainloop()
