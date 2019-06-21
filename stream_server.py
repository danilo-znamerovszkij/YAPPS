import io
import socket
import struct
import cv2
import numpy as np


## show the gui
# root = tk.Tk()
# root.geometry("400x300")
#
# app = MoveGUI.Window(root)
# root.mainloop()

# Start a socket listening for connections on 0.0.0.0:8000 (0.0.0.0 means
# all interfaces)
server_socket = socket.socket()
server_socket.bind(('192.168.0.101', 8001))
server_socket.listen(0)
print('listening')


## Set the parameters for dice recognition
min_threshold = 10                      # these values are used to filter our detector.
max_threshold = 200                     # they can be tweaked depending on the camera distance, camera angle, ...
min_area = 100                          # ... focus, brightness, etc.
min_circularity = .3
min_inertia_ratio = .5
counter = 0                             # script will use a counter to handle FPS.
readings = [0, 0]                       # lists are used to track the number of pips.
display = [0, 0]

# Accept a single connection and make a file-like object out of it
connection = server_socket.accept()[0].makefile('rb')

try:
    while True:
        # Read the length of the image as a 32-bit unsigned int. If the
        # length is zero, quit the loop
        image_len = struct.unpack('<L', connection.read(struct.calcsize('<L')))[0]
        #print(image_len)
        if not image_len:
            break
        # Construct a stream to hold the image data and read the image
        # data from the connection
        
        image_stream = io.BytesIO()
        image_stream.write(connection.read(image_len))
        # Rewind the stream, open it as an image with PIL and do some
        # processing on it
        image_stream.seek(0)
        
        file_bytes = np.asarray(bytearray(image_stream.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

##lets try to detect some dice
        params = cv2.SimpleBlobDetector_Params()  # declare filter parameters.
        params.filterByArea = True
        params.filterByCircularity = True
        params.filterByInertia = True
        params.minThreshold = min_threshold
        params.maxThreshold = max_threshold
        params.minArea = min_area
        params.minCircularity = min_circularity
        params.minInertiaRatio = min_inertia_ratio

        detector = cv2.SimpleBlobDetector_create(params)  # create a blob detector object.

        keypoints = detector.detect(img)  # keypoints is a list containing the detected blobs.

        # here we draw keypoints on the frame.
        im_with_keypoints = cv2.drawKeypoints(img, keypoints, np.array([]), (0, 0, 255),
                                              cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

        #cv2.imshow("Dice Reader", im_with_keypoints)  # display the frame with keypoints added.

        reading = len(keypoints)  # 'reading' counts the number of keypoints (pips).

        if counter % 10 == 0:  # enter this block every X frames.
            readings.append(reading)  # note the reading from this frame.

            if readings[-1] == readings[-2] == readings[-3]:  # if the last 3 readings are the same...
                display.append(readings[-1])  # ... then we have a valid reading.

            # if the most recent valid reading has changed, and it's something other than zero, then print it.
            if display[-1] != display[-2] and display[-1] != 0:
                msg = str(display[-1]) + "\n****"
                print(msg)

        counter += 1

        try:
            x0 = keypoints[0].pt
            y0 = keypoints[1].pt
            msg = "x0: " + str(x0) + "\ny0: " + str(y0) + " \n"
            print(msg)
        except:
            pass



        k = cv2.waitKey(30) & 0xff  # press [Esc] to exit.
        if k == 27:
            break




        cv2.imshow("Video", im_with_keypoints)

        if cv2.waitKey(1) == ord("q"):
            cv2.destroyAllWindows()
            break

finally:
    connection.close()
    server_socket.close()
