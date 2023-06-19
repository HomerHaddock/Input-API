# 1. Input API

- [1. Input API](#1-input-api)
  - [1.1. A Brief Description of Input API](#11-a-brief-description-of-input-api)
  - [Installing Input API](#installing-input-api)
  - [1.2. Basic Usage](#12-basic-usage)
    - [1.2.1. Numerical input](#121-numerical-input)
    - [1.2.2. Clearing the terminal](#122-clearing-the-terminal)
    - [1.2.3. Boolean input](#123-boolean-input)
  - [1.3. Advanced Usage](#13-advanced-usage)
    - [1.3.1. Numbers](#131-numbers)
      - [1.3.1.1. Integers](#1311-integers)
        - [1.3.1.1.1. The newLineInt input](#13111-the-newlineint-input)
        - [1.3.1.1.2. The sameLineInt input](#13112-the-samelineint-input)
        - [1.3.1.1.3. Error treatment and handling](#13113-error-treatment-and-handling)
      - [1.3.1.2. Floating point](#1312-floating-point)
        - [1.3.1.2.1. newLineFloat input](#13121-newlinefloat-input)
        - [1.3.1.2.2. sameLineFloat](#13122-samelinefloat)
        - [1.3.1.2.3. Error treatment and handling](#13123-error-treatment-and-handling)
    - [1.3.2. Strings](#132-strings)
      - [1.3.2.1. newLineStr](#1321-newlinestr)
      - [1.3.2.2. sameLineStr](#1322-samelinestr)
      - [1.3.2.3. Error treatment and handling](#1323-error-treatment-and-handling)
    - [1.3.3. Booleans](#133-booleans)
      - [1.3.3.1. yesNo](#1331-yesno)
      - [1.3.3.2. Error treatment and handling](#1332-error-treatment-and-handling)
    - [1.3.4. Menus](#134-menus)
      - [1.3.4.1. singleSelect menus](#1341-singleselect-menus)
        - [1.3.4.1.1. numericSerial](#13411-numericserial)
          - [1.3.4.1.1.1. Usage](#134111-usage)
          - [1.3.4.1.1.2. Parameters](#134112-parameters)
          - [1.3.4.1.1.3. Output](#134113-output)
          - [1.3.4.1.1.4. Error treatment and handling](#134114-error-treatment-and-handling)
        - [1.3.4.1.2. numericIndex](#13412-numericindex)
          - [1.3.4.1.2.1. Usage](#134121-usage)
          - [1.3.4.1.2.2. Parameters](#134122-parameters)
          - [1.3.4.1.2.3. Output](#134123-output)
          - [1.3.4.1.2.4. Error treatment and handling](#134124-error-treatment-and-handling)
        - [1.3.4.1.3. alphabetical](#13413-alphabetical)
          - [1.3.4.1.3.1. Usage](#134131-usage)
          - [1.3.4.1.3.2. Parameters](#134132-parameters)
          - [1.3.4.1.3.3. Output](#134133-output)
          - [1.3.4.1.3.4. Error treatment and handling](#134134-error-treatment-and-handling)
      - [1.3.4.2. multiSelect menus](#1342-multiselect-menus)
        - [1.3.4.2.1. returnSelected menus](#13421-returnselected-menus)
          - [1.3.4.2.1.1. numericSerial](#134211-numericserial)
          - [1.3.4.2.1.2. Usage](#134212-usage)
          - [1.3.4.2.1.3. Parameters](#134213-parameters)
          - [1.3.4.2.1.4. Output](#134214-output)
          - [1.3.4.2.1.5. Error treatment and handling](#134215-error-treatment-and-handling)
        - [1.3.4.2.2. returnDeselected](#13422-returndeselected)
          - [1.3.4.2.2.1. numericSerial](#134221-numericserial)
          - [1.3.4.2.2.2. Usage](#134222-usage)
          - [1.3.4.2.2.3. Parameters](#134223-parameters)
          - [1.3.4.2.2.4. Output](#134224-output)
          - [1.3.4.2.2.5. Error treatment and handling](#134225-error-treatment-and-handling)
    - [1.3.5. RDCs](#135-rdcs)
      - [1.3.5.1. RDC](#1351-rdc)
        - [1.3.5.1.1. Usage](#13511-usage)
        - [1.3.5.1.2. Parameters](#13512-parameters)
        - [1.3.5.1.3. Output](#13513-output)
        - [1.3.5.1.4. Error treatment and handling](#13514-error-treatment-and-handling)
      - [1.3.5.2. newLineRDC](#1352-newlinerdc)
        - [1.3.5.2.1. Usage](#13521-usage)
        - [1.3.5.2.2. Parameters](#13522-parameters)
        - [1.3.5.2.3. Output](#13523-output)
        - [1.3.5.2.4. Error treatment and handling](#13524-error-treatment-and-handling)
      - [1.3.5.3. sameLineRDC](#1353-samelinerdc)
        - [1.3.5.3.1. Usage](#13531-usage)
        - [1.3.5.3.2. Parameters](#13532-parameters)
        - [1.3.5.3.3. Output](#13533-output)
        - [1.3.5.3.4. Error treatment and handling](#13534-error-treatment-and-handling)
    - [1.3.6. otherFunc](#136-otherfunc)
      - [1.3.6.1. pause](#1361-pause)
        - [1.3.6.1.1. standard](#13611-standard)
          - [1.3.6.1.1.1. Usage](#136111-usage)
          - [1.3.6.1.1.2. Parameters](#136112-parameters)
          - [1.3.6.1.1.3. Output](#136113-output)
          - [1.3.6.1.1.4. Error treatment and handling](#136114-error-treatment-and-handling)
        - [1.3.6.1.2. showValue](#13612-showvalue)
          - [1.3.6.1.2.1. Usage](#136121-usage)
          - [1.3.6.1.2.2. Parameters](#136122-parameters)
          - [1.3.6.1.2.3. Error treatment and handling](#136123-error-treatment-and-handling)
      - [1.3.6.2. clearScreen](#1362-clearscreen)
        - [1.3.6.2.1. auto](#13621-auto)
          - [1.3.6.2.1.1. Usage](#136211-usage)
        - [1.3.6.2.2. manual](#13622-manual)
          - [1.3.6.2.2.1. Usage](#136221-usage)
          - [1.3.6.2.2.2. Parameters](#136222-parameters)
          - [1.3.6.2.2.3. How to properly use manual](#136223-how-to-properly-use-manual)
  - [1.4. TODO](#14-todo)
    - [1.4.1. In Major Updates](#141-in-major-updates)
      - [1.4.1.1. Pre-set Inputs](#1411-pre-set-inputs)
      - [1.4.1.2. Iterable Inputs](#1412-iterable-inputs)
      - [1.4.1.3. A Config Function](#1413-a-config-function)
      - [1.4.1.4. Call later/repeat input](#1414-call-laterrepeat-input)
    - [1.4.2. In Minor Updates](#142-in-minor-updates)
      - [1.4.2.1. New multiSelect Menu Types](#1421-new-multiselect-menu-types)
      - [1.4.2.2. New singleSelect Menu Type](#1422-new-singleselect-menu-type)
      - [1.4.2.3. Adding A Changelog](#1423-adding-a-changelog)

## 1.1. A Brief Description of Input API

Input API is a python package made and maintained by Homer Haddock for the express purpose of making terminal I/O both easier and simpler! When using Input API you are given several options for input, including but not limited to:

- Numbers
  - Both integers and floating point numbers
- Booleans
- Strings
- Menus

## Installing Input API

When receiving a copy of Input API you need to install it first, here is a short tutorial on how to install the Input API.

1. Install Python (v3.7 or greater)
2. Open the folder that has the .whl file for the Input API (e.g. `inputapi-2.0.0-py3-none-any.whl`)
3. Open the .whl file with your Python installation (Not IDLE)
4. Wait for the window to close
5. Input API has been globally installed on your computer

If you are using a virtual environment you just run.

For Windows:

`pip install Path/To/File.whl`

For Linux:

`python3 -m pip install Path/To/File.whl`

## 1.2. Basic Usage

Now for all of the examples of use we will be importing like so:

```python
import inputapi as inp
```

Note: This way of importing is easier for IDE's that don't have an "Auto-Complete" or "AI-assisted dev." feature

When importing Input API we have what is called 'The Basic Library'.
The Basic Library while making usage easier it is also backwards compatible with 1.X versions of Input API without having to rewrite the code.

### 1.2.1. Numerical input

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

### 1.2.2. Clearing the terminal

If you wish to clear the terminal by using the clearScreen function[^1]:

```python
import inputapi as inp

inp.clearScreen()
```

### 1.2.3. Boolean input

If you need a boolean input we have out yesNo function for that exact reason!

```python
import inputapi as inp

inp.yesNo({params})
```

Fun Fact[^3]: yesNo is the only input to be in the boolean category making it the loneliest function in the package!

## 1.3. Advanced Usage

This style of usage is good for if you need specific input. We will also include the parameters for the inputs with examples.

### 1.3.1. Numbers

#### 1.3.1.1. Integers

Integers serve the purpose of returning integers, integers have two ways to input:

| Type of input |              Best case for use              |
| :------------ | :-----------------------------------------: |
| New Line      |    When there are small amounts of input    |
| Same Line     | When there is a lot of inputs in succession |

##### 1.3.1.1.1. The newLineInt input

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

##### 1.3.1.1.2. The sameLineInt input

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

You can find the parameters [here](#13111-the-newlineint-input)

##### 1.3.1.1.3. Error treatment and handling

When the inputs face invalid characters, we have error messages to show the user what is allowed and what isn't:

```python
#This error message will appear when the user inputs an invalid character, in this case we will put a decimal in

Number:
>21.6
WARNING: Invalid character ['.'], to ensure the program runs correctly please enter only these characters ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-']
```

```python
#This one will be displayed when inputing a negative number when negative numbers are disabled


X=-16
WARNING: Invalid character ['-'], to ensure the program runs correctly please enter only these characters ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
```

```python
#For this example we will put in a number under the minimum

Y=4
WARNING: Number [4] below minimum [5]
```

For going over the max there are two messages.  
What is picked is depending on the amount of digits for both max and what is entered:

```python
#A number that is greater than max (Same amount of digits as max)

Enter 433724:
>433725
WARNING: Number [433725] above maximum [433724]
```

```python
#We will go above the maximum for this example (More digits than max has)

Enter a 6 digit number:
>581919921
WARNING: Too many characters, maximum amount is [6] characters, you entered [9]
```

#### 1.3.1.2. Floating point

Floating point inputs are great for decimal numbers (e.g. The radius of a circle, width of a box).  
We have two ways for requesting an float:

| Type of input |                            Best use case                             |
| :------------ | :------------------------------------------------------------------: |
| newLineFloat  |                 Small amount of inputs in succession                 |
| sameLineFloat | Multiple inputs with each one after another, or retrieving variables |

##### 1.3.1.2.1. newLineFloat input

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

When using newLineFloat you get an output similar to [newLineInt](#13111-the-newlineint-input)

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

##### 1.3.1.2.2. sameLineFloat

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

Parameters are found [here](#1312-floating-point).

##### 1.3.1.2.3. Error treatment and handling

For most of these can be found in [the integer's error handling](#13113-error-treatment-and-handling) except for one error.  
When dealing with decimal points ("."), it can't just be blocked, so we have a solution from the 1.X versions of the Input API:

```python
#The conversion from straight string to float only works if all charecters are numbers and there are no more that one decimal point
#So this is what will happen if we try to break it

Only one decimal point:
>2.2.2
#The result is 2.22
```

How this works is when there is more than one point (e.g. `1.2.3`), it will only acknowledge the first decimal place and remove the others (`1.2.3` -> `1.23`).

### 1.3.2. Strings

Strings works like `input()` but allows for more options and helps with error handling so you don't need something like this copy and pasted 20 times:

```python
while True:
  user = input(request)
  try:
    convert(user)
  except:
    continue
  else:
    break
#convert() is the stand in for what you wan't the string converted to
```

Strings were first introduced in Input API version 1.2.0 as newLineStr, got a bug fix in 1.2.1 (Like an hour after 1.2.0 got built).  
Everything[^4] in the Input API is dependant on the string input since it gives more viability and ease of use. There are two types of string input and they are:

| Type of input |                                                                         Best use case                                                                         |
| :------------ | :-----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| newLineStr    |                                                             Small amount of inputs in succession                                                              |
| sameLineStr   | Multiple inputs with each one after another, getting multiple strings, and replacing the character that sits left of the user input (`>`) with something else |

#### 1.3.2.1. newLineStr

newLineStr has (for the thousandth time) two ways to be used:

```python
import inputapi as inp

#First way
inp.newLineStr({params})
```

```python
import inputapi as inp

#Second way
inp.strings.newLineStr({params})
```

When using the newLineStr the user using the program will have this as the output:

```python
#The request, "String:"

String:
>
```

We have the parameters for newLineStr as:

| Parameter     | data type | default             | Purpose                                                                                 |
| :------------ | :-------- | :------------------ | :-------------------------------------------------------------------------------------- |
| request       | string    | `'Input a string:'` | Is displayed when requesting input                                                      |
| minLength     | integer   | `0`                 | Amount of characters needed for input                                                   |
| maxLength     | integer   | None                | Max amount of characters allowed in input                                               |
| allowOnly     | string    | None                | Only allows an input if all characters are within the string, (Does nothing if default) |
| clearOnLoad   | boolean   | `False`             | Clears terminal before loading input                                                    |
| clearWhenDone | boolean   | `False`             | Clears terminal after getting input                                                     |

#### 1.3.2.2. sameLineStr

sameLineStr has only one way to be used:

```python
import inputapi as inp

#Only way
inp.strings.sameLineStr({params})
```

The output for sameLineStr is:

```python
#The request, "String="
String=
```

The parameters for sameLineStr are:
| Parameter | data type | default | Purpose |
| :------------ | :-------- | :---------- | :-------------------------------------------------------------------------------------- |
| request | string | `'String='` | Is displayed when requesting input |
| minLength | integer | `0` | Amount of characters needed for input |
| maxLength | integer | None | Max amount of characters allowed in input |
| allowOnly | string | None | Only allows an input if all characters are within the string, (Does nothing if default) |
| clearOnLoad | boolean | `False` | Clears terminal before loading input |
| clearWhenDone | boolean | `False` | Clears terminal after getting input |

#### 1.3.2.3. Error treatment and handling

When it comes to error handling on strings, we have three potential errors that can happen:

```python
#This happens when the user inputs less than the minimum amount of characters

Just enter three characters:
>No
WARNING: Input requires [3] characters or more, you entered [2]
```

```python
#This happens when the user inputs more than the maximum amount of characters

Three characters or less:
>Four
WARNING: Input requires [3] characters or less, you entered [4]
```

There are three separate messages related to `allowOnly` depending on length of the amount allowed:

```python
#When there is less than 20 characters allowed
#In this case there is only numbers allowed

Number=Boo!
WARNING: Input has invalid character [B], allowed characters are [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
```

```python
#When there is more than 30 characters allowed
#In this case there is only letters and numbers allowed

Enter only what a normal person would:
>!@\#$%^&*()_+-=
WARNING: Input has invalid character [!], allowed characters are [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t ... 5, 6, 7, 8, 9]
```

```python
#This is what happens when there is more than 20 but less than 30 characters allowed
#In this case there is only lowercase letters and isn't 'a' allowed

Please don't yell:
>AAAAA
WARNING: Input has invalid character [A], allowed characters are [b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u ... z]
```

### 1.3.3. Booleans

The only boolean input there is is `yesNo` which is a boolean input that only allows for `y` or `n` as input. When input is given it will turn it into a boolean value (`True` or `False`).

The Booleans best case use is for when you want to get a yes or no answer from the user. It is also used in the `confirm` input. (Refer to menus for more info about confirming input [Placeholder Link For Menus])

#### 1.3.3.1. yesNo

yesNo has two ways to be used:

```python
import inputapi as inp

#The simple way
inp.yesNo({params})
```

```python
import inputapi as inp

#The hard way
inp.boolean.yesNo({params})
```

yesNo has two different outputs:

```python
#When numeric input is allowed (default)
#This is was added in 2.0.0

#Request is 'Do you breathe air?'
Do you breathe air?
Numeric response allowed (Y=1, n=2)
[Y/n]:
```

```python
#When numeric isn't allowed
#Request is 'Is your fride running?'

Is your fridge running?
[Y/n]:
```

The parameters for yesNo are:
| Parameter | data type | default | Purpose |
| :------------ | :-------- | :------------- | :----------------------------------- |
| request | string | `'Yes or no?'` | Is displayed when requesting input |
| allowNumeric | boolean | `True` | Allows for numeric input (Y=1, n=2) |
| clearOnLoad | boolean | `False` | Clears terminal before loading input |
| clearWhenDone | boolean | `False` | Clears terminal after getting input |

#### 1.3.3.2. Error treatment and handling

The errors in yesNo mainly happen through the sameLineStr but they are:

```python
#When something not allowed is entered (More than 1 character)

Did you catch the fridge?
Numeric response allowed (Y=1, n=2)
[Y/n]:Still trying to
WARNING: Input requires [1] characters or less, you entered [15] characters
```

```python
#Something not allowed is entered (Numeric not allowed)

Can you see me?
[Y/n]:1
WARNING: Input has invalid character [1], allowed characters are ['Y', 'N', 'y', 'n']
```

### 1.3.4. Menus

Menus allow the user to select a set of given options, there could be only one to select or multiple.

#### 1.3.4.1. singleSelect menus

These menus present multiple options but only allow the user to pick one. These can be used for the 'main hub' of a program to use other functions and return after. The returned value is the value assigned to the option.

##### 1.3.4.1.1. numericSerial

The numericSerial is the menu used in 1.X versions of Input API. All options are given a number from 1 to length of options given.

###### 1.3.4.1.1.1. Usage

Two ways to call and use this function.

```python
#The 1.X version of using the function
import inputapi as inp

inp.menu({params})
```

```python
#The new way of using numericSerial
import inputapi as inp

inp.menus.singleSelect.numericSerial({params})
```

###### 1.3.4.1.1.2. Parameters

The parameters of numericSerial are as follows:

| Parameter     | data type | default    | purpose                                                                  |
| :------------ | :-------- | :--------- | :----------------------------------------------------------------------- |
| \*args        | Any       | No default | Options that are displayed to the user                                   |
| clearOnLoad   | boolean   | `False`    | Clears terminal before displaying output                                 |
| clearWhenDone | boolean   | `False`    | Clears terminal after user gives input                                   |
| title         | string    | `'Menu'`   | What will be displayed as the name/purpose of the menu (`---{title}---`) |

###### 1.3.4.1.1.3. Output

The output of the numericSerial is:

```python
#An example of game option selection is

#Note: Titles have a white background and black text
#but cannot be rendered properly in markdown
---Where do you go?---
1: To the blazing inferno
2: To the tree that reads books

To select an option input the number assigned to it:
>
```

###### 1.3.4.1.1.4. Error treatment and handling

The errors of numericSerial is the [newLineInt error treatment hand handling](#13113-error-treatment-and-handling) with the following exception:

```python
#When giving a response not within the given options it will just ignore it

---What animal do you prefer---
1: Cat
2: Dog

To select an option input the number assigned to it:
>3
To select an option input the number assigned to it:
>
```

##### 1.3.4.1.2. numericIndex

The numericIndex menu is almost the same as [numericSerial](#13411-numericserial) with the exception that instead of starting at 1 instead it starts at 0.

###### 1.3.4.1.2.1. Usage

There is only one way to use numericIndex:

```python
import inputapi as inp

inp.menus.singleSelect.numericIndex({params})
```

###### 1.3.4.1.2.2. Parameters

The parameters of numericIndex are the same as [numericSerial](#134112-parameters):

| Parameter     | data type | default    | purpose                                                                  |
| :------------ | :-------- | :--------- | :----------------------------------------------------------------------- |
| \*args        | Any       | No default | Options that are displayed to the user                                   |
| clearOnLoad   | boolean   | `False`    | Clears terminal before displaying output                                 |
| clearWhenDone | boolean   | `False`    | Clears terminal after user gives input                                   |
| title         | string    | `'Menu'`   | What will be displayed as the name/purpose of the menu (`---{title}---`) |

###### 1.3.4.1.2.3. Output

This is what the menu would output when called:

```python
#Now lets show what a 'main hub' of a script could look like

---Cool Math Program---
0: Algebra
1: Geometry
2: Calculus
3: Quit

To select an option input the number assigned to it:
>
```

###### 1.3.4.1.2.4. Error treatment and handling

It's just the same as [numericSerial](#134114-error-treatment-and-handling).

##### 1.3.4.1.3. alphabetical

The alphabetical menu is the most unique of all singleSelect menus being that instead of using numbers as the selectable options it uses the Modern Latin Alphabet (aka The English Alphabet).

###### 1.3.4.1.3.1. Usage

Only one way to use the function:

```python
import inputapi as inp

inp.menus.singleSelect.alphabetical({params})
```

###### 1.3.4.1.3.2. Parameters

The parameters are the same as [numericSerial and numericIndex](#134112-parameters):

| Parameter     | data type | default    | purpose                                                                  |
| :------------ | :-------- | :--------- | :----------------------------------------------------------------------- |
| \*args        | Any       | No default | Options that are displayed to the user                                   |
| clearOnLoad   | boolean   | `False`    | Clears terminal before displaying output                                 |
| clearWhenDone | boolean   | `False`    | Clears terminal after user gives input                                   |
| title         | string    | `'Menu'`   | What will be displayed as the name/purpose of the menu (`---{title}---`) |

###### 1.3.4.1.3.3. Output

The output of alphabetical is as follows:

```python
#This could be used for trivia questions
#Also the correct statement is 'C'

---Guess The Correct Statement---
A: The plural word for octopus is octopi
B: Luigi`s last name is Luigi since Mario`s is Mario
C: In a State of the US it is illegal to wear a fake mustache to church if it makes someone laugh

To select an option input the letters next to it:
>
```

When given more options than character an additional character will be given:

```python
#I can't bother making something creative for this

---Select One---
A: Option 1
B: Option 2
C: Option 3
...
X: Option 24
Y: Option 25
Z: Option 26
AA: Option 27
```

###### 1.3.4.1.3.4. Error treatment and handling

It is actually the same as [numericSerial](#134114-error-treatment-and-handling) with the following exception.

```python
#Since it uses different characters for input this is the message for invalid characters

---What is the better number?---
A: 1
B: 2

To select an option input the letters next to it:
>1
WARNING: Input has invalid character [1], allowed characters are ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O' ... 'v', 'w', 'x', 'y', 'z']
>
```

#### 1.3.4.2. multiSelect menus

With multiSelect menus instead of only allowing one option to be selected you can select more than one, hence the name 'multiSelect' and 'singleSelect'.

##### 1.3.4.2.1. returnSelected menus

returnSelected menus return what was selected by the user.
(Since the header limit is reached the one menu will have it's documentation outside of it's normal bounds)

###### 1.3.4.2.1.1. numericSerial

numericSerial has near same functionality as [singleSelect numericSerial](#13411-numericserial) except for a few changes to allow it to be multiSelect.

###### 1.3.4.2.1.2. Usage

The only menu there is has only one way to be used.

```python
import inputapi as inp

inp.menus.multiSelect.returnSelected.numericSerial({params})
```

###### 1.3.4.2.1.3. Parameters

The parameters for the multiSelect menu are:

| Parameter             | data type | default    | purpose                                                                  |
| :-------------------- | :-------- | :--------- | :----------------------------------------------------------------------- |
| \*args                | Any       | No default | Options that are displayed to the user                                   |
| confirmChoice         | boolean   | `True`     | Ensures that what the user selected was what they intended to select     |
| showSelectedOnRefresh | boolean   | `True`     | Allows users to see what they selected (See Output for further detail)   |
| allowNoSelection      | boolean   | `False`    | Allows the user to simply select nothing                                 |
| clearOnLoad           | boolean   | `False`    | Clears terminal before displaying output                                 |
| cleanOnRefresh        | boolean   | `False`    | Clears terminal when an option is selected                               |
| clearWhenDone         | boolean   | `False`    | Clears terminal after user selects options                               |
| title                 | string    | `'Menu'`   | What will be displayed as the name/purpose of the menu (`---{title}---`) |

###### 1.3.4.2.1.4. Output

The output in a single state is almost identical to [numericSerial](#13411-numericserial) but the difference between selections is what will be documented.

```python
#For our first output we will have all values default
#You can replecate this with
#inp.menus.multiSelect.returnSelected.numericSerial('Option 1', 'Option 2', 'Option 3')

---Menu---
1: Option 1
2: Option 2
3: Option 3
0: Done

Multiple selection menu
To select an option input the number next to it:
>1

---Menu---
1: *Option 1
2: Option 2
3: Option 3
0: Done

Multiple selection menu
To select an option input the number next to it:
>2

---Menu---
1: *Option 1
2: *Option 2
3: Option 3
0: Done

Multiple selection menu
To select an option input the number next to it:
>3

---Menu---
1: *Option 1
2: *Option 2
3: *Option 3
0: Done

Multiple selection menu
To select an option input the number next to it:
>2

---Menu---
1: *Option 1
2: Option 2
3: *Option 3
0: Done

Multiple selection menu
To select an option input the number next to it:
>0

Option 1, Option 3
Confirm choice?
Numeric response allowed (Y=1, n=2)
[Y/n]:1

# This returned ['Option 1', 'Option 3']
```

But when showSelectedOnRefresh is `False` you get a different output.

```python
#This one will be recreated with
#inp.menus.multiSelect.returnSelected.numericSerial('Option 1', 'Option 2', 'Option 3', showSelectedOnRefresh=False)

---Menu---
1: Option 1
2: Option 2
3: Option 3
0: Done

Multiple selection menu
To select an option input the number next to it:
>1

---Menu---
1: *Option 1
2: Option 2
3: Option 3
0: Done

Multiple selection menu
To select an option input the number next to it:
>2

---Menu---
1: *Option 1
2: *Option 2
3: Option 3
0: Done

Multiple selection menu
To select an option input the number next to it:
>3

---Menu---
1: *Option 1
2: *Option 2
3: *Option 3
0: Done

Multiple selection menu
To select an option input the number next to it:
>2

---Menu---
1: *Option 1
2: Option 2
3: *Option 3
0: Done


---Menu---
1: Option 1
2: Option 2
3: Option 3
0: Done

Multiple selection menu
To select an option input the number next to it:
>1

---Menu---
1: Option 2
2: Option 3
0: Done

Multiple selection menu
To select an option input the number next to it:
>2

---Menu---
1: Option 2
0: Done

Multiple selection menu
To select an option input the number next to it:

---Menu---
1: Option 1
2: Option 2
3: Option 3
0: Done

Multiple selection menu
To select an option input the number next to it:
>1

---Menu---
1: Option 2
2: Option 3
0: Done

Multiple selection menu
To select an option input the number next to it:
>2

---Menu---
1: Option 2
0: Done

Multiple selection menu
To select an option input the number next to it:
>1

Option 1, Option 2, Option 3
Confirm choice?
Numeric response allowed (Y=1, n=2)
[Y/n]:y

#This returned ['Option 1', 'Option 2', 'Option 3']
```

With showSelectedOnRefresh disabled it makes correcting errors more difficult and harder to select options but can remove the possibilities of selecting one option twice by accident. Also if all options are selected it will ask if you selected all options without you needing to select `Done`.

###### 1.3.4.2.1.5. Error treatment and handling

The only possible errors are the ones from both [newLineInt](#13113-error-treatment-and-handling) and [yesNo](#1332-error-treatment-and-handling) since they are what the user inputs through.

##### 1.3.4.2.2. returnDeselected

returnDeselected is almost the same as [returnSelected](#134211-numericserial) with the only difference being that instead of returning what the user selected it returns what the user **didn't** select.

###### 1.3.4.2.2.1. numericSerial

numericSerial assigns numbers to the options from 1 to the length of \*args.

###### 1.3.4.2.2.2. Usage

There is only one way to use this menu:

```python
import inputapi as inp

inp.menus.multiSelect.returnDeselected.numericSerial({params})
```

###### 1.3.4.2.2.3. Parameters

The parameters are identical to [returnSelected's parameters](#134213-parameters).

| Parameter             | data type | default    | purpose                                                                  |
| :-------------------- | :-------- | :--------- | :----------------------------------------------------------------------- |
| \*args                | Any       | No default | Options that are displayed to the user                                   |
| confirmChoice         | boolean   | `True`     | Ensures that what the user selected was what they intended to select     |
| showSelectedOnRefresh | boolean   | `True`     | Allows users to see what they selected (See Output for further detail)   |
| allowNoSelection      | boolean   | `False`    | Allows the user to simply select nothing                                 |
| clearOnLoad           | boolean   | `False`    | Clears terminal before displaying output                                 |
| cleanOnRefresh        | boolean   | `False`    | Clears terminal when an option is selected                               |
| clearWhenDone         | boolean   | `False`    | Clears terminal after user selects options                               |
| title                 | string    | `'Menu'`   | What will be displayed as the name/purpose of the menu (`---{title}---`) |

###### 1.3.4.2.2.4. Output

The output is identical to [returnSelected](#134214-output) where the output is the inverse.

```python
---Menu---
1: Option 1
2: Option 2
3: Option 3
0: Done

Multiple selection menu
To select an option input the number next to it:
>2

---Menu---
1: Option 1
2: *Option 2
3: Option 3
0: Done

Multiple selection menu
To select an option input the number next to it:
>0

Option 2
Confirm choice?
Numeric response allowed (Y=1, n=2)
[Y/n]:1

#This returned ['Option 1', 'Option 3']
```

###### 1.3.4.2.2.5. Error treatment and handling

Refer to [returnSelected](#134215-error-treatment-and-handling) for error treatment and handling.

### 1.3.5. RDCs

RDC (aka Radius Diameter Circumference) leans more on the mathematical part. RDC takes a Radius, Diameter, or Circumference of a circle and returns the radius.

#### 1.3.5.1. RDC

RDC was implemented in the 1.X versions of Input API, this is the most basic RDC in that you need another input for it to work.

##### 1.3.5.1.1. Usage

There are two ways to use RDC:

```python
#The 1.X way to use RDC
import inputapi as inp

inp.RDC({params})
```

```python
#The new way to use RDC
import inputapi as inp

inp.RDCs.RDC({params})
```

##### 1.3.5.1.2. Parameters

| Parameter     | data type | default    | purpose                             |
| :------------ | :-------- | :--------- | :---------------------------------- |
| length        | float     | No default | The value to be converted to radius |
| clearOnLoad   | boolean   | `False`    | Clears terminal before display      |
| clearWhenDone | boolean   | `False`    | Clears terminal when converted      |

##### 1.3.5.1.3. Output

The only output RDC has is:

```python
---RDC---
1: Radius
2: Diameter
3: Circumference

To select an option input the number assigned to it:
>
```

##### 1.3.5.1.4. Error treatment and handling

All error treatment and handling is dealt by the [menu](#134114-error-treatment-and-handling) RDC uses. The only error that can happen is if length is not a number.

#### 1.3.5.2. newLineRDC

newLineRDC doesn't require you to input length, it will simply just request the length with [newLineFloat](#13121-newlinefloat-input) then returns radius.

##### 1.3.5.2.1. Usage

Only one way to use newLineRDC:

```python
import inputapi as inp

inp.RDCs.newLineRDC({params})
```

##### 1.3.5.2.2. Parameters

The parameters are:

| Parameter      | data type | default | purpose                        |
| :------------- | :-------- | :------ | :----------------------------- |
| clearOnLoad    | boolean   | `False` | Clears terminal before display |
| clearOnRefresh | boolean   | `False` | Clears terminal between inputs |
| clearWhenDone  | boolean   | `False` | Clears terminal when converted |

##### 1.3.5.2.3. Output

The output for newLineRDC isn't much:

```python
#Let's do a radius of 5
RDC:
>5

---RDC---
1: Radius
2: Diameter
3: Circumference

To select an option input the number assigned to it:
>1

# This returned 5.0
```

##### 1.3.5.2.4. Error treatment and handling

The errors for newLineRDC are handled by [newLineFloat](#13123-error-treatment-and-handling) and [singleSelect's numericSerial](#134114-error-treatment-and-handling).

#### 1.3.5.3. sameLineRDC

sameLineRDC uses [sameLineFloat](#13122-samelinefloat) as the input instead of [newLineFloat](#13121-newlinefloat-input), this makes the input more compact and takes up less space for input.

##### 1.3.5.3.1. Usage

There is only one way to use sameLineRDC:

```python
import inputapi as inp

inp.RDCs.sameLineRDC({params})
```

##### 1.3.5.3.2. Parameters

These are the parameters for sameLineRDC:

| Parameter      | data type | default | purpose                        |
| :------------- | :-------- | :------ | :----------------------------- |
| clearOnLoad    | boolean   | `False` | Clears terminal before display |
| clearOnRefresh | boolean   | `False` | Clears terminal between inputs |
| clearWhenDone  | boolean   | `False` | Clears terminal when converted |

##### 1.3.5.3.3. Output

The output for sameLineRDC is as follows:

```python
#Lets do a diameter of 26
RDC=26

---RDC---
1: Radius
2: Diameter
3: Circumference

To select an option input the number assigned to it:
>2

#This returned 13.0
```

##### 1.3.5.3.4. Error treatment and handling

All possible errors happen through [sameLineFloat](#13123-error-treatment-and-handling) and [singleSelect's numericSerial](#134114-error-treatment-and-handling).

### 1.3.6. otherFunc

otherFunc is what features the Input API has but isn't actually input. Just about all inputs require otherFunc to work just enough to keep afloat. You don't need to master this to actually be good at using Input API.

#### 1.3.6.1. pause

With pause it will stop the program until a user presses ENTER, this is really simple and is never used by any input.

##### 1.3.6.1.1. standard

standard is the first pause function and just pauses with no other noteworthy functionality.

###### 1.3.6.1.1.1. Usage

There are two ways to use standard:

```python
#This one actually makes sense
import inputapi as inp

inp.pause({params})
```

```python
#The reimagined way
import inputapi as inp

inp.otherFunc.pause.standard({params})
```

###### 1.3.6.1.1.2. Parameters

The parameters for standard is:

| Parameter     | data type | default | purpose                        |
| :------------ | :-------- | :------ | :----------------------------- |
| clearOnLoad   | boolean   | `False` | Clears terminal before pausing |
| clearWhenDone | boolean   | `False` | Clears terminal when resuming  |

###### 1.3.6.1.1.3. Output

The output is really lackluster:

```python
#Anything can be printed before pausing
#If clearOnLoad is False
Press ENTER to continue:
```

###### 1.3.6.1.1.4. Error treatment and handling

If you can find an error that can only happen with standard... congrats at breaking the most simple function the Input API has.

##### 1.3.6.1.2. showValue

This works almost identical to [standard](#13611-standard) but allows you to print values while having clearOnLoad `True`.

###### 1.3.6.1.2.1. Usage

Only one way to use showValue:

```python
import inputapi as inp

inp.otherFunc.pause.showValue({params})
```

###### 1.3.6.1.2.2. Parameters

The parameters for showValue are:

| Parameter     | data type | default    | purpose                             |
| :------------ | :-------- | :--------- | :---------------------------------- |
| \*values      | Any       | No default | The values to be displayed on pause |
| clearOnLoad   | boolean   | `False`    | Clears terminal before pausing      |
| clearWhenDone | boolean   | `False`    | Clears terminal when resuming       |

###### 1.3.6.1.2.3. Error treatment and handling

The errors that can happen are un-treatable and will break the script.

#### 1.3.6.2. clearScreen

clearScreen is the only part of Input API that is depended to the point of breaking. If clearScreen breaks then everything that wants to clear the terminal will break. clearScreen will only work with Windows, MacOS, and Linux based systems. Anything else is either lucky enough to be under the umbrella or incompatible entirely.

##### 1.3.6.2.1. auto

auto will clear the terminal while not needing info on the OS. It instead will ask Python through `os` to get info on the OS to use the right command to clear the terminal. This function has no parameters or errors, so you can just call it and nothing bad will happen.

###### 1.3.6.2.1.1. Usage

Two ways to use auto:

```python
#The original way
import inputapi as inp

inp.clearScreen()
```

```python
#The way Input API uses auto

inp.otherFunc.clearScreen.auto()
```

##### 1.3.6.2.2. manual

manual clearScreen gives you the ability to clear the terminal for one OS and not all. Though MacOS and Linux based systems use the same command for their clearing, it's more allow Windows to clear or allow the other two to clear.

###### 1.3.6.2.2.1. Usage

Only one way to use manual:

```python
import inputapi as inp

inp.otherFunc.clearScreen.manual({params})
```

###### 1.3.6.2.2.2. Parameters

The parameter for manual is:

| Parameter | data type | default    | purpose                             |
| :-------- | :-------- | :--------- | :---------------------------------- |
| OS        | string    | No default | What OS you want to be cleared |

###### 1.3.6.2.2.3. How to properly use manual

When calling the function you have to tell manual the name of the OS. While it requires the spelling to be correct, manual isn't case sensitive.

```python
#Lets go through every OS supported
import inputapi as inp

#This will make using manual easier to call
manual = inp.otherFunc.clearScreen.manual

#Windows
manual(OS='Windows')

#MacOS
manual(OS='MACOS')

#Linux based systems
manual(OS='linux')

#This will raise an error
manual(OS='WindowsOS')

#This too will raise an error
manual()
```

## 1.4. TODO

This will be some things to expect to happen as Input API gets more updates. With some coming in the next major update, others in the minor updates.

### 1.4.1. In Major Updates

These will be added in the next major updates, some may appear in the same, others might be the only change.

NOTE: These ideas are in no order whatsoever, any combination of when these will be added is possible

#### 1.4.1.1. Pre-set Inputs

Pre-set Inputs will be a way to have a series of inputs with the parameters set. A file with inputs could be read by the Input API and saved as a readable file or a compressed format to save on space. There will also be some built-in formats to make easier inputs too. This will be compatible with both older and more recent updates.

```python
import inputapi as inp

#So instead of having something like this
inp.numeric.newLineFloat('Gimmie a number:')
inp.boolean.yesNo('Are you sure?')

#You could
fileInput = inp.presets.readFrom('/File.ext') #File extension will be given (.ext isn't it)
fileInput.getNumber()

#Or maybe
inp.presets.number.intWithConfirm('Gimmie a number', 'Are you sure?') #This is not a guarantee to be added to presets (At least not in this exact way)
```

#### 1.4.1.2. Iterable Inputs

This update will allow input for multiple elements of a list or array. This will allow multiple types of inputs in one.

```python
import inputapi as inp

#This could be how the input could be used
inp.iterables.list.newLineList()
inp.iterables.tuple.sameLineTuple()
inp.iterables.set.newLineSet()
```

#### 1.4.1.3. A Config Function

This function will allow you to determine multiple factors throughout Input API, maybe relax some restrictions or make some more strict. More power will be given to you when receiving input when this comes to existence.

```python
import inputapi as inp

#Could be this
inp.config({params})

#Maybe this
inp.strings.config({params})

#Or this
inp.config.var = {Var}

#There is some other things tht could be how config works but this is still possible
```

#### 1.4.1.4. Call later/repeat input

This update will allow you to have a set of inputs within the script to be called over time and not when the line is read.

```python
import inputapi as inp

#So instead of input being here
inp.strings.newLineStr() #This is the input *function*

#You could save it
input = inp.strings.NewLineStr({params}) #This could be a class (Name is a placeholder)

#Then call it later
if __name__ == '__main__':
  input()

  #Or repeat the input
  while True:
    user = input()
    print(user)
    if user == 'Quit':
      break
```

### 1.4.2. In Minor Updates

These updates will be added between major updates or with them.

#### 1.4.2.1. New multiSelect Menu Types

There will be new multiSelect menu types for both returnSelected and returnDeselected. These types will be from the singleSelect menus.

#### 1.4.2.2. New singleSelect Menu Type

There will be a new singleSelect menu type that will be exclusive to singleSelect. This will have the same output as a multiSelect menu but won't let you select multiple.

#### 1.4.2.3. Adding A Changelog

There will be a changelog that will list every change from 1.0.0 to the latest update. This will be publicly available to all distributions and to the GitHub repository.

[^1]:
    clearScreen is does not need any information about the OS to work[^2]
    It will automatically tell what OS is running the code and use the command used by the OS to clear the terminal

[^2]: Feature is only supported on Windows, MacOS, and Linux based systems
[^3]: Fun Fact's although being labeled as "Fun" is more fact than fun and could be a "Sad Fact" depending on the fact!
[^4]: Not everything, just what takes input, clearScreen and pause don't rely on it working to function
