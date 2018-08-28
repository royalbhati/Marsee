'''
Usage : $ python test.py eda.py

'''



import os
import nbformat
from nbformat.v4 import new_notebook, new_code_cell
import subprocess
import sys
nb = new_notebook()
with open(sys.argv[1]) as f:
    code = f.read()

nb.cells.append(new_code_cell(code))
nbformat.write(nb, sys.argv[1][:-3]+'.ipynb')

name=sys.argv[1][:-3]+'.ipynb'

# os.system('jupyter nbconvert --execute --to'+name+'--inplace'+name)  
# jupyter nbconvert --execute --to notebook --inplace <notebook>
print('#'*5,'Doing EDAAAAAAAAAAAAAAAAAA ','#'*10)
subprocess.check_call(['jupyter','nbconvert','--execute','--to',name,'--inplace',name])
subprocess.check_call(['ipython','nbconvert','--to','html',name])
print('#'*5,'Saved in ',name[:-6]+'.html','#'*10)
