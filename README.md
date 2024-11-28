Restaurant Food Ordering System
Welcome to the Restaurant Food Ordering System! This is a PyQt5-based desktop application that enables users to view a menu, create an order, and maintain an order history using an SQLite database. It's designed for restaurant owners and developers seeking to learn about graphical interfaces and database integration in Python.



🚀 Features
Dynamic Menu: Browse and add items to your order directly from the menu tab.
Order Summary: View and manage your current order with an option to delete individual items.
Order History: Review past orders stored in an SQLite database.
Database Integration: All data is saved and retrieved using SQLite for persistence.
User-Friendly Interface: Clean and intuitive UI created using PyQt5.
🛠️ Technologies Used
Programming Language: Python
Framework: PyQt5 (GUI)
Database: SQLite (local database for storing order history)
📂 File Structure
bash
Copy code
Restaurant-Food-Ordering-System/
├── index.py              # Main application script
├── orders_gui.db         # SQLite database (created at runtime)
├── README.md             # Project documentation
└── app_icon.png          # Application icon (optional)
⚙️ Installation and Usage
Clone the repository:

bash
Copy code
git clone https://github.com/reshuk-code/Restaurant-Food-Ordering-System---Source-Code-.git
cd Restaurant-Food-Ordering-System
Install dependencies: Ensure you have Python installed, then install the required libraries:

bash
Copy code
pip install pyqt5
Run the application:

bash
Copy code
python index.py
Navigate through the app:

Use the Menu tab to add items to your order.
Review your items in the Order Summary tab.
Check past orders in the Order History tab.
🗂️ Database Schema
The SQLite database (orders_gui.db) has a single table called orders with the following structure:

Column Name	Data Type	Description
order_id	INTEGER	Primary key (autoincrement)
item_name	TEXT	Name of the ordered item
quantity	INTEGER	Quantity of the item
total_price	REAL	Total price for the item(s)
🤝 Contributions
Contributions are welcome! If you’d like to add features, fix bugs, or improve the project, follow these steps:

Fork the repository.
Create a new branch:
bash
Copy code
git checkout -b feature-name
Make your changes and commit:
bash
Copy code
git commit -m "Description of changes"
Push your branch:
bash
Copy code
git push origin feature-name
Create a pull request and describe your changes.
📝 License
This project is licensed under the MIT License. See the LICENSE file for more details.

💡 Future Enhancements
Add functionality to update item quantities in the order summary.
Include pricing information in the menu.
Implement a receipt generation feature for completed orders.
Add support for item categories and dynamic menu updates.
📧 Contact
For any queries or suggestions, feel free to contact me:

GitHub: reshuk-code
Email: reshuksapkota2007@gmail.com
🌟 If you find this project helpful, please give it a star ⭐ on GitHub!
