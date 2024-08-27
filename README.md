![LastCommit](https://img.shields.io/github/last-commit/ecopque/visualcalc_calculator?logo=python&logoColor=white&label=Last+update&color=9bf12&&style=flat)&nbsp;

# VisualCalc Calculator

This is VisualCalc, a basic calculator created entirely in Python. In this project, PySide6 was used, one of the most powerful and versatile libraries for creating graphical interfaces in Python. PySide6 is an official Qt binding for Python, allowing you to create feature-rich applications with a modern look and feel.

## How to Use

- Run the program.
- Enter two numbers when prompted.
- Enter an operator (+, -, *, / or (^ or P)) to perform the desired operation.
- The program will display the result of the operation.

## Features

- Validates user input to ensure only valid numbers and operators are used.
- Handles exceptions gracefully, preventing the program from crashing.
- Provides a simple and intuitive interface for performing calculations.

## Main Calculator Components

- <strong>Buttons:</strong>
Calculator buttons are created using PySide6's QPushButton class. Each button represents a specific number, operator, or function (such as clearing or calculating the result). The cls_button custom class is an extension to QPushButton that allows you to further configure the style and behavior of buttons. Below is an example of how we configure a button.
- <strong>Layout:</strong>
To organize the buttons in a grid, we use QGridLayout. The cls_buttonsgrid class extends QGridLayout and is responsible for adding and positioning each button in the grid, as well as connecting button signals to the appropriate slots that perform calculator functions.
- <strong>Display:</strong>
The calculator display is an instance of cls_display, a custom class that manages the display of numbers and results of operations. It is connected to several signals that react to user input and update the interface as needed.
- <strong>Slots and Connections:</strong>
We use the PySide6 concept of slots to define the functions that will be executed in response to the events generated by the buttons. For example, the _mtd_invertnumber method inverts the sign of the number currently displayed on the display:

https://linktr.ee/edsoncopque
## Images of the calculator

![2024-05-06](https://github.com/ecopque/basic_calculator/blob/main/files/A000_-_vscode.png)
![2024-05-06](https://github.com/ecopque/basic_calculator/blob/main/files/A010_-_map.png)
![2024-05-06](https://github.com/ecopque/basic_calculator/blob/main/files/A020_-_vscalc.png)
