import logging

#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

logging.basicConfig(level=logging.DEBUG,filename='data.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
# name = input("Enter Your Name:\n")
# logging.info(f"{name} has logged in successfully !!")

# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')

def add_few_number(a: int, b: int) -> int:
    logging.debug(f"Reseived numbers: {a} and {b}")
    return a + b

add_few_number(a=6, b=7)

# def mone_collected(amount: float) -> None:
#     logging.info(f"Amount of money received: {amount}")
#     if amount == 0:
#         logging.warning('Expected amount larger than 0')
#     #doing smth else

# # try:
# #     #some code here
# # except Exception as e:
# #     logging.error(f"Error received: {e}")

# def emergency_stop(is_stop_event: bool) -> None:
#     if is_stop_event:
#         logging.critical(f"Had to stop device due to unexpexted stop event")
#         # func stop()