from integral_reaction_path_analysis import main_rpd, freeflame_simulation

########################################################################################################################
# Main script
# Define chemical kinetic model to be used in analysis
model = 'ffcm1.yaml'

# Output filename
outfile = 'rpd_output.txt'

# Create a flame object from Cantera's FreeFlame simulation - can use functionality provided or reload another solution
flame_obj = freeflame_simulation(model, 1.0, 298, 101325*1, 0.21, 0.03)

# Run main reaction path analysis code
main_rpd(model, flame_obj, outfile, threshold=0.02)
