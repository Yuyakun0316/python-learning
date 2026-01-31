import os
import fitz 
import openpyxl

def extract_information_from_pdf(pdf_path, filename):
    doc = fitz.open(pdf_path)

    extracted_date = {
        "ファイル名": filename.replace('.pdf', ''),
        "件名": "",
        "請求日": "",
        "請求金額": "",
        "お支払い期限": "",
        "振込先": ""
    }

    for page in doc:
        text = page.get_text()
        lines = text.split('\n')
        for i, line in enumerate(lines):
            if 'ご請求金額' in line and i+1 < len(lines):
                extracted_date["請求金額"] = ''.join(filter(str.isdigit, lines[i+1].strip()))
            elif 'お支払い期限' in line and i+1 < len(lines):
                extracted_date["お支払い期限"] = lines[i+1].strip()
            elif '振込先' in line:
                transfer_info = lines[i+1].strip() if i+1 < len(lines) else ''
                transfer_info += ' ' + lines[i+2].strip() if i+2 < len(lines) else ''
                extracted_date["振込先"] = transfer_info
            elif '件名' in line and i+1 <len(lines):
                extracted_date["件名"] = lines[i+1].strip()
            elif '請求日' in line:
                extracted_date["請求日"] = lines[i+1].strip()
    return extracted_date

def write_information_to_excel(all_extracted_data, excel_path):
    """抽出した情報をExcelファイルに書き出す"""
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(["ファイル名", "件名", "請求日", "請求金額", "お支払い期限", "振込先"])
    for data in all_extracted_data:
        ws.append([
            data["ファイル名"],
            data["件名"],
            data["請求日"],
            data["請求金額"],
            data["お支払い期限"],
            data["振込先"]
        ])
    wb.save(excel_path)

directory_path = '.'
excel_path = 'invoice_data.xlsx'

all_extracted_data = []

for filename in os.listdir(directory_path):
    if filename.endswith('.pdf'):
        pdf_path = os.path.join(directory_path, filename)
        extracted_data = extract_information_from_pdf(pdf_path, filename)
        all_extracted_data.append(extracted_data)

write_information_to_excel(all_extracted_data, excel_path)

print("情報の抽出とExcelへの書き出しが完了しました。")