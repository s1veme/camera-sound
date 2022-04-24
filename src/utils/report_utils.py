import xlsxwriter


class GenerateReport:
    def __init__(self, path: str) -> None:
        self.path = path
        self.workbook = None
        self.worksheet = None

    def generate_report(self, data: dict) -> str:
        self._create_file()
        # self._fill_worksheet(data)
        self.__test_fill_worksheet(data, 50)  # Do not use it in production
        self.workbook.close()

        return self.path

    def _create_file(self) -> None:
        self.workbook = xlsxwriter.Workbook(self.path)
        self.worksheet = self.workbook.add_worksheet()

    def _fill_worksheet(self, data: dict) -> None:
        row = 0
        col = 0

        for title, value in data.items():
            self.worksheet.write(row, col, title)
            if isinstance(value, str):
                self.worksheet.write(row + 1, col, value)
            if isinstance(value, list):
                for item in value:
                    self.worksheet.write(row + 1, col, item)
                    row += 1
            row = 0
            col += 1

    def __test_fill_worksheet(self, data: dict, limit: int = 50) -> None:
        """ This function is needed only for tests. Do not use it in production """
        row = 0
        col = 0

        for title, value in data.items():
            self.worksheet.write(row, col, title)
            if isinstance(value, str):
                for _ in range(limit):
                    self.worksheet.write(row + 1, col, value)
                    row += 1
            row = 0
            col += 1
