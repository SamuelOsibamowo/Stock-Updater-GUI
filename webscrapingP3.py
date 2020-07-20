from tkinter import *
from selenium import webdriver
import smtplib


root = Tk()

stock_name = ''
price = ''
watchlist = {'UAVS': '3.28', 'NFLX': '492.9'}
search = Entry(root)
search.pack()


def the_click():
    global price
    #Grabs the URL and the path so selenium can use chrome
    URL = ("http://thestockmarketwatch.com/stock/?stock=" + search.get())
    PATH = "C:\Program Files (x86)\chromedriver.exe"

    #Prevents Selenium from opening a chrome tab
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    driver = webdriver.Chrome(PATH,options=op)
    driver.get(URL)

    #searches for the stock price and captures it
    bob = driver.find_element_by_id("divPrice")
    price = (bob.text[:5])
    Label_1 = Label(root,text= search.get() + " Stock Price = " + price)
    Label_1.pack()


def the_watchlist():
    watch_Label0 = Label(root, text = 'Watchlist')
    watch_Label0.pack()
    for x in watchlist:
        watch_Label = Label(root,text= x + ' ' + watchlist[x])
        watch_Label.pack()

def check_stock():
    for x in watchlist:
        old_price = watchlist[x]
        global price
        global stock_name
        #Grabs the URL and the path so selenium can use chrome
        URL = ("http://thestockmarketwatch.com/stock/?stock=" + x)
        PATH = "C:\Program Files (x86)\chromedriver.exe"

        #Prevents Selenium from opening a chrome tab
        op = webdriver.ChromeOptions()
        op.add_argument('headless')
        driver = webdriver.Chrome(PATH,options=op)
        driver.get(URL)

        #searches for the stock price and captures it
        bob = driver.find_element_by_id("divPrice")
        price = (bob.text[:5])
        
        if float(price) < float(old_price) * 0.7:
            stock_name = x
            send_email()


def send_email():
    content = "The stock price is below 30 percent for " + stock_name
    email = smtplib.SMTP('smtp.gmail.com',587)
    email.ehlo()
    email.starttls()
    email.login('samuelosibamowo2@gmail.com', 'Ademitope39')
    email.sendmail('samuelosibamowo2@gmail.com', 'samuelosibamowo@gmail.com', content)
    email.quit()



search_button = Button(root, text="search", command = the_click, bg='gray')
search_button.pack()
watchlist_button = Button(root, text="View Watchlist", command= the_watchlist, bg='gray')
watchlist_button.pack()

check_stock()
root.mainloop()






