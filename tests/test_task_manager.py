# tests/test_task_manager.py

# The below line of code imports the unittest module for writing and running tests
import unittest

# The below line of code imports the TaskManagerORM class and StatusEnum from task_manager.orm for testing purposes
from task_manager.orm import TaskManagerORM, StatusEnum

# The below line of code imports the Project and Task classes from task_manager.models for testing purposes
from task_manager.models import Project, Task

# The below line of code defines a test case class inheriting from unittest.TestCase
class TestTaskManagerORM(unittest.TestCase):

    # The below code sets up a clean database before each test runs
    def setUp(self):
        """Set up a clean database before each test."""
        self.orm = TaskManagerORM(db_url='sqlite:///:memory:')
        self.orm.create_project("Test Project", "A project for testing")
        self.project_id = self.orm.get_all_projects()[0].id
    
    # The below code tests creating a new project
    def test_create_project(self):
        """Test creating a new project."""
        self.orm.create_project("New Project", "Another test project")
        projects = self.orm.get_all_projects()
        self.assertEqual(len(projects), 2)
        self.assertEqual(projects[1].name, "New Project")
    
    # The below code tests deleting a project
    def test_delete_project(self):
        """Test deleting a project."""
        self.orm.delete_project(self.project_id)
        projects = self.orm.get_all_projects()
        self.assertEqual(len(projects), 0)
    
    # The below code tests creating a new task
    def test_create_task(self):
        """Test creating a new task."""
        self.orm.create_task("Test Task", "A task for testing", StatusEnum.todo, self.project_id)
        tasks = self.orm.get_all_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].title, "Test Task")
    
    # The below code tests deleting a task
    def test_delete_task(self):
        """Test deleting a task."""
        self.orm.create_task("Test Task", "A task for testing", StatusEnum.todo, self.project_id)
        task_id = self.orm.get_all_tasks()[0].id
        self.orm.delete_task(task_id)
        tasks = self.orm.get_all_tasks()
        self.assertEqual(len(tasks), 0)
    
    # The below code tests finding a project by the ID
    def test_find_project_by_id(self):
        """Test finding a project by ID."""
        project = self.orm.find_project_by_id(self.project_id)
        self.assertIsNotNone(project)
        self.assertEqual(project.name, "Test Project")
    
    # The below code tests finding a task by the ID
    def test_find_task_by_id(self):
        """Test finding a task by ID."""
        self.orm.create_task("Test Task", "A task for testing", StatusEnum.todo, self.project_id)
        task_id = self.orm.get_all_tasks()[0].id
        task = self.orm.find_task_by_id(task_id)
        self.assertIsNotNone(task)
        self.assertEqual(task.title, "Test Task")
    
    # The below code tests getting tasks by the project ID
    def test_get_tasks_by_project(self):
        """Test getting tasks by project ID."""
        self.orm.create_task("Test Task 1", "A task for testing 1", StatusEnum.todo, self.project_id)
        self.orm.create_task("Test Task 2", "A task for testing 2", StatusEnum.in_progress, self.project_id)
        tasks = self.orm.get_tasks_by_project(self.project_id)
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0].title, "Test Task 1")
        self.assertEqual(tasks[1].title, "Test Task 2")

# The below code runs the tests when the script is executed
if __name__ == '__main__':
    unittest.main()
