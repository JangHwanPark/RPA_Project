from openpyxl import Workbook
wb = Workbook() # 새로운 워크북 생성
ws = wb.active # 현재 활성화된 시트 가져옴
ws.title = "NadoSheet" # sheet의 이름 변경
wb.save("sample.xlsx")
wb.close()