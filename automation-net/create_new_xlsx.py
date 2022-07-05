import openpyxl
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "Data"

ws.append(['Hostname', 'Model'])

wb.save('test.xlsx')