import cv2
import os

folder = "screenshots"
output_file = "video.mp4"

images = sorted([img for img in os.listdir(folder) if img.endswith(".png")])

frame = cv2.imread(os.path.join(folder,images[0]))
height, width, layers = frame.shape

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
video = cv2.VideoWriter(output_file,fourcc,2,(width,height))


for image in images:
    img_path = os.path.join(folder,image)
    frame = cv2.imread(img_path)
    video.write(frame)

video.release()
print("The video's done !!")
