# Input API

- [Input API](#input-api)
  - [1.1. A Brief Description of Input API](#11-a-brief-description-of-input-api)
  - [1.2. Basic Usage](#12-basic-usage)
    - [Numerical input](#numerical-input)
    - [Clearing the terminal](#clearing-the-terminal)
    - [Boolean input](#boolean-input)
  - [1.3. Advanced Usage](#13-advanced-usage)
    - [Numbers](#numbers)
      - [Integers](#integers)
        - [The newLineInt input](#the-newlineint-input)
        - [The sameLineInt input](#the-samelineint-input)
        - [Error treatment and handling](#error-treatment-and-handling)
      - [Floating point](#floating-point)
        - [newLineFloat input](#newlinefloat-input)
        - [sameLineFloat](#samelinefloat)
        - [Error handling and treatment](#error-handling-and-treatment)

## 1.1. A Brief Description of Input API

Input API is a python package made and maintained by Nathan K for the express purpose of making CLI (Command Line Interface) I/O both easier and simpler!When using Input API you are given several options for input, including but not limited to:

- Numbers
  - Both integers and floating point numbers
- Booleans
- Strings
- Menus

## 1.2. Basic Usage

Now for all of the examples of use we will be importing like so:

```python
import inputapi as inp
```

Note: This way of importing is easier for IDE's that don't have an "Auto-Complete" or "AI-assisted dev." feature

When importing Input API we have what is called 'The Basic Library'.
The Basic Library while making usage easier it is also backwards compatible with 1.X versions of Input API without having to rewrite the code.

### Numerical input

With numerical input you can access both floating point and integer numbers!
An integer input is used as shown:

```python
import inputapi as inp

inp.newLineInt({params})
```

Note: We will cover parameters in [Advanced Usage](#13-advanced-usage)

Floating point numbers can be used as shown:

```python
import inputapi as inp

inp.newLineInt({params})
```

### Clearing the terminal

If you wish to clear the terminal by using the clearScreen function[^1]:

```python
import inputapi as inp

inp.clearScreen()
```

### Boolean input

If you need a boolean input we have out yesNo function for that exact reason!

```python
import inputapi as inp

inp.yesNo({params})
```

Fun Fact[^3]: yesNo is the only input to be in the boolean category making it the loneliest function in the package!

## 1.3. Advanced Usage

This style of usage is good for if you need specific input. We will also include the parameters for the inputs with examples.

### Numbers

#### Integers

Integers serve the purpose of returning integers, integers have two ways to input:

| Type of input |              Best case for use              |
| :------------ | :-----------------------------------------: |
| New Line      |    When there are small amounts of input    |
| Same Line     | When there is a lot of inputs in succession |

##### The newLineInt input

There are two ways to use this input:

```python
import inputapi as inp

#This is the basic way of using newLineInt
inp.newLineInt({params})
```

```python
import inputapi as inp

#This is the advanced way of using newLineInt
inp.numerical.integer.newLineInt({params})
```

newLineInt will output the request like this:

```python
#For this example the request string is "Number:"

Number:
>
#The ">" is where the user will input the number
```

The parameters for the input are as follows:

| Parameter     | data type | default               | Purpose it serves                                           |
| :------------ | :-------- | :-------------------- | :---------------------------------------------------------- |
| request       | string    | `"Input an integer:"` | What the user will see when the input is requested          |
| allowNeg      | boolean   | `True`                | Determines if the user can give a negative number           |
| min           | integer   | No limit              | What is the lowest number allowed                           |
| max           | integer   | No limit              | What is the highest number allowed                          |
| clearOnLoad   | boolean   | `False`               | When the function is run, should the terminal be cleared    |
| clearWhenDone | boolean   | `False`               | When the input is retrieved, should the terminal be cleared |

##### The sameLineInt input

The sameLineInt has only one way to access the function:

```python
import inputapi as inp

inp.numerical.integer.sameLineInt({params})
```

This is what sameLineInt will output:

```python
#For this example we will have two requests, one will be "X=" and the other will be "Y="

#This is the first request
X=
#And when "X" has been given the next request is shown
Y=

#The user will enter the number at the end of the string
```

You can find the parameters [here](#the-newlineint-input)

##### Error treatment and handling

When the inputs face invalid characters, we have error messages to show the user what is allowed and what isn't:

```python
#This error message will appear when the user inputs an invalid character, in this case we will put a decimal in

Number:
>21.6
ERROR: Invalid character ['.'], to ensure the program runs correctly please enter only these characters ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-']
```

```python
#This one will be displayed when inputing a negative number when negative numbers are disabled


X=-16
ERROR: Invalid character ['-'], to ensure the program runs correctly please enter only these characters ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
```

```python
#For this example we will put in a number under the minimum

Y=4
ERROR: Number [4] below minimum [5]
```

For going over the max there are two messages.  
What is picked is depending on the amount of digits for both max and what is entered:

```python
#A number that is greater than max (Same amount of digits as max)

Enter 433724:
>433725
ERROR: Number [433725] above maximum [433724]
```

```python
#We will go above the maximum for this example (More digits than max has)

Enter a 6 digit number:
>581919921
ERROR: Too many characters, maximum amount is [6] characters, you entered [9]
```

#### Floating point

Floating point inputs are great for decimal numbers (e.g. The radius of a circle, width of a box).  
We have two ways for requesting an float:

| Type of input |                            Best use case                             |
| :------------ | :------------------------------------------------------------------: |
| newLineFloat  |                 Small amount of inputs in succession                 |
| sameLineFloat | Multiple inputs with each one after another, or retrieving variables |

##### newLineFloat input

Calling the function can be done in two ways:

```python
import inputapi as inp

#Basic usage
inp.newLineFloat({params})
```

```python
import inputapi as inp

#Advanced usage
inp.numerical.float.newLineFloat({params})
```

When using newLineFloat you get an output similar to [newLineInt](#the-newlineint-input)

```python
#This time the request is "Number including decimal:"

Number including decimal:
>
```

The parameters for newLineFloat are very similar to integer inputs but are as follows:

| Parameter     | data type | default               | Purpose it serves                                           |
| :------------ | :-------- | :-------------------- | :---------------------------------------------------------- |
| request       | string    | `"Input an integer:"` | What the user will see when the input is requested          |
| allowNeg      | boolean   | `True`                | Determines if the user can give a negative number           |
| min           | integer   | No limit              | What is the lowest number allowed                           |
| max           | integer   | No limit              | What is the highest number allowed                          |
| clearOnLoad   | boolean   | `False`               | When the function is run, should the terminal be cleared    |
| clearWhenDone | boolean   | `False`               | When the input is retrieved, should the terminal be cleared |

##### sameLineFloat

sameLineFloat has only one way to be used:

```python
import inputapi as inp

inp.numerical.float.sameLineFloat({params})
```

The input function outputs like so:

```python
#Request string is "Float="

Float=
```

Parameters are found [here](#floating-point).

##### Error handling and treatment

For most of these can be found in [the integer's error handling](#error-treatment-and-handling) except for one error.  
When dealing with decimal points ("."), it can't just be blocked, so we have a solution from the 1.X versions of the Input API:

```python
#The conversion from straight string to float only works if all charecters are numbers and there are no more that one decimal point
#So this is what will happen if we try to break it

Only one decimal point:
>2.2.2
#The result is 2.22
```

How this works is when there is more than one point (e.g. `1.2.3`), it will only acknowledge the first decimal place and remove the others (`1.2.3` -> `1.23`).

[^1]:
    clearScreen is does not need any information about the OS to work[^2]
    It will automatically tell what OS is running the code and use the command used by the OS to clear the terminal

[^2]: Feature is only supported on Windows, MacOS, and Linux based systems
[^3]: Fun Fact's although being labeled as "Fun" is more fact than fun and could be a "Sad Fact" depending on the fact!
