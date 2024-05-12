## File Handling in python
In this tutorial, we are discussing Python file handling. Python supports the file-handling process. Till now, we were taking the input from the console and writing it back to the console to interact with the user. Users can easily handle the files, like read and write the files in Python. In another programming language, the file-handling process is lengthy and complicated. But we know Python is an easy programming language. So, like other things, file handling is also effortless and short in Python.

Sometimes, it is not enough to only display the data on the console. The data to be displayed may be very large, and only a limited amount of data can be displayed on the console since the memory is volatile, it is impossible to recover the programmatically generated data again and again.

The file handling plays an important role when the data needs to be stored permanently into the file. A file is a named location on disk to store related information. We can access the stored information (non-volatile) after the program termination.
In Python, files are treated in two modes as text or binary. The file may be in the text or binary format, and each line of a file is ended with the special character like a comma (,) or a newline character. Python executes the code line by line. So, it works in one line and then asks the interpreter to start the new line again. This is a continuous process in Python.

Hence, a file operation can be done in the following order.

- Open a file
- Read or write - Performing operation
- Close the file

### Open file
file opening is done with the **open()** function, This function will accepts two arguments ( file name and access mode)
**Syntax**
```
file object = open(filename,access mode)
```
File access modes 
Here's the provided information in markdown table format:

| Mode | Description |
|------|-------------|q
| r    | r means to read. So, it opens a file for read-only operation. The file pointer exists at the beginning. The file is by default open in this mode if no access mode is passed. |
| rb   | It opens the file to read-only in binary format. The file pointer exists at the beginning of the file. |
| r+   | It opens the file to read and write both. The file pointer exists at the beginning of the file. |
| rb+  | It opens the file to read and write both in binary format. The file pointer exists at the beginning of the file. |
| w    | It opens the file to write only. It overwrites the file if previously exists or creates a new one if no file exists with the same name. The file pointer exists at the beginning of the file. |
| wb   | It opens the file to write only in binary format. It overwrites the file if it exists previously or creates a new one if no file exists. The file pointer exists at the beginning of the file. |
| w+   | It opens the file to write and read both. It is different from r+ in the sense that it overwrites the previous file if one exists whereas r+ doesn't overwrite the previously written file. It creates a new file if no file exists. The file pointer exists at the beginning of the file. |
| wb+  | It opens the file to write and read both in binary format. The file pointer exists at the beginning of the file. |
| a    | It opens the file in the append mode. The file pointer exists at the end of the previously written file if exists any. It creates a new file if no file exists with the same name. |
| ab   | It opens the file in the append mode in binary format. The pointer exists at the end of the previously written file. It creates a new file in binary format if no file exists with the same name. |
| a+   | It opens a file to append and read both. The file pointer remains at the end of the file if a file exists. It creates a new file if no file exists with the same name. |
| ab+  | It opens a file to append and read both in binary format. The file pointer remains at the end of the file. |