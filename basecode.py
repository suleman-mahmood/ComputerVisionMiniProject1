import cv2
import threading


def main():

    print("Press 1 for pre-recorded videos, 2 for live stream: ")
    option = int(input())

    def func(option, val, http):

        if option == 1:
            # Record video
            windowName = "Sample Feed from Camera " + str(val)
            cv2.namedWindow(windowName)

            # sample code for mobile camera video capture using IP camera
            capture = cv2.VideoCapture(http)
    # ---------------------------------------------------------------------------------------------------------------------------------------
            # define size for recorded video frame for video
            width = int(capture.get(3))
            height = int(capture.get(4))
            size = (width, height)
    # --------------------------------------------------------------------------------------------------------------------------------------
            # frame of size is being created and stored in .avi file
            file_name = 'Recording' + str(val) + '.avi'
            optputFile = cv2.VideoWriter(
                file_name, cv2.VideoWriter_fourcc(*'MJPG'), 10, size)

    # -------------------------------------------------------------------------------------------------------------------------------------
            # check if feed exists or not for camera
            if capture.isOpened():
                ret, frame = capture.read()
            else:
                ret = False

    # --------------------------------------------------------------------------------------------------------------------------------
            while ret:
                ret, frame = capture.read()

                # sample feed display from camera
                cv2.imshow(windowName, frame)

                # saves the frame from camera
                optputFile.write(frame)

                # escape key (27) to exit
                if cv2.waitKey(1) == 27:
                    break
    # ----------------------------------------------------------------------------------------------------------------------------------
            capture.release()
            optputFile.release()

            cv2.destroyWindow(windowName)
    # ------------------------------------------------------------------------------------------------------------------------------------
        elif option == 2:

            # live stream
            windowName = "Live Stream Camera " + str(val)
            cv2.namedWindow(windowName)

            # sample code for mobile camera video capture using IP camera
            capture = cv2.VideoCapture(http)

            if (capture.isOpened()):  # check if feed exists or not for camera
                ret, frame = capture.read()

            else:
                ret = False

            while ret:
                ret, frame = capture.read()

                cv2.imshow(windowName, frame)

                if cv2.waitKey(1) == 27:
                    break

            capture.release()
            cv2.destroyWindow(windowName)

        else:
            print("Invalid option entered. Exiting...")

    # threading to take input of three cameras simultaneosly
    t1 = threading.Thread(target=func, args=(option, 1, "http://10.130.140.37:8080/video",))
    t2 = threading.Thread(target=func, args=(option, 2, 'http://10.130.19.186:8080/video',))
    t3 = threading.Thread(target=func, args=(option, 3, 'http://10.130.9.23:8080/video',))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()


main()
