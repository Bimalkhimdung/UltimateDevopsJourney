import psycopg2
import logging
from typing import Optional, Tuple
from dataclasses import dataclass
import os
from pathlib import Path
import yaml
import getpass
import re

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('database_operations.log'),
        logging.StreamHandler()
    ]
)

@dataclass
class DatabaseConfig:
    """Configuration for database connection"""
    dbname: str
    user: str
    password: str
    host: str
    port: int = 5432

class DatabaseManager:
    """Manages database operations including creation and user management"""
    
    def __init__(self, config: DatabaseConfig):
        self.config = config
        self.connection = None
        self.cursor = None

    def connect(self) -> None:
        """Establish database connection"""
        try:
            self.connection = psycopg2.connect(
                dbname=self.config.dbname,
                user=self.config.user,
                password=self.config.password,
                host=self.config.host,
                port=self.config.port
            )
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
            logging.info("Successfully connected to the database")
        except psycopg2.Error as e:
            logging.error(f"Failed to connect to database: {e}")
            raise

    def close(self) -> None:
        """Close database connection"""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        logging.info("Database connection closed")

    @staticmethod
    def validate_input(input_str: str, input_type: str) -> bool:
        """Validate user input"""
        if not input_str:
            logging.error(f"Empty {input_type} provided")
            return False
        
        # Basic SQL injection prevention
        if re.search(r'[;\'"]', input_str):
            logging.error(f"Invalid characters in {input_type}")
            return False
        
        return True

    def check_database_exists(self, db_name: str) -> bool:
        """Check if database exists"""
        try:
            self.cursor.execute(
                "SELECT 1 FROM pg_database WHERE datname = %s",
                (db_name,)
            )
            return bool(self.cursor.fetchone())
        except psycopg2.Error as e:
            logging.error(f"Error checking database existence: {e}")
            return False

    def check_user_exists(self, username: str) -> bool:
        """Check if user exists"""
        try:
            self.cursor.execute(
                "SELECT 1 FROM pg_roles WHERE rolname = %s",
                (username,)
            )
            return bool(self.cursor.fetchone())
        except psycopg2.Error as e:
            logging.error(f"Error checking user existence: {e}")
            return False

    def create_user(self, username: str, password: str) -> bool:
        """Create a new database user"""
        try:
            self.cursor.execute(
                "CREATE ROLE %s WITH PASSWORD %s",
                (username, password)
            )
            self.cursor.execute(f"ALTER ROLE {username} LOGIN")
            logging.info(f"User {username} created successfully")
            return True
        except psycopg2.Error as e:
            logging.error(f"Error creating user: {e}")
            return False

    def create_database(self, db_name: str, owner: str) -> bool:
        """Create a new database"""
        try:
            self.cursor.execute(f"CREATE DATABASE {db_name}")
            self.cursor.execute(f"GRANT ALL ON DATABASE {db_name} TO {owner}")
            self.cursor.execute(f"ALTER DATABASE {db_name} OWNER TO {owner}")
            logging.info(f"Database {db_name} created successfully")
            return True
        except psycopg2.Error as e:
            logging.error(f"Error creating database: {e}")
            return False

def load_config() -> DatabaseConfig:
    """Load database configuration from config file or environment variables"""
    config_path = Path("config.yaml")
    
    if config_path.exists():
        with open(config_path) as f:
            config_data = yaml.safe_load(f)
            return DatabaseConfig(**config_data)
    
    # Fallback to environment variables
    return DatabaseConfig(
        dbname=os.getenv("DB_NAME", "shikhar"),
        user=os.getenv("DB_USER", "shikhar_insurance_user"),
        password=os.getenv("DB_PASSWORD", "Al1*+1IJSJA92Fd3"),
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", "5432"))
    )

def main():
    """Main function to handle database operations"""
    try:
        config = load_config()
        db_manager = DatabaseManager(config)
        db_manager.connect()

        while True:
            db_name = input("Enter database name: ").strip()
            if not DatabaseManager.validate_input(db_name, "database name"):
                continue

            db_user = input("Enter database user: ").strip()
            if not DatabaseManager.validate_input(db_user, "username"):
                continue

            if not db_manager.check_user_exists(db_user):
                choice = input(f"User {db_user} does not exist. Create one? (Y/N): ").strip().lower()
                if choice == 'y':
                    password = getpass.getpass(f"Enter password for {db_user}: ")
                    if not db_manager.create_user(db_user, password):
                        print("Failed to create user")
                        break
                else:
                    print("Exiting without creating database")
                    break

            if db_manager.check_database_exists(db_name):
                choice = input(f"Database {db_name} already exists. Create another? (Y/N): ").strip().lower()
                if choice == 'n':
                    print("Exiting without creating database")
                    break
                continue

            if db_manager.create_database(db_name, db_user):
                print(f"Database {db_name} created successfully and ownership granted to user {db_user}")
                break

    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        if 'db_manager' in locals():
            db_manager.close()

if __name__ == "__main__":
    main()
