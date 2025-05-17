---
title: "<strong>Quadratics Solver</strong>"
date: "2021-07-01"
imageUrl: "/img/quadratic.png"
subtitle: "I May Have Used This For My Homework :)"
---

## What does it do?

This quadratics solver app uses matplotlib to graph a quadratic equation. This application also solves the equation in vertex form, solves for the roots, and solves for the vertex. 

## Source Code

```python
# main.py

from equation import Equation, graph

def main():
    # User input
    while True:
        try:
            a = int(
                input('What is the "a" value of your equation? (in standard form):\n')
            )
            b = int(input('"b" value? (in standard form):\n'))
            c = int(input('"c" value? (in standard form):\n'))
            break

        except:
            pass

    # Equation class
    equation = Equation((a, b, c))

    standard_form = equation.get_standard_form()
    vertex_form = equation.get_vertex_form()
    a, b, c = equation.values
    x1, x2 = equation.get_zeros()
    x, y = equation.get_vertex()

    print(
        """
    [+] Standard Form = {}\n
    [+] Vertex Form = {}\n
    [+] 1st zero/root = {}\n
    [+] 2nd zero/root = {}\n
    [+] Vertex = {}\n
    [+] AOS: x = {}""".format(
            standard_form, vertex_form, x1, x2, (x, y), x
        )
    )

    graph(equation)

if __name__ == "__main__":
    main()
```

```python
# equation.py
import math
import matplotlib.pyplot as plt


class Equation:
    def __init__(self, values):
        self.values = values

    def get_zeros(self):
        a, b, c = self.values
        x = (b ** 2) - (4 * a * c)

        x1 = (-b + math.sqrt(x)) / (2 * a)
        x2 = (-b - math.sqrt(x)) / (2 * a)

        return x1, x2

    def get_vertex(self):
        a, b, c = self.values

        x = (-b) / (2 * a)

        y = ((4 * a * c) - (b ** 2)) / (4 * a)

        return x, y

    def get_standard_form(self):
        a, b, c = self.values

        return "{}x^2 + {}x + {}".format(a, b, c)

    def get_vertex_form(self):
        a = self.values[0]
        h, k = self.get_vertex()

        return f"{a}(x-{h})^2 + {k}"


def graph(equation):
    a, b, c = equation.values
    r1, r2 = equation.get_zeros()

    if r1 < r2:
        x = r1
        y = r2

    else:
        x = r2
        y = r1

    roots1 = []
    roots2 = []

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    # Set axes
    # ax.spines['left'].set_position('center')
    # ax.spines['bottom'].set_position('zero')

    # ax.spines['right'].set_color('none') # remove vertical box line
    # ax.spines['top'].set_color('none') # remove horizontal box line

    # ax.xaxis.set_ticks_position('bottom')
    # ax.yaxis.set_ticks_position('left')

    while x < y:
        base = float((a * (x ** 2)) + (b * x) + c)

        roots1.append(x)
        roots2.append(base)
        x += 0.0001

    plt.plot(roots1, roots2, "g")
    plt.show()import math
import matplotlib.pyplot as plt


class Equation:
    def __init__(self, values):
        self.values = values

    def get_zeros(self):
        a, b, c = self.values
        x = (b ** 2) - (4 * a * c)

        x1 = (-b + math.sqrt(x)) / (2 * a)
        x2 = (-b - math.sqrt(x)) / (2 * a)

        return x1, x2

    def get_vertex(self):
        a, b, c = self.values

        x = (-b) / (2 * a)

        y = ((4 * a * c) - (b ** 2)) / (4 * a)

        return x, y

    def get_standard_form(self):
        a, b, c = self.values

        return "{}x^2 + {}x + {}".format(a, b, c)

    def get_vertex_form(self):
        a = self.values[0]
        h, k = self.get_vertex()

        return f"{a}(x-{h})^2 + {k}"


def graph(equation):
    a, b, c = equation.values
    r1, r2 = equation.get_zeros()

    if r1 < r2:
        x = r1
        y = r2

    else:
        x = r2
        y = r1

    roots1 = []
    roots2 = []

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    # Set axes
    # ax.spines['left'].set_position('center')
    # ax.spines['bottom'].set_position('zero')

    # ax.spines['right'].set_color('none') # remove vertical box line
    # ax.spines['top'].set_color('none') # remove horizontal box line

    # ax.xaxis.set_ticks_position('bottom')
    # ax.yaxis.set_ticks_position('left')

    while x < y:
        base = float((a * (x ** 2)) + (b * x) + c)

        roots1.append(x)
        roots2.append(base)
        x += 0.0001

    plt.plot(roots1, roots2, "g")
    plt.show()
```

Ensure both files are in the same project directory. Run `python main.py` to start the application.

{{< custom_link href="https://github.com/gavintranquilino/quadratics" text="GitHub Source Code" >}}