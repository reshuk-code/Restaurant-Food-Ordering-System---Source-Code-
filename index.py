import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QComboBox, QSpinBox, QTextEdit, QTableWidget,
    QTableWidgetItem, QMessageBox, QTabWidget, QFileDialog
)
from PyQt5.QtGui import QFont, QFontDatabase, QIcon
from PyQt5.QtCore import Qt
import sqlite3
from datetime import date
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Constants
menu = {
    "Tea": 45,
    "Mo:mo": 120,
    "Mo:mo(Chicken)": 185,
    "Chowmin": 120,
    "Chowmin(Chicken)": 230,
    "Burger": 150,
    "Burger(Chicken)": 190,
    "Chicken Chilly": 270,
    "Thakali Khana(Set-Combo)": 365,
    "Extra Cheese": 80,
}
today_date = date.today()

# Database Setup
def setup_database():
    conn = sqlite3.connect("orders_gui.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            notes TEXT,
            total_price INTEGER NOT NULL,
            order_date TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def save_order_to_db(item_name, quantity, notes, total_price):
    conn = sqlite3.connect("orders_gui.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO orders (item_name, quantity, notes, total_price, order_date)
        VALUES (?, ?, ?, ?, ?)
    """, (item_name, quantity, notes, total_price, today_date))
    conn.commit()
    conn.close()

# Main Application
class FoodOrderingApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Food Ordering System")
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QIcon("app_icon.png"))  # Add application icon
        self.initUI()

    def initUI(self):
        self.loadPoppinsFont()

        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        self.menu_tab = QWidget()
        self.order_summary_tab = QWidget()
        self.history_tab = QWidget()

        self.tabs.addTab(self.menu_tab, "Menu")
        self.tabs.addTab(self.order_summary_tab, "Order Summary")
        self.tabs.addTab(self.history_tab, "Order History")

        self.setupMenuTab()
        self.setupOrderSummaryTab()
        self.setupHistoryTab()

    def loadPoppinsFont(self):
        # Add the Poppins font
        font_id = QFontDatabase.addApplicationFont("Poppins-Regular.ttf")
        if font_id == -1:
            print("Failed to load Poppins font!")
        else:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            app.setFont(QFont(font_family))

    def setupMenuTab(self):
        layout = QVBoxLayout()

        header = QLabel("Hotel Random - Food Ordering System")
        header.setFont(QFont("Poppins", 18, QFont.Bold))
        header.setAlignment(Qt.AlignCenter)
        layout.addWidget(header)

        subheader = QLabel(f"Date: {today_date}")
        subheader.setFont(QFont("Poppins", 12))
        subheader.setAlignment(Qt.AlignCenter)
        layout.addWidget(subheader)

        self.item_dropdown = QComboBox()
        self.item_dropdown.addItems(menu.keys())
        layout.addWidget(self.item_dropdown)

        self.quantity_spinner = QSpinBox()
        self.quantity_spinner.setRange(1, 10)
        layout.addWidget(self.quantity_spinner)

        self.notes_input = QTextEdit()
        self.notes_input.setFont(QFont("Poppins", 10))
        self.notes_input.setPlaceholderText("Enter additional notes (e.g., less spicy)")
        layout.addWidget(self.notes_input)

        self.price_adjustment = QSpinBox()
        self.price_adjustment.setRange(-100, 10000)  # Adjust price by - 100 RS + 10000 RS
        self.price_adjustment.setSuffix(" RS")
        self.price_adjustment.setPrefix("Adjustment: ")
        layout.addWidget(self.price_adjustment)

        add_button = QPushButton("Add to Order")
        add_button.setFont(QFont("Poppins", 12))
        add_button.clicked.connect(self.addToOrder)
        layout.addWidget(add_button)

        self.menu_tab.setLayout(layout)

    def setupOrderSummaryTab(self):
        layout = QVBoxLayout()

        header = QLabel("Order Summary")
        header.setFont(QFont("Poppins", 16, QFont.Bold))
        header.setAlignment(Qt.AlignCenter)
        layout.addWidget(header)

        self.order_table = QTableWidget(0, 4)
        self.order_table.setFont(QFont("Poppins", 10))
        self.order_table.setHorizontalHeaderLabels(["Item", "Quantity", "Price", "Notes"])
        layout.addWidget(self.order_table)

        self.total_label = QLabel("Total: RS 0")
        self.total_label.setFont(QFont("Poppins", 14, QFont.Bold))
        layout.addWidget(self.total_label)

        process_button = QPushButton("Process Payment")
        process_button.setFont(QFont("Poppins", 12))
        process_button.clicked.connect(self.processPayment)
        layout.addWidget(process_button)

        self.order_summary_tab.setLayout(layout)

    def setupHistoryTab(self):
        layout = QVBoxLayout()

        header = QLabel("Order History")
        header.setFont(QFont("Poppins", 16, QFont.Bold))
        header.setAlignment(Qt.AlignCenter)
        layout.addWidget(header)

        self.history_table = QTableWidget(0, 5)
        self.history_table.setFont(QFont("Poppins", 10))
        self.history_table.setHorizontalHeaderLabels(["ID", "Item", "Quantity", "Notes", "Price"])
        layout.addWidget(self.history_table)

        export_button = QPushButton("Export as PDF")
        export_button.setFont(QFont("Poppins", 12))
        export_button.clicked.connect(self.exportAsPDF)
        layout.addWidget(export_button)

        self.history_tab.setLayout(layout)
        self.loadHistory()

    def addToOrder(self):
        item_name = self.item_dropdown.currentText()
        quantity = self.quantity_spinner.value()
        notes = self.notes_input.toPlainText()
        adjustment = self.price_adjustment.value()
        base_price = menu[item_name] * quantity
        final_price = base_price + adjustment

        row_count = self.order_table.rowCount()
        self.order_table.insertRow(row_count)
        self.order_table.setItem(row_count, 0, QTableWidgetItem(item_name))
        self.order_table.setItem(row_count, 1, QTableWidgetItem(str(quantity)))
        self.order_table.setItem(row_count, 2, QTableWidgetItem(f"RS {final_price}"))
        self.order_table.setItem(row_count, 3, QTableWidgetItem(notes))

        save_order_to_db(item_name, quantity, notes, final_price)
        self.updateTotal()

    def updateTotal(self):
        total = 0
        for row in range(self.order_table.rowCount()):
            total += int(self.order_table.item(row, 2).text().split(" ")[1])
        self.total_label.setText(f"Total: RS {total}")

    def processPayment(self):
        if self.order_table.rowCount() > 0:
            QMessageBox.information(self, "Payment Successful", "Your payment has been processed!")
            self.order_table.setRowCount(0)
            self.total_label.setText("Total: RS 0")
        else:
            QMessageBox.warning(self, "No Order", "Your order is empty!")

    def loadHistory(self):
        conn = sqlite3.connect("orders_gui.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM orders")
        rows = cursor.fetchall()
        conn.close()

        for row in rows:
            row_count = self.history_table.rowCount()
            self.history_table.insertRow(row_count)
            for col, data in enumerate(row):
                self.history_table.setItem(row_count, col, QTableWidgetItem(str(data)))

    def exportAsPDF(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save PDF", "", "PDF Files (*.pdf)")
        if file_path:
            pdf = canvas.Canvas(file_path, pagesize=letter)
            pdf.setFont("Helvetica", 10)
            pdf.drawString(50, 750, "Order History:")
            y = 730
            conn = sqlite3.connect("orders_gui.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM orders")
            rows = cursor.fetchall()
            conn.close()
            for row in rows:
                pdf.drawString(50, y, f"{row}")
                y -= 20
                if y < 50:
                    pdf.showPage()
                    y = 750
            pdf.save()
            QMessageBox.information(self, "Export Successful", f"History exported to {file_path}")

# Run the Application
if __name__ == "__main__":
    setup_database()
    app = QApplication(sys.argv)
    window = FoodOrderingApp()
    window.show()
    sys.exit(app.exec_())