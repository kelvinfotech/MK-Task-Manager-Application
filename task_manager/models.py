# task_manager/models.py

# The below lines of code import the necessary modules from SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship, declarative_base

# The below line of code imports the enum module for defining Enum types
import enum

# The below line of code creates a base class for declarative class definitions
Base = declarative_base()

# The below code defines an Enum class for task statuses
class StatusEnum(enum.Enum):
    todo = 'To Do'
    in_progress = 'In Progress'
    done = 'Done'

# The below line of code defines the Project class
class Project(Base):

    # The below line of code defines the table name
    __tablename__ = 'projects'

    # The below code defines columns for the Project table
    id = Column(Integer, primary_key=True)
    _name = Column('name', String, nullable=False)
    description = Column(String)

    # The below line of code defines a relationship with the Task table
    tasks = relationship('Task', back_populates='project')
    
    # The below code defines a property for the project name
    @property
    def name(self):
        return self._name
    
    # THe below code defines a setter method for the project name property
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Project name cannot be empty.")
        self._name = value

class Task(Base):

    # The below line of code defines the table name
    __tablename__ = 'tasks'

    # The below code defines columns for the Task table
    id = Column(Integer, primary_key=True)
    _title = Column('title', String, nullable=False)
    description = Column(String)
    status = Column(Enum(StatusEnum), default=StatusEnum.todo)
    project_id = Column(Integer, ForeignKey('projects.id'))

    # The below code defines a relationship with the Project table
    project = relationship('Project', back_populates='tasks')
    
    # The below code defines a property for the task title
    @property
    def title(self):
        return self._title

    # The below code defines a setter method for the task title property
    @title.setter
    def title(self, value):
        if not value:
            raise ValueError("Task title cannot be empty.")
        self._title = value
