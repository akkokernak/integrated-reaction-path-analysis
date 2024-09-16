# Using Integrated Reaction Path Analysis Code

## Required Packages
Python, Cantera, Numpy, Math, Graphviz Dot

## Integrated Reaction Path Analysis Code
The integrated reaction path analysis (IRPA) code (integral_reaction_path_analysis.py) contains all necessary functions to perform the IRPA for a particluar flame object generated from Cantera. This does not need to be modified in order to run the main code. However, the user can change the input parameters for the freeflame simulation function if desired.

## Main IRPA Code
Running the main IRPA code (irpa_main.py) calls necessary functions to 1) solve for a flame object and 2) perform an IRPA over the flame object. User should specify chemical kinetic model to be used for computations - this should be the same for both the flame object solution and the IRPA. Code should be modified to include the output file name. The flame simulation function is pre-coded for a methane flame. User should modify initial conditions for flame. Changes to fuel need to be made directly in the freeflame_simulation function from 'integral_reaction_path_analysis.py'. The user can opt to reload a previously computed flame object if preferred. The flame object is then used by the 'main_rpd' function to compute the IRPA. User should modify threshold level to desired number. Threshold designates what path fluxes are ultimately included in the IRPA. Normalized fluxes that are smaller than specified threshold level are not included in IRPA output file.

## How to Run
Run the main IRPA code (irpa_main.py) to perform an IRPA over the specified flame object.

## Output
**1. Parsed grid points**

As IRPA function parses through grid points in the flame, the program will print the current grid point number in the Python command window. This allows the user to know how far the program has progressed through the flame object. This can be turned off by commenting out line 126 in 'integral_reaction_path_analysis.py'.

**2. output.txt**

Output.txt file is created by code to be read by the Graphviz DOT software. This needs to be installed separately and run through a command line interface in order to actually create the path diagrams visualizing the IRPA computations.

## GraphViz DOT Software
Graphviz DOT should be installed from the following link: [Graphviz Software Download](https://graphviz.org/download/)
Graphviz should be added to Path variables in order to run from the command line.

# Example Command Line
User should navigate to the folder containing 'output.txt' from IRPA code. An example command line to generate the reaction path diagram using DOT as a .png file is as follows:

**dot -Tpng 'output.txt' -o 'output.png'**
