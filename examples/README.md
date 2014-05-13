Example data files:
 1. [ChuaCircuit.mat](ChuaCircuit.mat): Simulation result of
    Modelica.Electrical.Analog.Examples.ChuaCircuit from the
    [Modelica Standard Library] version 3.2 (2010-10-25, build 5) with a stop
    time of 2500 s.  This can be generated by
    [ChuaCircuit/sim-and-plot.py](ChuaCircuit/sim-and-plot.py) (via Dymola; the
    first result of the two) or by the example in the documentation for the
    *gen_sim_script* method of *modelicares.exps* (see
    [../doc/exps.html](../doc/exps.html)).
 2. [dsin.txt](dsin.txt): Parameter input file for
    Modelica.Electrical.Analog.Examples.ChuaCircuit, generated from Dymola 7.4.
 3. [load-csv.csv](load-csv.csv): From
    http://en.wikipedia.org/wiki/Comma-separated_values#Example, accessed
    2012-10-11.
 4. [PID.mat](PID.mat): Linearization result of
    Modelica.Blocks.Continuous.PID.
 5. [ThreeTanks.mat](ThreeTanks.mat): Simulation result of
    Modelica.Fluid.Examples.ThreeTanks.

IPython notebooks:
 1. [tutorial.ipynb](tutorial.ipynb): Tutorial for ModelicRes.

Scripts:
 1. [load-csv.py](load-csv.py): Example of using *modelicares.load_csv()*.

Folders:
 1. [ChuaCircuit](ChuaCircuit):  Contains an example script
    ([ChuaCircuit/sim-and-plot.py](ChuaCircuit/sim-and-plot.py)) to run
    Modelica.Electrical.Analog.Examples.ChuaCircuit with various settings and
    plot the results.  The results and plots are also saved there.
 2. [PID](PID):  Contains an example script ([PID/lin.py](PID/lin.py)) to
    linearize Modelica.Blocks.Continuous.PID with various settings and plot the
    results.  The results and plots are also saved there.

Images from the examples in the ModelicaRes documentation are generated here.


[Modelica Standard Library]: https://github.com/modelica/ModelicaStandardLibrary