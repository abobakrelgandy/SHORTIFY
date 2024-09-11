import os
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

Base = declarative_base()
from dotenv import load_dotenv
load_dotenv()

class DBStorage:
    """Interacts with the PostgreSQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize the DBStorage instance"""
        try:
            database_url = os.getenv('DATABASE_URL')
            if not database_url:
                raise ValueError("DATABASE_URL environment variable is not set.")
            self.__engine = create_engine(database_url)
            self.reload()  # Initialize the session here
        except SQLAlchemyError as e:
            print(f"Error initializing database connection: {e}")

    def new(self, obj):
        """Add the object to the current database session"""
        if self.__session is None:
            raise Exception("Session is not initialized.")
        try:
            print(obj)
            self.__session.add(obj)
        except SQLAlchemyError as e:
            print(f"Error adding object to session: {e}")

    def save(self):
        """Commit all changes of the current database session"""
        if self.__session is None:
            raise Exception("Session is not initialized.")
        try:
            self.__session.commit()
        except SQLAlchemyError as e:
            print(f"Error committing session: {e}")

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if self.__session is None:
            raise Exception("Session is not initialized.")
        if obj is not None:
            try:
                self.__session.delete(obj)
            except SQLAlchemyError as e:
                print(f"Error deleting object from session: {e}")

    def reload(self):
        """Reloads data from the database"""
        try:
            Base.metadata.create_all(self.__engine)
            sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
            self.__session = scoped_session(sess_factory)
        except SQLAlchemyError as e:
            print(f"Error reloading database: {e}")

    def close(self):
        """Call remove() method on the private session attribute"""
        if self.__session is not None:
            self.__session.remove()

    def get(self, cls, short_code):
        """Get the instance of link"""
        if self.__session is None:
            raise Exception("Session is not initialized.")
        try:
            instance = self.__session.query(cls).filter_by(short_code=short_code).first()
            return instance
        except SQLAlchemyError as e:
            print(f"Error retrieving object: {e}")
            return None
        
    def count(self, cls):
        """Return the count of saved links"""
        if self.__session is None:
            raise Exception("Session is not initialized.")
        try:
            instances = self.__session.query(cls).all()
            return len(instances)
        except SQLAlchemyError as e:
            print(f"Error counting objects: {e}")
            return 0
