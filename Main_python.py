import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def butane_isomerization():
    # Step 1: Define reactor parameters
    reactor_params = define_reactor_params()

    # Step 2: Simulate for coolant temperature = 300 K
    reactor_params['coolantTemp'] = 300
    volume = np.arange(0, 5.1, 0.1)
    sol_volume = simulate_reaction(volume, [0, 305], reactor_params)

    # Step 3: Simulate for coolant temperature = 315 K
    reactor_params['coolantTemp'] = 315
    length = np.linspace(0, 1.5923, 10)
    sol_length = simulate_reaction(length, [0, 305], reactor_params)

    # Step 4: Plot results
    plot_simulation_results(volume, sol_volume, length, sol_length)

    # Display maximum results
    print(f'Maximum temperature achieved in Reactor I: {max(sol_volume.y[1]):.2f} K')
    print(f'Maximum conversion achieved in Reactor I: {max(sol_volume.y[0]):.3f} mol/L')
    print(f'Maximum temperature achieved in Reactor II: {max(sol_length.y[1]):.3f} K')
    print(f'Maximum conversion achieved in Reactor II: {max(sol_length.y[0]):.3f} mol/L')


def define_reactor_params():
    return {
        'flowRate': 16.3,                # L/s
        'initialConcentration': 1.86,    # mol/L
        'enthalpyChange': -34500,        # J/mol
        'specificHeat': 159,             # J/(kg·K)
        'heatTransferCoeff': 5000        # W/(m²·K)
    }


def simulate_reaction(independent_var, initial_values, reactor_params):
    solution = solve_ivp(
        lambda x, y: reactor_equations(x, y, reactor_params),
        (independent_var[0], independent_var[-1]),
        initial_values,
        t_eval=independent_var,
        method='RK45'
    )
    return solution


def reactor_equations(_, vars, reactor_params):
    concentration = vars[0]
    temperature = vars[1]

    reaction_rate = calculate_reaction_rate(reactor_params, concentration, temperature)

    dC = calculate_concentration_change(reaction_rate, reactor_params)
    dT = calculate_temperature_change(reaction_rate, temperature, reactor_params)

    return [dC, dT]


def calculate_reaction_rate(reactor_params, concentration, temperature):
    k = 31.1 * np.exp(7906 * ((temperature - 360) / (360 * temperature)))
    K_eq = np.exp(-830.3 * ((temperature - 333) / (333 * temperature)))
    rate = -k * reactor_params['initialConcentration'] * (1 - ((1 + (1 / K_eq)) * concentration))
    return rate


def calculate_concentration_change(rate, reactor_params):
    return -rate / reactor_params['flowRate']


def calculate_temperature_change(rate, temperature, reactor_params):
    return ((rate * reactor_params['enthalpyChange']) - (reactor_params['heatTransferCoeff'] * (temperature - reactor_params['coolantTemp']))) / \
           (reactor_params['flowRate'] * reactor_params['specificHeat'])


def plot_simulation_results(volume, sol_volume, length, sol_length):
    plt.figure(figsize=(12, 10))

    # Volume-based plots
    plt.subplot(2, 2, 1)
    plt.plot(sol_volume.t, sol_volume.y[1], 'k')
    plt.xlabel('Volume (m³)')
    plt.ylabel('Temperature (K)')
    plt.title('Temperature vs. Volume')

    plt.subplot(2, 2, 2)
    plt.plot(sol_volume.t, sol_volume.y[0], 'r')
    plt.xlabel('Volume (m³)')
    plt.ylabel('Conversion (mol/L)')
    plt.title('Conversion vs. Volume')

    # Length-based plots
    plt.subplot(2, 2, 3)
    plt.plot(sol_length.t, sol_length.y[1], 'b')
    plt.xlabel('Length (m)')
    plt.ylabel('Temperature (K)')
    plt.title('Temperature vs. Length')

    plt.subplot(2, 2, 4)
    plt.plot(sol_length.t, sol_length.y[0], 'y')
    plt.xlabel('Length (m)')
    plt.ylabel('Conversion (mol/L)')
    plt.title('Conversion vs. Length')

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    butane_isomerization()
