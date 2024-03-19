# Checkout System

This repository contains a simple checkout system implemented in Python. The application allows calculating the total price of a shopping cart based on a set of pricing rules for items.

The project has two versions: Version A is implemented with simple Python scripts, while Version B is a Django application with a more structured database modeling to handle more scenarios.

#Version A

## Running the Program

To run the project, follow these steps:

1. Ensure you have Python 3.8 installed on your system.
2. Clone this repository to your local machine.
3. Navigate to the project directory.
4. Run the `main.py` file using Python 3.8:

   ```
   python main.py
   ```
   
This will execute the program and display the output, which includes running tests on item pricing and printing the results.

```
Running tests on the following Item pricing:
----------------------------------------
Item A. Unit price: 50, Special Price: 130 for 3 units
Item B. Unit price: 30, Special Price: 45 for 2 units
Item C. Unit price: 20. No discounts.
Item D. Unit price: 15. No discounts.
----------------------------------------
Test with 0 items passed
Test A passed
Test AB passed
Test CDBA passed
Test AA passed
Test AAA passed
Test AAAA passed
Test AAAAA passed
Test AAAAAA passed
Test AAAB passed
Test AAABB passed
Test AAABBD passed
Test DABABA passed
```

## Code Structure

The code is divided into the following files:

- `main.py`: Modify the `item_pricing` dictionary and start the program.
- `test.py`: Contains asserts for tests.
- `utils.py`: Contains utility functions, in this case, only the print function.
- `checkout_system.py`: Contains functions that handle the calculation of cart prices based on `items_pricing`.
- `models.py`: Contains classes that map real-world objects, in this case, only `Item`.

