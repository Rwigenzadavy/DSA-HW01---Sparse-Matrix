class SparseMatrix:
    def __init__(self, rows=0, cols=0):
        self.rows = rows
        self.cols = cols
        self.data = {} 

    @classmethod
    def from_file(cls, filepath):
        with open(filepath, 'r') as file:
            lines = [line.strip() for line in file if line.strip()]

        rows = int(lines[0].split('=')[1])
        cols = int(lines[1].split('=')[1])
        matrix = cls(rows, cols)

        for line in lines[2:]:
            if line[0] != '(' or line[-1] != ')':
                raise ValueError("Invalid format")
            parts = line[1:-1].split(',')
            if len(parts) != 3:
                raise ValueError("Invalid matrix entry")
            r, c, v = int(parts[0]), int(parts[1]), int(parts[2])
            if r >= rows or c >= cols:
                raise ValueError("Index out of bounds")
            matrix.data[(r, c)] = v

        return matrix

    def get_element(self, row, col):
        return self.data.get((row, col), 0)

    def set_element(self, row, col, value):
        if value != 0:
            self.data[(row, col)] = value
        elif (row, col) in self.data:
            del self.data[(row, col)]

    def add(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix size must match")
        result = SparseMatrix(self.rows, self.cols)
        keys = set(self.data) | set(other.data)
        for key in keys:
            total = self.get_element(*key) + other.get_element(*key)
            if total != 0:
                result.set_element(*key, total)
        return result

    def subtract(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix size must match")
        result = SparseMatrix(self.rows, self.cols)
        keys = set(self.data) | set(other.data)
        for key in keys:
            diff = self.get_element(*key) - other.get_element(*key)
            if diff != 0:
                result.set_element(*key, diff)
        return result

    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError("Matrix size invalid for multiplication")
        result = SparseMatrix(self.rows, other.cols)
        for (i, k1), v1 in self.data.items():
            for (k2, j), v2 in other.data.items():
                if k1 == k2:
                    old = result.get_element(i, j)
                    result.set_element(i, j, old + v1 * v2)
        return result

    def __str__(self):
        lines = [f"rows={self.rows}", f"cols={self.cols}"]
        for (r, c), v in sorted(self.data.items()):
            lines.append(f"({r}, {c}, {v})")
        return "\n".join(lines)
