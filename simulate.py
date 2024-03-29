"""
Starts an individual simulation
"""
import sys

from simulation import Simulation


def begin_simulation(show_gui: bool, solution_id: int):
    """
    Begins one simulation
    :param show_gui: Should the graphical representation of the simulation be shown
    :param solution_id: The id of the solution being simulated
    """
    simulation = Simulation(show_gui, solution_id)

    simulation.run()

    simulation.get_fitness()


# Runs when simulate is called in parallel mode in solution.py
if __name__ == "__main__":
    if sys.argv[1] == "GUI":
        gui = True
    else:
        gui = False

    sol_id = int(sys.argv[2])

    begin_simulation(show_gui=gui, solution_id=sol_id)
