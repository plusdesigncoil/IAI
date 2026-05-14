
import openpyxl
import json

_PK = 0xBEEF

def encode_price(price):
    try:
        p = int(float(price))
        return p ^ _PK
    except:
        return 0

wb = openpyxl.load_workbook('IAI מחירון.xlsx', data_only=True)
ws = wb.active

categories = {}

# Skip header row
for row in ws.iter_rows(min_row=2, values_only=True):
    if not row or not any(row):
        continue
    
    main_cat_num = row[0]
    sub_cat_num = row[1]
    cat_name = row[2]
    product_name = row[3]
    unit = row[4]
    price = row[5]
    
    if not cat_name or not product_name:
        continue
        
    if cat_name not in categories:
        categories[cat_name] = []
    
    # Determine type
    ptype = "unit"
    if unit:
        if 'מ"ר' in unit:
            ptype = "sqm"
        elif 'מטר רץ' in unit or 'מ"א' in unit:
            ptype = "length"
        elif 'יום' in unit or 'שעה' in unit:
            ptype = "unit" # Treated as unit (price * qty)
    
    # Contract number
    contract = sub_cat_num if sub_cat_num else "X"
    
    categories[cat_name].append({
        "name": product_name,
        "contract": contract,
        "unit": unit if unit else "",
        "price": encode_price(price),
        "type": ptype
    })

# Format as JavaScript array
js_output = "const PRODUCTS = [\n"
for cat_name, items in categories.items():
    js_output += f'  {{ cat:"{cat_name}", items:[\n'
    for item in items:
        js_output += f'    {{ name:{json.dumps(item["name"], ensure_ascii=False)}, contract:{json.dumps(item["contract"])}, unit:{json.dumps(item["unit"], ensure_ascii=False)}, price:{item["price"]}, type:"{item["type"]}" }},\n'
    js_output += "  ]},\n"
js_output += "];"

if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    print(js_output)
