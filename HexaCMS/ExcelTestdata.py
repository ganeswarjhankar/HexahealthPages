from selenium import webdriver
import openpyxl

#open the excel file
workbook=openpyxl.load_workbook("path")
sheet=workbook["Sheet_Doctor"]
total_rows=sheet.max_row

for row in range(2,total_rows+1):
    pass

