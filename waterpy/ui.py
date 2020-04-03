"""Objects and functions that aid in the transition from UI to main"""

import os

class ui:
    """Likely a temporary place holder while we work out how to pass
    between pyQT and here """
    input_directory = 'dir'
    characteristics = 'file'
    parameters = 'file'
    timeseries = 'file'
    twi = 'file'
    pet = 'hamon'
    snow = 'option'
    karst = 'option'
    rand = 'option'
    matrices = 'option'


def ini_write(file, ui):
    """Build the modelconfig.ini file from user inputs"""
    config_file = open(file, "w")
    lines = []
    # inputs are going to be brain hurty.
    lines.extend(("[Inputs] \n",
                  "input_dir = {} \n".format(ui.input_directory),
                  "characteristics_basin_file = ${Inputs:input_dir}" + "\\{} \n".format(ui.characteristics),
                  "parameters_land_type_file = ${Inputs:input_dir}" + "\\{} \n".format(ui.parameters),
                  "timeseries_file = ${Inputs:input_dir}" + "\\{} \n".format(ui.timeseries),
                  "twi_file = ${Inputs:input_dir}\\" + "{} \n".format(ui.twi),
                  "\n[Options] \n",
                  "option_pet = {} \n".format(ui.pet),
                  "option_snowmelt = {}\n".format(ui.snow),
                  "option_karst = {}\n".format(ui.karst),
                  "option_randomize_daily_to_hourly = {}\n".format(ui.rand),
                  "option_write_output_matrices = {}\n".format(ui.matrices)))

    for line in lines:
        config_file.write(line)
    config_file.close()

    return os.path.abspath(file)
