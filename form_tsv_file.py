from database import quantity_by_countries


def create_tsv_file():
    with open('data.tsv', 'w', encoding='utf-8') as file:
        for query in quantity_by_countries:
            file.write(f'{query[0]} - {query[1]}\n')


if __name__ == '__main__':
    create_tsv_file()
