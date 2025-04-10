import cv2

def get_available_cameras():
      available_cameras = []

      for i in range(5):
            cap = cv2.VideoCapture(0)

            cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))


            if cap.isOpened():
                    available_cameras.append(i)
                    cap.release()
      return available_cameras


cameras = get_available_cameras()
if cameras:
      print("Available Cameras:", cameras)
else:
      print("No Cameras Found")