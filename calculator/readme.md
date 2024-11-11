# Calculator Application

This is a basic calculator application built with Python and Tkinter. The app provides essential calculator functions, including addition, subtraction, multiplication, and division, in a simple, user-friendly GUI for Windows.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Requirements](#requirements)
- [Usage](#usage)
- [Code Overview](#code-overview)
- [Customization](#customization)

---


![Calculator Screenshot](https://github.com/negarslh97/Mini-project/blob/main/calculator/image.png) 

## Features

- **Basic Arithmetic Operations**: Perform addition, subtraction, multiplication, and division.
- **Clear Button**: Reset the calculator to start a new calculation.
- **Modern Design**: Styled with a dark theme for a sleek, modern look.
- **Responsive Layout**: Button resizing and grid arrangement for a better user experience.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/negarslh97/Mini-project.git
   cd Mini-project/calculator
   ```

2. **Run the application**:
   Make sure you have Python 3 installed, then run the app with:
   ```bash
   python main.py
   ```

## Requirements

- **Python 3.x**: This app uses Python's built-in Tkinter library, which comes pre-installed with Python.
- **Tkinter**: Tkinter is included with Python installations by default, but if not installed, you can add it with:
  ```bash
  pip install tk
  ```

## Usage

1. **Start the App**: Run `main.py` to open the calculator window.
2. **Perform Calculations**:
   - Use the buttons to input numbers and operations.
   - Press `=` to calculate the result.
   - Use `Clear` to reset the calculation.
3. **Exit**: Close the window to exit the app.

## Code Overview

- **`main.py`**: Contains the main code for the calculator application.
  - **`press(num)`**: Adds each button press to the expression.
  - **`equal_press()`**: Evaluates the current expression.
  - **`clear()`**: Resets the calculator display.

## Customization

You can modify the calculator's appearance by changing the colors, fonts, or button layout in the code. For example:
- **Button Colors**: Customize button backgrounds and text colors in the `button_bg`, `button_fg`, and `highlight_bg` variables.
- **Font**: Modify the font family, size, and style in the `font.Font` configurations.

