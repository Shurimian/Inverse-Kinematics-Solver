import PySimpleGUI as sg
import numpy as np
import numpy.linalg as lin
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

# Content of the GUI
GUIContent = [[sg.Text("Joint Type")], [sg.Button("Revolute")], [sg.Button("Exit")], [sg.Text("Mode")], [sg.Button("Inverse Kinematics")], [sg.Button("Forwards Kinematics")]]

# Create GUI Window
window = sg.Window(title="Build-A-Bot", layout=GUIContent, margins=(480, 270))

# Create loop for GUI
while True:
    event, values = window.read()

    # End program if user closes window or presses the OK button
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    elif event == "Revolute":
        print("Revolute Joint")
    elif event == "Inverse Kinematics":
        print("Inverse Kinematics")
    elif event == "Forwards Kinematics":
        print("Forwards Kinematics")

window.close()