import cv2
import numpy as np

window_name = 'Video Processing'
cv2.namedWindow(window_name)

def on_x_slider_change(x):
    global x_value
    x_value = x

def on_resolution_slider_change(resolution):
    global output_resolution
    output_resolution = resolution

x_value = 0
output_resolution = 200
cv2.createTrackbar('X Value', window_name, x_value, 255, on_x_slider_change)
cv2.createTrackbar('Resolution', window_name, output_resolution, 1440, on_resolution_slider_change)


video_capture = cv2.VideoCapture('prod.mp4')

while True:
    ret, frame = video_capture.read()

    if not ret:
        break

    if video_capture.get(cv2.CAP_PROP_POS_FRAMES) % 5 == 0:
        yuv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)
        yuv_frame[:, :, 1] = x_value
        output_frame = cv2.resize(yuv_frame, (output_resolution, output_resolution))
        cv2.imshow(window_name, output_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
