import PySimpleGUI as sg

# Define the layout
layout = [
    [sg.Text('Downloading IMD gridded Data as CSV Files', size=(40, 1), font=("Helvetica", 14))],
    [sg.Text('Choose the time range to download', size=(40, 1))],
    [sg.Text('Start Date', size=(10, 1), justification='center'), sg.Text('End Date', size=(10, 1), justification='center')],
    [sg.CalendarButton('Start Date', target=(1, 2), key='start_date', format='%Y-%m-%d'), sg.CalendarButton('End Date', target=(1, 3), key='end_date', format='%Y-%m-%d')],
    [sg.Text('Coordinates input file (csv file with lat as first column and lon as second column)', size=(40, 2))],
    [sg.In(), sg.FileBrowse()],
    [sg.Checkbox('TMAX', default=True, key='tmaxcheck'), sg.Checkbox('TMIN', key='tmincheck'), sg.Checkbox('RAIN', key='raincheck')],
    [sg.Submit(), sg.Cancel()]
]

# Create the window
window = sg.Window('IMD-GRD-EXTRACT', layout, default_element_size=(40, 1))

# Event loop
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Cancel':
        break
    elif event == 'Submit':
        # Process the selected dates and other input values
        start_date = values['start_date']
        end_date = values['end_date']
        print("Start Date:", start_date)
        print("End Date:", end_date)
        print("Coordinates file:", values[0])  # Assuming the file input field key is 0
        print("TMAX:", values['tmaxcheck'])
        print("TMIN:", values['tmincheck'])
        print("RAIN:", values['raincheck'])

window.close()
