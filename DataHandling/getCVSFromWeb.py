from bs4 import BeautifulSoup
import csv

with open('data.txt', 'r', encoding='utf-8') as file:
    actual_file_content = file.read()

soup = BeautifulSoup(actual_file_content, 'html.parser')

data_rows = []
for row in soup.find_all('tr'):
    cells = row.find_all('td')
    if not cells:
        cells = row.find_all('th')
    if cells:
        first_cell_text = cells[0].get_text(strip=True)
        if "Total" in first_cell_text:
            parts = first_cell_text.split()
            year = parts[0]
            row_data = [year, "Total"] + [cell.get_text(strip=True) for cell in cells[1:4]]
        elif "% Chg over" in first_cell_text:
            parts = first_cell_text.split()
            year = parts[-1]
            row_data = ["% Chg over", year] + [cell.get_text(strip=True) for cell in cells[1:4]]
        else:
            row_data = [cell.get_text(strip=True) for cell in cells[:5]]
        data_rows.append(row_data)

csv_file_path = 'dataset1.csv'
with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    for row in data_rows:
        writer.writerow(row)
