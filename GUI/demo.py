import PySimpleGUI as sg

sg.theme('DarkAmber') #touch of color

#stufff in side window
layout = [ [sg.Text('Some text on first row'), 
[sg.Text('Enter sumn on row2'), sg.InputText()],[sg.Button("Ok"),sg.Button('Cancel')]]

window = sg.Window("Window Title", layout)

#event loop to process events and get the values of inputs
while True: 
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': #if user closes window or clicks cancel
        break
    print('You entered' , values[0])

window.close()    

          