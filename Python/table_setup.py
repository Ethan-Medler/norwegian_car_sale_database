Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import sqlite3, os
>>> os.chdir(r"C:\Users\ebmed\Documents\Car Sale Dataset")
>>> con = sqlite3.connect(r"C:\Users\ebmed\Documents\Car Sale Dataset\carsalesdatabase.db")
>>> cur = con.cursor()
>>> from create_table import tablecreator
>>> tablecreator(r"C:\Users\ebmed\Documents\Car Sale Dataset\car_sales_make.xlsx")
Please provide the table name here: car_make
CREATE TABLE car_make(Year real, Month real, Make text, Quantity real, Pct real)
>>> tablecreator(r"C:\Users\ebmed\Documents\Car Sale Dataset\car_sales_model.xlsx")
Please provide the table name here: car_model
CREATE TABLE car_model(Year real, Month real, Make text, Model text, Quantity real, Pct real)
>>> tablecreator(r"C:\Users\ebmed\Documents\Car Sale Dataset\car_sales_month.xlsx")
Please provide the table name here: car_month
CREATE TABLE car_month(Year real, Month real, Quantity real, Quantity_YoY real, Import real, Import_YoY real, Used text, Used_YoY text, Avg_CO2 real, Bensin_Co2 real, Diesel_Co2 real, Quantity_Diesel real, Diesel_Share real, Diesel_Share_LY real, Quantity_Hybrid text, Quantity_Electric text, Import_Electric text)
>>> 