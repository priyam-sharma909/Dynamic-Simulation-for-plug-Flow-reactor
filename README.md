# Butane Isomerization Reactor Simulation

## Project Overview

This project simulates the isomerization of normal butane to isobutane in a plug flow reactor (PFR) with a cooling jacket for temperature control. The simulation dynamically tracks the temperature and conversion profiles along the reactor’s volume and length using ordinary differential equations (ODEs).

The simulation compares reactor performance under two different coolant temperatures: 300 K and 315 K.

---

## Key Equations Used

### 1. Reaction Rate

The reaction rate is defined as:

$$
r_A = -k \cdot C_{A0} \left[ 1 - \left( 1 + \frac{1}{K_{eq}} \right) X \right]
$$

Where:
- \( k = 31.1 \cdot e^{7906 \left( \frac{T - 360}{360T} \right)} \) is the rate constant.
- \( K_{eq} = e^{-830.3 \left( \frac{T - 333}{333T} \right)} \) is the equilibrium constant.

---

### 2. Conversion Change

The change in conversion with reactor volume is given by:

$$
\frac{dX}{dV} = \frac{-r_A}{F_{A0}}
$$

Where:
- \( X \) is the conversion.
- \( F_{A0} \) is the molar flow rate of the reactant.

---

### 3. Temperature Change

The temperature change inside the reactor is governed by:

$$
\frac{dT}{dV} = \frac{ \Delta H_r \cdot r_A - U_a (T - T_a) }{ F_{A0} \cdot C_p }
$$

Where:
- \( \Delta H_r \) is the heat of reaction.
- \( U_a \) is the heat transfer coefficient.
- \( T_a \) is the coolant temperature.
- \( C_p \) is the specific heat capacity of the fluid.

---

## Technologies Used

- MATLAB (ODE Solvers, Plotting)
- Process Simulation
- Chemical Reaction Engineering

---

## File Structure


---

## How to Run

1. Open the `butane_isomerization.m` file in MATLAB.
2. Run the script directly.
3. The simulation will:
   - Solve the ODEs for both coolant temperatures.
   - Plot temperature and conversion against reactor volume and length.
   - Display maximum temperature and conversion results in the console.

---

## Simulation Results

### Coolant Temperature: 300 K
- Maximum Temperature: 308.04 K
- Maximum Conversion: 0.275 mol/L

### Coolant Temperature: 315 K
- Maximum Temperature: 361.21 K
- Maximum Conversion: 0.460 mol/L

---

## Output Plots

- Temperature vs. Reactor Volume
- Conversion vs. Reactor Volume
- Temperature vs. Reactor Length
- Conversion vs. Reactor Length

---

## Future Improvements

- Add multi-reactor system analysis.
- Perform sensitivity studies on process parameters such as coolant temperature, flow rate, and heat transfer coefficient.
- Incorporate real-time visualization and interactive dashboards.
- Extend the model to complex multi-phase systems.

---
