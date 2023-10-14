from excel_sheet import wb_data


excel_file_path = r'C:\Users\leoba\PycharmProjects\manuscript_solution_test_case\data.xlsx'
sheet_titles = {
    'ID_TOVAR': 0,
    'TOVAR': 1,
    'ID_ISG': 2,
    'ISG': 3,
    'COUNTRY': 4,
    'BARCODE': 5
}


def form_isg_table_rows(data):
    table_rows = []
    for row in data:
        table_rows.append((row[sheet_titles['ID_ISG']], row[sheet_titles['ISG']]))

    return table_rows


def form_country_table_rows(data):
    table_rows = []
    for row in data:
        table_rows.append(row[sheet_titles['COUNTRY']])

    return table_rows


def generate_barcode(row):
    try:
        barcode = row[sheet_titles['BARCODE']]
    except IndexError:
        barcode = None

    return barcode


isg_table_rows = list(set(form_isg_table_rows(wb_data)))
country_table_rows = list(set(form_country_table_rows(wb_data)))

if __name__ == '__main__':
    print(len(country_table_rows))
