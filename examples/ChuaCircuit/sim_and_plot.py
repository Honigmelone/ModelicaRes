#!/usr/bin/python
"""Set up and run simulations in Dymola, and then plot the results.
"""
__author__ = "Kevin Davies"
__version__ = "2012-10-11"

import os
import matplotlib.pyplot as plt
from pathlib import Path

from modelicares import gen_experiments, SimRes, write_script, saveall

import sys
import scipy.io

from dymola.dymola_interface import DymolaInterface
from dymola.dymola_exception import DymolaException

# Settings
# Begin customize--------------------------------------------------------------

# Run the simulations? (otherwise, just plot)
RUN = True

# Name of the Modelica script (may include the path)
FNAME = 'run_sims.mos'

# Working directory
WORKING_DIR = os.path.join((os.getcwd()),'working_dir')



if not(os.path.exists(WORKING_DIR)):
    try:
        os.mkdir(WORKING_DIR)
    except OSError:
        print("Creation of the directory %s failed" % WORKING_DIR)


# List of Modelica packages that should be preloaded (besides the Modelica
# Standard Library)
# Each may be a *.mo file or a path where a package.mo file resides, e.g.,
# "/opt/dymola/Modelica/Library/VehicleInterfaces 1.1.1".
PACKAGES = []

# List or generator of simulations to run
EXPERIMENTS = gen_experiments(
    models=['Modelica.Electrical.Analog.Examples.ChuaCircuit'],
    params={'L.L': [15, 21]}, # Can use none for default
    args=dict(stopTime=[2500]))

# Formats in which to save the figures (e.g., ['pdf', 'eps', 'svg', 'png'])
# If the figures shouldn't be saved, specify an empty list.
FORMATS = ['pdf', 'png']

# End customize----------------------------------------------------------------

if RUN:
    # Create the script to load the packages, simulate, and save the results.
    MODELS, RESULTS_DIR = write_script(EXPERIMENTS, working_dir=WORKING_DIR,
                                       packages=PACKAGES, fname=FNAME)

    dymola = None

    def get_last_log(dymola):
        log = dymola.getLastErrorLog()
        print(log)

    try:
        # Instantiate the Dymola interface and start Dymola
        dymola = DymolaInterface()


        # dymola.ExecuteCommand("Advanced.CompileWith64=2")
        result = dymola.ExecuteCommand('Modelica.Utilities.System.setWorkDirectory("' + Path(WORKING_DIR).as_posix() + '")')

        print('DEBUG1')
        result = dymola.ExecuteCommand('RunScript("'+Path(os.path.join(os.getcwd(),FNAME)).as_posix()+'", true)')

        print('result code = '+str(result))

        if not result:
             print("Simulation failed. Below is the translation log.")
             get_last_log(dymola)

        # dymola.plot(["J1.w", "J2.w", "J3.w", "J4.w"])
        #dymola.plot(['STABLE_MOTION_G2_PRT.frame_a.f[1]','STABLE_MOTION_G2_PRT.frame_a.f[2]', 'STABLE_MOTION_G2_PRT.frame_a.f[3]'])
        #dymola.ExportPlotAsImage(os.path.join(dir_result, 'tmp.png'))

    except DymolaException as ex:
        print("Error: " + str(ex))

    if dymola is not None:
        dymola.close()
        dymola = None

else:
    MODELS = [experiment.model[experiment.model.rfind('.')+1:]
              for experiment in EXPERIMENTS]
    RESULTS_DIR = os.path.split(FNAME)[0]

# Create plots.
# Begin customize--------------------------------------------------------------

for i, model in enumerate(MODELS):
    sim = SimRes(os.path.join(RESULTS_DIR, str(i + 1), 'dsres.mat'))
    sim.plot(title="Chua Circuit with L = %.0f %s" % (sim['L.L'].IV(),
                                                      sim['L.L'].unit),
             ynames1=['L.i'], ylabel1='Current',
             ynames2=['L.der(i)'], ylabel2='Derivative of current',
             label=os.path.join(str(i + 1), model))

# End customize----------------------------------------------------------------

# Save the plots.
saveall(FORMATS)
plt.show()
