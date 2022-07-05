from openpyxl import Workbook, load_workbook

wb = load_workbook('test.xlsx')
ws = wb.active


wb.save('test.xlsx')