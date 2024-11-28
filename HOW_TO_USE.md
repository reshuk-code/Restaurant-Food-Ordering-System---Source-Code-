How to Run the Restaurant Food Ordering System

1. **Clone the Repository**:
   If you haven't already, clone the repository to your local machine using the following command:
git clone https://github.com/reshuk-code/Restaurant-Food-Ordering-System---Source-Code-.git

markdown
Copy code

2. **Install Dependencies**:
This project requires the following Python libraries:
- PyQt5
- sqlite3 (comes with Python)
- reportlab

To install PyQt5 and reportlab, run:
pip install pyqt5 reportlab

markdown
Copy code

3. **Set Up the Database**:
The system will automatically create a SQLite database (`orders_gui.db`) on the first run. This database will store the order information.

4. **Run the Application**:
To start the application, run the `index.py` file:
python index.py

vbnet
Copy code

5. **Use the Application**:
- Browse the menu and add items to your order.
- The "Order Summary" tab shows the current items added and their total price.
- You can delete items from the order summary by clicking the "Delete" button next to the items.
- After completing the order, you can process the payment.
- In the "Order History" tab, view and export the order history as a PDF.

6. **Exporting Data**:
You can export the order history to a PDF by clicking on the "Export as PDF" button in the "Order History" tab.

7. **Icons & Fonts**:
The application uses a custom app icon (`app_icon.png`) and a Poppins font (`Poppins-Regular.ttf`). Ensure that these files are available in the project directory for proper display.

8. **Troubleshooting**:
- If the application doesn't launch, ensure you have Python and the required dependencies installed.
- If the font or icon doesn't display correctly, verify the file paths are correct.

For any issues or contributions, feel free to open an issue or submit a pull request on the 