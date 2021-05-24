import PySimpleGUI as sg

# layout
def login():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Login', font=('Courier 20'))],
        [sg.Text('')],
        [sg.Text('Email'), sg.Input(key= 'user', size=(20, 1))],
        [sg.Text('Password'), sg.Input(key= 'password', password_char='*', size=(20, 1))],
        [sg.Button('Enter')]
    ]
    return sg.Window('Login', layout=layout, finalize=True)

# Mostrar janela 1
window1 = login()

while True:
    # ler interações
    window, events, values = sg.read_all_windows()

    # fechar janela
    if window == window1 and events == sg.WINDOW_CLOSED:
        break

    # pressionar botão 'Enter'
    if window == window1 and events == 'Enter':
        print(" Welcome, " + values['user'] +'.')
        break