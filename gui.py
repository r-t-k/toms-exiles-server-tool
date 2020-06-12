import PySimpleGUIQt as sg
import time
import rcon
import gportal

def app():
    def restart_buffer():
        rcon.warn_players()
        time.sleep(3)


    sg.ChangeLookAndFeel('System Default 1')
    layout = [
            [sg.Text('Greater Wynnewood Exile Park', justification='c', font=('Courier', 22))],
            [sg.Text('STATUS:', key='-OUTPUT-')],
            [sg.Button('Restart', size=(150,50)), sg.Exit(size=(150,50))],
            ]

    window = sg.Window("Tom's Exile Server Tool", auto_size_text=True, auto_size_buttons=True,  font=('Helvetica', 16)).Layout(layout)

    while True:
        event, values = window.Read()
        print(event, values)
        if event is None or event == 'Exit':
            break
        if event == 'Restart':
            window['-OUTPUT-'].update('server restarted')
            restart_buffer()
            gportal.restart_server()
        
        
    window.close()