import openpyxl

class MyOpen:
    def __init__(self, path, access_attr="r"):
        self.file = openpyxl.load_workbook("1.xlsx")

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.save()




