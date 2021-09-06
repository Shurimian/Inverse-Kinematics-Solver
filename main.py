import PySimpleGUI as sg
import numpy as np
import numpy.linalg as lin
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

# Content of the GUI
GUIContent = [
    [sg.T("Joint Type")], 
    [sg.B("Revolute")], 
    [sg.T("Mode")], 
    [sg.B("Inverse Kinematics"), sg.B("Forwards Kinematics")],
    [sg.B("Exit")]
]

# Create GUI Window
window = sg.Window(title="Build-A-Bot", layout=GUIContent, margins=(480, 270))

# Create loop for GUI
while True:
    event, values = window.read()

    # End program if user closes window or presses the OK button
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == "Revolute":
        print("Revolute Joint")
    elif event == "Inverse Kinematics":
        print("Inverse Kinematics")
    elif event == "Forwards Kinematics":
        print("Forwards Kinematics")

window.close()