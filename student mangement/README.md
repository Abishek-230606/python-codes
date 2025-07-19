# 🎓 Student Manager

A simple Python-based Student Management System that allows you to add, update, delete, and store student records including their subject-wise marks using a JSON file as the local database.

---

## 🚀 Features

- ✅ Add new students  
- ✅ Enter marks for 3 subjects per student  
- ✅ Update student marks  
- ✅ Delete a student and their records  
- ✅ Save and load data using a `.json` file  
- ✅ Console-based interactive menu system  

---

## 📁 Project Structure

student-manager/
├── student_data.json # Local JSON database for student records
├── student_manager.py # Main Python program
└── README.md # Project documentation


---

## 📦 How to Run

1. Make sure Python is installed.
2. Clone the repository or download the project folder.
3. Run the program:
4. 
python student_manager.py
🧠 How It Works
Data is stored in a dictionary format:

{
  "name": ["abishek", "john"],
  "marks": {
    "abishek": [90, 85, 78],
    "john": [88, 76, 91]
  }
}
On each operation (add/update/delete), the data is saved to a JSON file (student_data.json) to persist even after the program closes.

🔧 Requirements
Python 3.x

No external libraries required (uses built-in json module)

🙌 Author
Abishek JS
CSE Student | AI & ML Enthusiast
