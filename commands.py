    #     self.Home_btn.clicked.connect(self.showHomePage)
    #     self.Models_btn.clicked.connect(self.showModelsPage)
    #     self.Forecasting_btn.clicked.connect(self.showForecastingPage)
    #     self.Datasets_btn.clicked.connect(self.showDatasetsPage)

    # def showHomePage(self):
    #     self.stackedWidget.setCurrentIndex(0)  # Index of the home page in the stacked widget

    # def showModelsPage(self):
    #     self.stackedWidget.setCurrentIndex(1)  # Index of the models page in the stacked widget

    # def showForecastingPage(self):
    #     self.stackedWidget.setCurrentIndex(3)  # Index of the forecasting page in the stacked widget

    # def showDatasetsPage(self):

    #     import sqlite3
    #     from PyQt5.QtWidgets import QTableWidgetItem
    #     self.stackedWidget.setCurrentIndex(2)  # Index of the datasets page in the stacked widget
    #     # Connect to the SQLite database
    #     conn = sqlite3.connect('Thesis_DB.db')
    #     cursor = conn.cursor()

    #     # Fetch regions from the database
    #     cursor.execute("SELECT name FROM Region")
    #     regions = cursor.fetchall()

    #     # Set the number of rows in the table
    #     num_rows = len(regions)
    #     num_columns = len(regions[0]) if regions else 0
    #     self.tableWidget.setRowCount(num_rows)
    #     self.tableWidget.setColumnCount(num_columns)

    #     # Populate the table with the regions
    #     for row, record in enumerate(regions):
    #         for col, value in enumerate(record):
    #             item = QtWidgets.QTableWidgetItem(str(value))
    #             self.tableWidget.setItem(row, col, item)

    #     # Adjust the table size to fit the contents
    #     self.tableWidget.resizeColumnsToContents()
    #     self.tableWidget.resizeRowsToContents()

print()
input()
type()
turtle()
len(y)




