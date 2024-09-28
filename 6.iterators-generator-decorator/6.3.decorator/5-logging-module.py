# use logging instead of print() to save and check in runtime
import logging

logging.basicConfig(
    level=logging.DEBUG, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='app.log',
    filemode='w'
)

def divide(a, b):
    logging.debug(f"Dividing {a} by {b}")
    result = a / b
    logging.info(f"Result: {result}")
    return result


result = divide(10, 2)
result = divide(10, 0)  # This will generate a
# ZeroDivisionError, and the log messages will capture it

# level(low -> high): DEBUG, INFO, WARNING, ERROR, EXCEPTION, CRITICAL
# - DEBUG: details
# - INFO: common information
# - WARNING:
# - ERROR:
# - EXCEPTION: exceptions (includes traceback)
# - CRITICAL:  extremely errors
