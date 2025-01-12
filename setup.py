import cx_Freeze
import sys
import os
base = None

if sys.platform =='win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY']=r"C:\Users\PC\AppData\Local\Programs\Python\Python311\tcl\tcl8.6"
os.environ['TCL_LIBRARY']=r"C:\Users\PC\AppData\Local\Programs\Python\Python311\tcl\tk8.6"

executable=[cx_Freeze("login.py",base=base,icon="Face.ico")]

cx_Freeze.setup(
    name='Facial Recognition Software',
    options={"build_exe":{"pakages":["tkinter","os"],"include_files":["Face.ico","tcl86t.dll","tk86t.dll","College_image","data","database","Attendence_report"]}},  
    version='1.0',
    description='Face Recognition Automatic System   | Developed By AviralPandey',
    packages=['your_package'],  # Replace 'your_package' with the actual name of your package
    executables=executables
    )
   