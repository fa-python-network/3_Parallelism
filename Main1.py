"""Основные задания лабораторной"""
from Matrix import Matrix

if __name__ == "__main__":
    Matrix1 = Matrix(file="input.txt")
    Matrix2 = Matrix(file="input2.txt")

    Matrix3 = Matrix1 * Matrix2
    with open("output.txt", "w") as out:
        print(Matrix3, file=out)