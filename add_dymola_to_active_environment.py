# this works on windows
import os
import sys

# this adds dymola as package to the installation
python_packages_path = os.path.join(os.path.dirname(sys.executable), 'Lib\\site-packages')

dymola_search_path1 = os.path.join('C:\\',  'Program Files',
                      'Dymola 2018 FD01',
                      'Modelica',
                      'Library',
                      'python_interface',
                      'dymola.egg')
dymola_search_path2 = os.path.join('C:\\',  'Program Files',
                      'Dymola 2018',
                      'Modelica',
                      'Library',
                      'python_interface',
                      'dymola.egg')

with open(os.path.join(python_packages_path, 'dymola-python-interface.pth'), 'w') as pathfile:
    pathfile.write(dymola_search_path2+'\n'+dymola_search_path1+'\n')