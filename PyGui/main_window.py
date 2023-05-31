import PySimpleGUI as sg
import cv2
import preprocessing_script

sg.theme('DarkAmber')

# Create the layout for the GUI
first_column = [
    [sg.Text('Select an image file:',font=(20))],
    [sg.Input(), sg.FileBrowse(), sg.Button('Load')],
    [sg.Button('Preprocessing',size=(15,1),pad=(10,10,10,0),font=(20)),sg.Button('Detection',size=(15,1),pad=(10,10,10,10),font=(20))], 
    [sg.Button('Exit',size=(10,1),pad=(10,10,10,10),font=(20))],
]
 
    
preprocessed_image = [

    
    ],

output_image = [

    ],

image_viewer_column = [

    [sg.Image(key='image_preview')]
    ]
    
layout = [[sg.Column([[sg.Column(first_column)]]),
           sg.VSeperator(),
           sg.Column([[sg.Frame("Input Image", image_viewer_column, size=(250,250)),
           sg.Frame("Preprocessed Image", preprocessed_image, size=(250,250))],
                      [sg.Frame("DR Detection", output_image, size=(250,250))]],
             element_justification='left')
           ]]



# Create the window
window = sg.Window('Image Processing GUI', layout, size=(1100, 550))

input_image = None

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event == 'Load':
        try:
            # read the selected image file
            input_image = cv2.imread(values[0])
            if input_image is None:
                sg.popup('Error: Invalid file path or file type')
                continue
            # resize the image to a thumbnail size
            thumbnail = cv2.resize(input_image, (250, 250))
            # Display the image in the preview window
            imgbytes = cv2.imencode('.png', thumbnail)[1].tobytes()
            window['image_preview'].update(data=imgbytes)
        except Exception as e:
            sg.popup(f"An error occurred: {e}")
    if event == 'Preprocessing':
    # call the pre-processing script here
        if input_image is None:
            sg.popup('Error: No input image specified')
        else:
            preprocessing_script.preprocessing(input_image)

    if event == 'Detection':
        # code for detection goes here
        sg.popup('Detection button clicked')

window.close()
