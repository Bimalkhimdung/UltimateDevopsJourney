# Day-One of Python Course
## Contents
- Variables

A Variable is a name given to the memory location. A value holding Python variable is also know as an **identifier**.
A Variable name must begin with a latter or an underscore, but they can be group of both letter and digits.

## Guildelines
- The variable's first character must be an underscore or alphabet (_).
- Every one of the characters with the exception of the main person might be a letter set of lower-case(a-z), capitalized (A-Z), highlight, or digit (0-9).
- White space and special characters (!, @, #, %, etc.) are not allowed in the identifier name. ^, &, *).
- Identifier name should not be like any watchword characterized in the language.
- Names of identifiers are case-sensitive; for instance, my name, and MyName isn't something very similar.

## Variables decleration best practices
- Camel Case - In the camel case, each word or abbreviation in the middle of begins with a capital letter. There is no intervention of whitespace. For example - nameOfStudent, valueOfVaraible.
- Pascal Case - It is the same as the Camel Case, but here the first word is also capital. For example - NameOfStudent, etc.
- Snake Case - In the snake case, Words are separated by the underscore. For example - name_of_student, etc.
## Variable types
- Local variable
    The variable which is declared inside a function or have scope within the function are know as local variable.
    
    ```
        def add():
            a=10
            b=30
            c=a+b
            print(c)
        
        add() #function call
        #Output = 40

    ```
- Global variable
    Global variables can be utilized all through the program, and its extension is in the whole program. Global variables can be used inside or outside the function.
    By default, a variable declared outside of the function serves as the global variable. 
