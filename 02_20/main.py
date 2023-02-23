# # Create a function that takes one parameter as number - age , other as name which is default 'Anatnas', and some args and keywords.
# # Print first Name with age;
# # And then print all arguments with key arguments.

# def  print_name_age_with_arguments(age:int, name:str = "Antanas", *args, **kwargs) -> None:
#     print(f'Name {name}, age {age}')
#     print(f"Free arguments: {args if args else 'args not been '}, free key eord arguments{kwargs if kwargs else ''}")

# print_name_age_with_arguments(25, "Tom")
#-------------------------------------------------------------------------------------------------------------------
from typing import Optional, Union


# def divider(number: Union[float, int]) -> Union[float, int]:
#     return number / 2 if isinstance(number, float) else number // 2
# try: 
#     my_divided_number = divider(10)
#     print(my_divided_number)
#     print(my_divided_number /0) 
# except TypeError:
#     print("Wrong type provided!")
# except ZeroDivisionError:
#     print("Never divided with 0")    
    
# try:
#     my_divided_number = divider("A")
#     print(my_divided_number)
# except ZeroDivisionError:
#     print("my specific message to print")
# # basic error message
# except Exception as e:
#     print(f"Error: {e}")

def divider(number: Union[float, int]) -> Optional(Union[float, int]):
    try:
        return number / 2 if isinstance(number, float) else number // 2
    except TypeError:
        print("Wrong type received")
    except Exception as e:
        print(f"Error: {e}")