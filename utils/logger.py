import logging
import sys
import os
from logging.handlers import RotatingFileHandler

# 2. Default Log Format (Global Constant)
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

# 3. Function Signature for setup_logger
def setup_logger(name='app', log_file='logs/app.log', level=logging.INFO, log_to_console=True, log_to_file=True, max_bytes=10*1024*1024, backup_count=5):
    """
    Configures and returns a logger instance.

    Args:
        name (str): Name of the logger.
        log_file (str): Path to the log file for file logging.
        level (int): Logging level (e.g., logging.INFO, logging.DEBUG).
        log_to_console (bool): If True, logs will be output to the console.
        log_to_file (bool): If True, logs will be written to a rotating file.
        max_bytes (int): Maximum size of the log file in bytes before rotation.
        backup_count (int): Number of backup log files to keep.

    Returns:
        logging.Logger: Configured logger instance.
    """
    # 4.a. Get a logger instance
    logger = logging.getLogger(name)
    
    # 4.b. Set the logger's level
    logger.setLevel(level)
    
    # 4.c. Prevent log propagation
    logger.propagate = False
    
    # 4.d. Clear Existing Handlers
    if logger.hasHandlers():
        logger.handlers.clear()
        
    # 4.e. Create a formatter
    formatter = logging.Formatter(LOG_FORMAT)
    
    # 4.f. Console Handler Configuration
    if log_to_console is True:
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        console_handler.setLevel(level) # Set level for handler
        logger.addHandler(console_handler)
        
    # 4.g. Rotating File Handler Configuration
    if log_to_file is True:
        # Ensure Log Directory Exists
        log_dir = os.path.dirname(log_file)
        if log_dir and not os.path.exists(log_dir): # Check if log_dir is not an empty string
            os.makedirs(log_dir, exist_ok=True)
            
        # Create the handler
        file_handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count, encoding='utf-8')
        file_handler.setFormatter(formatter)
        file_handler.setLevel(level) # Set level for handler
        logger.addHandler(file_handler)
        
    # 4.h. Return the logger
    return logger

if __name__ == '__main__':
    # Example Usage (optional, can be removed or kept for testing)
    # Create a logger for the main application
    main_logger = setup_logger(name='my_app', log_file='logs/my_app.log', level=logging.DEBUG)
    main_logger.debug("This is a debug message for my_app.")
    main_logger.info("This is an info message for my_app.")
    main_logger.warning("This is a warning message for my_app.")

    # Create another logger for a specific module
    module_logger = setup_logger(name='my_module', log_file='logs/my_module.log', level=logging.INFO, log_to_console=False)
    module_logger.info("This is an info message for my_module (file only).")
    try:
        1 / 0
    except ZeroDivisionError:
        module_logger.error("An error occurred in my_module.", exc_info=True)

    # Test log directory creation with relative path
    test_logger = setup_logger(name='test_relative', log_file='relative_logs/test.log', level=logging.DEBUG)
    test_logger.debug("Testing relative log path.")
    
    # Test logger with only console output
    console_only_logger = setup_logger(name='console_only', log_to_file=False, level=logging.DEBUG)
    console_only_logger.debug("This message should only appear on the console.")

    print(f"Log files should be in '{os.path.abspath('logs')}' and '{os.path.abspath('relative_logs')}' if file logging was enabled.")
