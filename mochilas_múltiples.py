# -*- coding: utf-8 -*-
"""mochilas_múltiples.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BKsw0UHcsnh8Y-wG-V9OrJ63ZgOAdDKA
"""

!pip install ortools #Importa las bibliotecas

"""Solve a multiple knapsack problem using a MIP solver."""
from ortools.linear_solver import pywraplp #importar librerias


def main():
    #crear los datos
    """
    weights: Un vector que contiene los pesos de los elementos.
    values: Un vector que contiene los valores de los elementos.
    capacities: Un vector que contiene las capacidades de las discretizaciones.
    """
    data = {}
    data["weights"] = [48, 30, 42, 36, 36, 48, 42, 42, 36, 24, 30, 30, 42, 36, 36]
    data["values"] = [10, 30, 25, 50, 35, 30, 15, 40, 30, 35, 45, 10, 20, 30, 25]
    assert len(data["weights"]) == len(data["values"])
    data["num_items"] = len(data["weights"])
    data["all_items"] = range(data["num_items"])

    data["bin_capacities"] = [100, 100, 100, 100, 100]
    data["num_bins"] = len(data["bin_capacities"])
    data["all_bins"] = range(data["num_bins"])

    # Declara el agente de resolución de MIP
    solver = pywraplp.Solver.CreateSolver("SCIP")
    if solver is None:
        print("SCIP solver unavailable.")
        return

    # Variables.
    # x[i, b] = 1 if item i is packed in bin b.
    """
    Cada x[(i, j)] es una variable de 0 a 1, en la que i es un elemento y j es un contenedor.
    En la solución, x[(i, j)] será 1 si el elemento i se coloca en la papelera j; de lo contrario, 0.
    """
    x = {}
    for i in data["all_items"]:
        for b in data["all_bins"]:
            x[i, b] = solver.BoolVar(f"x_{i}_{b}")

    # Constraints.
    # Each item is assigned to at most one bin.
    """
    Las restricciones son las siguientes:
    1. Cada artículo puede colocarse como máximo un contenedor.
    Para esta restricción, se requiere que la suma de x[i, j] en todas las discretizaciones j sea menor o igual que 1.
    2. El peso total empaquetado en cada discretización no puede superar su capacidad.
    Para esta restricción, se requiere que la suma de los pesos de los elementos ubicados en la discretización j sea menor o igual que la capacidad de la discretización.
"""
    for i in data["all_items"]:
        solver.Add(sum(x[i, b] for b in data["all_bins"]) <= 1)

    # The amount packed in each bin cannot exceed its capacity.
    for b in data["all_bins"]:
        solver.Add(
            sum(x[i, b] * data["weights"][i] for i in data["all_items"])
            <= data["bin_capacities"][b]
        )

    # Objective.
    # Maximize total value of packed items.
    """
    Ten en cuenta que x[i, j] * data['values'][i] agrega el valor del elemento i al objetivo si el elemento se coloca en la papelera j.
    Si i no se coloca en ninguna discretización, su valor no contribuye al objetivo.
    """

    objective = solver.Objective()
    for i in data["all_items"]:
        for b in data["all_bins"]:
            objective.SetCoefficient(x[i, b], data["values"][i])
    objective.SetMaximization()

    print(f"Solving with {solver.SolverVersion()}")
    status = solver.Solve()

    #imprimir la solución

    if status == pywraplp.Solver.OPTIMAL:
        print(f"Total packed value: {objective.Value()}")
        total_weight = 0
        for b in data["all_bins"]:
            print(f"Bin {b}")
            bin_weight = 0
            bin_value = 0
            for i in data["all_items"]:
                if x[i, b].solution_value() > 0:
                    print(
                        f"Item {i} weight: {data['weights'][i]} value: {data['values'][i]}"
                    )
                    bin_weight += data["weights"][i]
                    bin_value += data["values"][i]
            print(f"Packed bin weight: {bin_weight}")
            print(f"Packed bin value: {bin_value}\n")
            total_weight += bin_weight
        print(f"Total packed weight: {total_weight}")
    else:
        print("The problem does not have an optimal solution.")


if __name__ == "__main__":
    main()