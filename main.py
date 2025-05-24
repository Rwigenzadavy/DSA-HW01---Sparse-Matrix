import os
from sparse_matrix import SparseMatrix

def list_input_files(folder):
    files = [f for f in os.listdir(folder) if f.endswith(".txt")]
    return files

def choose_file(files, prompt):
    for i, f in enumerate(files):
        print(f"{i + 1}. {f}")
    choice = int(input(prompt)) - 1
    return files[choice]

def main():
    input_folder = "sample_inputs"
    input_files = list_input_files(input_folder)

    print("Choose an operation:\n1. Add\n2. Subtract\n3. Multiply")
    choice = input("Enter choice (1/2/3): ")

    print("\nAvailable input files:")
    file1 = choose_file(input_files, "Enter number for first matrix file: ")
    file2 = choose_file(input_files, "Enter number for second matrix file: ")

    matrix1 = SparseMatrix.from_file(os.path.join(input_folder, file1))
    matrix2 = SparseMatrix.from_file(os.path.join(input_folder, file2))

    if choice == '1':
        result = matrix1.add(matrix2)
    elif choice == '2':
        result = matrix1.subtract(matrix2)
    elif choice == '3':
        result = matrix1.multiply(matrix2)
    else:
        print("Invalid operation choice.")
        return

    output_filename = input("Enter name for the output file (e.g. result.txt): ")
    with open(output_filename, 'w') as f:
        f.write(str(result))

    print(f"\n✅ Operation completed. Result saved to {output_filename}.")

if __name__ == "__main__":
    main()
