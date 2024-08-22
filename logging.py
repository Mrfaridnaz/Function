import logging

# Configure logging
logging.basicConfig(filename="test1.log",
                    level=logging.INFO,
                    format='%(levelname)s %(asctime)s %(name)s %(message)s')

def divide(a, b):
    logging.info("The numbers entered by the user are %s and %s", (a, b))
    try:
        logging.info("We are into the function")
        div = a / b
        logging.info("We have completed the division operation")
        return div
    except Exception as e:
        logging.exception("An error occurred: %s", e)
        return None  # Return None if there's an error

# Example usage
result = divide(5, 4)
print(f"Result of division: {result}")
