# Terminal Utilities

This repository contains Python scripts for text manipulation and formatting in the terminal. The scripts provide functionality for printing styled messages, applying colors, and creating formatted menus and headers.

## Included Scripts

### 1. `text_utils.py`

This script demonstrates various text printing functions, including transformations to uppercase/lowercase, centering, justification, and substring replacement.

- **Included Functions:**
  - `upper()`
  - `lower()`
  - `capitalize()`
  - `title()`
  - `swapcase()`
  - `center()`
  - `ljust()`
  - `rjust()`
  - `zfill()`
  - `count()`
  - `find()`
  - `rfind()`
  - `index()`
  - `rindex()`
  - `startswith()`
  - `endswith()`
  - `replace()`
  - `split()`
  - `rsplit()`
  - `partition()`
  - `rpartition()`
  - `join()`
  - `strip()`
  - `encode()`
  - `decode()`
  - `isalnum()`
  - `isalpha()`
  - `isascii()`
  - `isdecimal()`
  - `isdigit()`
  - `isidentifier()`
  - `islower()`
  - `isnumeric()`
  - `isprintable()`
  - `isspace()`
  - `istitle()`
  - `isupper()`

### 2. `colors.py`

This script provides a collection of ANSI color codes for styling text and background in the terminal. It includes normal colors, bold colors, and text-background color combinations.

- **Text Colors:**
  - Black, Red, Green, Yellow, Blue, Purple, Cyan, White
- **Background Colors:**
  - Black, Red, Green, Yellow, Blue, Purple, Cyan, White
- **Bold Text Colors:**
  - Variants for each color
- **Combinations:**
  - Variants for every possible combinations of letter colors and background colors, also in bold options

### 3. `interface.py`

This script contains functions for formatting terminal output, including creating lines and menus, and clearing the console.

- **Included Functions:**
  - `line(size)`: Prints a line of characters.
  - `menu(*options, topline=True, bottomline=True, size=42)`: Prints a menu with the provided options.
  - `header(title, topline=True, bottomline=True, size=42)`: Prints a header with the title centered.
  - `clearConsole(cooldown=1)`: Clears the console after a waiting period.

## Usage

To use these scripts, you can import them into your own Python projects or run each script directly to see their functionalities.

## Contributions

Contributions are welcome! If you have improvements or suggestions, feel free to open an issue or submit a pull request.

## Credits

Made with love by [Luan Vieira](https://github.com/lcsvme). Check out my other projects on GitHub!
