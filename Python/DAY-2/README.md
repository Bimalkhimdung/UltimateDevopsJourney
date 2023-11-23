## DATA Types
This is a Day-2 of complete python course for my Ultimate Devops Journey Course.

- what is data type ?
    Data type simply identification of which type of data is stored by a variable.
    for example. 
    ```
        a=5
        print(type(a))
        gives output as 
        <class int>
    ```
**Standard Data Types**
1. Numbers [^1]
    -  Interger
    -  Complex Numbers.
    -  Float
2. Sequence Type
    - String
    - List
    - Tuple
3. Boolean
4. Set
5. Dictionary
### Numbers
Numeric values are stored in numbers. The whole number, float, and complex qualities have a place with a Python Numbers datatype. Python offers the type() function to determine a variable's data type.
    
```
     print(type(variable))  
```
## Sequence Type
### String
- The sequence of characters in the quotation marks can be used to describe the string.
- A string can be defined in Python using single, double, or triple quotes.

    ``` 
    str = "string using double quotes"  
    print(str)
    ```
### list
- In python list can contains different data types unlike in 'c' with only same data types
- list are represented inside square bracket [] and values are separated by comma (,)
- We can use slice method to get values of data
> [!NOTE] 
> python indexing is start form 0. not 1 
- We can use slice [:] operators to gain access of list.
- we can change the value of list.

### Tuple
- In many ways tuple is like a list
- List is represented by [] where as tuple is represented bt ()
- We can not alter the value or size of tuple so it's read-only structure.

### Dictionary
A dictionary is a key-value pair set arranged in any order.