# task_manager/orm.py

# The below lines of code import SQLAlchemy modules for the database operations
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# The below line of code imports data models and Enum from task_manager package
from task_manager.models import Base, Project, Task, StatusEnum

# The below code defines a class for managing the database operations
class TaskManagerORM:
    def __init__(self, db_url='sqlite:///task_manager.db'):

        # The below line of code creates an engine to connect to the database
        self.engine = create_engine(db_url)

        # The below line of code creates tables defined in the data models
        Base.metadata.create_all(self.engine)

        # The below line of code creates a sessionmaker to interact with the database
        self.Session = sessionmaker(bind=self.engine)
    
    # The below code method creates a new project in the database
    def create_project(self, name, description):
        session = self.Session()
        try:
            project = Project(name=name, description=description)
            session.add(project)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
    
    # The below code method deletes a project from the database
    def delete_project(self, project_id):
        session = self.Session()
        project = session.query(Project).filter_by(id=project_id).first()
        if project:
            session.delete(project)
            session.commit()
        session.close()
    
    # The below code method retrieves all projects from the database
    def get_all_projects(self):
        session = self.Session()
        projects = session.query(Project).all()
        session.close()
        return projects
    
    # The below code method finds a project by its ID
    def find_project_by_id(self, project_id):
        session = self.Session()
        project = session.query(Project).filter_by(id=project_id).first()
        session.close()
        return project
    
    # The below code method creates a new task in the database
    def create_task(self, title, description, status, project_id):
        session = self.Session()
        try:
            task = Task(title=title, description=description, status=status, project_id=project_id)
            session.add(task)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
    
        # The below code method deletes a task from the database
    def delete_task(self, task_id):
        session = self.Session()
        task = session.query(Task).filter_by(id=task_id).first()
        if task:
            session.delete(task)
            session.commit()
        session.close()
    
    # The below code method retrieves all tasks from the database
    def get_all_tasks(self):
        session = self.Session()
        tasks = session.query(Task).all()
        session.close()
        return tasks
    
    # The below code method finds a task by its ID
    def find_task_by_id(self, task_id):
        session = self.Session()
        task = session.query(Task).filter_by(id=task_id).first()
        session.close()
        return task
    
    # The below code method retrieves tasks associated with a specific project
    def get_tasks_by_project(self, project_id):
        session = self.Session()
        tasks = session.query(Task).filter_by(project_id=project_id).all()
        session.close()
        return tasks
