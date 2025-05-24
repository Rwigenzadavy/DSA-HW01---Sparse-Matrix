from sparse_matrix import SparseMatrix

def main():
    print("Choose operation:\n1. Add\n2. Subtract\n3. Multiply")
    choice = input("Enter 1, 2 or 3: ").strip()

    file1 = input("Enter filename for matrix 1 (e.g., sample_inputs/matrix1.txt): ").strip()
    file2 = input("Enter filename for matrix 2 (e.g., sample_inputs/matrix2.txt): ").strip()
    output_file = input("Enter output filename (e.g., result.txt): ").strip()

    try:
        m1 = SparseMatrix.from_file(file1)
        m2 = SparseMatrix.from_file(file2)

        if choice == '1':
            result = m1.add(m2)
        elif choice == '2':
            result = m1.subtract(m2)
        elif choice == '3':
            result = m1.multiply(m2)
        else:
            print("Invalid option")
            return

        with open(output_file, 'w') as f:
            f.write(str(result))
        print("Operation completed. Result saved to", output_file)

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
