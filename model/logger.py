"""
logger.py

This module configures and centralize logging for the application.
It ensures that logs are consistently formatted, stored, and accessible
throughout the project, following Python's standard `logging` library.

Configuration:
    - Logs are stored in the `logs/` directory (created automatically if missing)
    - All logs are written to `app.log`
    - Log level is set to INFO by default.
    - Log format includes timestamp, level, logger name, and message.

Available Loggers:
    - app_logger -> General application-level logs.
    - employee_logger -> Logs related to employee operations.
    - customer_logger -> Logs related to customer operations.
    - auth_logger -> Logs related to authentication and authorization.

Usage Example:
    from model.logger import app_logger, employee_logger

    app_logger_info("Application started successfully.")
    employee_logger.warning("Attempted to register an already deleted employee.")

Notes:
    - This centralized configuration avoid duplicated setup across modules.
    - New logger can be added here if needed for other modules.
"""


import logging
import os

# path
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# config
logging.basicConfig(
    filename=os.path.join(LOG_DIR, "app.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

# loggers
app_logger = logging.getLogger("App")
employee_logger = logging.getLogger("Employee")
customer_logger = logging.getLogger("Customer")
auth_logger = logging.getLogger("Auth")
author_logger = logging.getLogger("Author")
