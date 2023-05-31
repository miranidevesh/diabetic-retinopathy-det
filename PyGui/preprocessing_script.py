import PySimpleGUI as sg
import cv2


def preprocessing(input_image):
    sg.theme('DarkAmber')


    # Create the layout for the GUI
    first_column = [
        [sg.Text('Select image pre-processing techniques:',font=(20))],
        [sg.Checkbox('Grayscale', 'technique',font=(20)), sg.Checkbox ('CLAHE', 'technique',font=(20)),sg.Checkbox('Resize', 'technique',font=(20))],
        [sg.Checkbox('Normalize', 'technique',font=(20))],
        [sg.Button('Process',pad=(10,10,10,10),font=(20),size=(10,1)), sg.Button('Cancel',font=(20),size=(10,1))],
    ]

    image_viewer_column = [

        [sg.Image(key='preprocessed_image')]
    ]

    layout = [
        [sg.Column(first_column),
        sg.VSeperator(),
        sg.Frame("Preprocessed Image",image_viewer_column,size=(250,250))
        ]
    ]

    # Create the window
    window = sg.Window('Image Processing GUI', layout, size=(600, 270),finalize=True)


    #Resizing the image
    thumbnail = cv2.resize(input_image, (250, 250))
    # update the preview window with the input image
    imgbytes = cv2.imencode('.png', thumbnail)[1].tobytes()
    window['preprocessed_image'].update(data=imgbytes)
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break
        if event == 'Process':
            
            technique = values[1]
            if technique == 'Grayscale':
                    output_image = cv2.imread(input_image)
                    output_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

                    
            elif technique == 'CLAHE':
                ret, output_image = cv2.threshold(input_image, 127, 255, cv2.THRESH_BINARY)
            elif technique == 'Resize':
                output_image = cv2.GaussianBlur(input_image, (5, 5), 0)
            elif technique == 'Normalize':
                output_image = cv2.GaussianBlur(input_image, (5, 5), 0)
            else:
                output_image = input_image
            # resize the output image to a thumbnail size
            thumbnail = cv2.resize(output_image, (250, 250))
            # update the preview window with the processed image
            imgbytes = cv2.imencode('.png', thumbnail)[1].tobytes()
            window['preprocessed_image'].update(data=imgbytes)

    window.close()
