from openpyxl import Workbook


class DataStorageFile(Workbook):

    def __init__(self, file_name):
        super().__init__()
        self.file_name = file_name
        self.worksheet = self.active

        self.worksheet.append(
            [
                'num',
                'product_name',
                'product_category',
                'product_price',
                'product_rating',
                'product_reviews_number',
                'product_specs',
                'url'
            ]
        )

    def add_data(self, row_data):
        self.worksheet.append(row_data)
        self.save(self.file_name)
