#### Chapter 2: Variable and Statements
###### Glossary

- *Variable*: Name that refers to some value (Similar to vectors in R. They are **NOT** the same though)
    - *Assignment Statement*: The act of creating a variable (e.g. x = 67)
        - **Note**: You can apply arithmetic operators and functions to variables just like regular values
- *State Diagram*: Better with a visual, but essentially the *Environment* tab in RStudio that tells you what values a vector contains, in this case you've written it on paper or some software to denote what value a variable holds.
- *Variable Names*: What you call or assign your variable to be denoted as. 
    - **Note**: Variable names can **NOT** start with a number. Good practice also tells you to use lowercase, but it's not illegal to use uppercase 
- *Keywords*: Built in python variables that can **NOT** be used as variable names. No need to memorize them since they have a special color denotion in may python systems.
- *import*: One of the more important keywords that lets you access more python features using modules
- *Module*: A collection of variables and functions 
- *Expression*: Can be a single value (Integers, Floats, Strings) or a collection of values and operators. It can also include variable names and function calls.
    - *Evaluation*: Computing the value of an expression (You're evaluating some expression and displaying it's value)
    - *print()*: Function to display more than one expression at a time
- *Statement*: Unit of code that has an effect but **NO** output. (e.g. x = 67 will **NOT** produce any output but will internally store 67 into the variable x, imports are also statements.)
    - *Execution*: Running a statement (You're executing some statement, but there's no need to *evaluate* or display the result)
- *Argument*: The expression withing a function (e.g. int('101'))
- *Comments*: Natural language notes to better understand formal language code once it becomes too dense. Just a good practice really. (Use #, comments will **NOT** be ran when executing code)
    - **Note**: Good comments do not redundantly tell what the code does, rather explain *why* the code was written
- *Debugging*: There are three kind's of error you'll run into; Syntax, Runtime, and Semantic.
    - *Syntax Error*: Refers to structure and of a program and rules about the structure. More often than not I'm pretty sure this refers to misspelling something
    - *Runtime Error*: aka. exception; This happens when there are no syntax errors, but something still goes wrong, something exceptional.
    - *Semantic Error*: There is no error message and the code runs, but it doesn't do what you wan't.

###### Excerpts
- ***Variable naming convention***: They can contain both letters and numbers, but they can't begin with a number. It is legal to use uppercase letters, but it is conventional to use only lower case for variable names.