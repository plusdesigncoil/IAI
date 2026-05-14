
# Task Progress: Price List Update

## Completed Status (May 13, 2026)
- [x] Processed `IAI מחירון.xlsx` using Python script.
- [x] Updated `PRODUCTS` array in `index.html` with all 30 categories.
- [x] Updated XOR price encryption for all new items.
- [x] Synchronized `CATEGORY_RULES` for PDF parsing.
- [x] Synchronized `PG_EXCLUDED_NAMES` for auto-quote generation.
- [x] Updated `buildPdfReplacementQuote` to use new installer and design item names.
- [x] Added new product line `1.3 (ב)` (דגל בד סאטן 125X430) to both Excel and `index.html`.
- [x] Updated item `24.1` (קוליסת עץ): new description, unit set to `מ"ר`, and price set to `200`.



## Key Changes in Logic
- **New Item Names**: 
    - Design: `שעת גרפיקאי` (replaced `שעות עיצוב`)
    - Installation: `יום עבודה - מתקין מוסמך 1` and `יום עבודה - מתקין מוסמך 1 + עוזר`.
- **New Category Rules**: Updated regex patterns to map PDF descriptions to new catalog names (e.g., "מדבקת קיר" now maps to "וניל לבן טקסטורי - מחוספס").

## Future Updates
To update prices again:
1. Modify `IAI מחירון.xlsx`.
2. Run `python process_prices.py`.
3. Copy the output `const PRODUCTS` array into `index.html`.
