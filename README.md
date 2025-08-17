# Modern To-Do List Application 📝

This is a simple and elegant to-do list application built with Python's `tkinter` library. It provides a clean, modern user interface to help you manage your tasks efficiently.

## ✨ Features

*   ✅ **Add Tasks:** Quickly add new tasks with a title, description, due date, and priority level.
*   ✏️ **Edit Tasks:** Modify the details of any existing task.
*   🗑️ **Delete Tasks:** Remove tasks you've completed or no longer need.
*   📊 **Clear Task View:** Displays all tasks in a clean, easy-to-read table format.
*   ⭐ **Priority Levels:** Assign 'High', 'Medium', or 'Low' priority to each task.
*   📅 **Date Picker:** A user-friendly calendar widget to select due dates.

## 📸 Screenshot

*(A screenshot of the application interface would go here)*

## 🛠️ Requirements

To run this application, you'll need:

*   Python 3.x
*   The `tkcalendar` library

## 🚀 How to Run

1.  **Clone or download the repository.**

2.  **Install the necessary dependencies:**
    Open your terminal or command prompt and run the following command:
    ```bash
    pip install tkcalendar
    ```

3.  **Run the application:**
    Navigate to the project directory in your terminal and execute the script:
    ```bash
    python todolist.py
    ```

## Code Overview

The application is built using the `tkinter` library for the graphical user interface.

*   **`todolist.py`**: This is the main file containing all the application logic.
    *   `add_task()`: Handles the logic for adding a new task to the list.
    *   `delete_task()`: Deletes the currently selected task.
    *   `edit_task()`: Opens dialog boxes to edit the details of a selected task.
    *   **UI Setup**: The rest of the code is dedicated to building the user interface, including the input fields, buttons, and the `Treeview` widget for displaying tasks. The `ttk` themed widgets are used to give the application a modern look and feel.
