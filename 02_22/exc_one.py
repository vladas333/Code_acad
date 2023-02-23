import logging

# in terminal
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
# in data.log file
# logging.basicConfig(level=logging.DEBUG,filename='data.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

#sr_name = input("Enter Your Name:\n")
#birth_year = int(input("Enter Your bith year:\n"))
#your_city = input("Which city you like:")



try:
    birth_year = int(input("Enter Your bith year:\n"))
    birth_year == int(birth_year)
except TypeError:
    logging.critical("No valid year! Please try again ...")
except Exception as e:
    logging.error(f"Error: {e}")



    


#logging.info(f"Your birth year is:{birth_year}.")


# if __name__ == "__main__":
#     birth_year = input("Enter Your bith year:\n")

# try:
#     if birth_year == int
# except ValueError:
#     logging.warning(f"You enter bad data")



# def contact_info(sr_name: str, birth_year: int, your_city: str) -> None:
#     logging.info(f"{sr_name} has logged in successfully !!")
#     logging.info(f"Your birth year is{birth_year}.")
#     logging.info(f"Your favorit city {your_city}")