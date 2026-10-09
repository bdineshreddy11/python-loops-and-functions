#  Python Programming — Loops, Control Statements & Functions

A practical collection of Python programs demonstrating iteration, loop control, reusable functions, user input, and mathematical calculations through simple, real-world programming examples.

---

## 📌 About the Project

This project focuses on strengthening Python fundamentals through three programs:

* 🎯 **Number Guessing Game** — Random number generation and loop control.
* ✖️ **Multiplication Table Generator** — Iteration using `for` and `range()`.
* ⚖️ **BMI Calculator** — Function definition, parameters, return values, and mathematical calculations.

Each program demonstrates a different programming concept and provides an opportunity to practice problem-solving.

---

## 📂 Project Structure

```text
Python-Loops-and-Functions/
│
├── number_guessing_game.py
├── multiplication_table.py
├── bmi_calculator.py
└── README.md
```

---

## 🎯 1. Number Guessing Game

### Objective

Create a game in which the user tries to guess a randomly generated number between 1 and 10.

### Concepts Used

* `while` loop
* `if`, `elif`, and `else`
* `break` and `continue`
* `random` module
* User input and conditional logic

### How It Works

1. Generate a random number between 1 and 10 using `random.randint()`.
2. Set the maximum number of valid guesses to three.
3. Ask the user to enter a guess.
4. Display a message if the guess is outside the valid range.
5. Inform the user if the guess is too high or too low.
6. Stop the loop when the user guesses correctly.
7. Display a message when all valid attempts are exhausted.

### Sample Output

```text
Guess the number (between 1 and 10): 2
Too low. Try again.

Guess the number (between 1 and 10): 15
Your guess is out of range.
Please guess a number between 1 and 10.

Guess the number (between 1 and 10): 5
Congratulations! You guessed the correct number.
```

**Key Learning:** Use `continue` to skip the remaining statements in the current iteration and `break` to exit a loop immediately. A `while-else` clause runs when the loop finishes normally without being terminated by `break`.

---

## ✖️ 2. Multiplication Table Generator

### Objective

Generate a multiplication table from 1 to 10 for a number entered by the user.

### Concepts Used

* `for` loop
* `range()` function
* User input
* Type conversion using `int()`
* Arithmetic operators
* Formatted strings (f-strings)

### How It Works

1. Ask the user to enter a number.
2. Use `range(1, 11)` to iterate from 1 through 10.
3. Multiply the entered number by each iteration value.
4. Display the multiplication expression and result.

### Sample Output

```text
Enter the number for which you want the multiplication table: 5

5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
```

**Key Learning:** `range(1, 11)` generates values from 1 to 10 because the ending value, 11, is excluded.

---

## ⚖️ 3. BMI Calculator

### Objective

Calculate Body Mass Index (BMI) using a user-defined Python function.

### Concepts Used

* Function definition using `def`
* Function parameters and arguments
* `return` statement
* Floating-point numbers
* Arithmetic operations
* Output formatting

### Formula

$$
BMI = \frac{\text{Weight (kg)}}{\text{Height (m)}^2}
$$

### How It Works

1. Define the function `calculate_bmi(weight, height)`.
2. Accept the user's weight in kilograms.
3. Accept the user's height in meters.
4. Calculate BMI by dividing weight by the square of height.
5. Return the calculated value from the function.
6. Display the result rounded to two decimal places.

### Sample Output

```text
Enter your weight in kg: 58
Enter your height in meters: 1.62

Your BMI is: 22.10
```

**Key Learning:** A function makes code reusable. Parameters receive input values, while `return` sends the calculated result back to the calling code.

*Note: BMI is a screening measure and is not, by itself, a complete assessment of health.*

---

## 🛠️ Technologies and Concepts

| Category             | Details                                |
| -------------------- | -------------------------------------- |
| Programming Language | Python 3                               |
| Standard Library     | `random`                               |
| Loops                | `while`, `for`                         |
| Control Statements   | `break`, `continue`, `else`, `pass`    |
| Functions            | `def`, parameters, arguments, `return` |
| Input and Output     | `input()`, `print()`                   |
| Type Conversion      | `int()`, `float()`                     |
| Formatting           | f-strings, `:.2f`                      |

---

## ⚙️ Requirements

* Python 3 installed on your computer.
* A code editor such as VS Code, PyCharm, or IDLE.
* A terminal or command prompt to execute the programs.

**External packages:** None required. The programs use Python's built-in functionality and standard library.

---

## ▶️ Installation and Execution

### Step 1: Clone the Repository

```bash
git clone <your-repository-url>
```

### Step 2: Navigate to the Project Folder

```bash
cd Python-Loops-and-Functions
```

### Step 3: Run a Program

Run each file separately:

```bash
python number_guessing_game.py
```

```bash
python multiplication_table.py
```

```bash
python bmi_calculator.py
```

On some Windows systems, you may need to use `py` instead of `python`.

---

## 📚 Important Python Concepts

| Concept             | Purpose                                                          |
| ------------------- | ---------------------------------------------------------------- |
| `while`             | Repeats a block while a condition is true.                       |
| `for`               | Iterates over a sequence or iterable.                            |
| `range()`           | Generates a sequence of integers.                                |
| `break`             | Terminates the nearest enclosing loop.                           |
| `continue`          | Skips to the next loop iteration.                                |
| `pass`              | Acts as a placeholder without performing an operation.           |
| `else` with `while` | Executes if the loop ends without `break`.                       |
| `def`               | Defines a reusable function.                                     |
| `return`            | Sends a result back to the caller.                               |
| `random.randint()`  | Generates a random integer within the specified inclusive range. |

---

## 🚀 Future Improvements

* Add input validation for non-numeric values.
* Display the number of guesses used in the guessing game.
* Allow users to choose the multiplication table's ending range.
* Validate that weight and height are positive values.
* Add BMI category interpretation using appropriate adult reference ranges.

---

## 🎓 Learning Outcomes

After completing these programs, you should be able to:

* Write programs using `while` and `for` loops.
* Control loop execution with `break` and `continue`.
* Understand the behavior of the loop `else` clause.
* Explain the purpose of `pass`.
* Define and call functions with parameters and return values.
* Perform calculations using user-provided data.
* Format output for clear and readable results.
* Organize Python programs into separate files.

---

## 👨‍💻 Author

**Python Programming Practice**

*Learning Python through practical coding, problem-solving, and consistent practice.*
