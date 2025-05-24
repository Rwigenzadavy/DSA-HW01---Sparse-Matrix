# Sparse Matrix Operations

This project implements a **sparse matrix data structure**

##  Features

- Load sparse matrices from text files
- Perform:
   - Matrix Addition
     
   - Matrix Subtraction
    
   - Matrix Multiplication
     
- Validate input format and dimensions
- Save the result to an output text file


---

# Technologies Used

Python 3

No external libraries used

Only built-in os module used for listing files


## Folder Structure

├── sample_inputs/ # Folder with input matrix files

├── main.py # Main runner program

├── sparse_matrix.py # SparseMatrix class

##  How to Run

1. install python on your system.
   
2. Clone the repository
    
3. Run the main program:
```bash
python main.py
```
4. Select the operation (add, subtract, multiply)


## The program will raise an error and exit if:

-The input file contains malformed entries (e.g., wrong parentheses, float values)

-The matrices are incompatible for the selected operation

-Non-integer values are found where integers are expected

6. Choose two input files from the list

7. Provide a name for the output file

