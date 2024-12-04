

---

# Django Week Planner

A simple yet efficient **Week Planner** web application built using Django. The Week Planner allows users to manage tasks for the week by adding, viewing, and marking tasks as completed. The project showcases a solid understanding of Django's core features, including models, forms, views, templates, and database migrations.

---

## Features

- **Add Tasks**: Users can add tasks specifying the title, description, day, time, and date from both the front-end interface and Django admin.
- **View Weekly Tasks**: Tasks are displayed in a list format, organized by day and time.
- **Mark Tasks as Completed**: Users can toggle a task's completion status using a dynamic button.
- **Responsive Design**: Includes intuitive and user-friendly interfaces for adding and managing tasks.
- **Database Integration**: Data is persisted using Django's ORM and supports dynamic updates.

---

## Screenshots

- **Task List View**  
  Displays tasks for the week, including their day, time, title, and completion status.  
  ![Task List Screenshot](https://github.com/AHM-Saiful-Islam/Fun-Project/blob/main/Week-Planer/Screenshots/Task%20List%20View%202.png)
  ![Task List Screenshot](https://github.com/AHM-Saiful-Islam/Fun-Project/blob/main/Week-Planer/Screenshots/Task%20List%20View.png)

- **Add Task Page**  
  Allows users to input new tasks with all required details.  
  ![Add Task Screenshot](https://github.com/AHM-Saiful-Islam/Fun-Project/blob/main/Week-Planer/Screenshots/Add%20Task%20Page.png)

---

## Workflow

1. **Set up a Virtual Environment**  
   ```bash
   python -m venv your_venv_name
   your_venv_name\Scripts\activate
   ```

2. **Install Django**  
   ```bash
   pip install django
   ```

3. **Create a Django Project and App**  
   ```bash
   django-admin startproject project_name
   cd project_name
   python manage.py startapp planner
   ```

4. **Configure the Project**  
   - Add the app (`planner`) to the `INSTALLED_APPS` list in the `settings.py` file.

5. **Define the Task Model**  
   Create the `Task` model in `planner/models.py` with fields for `title`, `description`, `day`, `time`, `date`, and `completed`.

6. **Run Migrations**  
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. **Create Forms**  
   Create a `TaskForm` in `planner/forms.py` for task input.

8. **Define Views**  
   Implement views in `planner/views.py` for adding tasks, displaying tasks, and toggling completion.

9. **Configure URLs**  
   - Define app-specific URLs in `planner/urls.py`.
   - Include app URLs in the main `project_name/urls.py`.

10. **Create Templates**  
    - `week_planner.html`: Displays tasks and their statuses.
    - `add_task.html`: Provides a form for adding new tasks.

---

## Project Structure

```plaintext
project_name/
├── project_name/
│   ├── settings.py
│   ├── urls.py
│   ├── ...
├── planner/
│   ├── templates/planner/
│   │   ├── week_planner.html
│   │   ├── add_task.html
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   ├── ...
├── manage.py
```

---

## Installation and Setup

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Development Server**  
   ```bash
   python manage.py runserver
   ```

4. **Access the Application**  
   Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

---

## Requirements

- **Python**: 3.x
- **Django**: 4.x or above
- Additional dependencies can be found in `requirements.txt`.  
  To generate it:
  ```bash
  pip freeze > requirements.txt
  ```

---

## Future Enhancements

- Add user authentication to allow personalized task management.
- Implement task priority levels (e.g., High, Medium, Low).
- Introduce notifications/reminders for upcoming tasks.
- Create a mobile-responsive design for better usability.

---

## About the Author

This project was developed by **AHM SAIFUL ISLAM** as a demonstration of Django expertise and software development skills. It showcases abilities in full-stack development, problem-solving, and clean code practices.

---

## License

This project is open-source and available under the [MIT License](LICENSE). Contributions are welcome!

---

## Feedback

Feel free to open an issue or contact me directly for any feedback or questions! 😊
