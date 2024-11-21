## Week Planer workflow
- create your venv. run 'python -m venv your_venv_name' on terminal
- your_venv_name\Scripts\activate to activate venv
- pip install django to install django
- Create a new Django project:
   django-admin startproject project_name
- cd project_name
- python manage.py startapp appName
- add appName to installed app list in settings file
- Define the Task Model in planner/models.py
- Run Migrations:
  python manage.py makemigrations
  python manage.py migrate
- Create Forms for Task Input in planner/forms.py
- Define Views in planner/views.py
- Configure URLs in planner/urls.py
- Include these URLs in the project’s weekplanner/urls.py
- Create Templates in planner/templates/planner/
week_planner.html, add_task.html.

## output
- run python manage.py runserver to check in brower



## requirement
- to produce project requirements run pip freeze > requirements.txt