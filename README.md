#README

Project:
Task Manager CLI Application.

Date:
12 June 2024.

Author:
Mwenda Kelvin.

Description:
The Task Manager CLI is a simple command-line application for managing tasks and projects whereby users can create, delete, list, and find tasks and projects, also the application uses SQLAlchemy for ORM (Object-Relational Mapping) and Click for the CLI (Command Line Interface) interface.

Project Setup:
In order to download or clone the projects, navigate to the green button written "<> Code" and click on it then copy the link and clone it from your terminal and the projects will be automatically be downloaded and accessible to your computer and to get them up and running, navigate to the project directory and open it with VSCode (Visual Studio Code), install the necessary dependencies using/by typing "pipenv install", activate the virtual environment using/by typing "pipenv shell", then run the project using/by typing "pipenv run python -m task_manager.cli run" and follow the on-screen menu whereby you can add projects and tasks, list them, find them by ID, and delete them.

Project Structure

(i) `cli.py`: This file contains the CLI (Command Line Interface) logic and menu.

(ii) `models.py`: This file defines the ORM (Object-Relational Mapping) models with SQLAlchemy.

(iii) `orm.py`: This file contains the ORM (Object-Relational Mapping) class with methods for database operations.

(iv) `Pipfile` and `Pipfile.lock`: Both of the files manage the project dependencies.

(v) `README.md`: This file contains the project description and setup instructions.

Live Link:
https://github.com/kelvinfotech/MK-Task-Manager-Application

Technologies Used:
Python

Support & Contact:
https://github.com/kelvinfotech or kelvinfotech@gmail.com

License:
The MIT License (MIT) Copyright (c) 2024 Mwenda Kelvin Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
