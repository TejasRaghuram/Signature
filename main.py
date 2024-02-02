import streamlit
import numpy
import cv2
from colour import Color
from PIL import Image

streamlit.title('Signature')

image = streamlit.file_uploader('Upload Image', type=['png'])

if image is not None:
    image = cv2.imread(image.name, cv2.IMREAD_GRAYSCALE)
    threshold = streamlit.slider('Threshold', min_value=0, max_value=255)
    color = Color(streamlit.color_picker('Pick A Color', '#ffffff'))

    if streamlit.button('Process'):
        output = []
        for row in image:
            output.append([])
            for pixel in row:
                if pixel < int(threshold):
                    output[len(output) - 1].append([int(color.red * 255), int(color.green * 255), int(color.blue * 255), 255])
                else:
                    output[len(output) - 1].append([0, 0, 0, 0])
        streamlit.image(numpy.array(output))
