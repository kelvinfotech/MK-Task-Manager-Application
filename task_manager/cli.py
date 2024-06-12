# task_manager/cli.py

# The below line of code imports the necessary module for creating command-line interfaces
import click

# The below line of code imports the ORM (Object-Relational Mapping) class and Enum from the task_manager package
from task_manager.orm import TaskManagerORM, StatusEnum

# The below line of code initializes an instance of TaskManagerORM for interacting with the database
task_manager = TaskManagerORM()

# The below function displays the menu options to the user(s)
def display_menu():
    click.echo("Task Manager CLI")
    click.echo("1. Add Project")
    click.echo("2. Delete Project")
    click.echo("3. List All Projects")
    click.echo("4. Find Project by ID")
    click.echo("5. Add Task")
    click.echo("6. Delete Task")
    click.echo("7. List All Tasks")
    click.echo("8. Find Task by ID")
    click.echo("9. List Tasks by Project")
    click.echo("10. Exit")

# The below function to prompts the user for input and returns the choice as an integer
def get_choice():
    choice = click.prompt("Enter your choice", type=int)
    return choice

# The below code define a command group using click.group(), that serves as the entry point for the CLI (Command Line Interface) application
@click.group()
def cli():
    pass

# The below code defines a command using @click.command(), that is executed when the CLI (Command Line Interface) is invoked
@click.command()
def run():
    """Run the Task Manager CLI."""

    # The below code continuously displays the menu and prompts the user for input until they choose the exit option
    while True:
        display_menu()
        choice = get_choice()

        # Based on the user's choice, the below code performs various operations on the projects and tasks
        if choice == 1:
            name = click.prompt("Enter project name")
            description = click.prompt("Enter project description")
            try:
                task_manager.create_project(name, description)
                click.echo(f'Project {name} added.')
            except ValueError as e:
                click.echo(f'Error: {e}')
        elif choice == 2:
            project_id = click.prompt("Enter project ID to delete", type=int)
            task_manager.delete_project(project_id)
            click.echo(f'Project {project_id} deleted.')
        elif choice == 3:
            projects = task_manager.get_all_projects()
            for project in projects:
                click.echo(f'{project.id}: {project.name} - {project.description}')
        elif choice == 4:
            project_id = click.prompt("Enter project ID to find", type=int)
            project = task_manager.find_project_by_id(project_id)
            if project:
                click.echo(f'{project.id}: {project.name} - {project.description}')
            else:
                click.echo(f'Project {project_id} not found.')
        elif choice == 5:
            title = click.prompt("Enter task title")
            description = click.prompt("Enter task description")
            status = click.prompt("Enter task status", type=click.Choice([status.name for status in StatusEnum]))
            project_id = click.prompt("Enter project ID for the task", type=int)
            try:
                task_manager.create_task(title, description, StatusEnum[status], project_id)
                click.echo(f'Task {title} added.')
            except ValueError as e:
                click.echo(f'Error: {e}')
        elif choice == 6:
            task_id = click.prompt("Enter task ID to delete", type=int)
            task_manager.delete_task(task_id)
            click.echo(f'Task {task_id} deleted.')
        elif choice == 7:
            tasks = task_manager.get_all_tasks()
            for task in tasks:
                click.echo(f'{task.id}: {task.title} - {task.description} - {task.status.name} - Project ID: {task.project_id}')
        elif choice == 8:
            task_id = click.prompt("Enter task ID to find", type=int)
            task = task_manager.find_task_by_id(task_id)
            if task:
                click.echo(f'{task.id}: {task.title} - {task.description} - {task.status.name} - Project ID: {task.project_id}')
            else:
                click.echo(f'Task {task_id} not found.')
        elif choice == 9:
            project_id = click.prompt("Enter project ID to list tasks", type=int)
            tasks = task_manager.get_tasks_by_project(project_id)
            for task in tasks:
                click.echo(f'{task.id}: {task.title} - {task.description} - {task.status.name}')
        elif choice == 10:
            click.echo("Exiting Task Manager CLI.")
            break
        else:
            click.echo("Invalid choice. Please try again.")

# The below code adds the run() command to the cli group
cli.add_command(run)

# In the below code, the script is executed directly, that runs the CLI (Command Line Interface) application
if __name__ == '__main__':
    cli()
