"""Дополнительное задание 2"""
from multiprocessing import Queue
from Matrix import Matrix
from random import randint
from multiprocessing import Process
from time import sleep


def creating(q):
    while True:
        size = randint(2, 7)
        a = Matrix(a=size, b=size, random=True)
        b = Matrix(a=size, b=size, random=True)
        print(f"Сгенерированы матрицы:\n{a}\n{b}\n--------------------------")
        q.put([a, b])
        sleep(8)  # Эта функция выполняется намного быстрее умножения, поэтому ждём


def reading(q):
    while True:
        Matrix = q.get()
        MultMatrix = Matrix[0] * Matrix[1]
        print(
            f"Умножены матрицы: {Matrix[0]} и {Matrix[1]},\nРезультат: {MultMatrix}\n-------------------------------")


if __name__ == "__main__":
    q = Queue()
    creating_proc = Process(target=creating, args=[q])
    mult_proc = Process(target=reading, args=[q])
    creating_proc.start()
    mult_proc.start()
