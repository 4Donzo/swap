import cv2


def get_frames(path):

  vidcap = cv2.VideoCapture(path)

  success,image = vidcap.read()
  count = 0
  success = True
  
  while success:
    success, image = vidcap.read()
    if success:
        count += 1
        frame_path = f"extracted_frames/frame{count}.jpg"
        cv2.imwrite(frame_path, image)
    else:
        print("Finished extracting frames from video")
