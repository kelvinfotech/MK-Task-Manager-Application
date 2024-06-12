# Task Manager CLI Application

## Description
The Task Manager CLI is a simple command-line application for managing tasks and projects. Users can create, delete, list, and find tasks and projects. The application uses SQLAlchemy for ORM and Click for the CLI interface.

## Setup

1. Fork the repository.

2. Clone the repository.

3. Navigate to the project directory and open it with VSCode (Visual Studio Code).

4. Install the necessary dependencies using/by typing "pipenv install".

5. Activate the virtual environment using/by typing "pipenv shell".

6. Run the project using/by typing "pipenv run python -m task_manager.cli run".

## Usage

In order to use/interact with the application after running "pipenv run python -m task_manager.cli run" in the terminal, follow the on-screen menu plus you can add projects and tasks, list them, find them by ID, and delete them.

## Project Structure

(i) `cli.py`: This file contains the CLI (Command Line Interface) logic and menu.

(ii) `models.py`: This file defines the ORM (Object-Relational Mapping) models with SQLAlchemy.

(iii) `orm.py`: This file contains the ORM (Object-Relational Mapping) class with methods for database operations.

(iv) `Pipfile` and `Pipfile.lock`: Both of the files manage the project dependencies.

(v) `README.md`: This file contains the project description and setup instructions.
