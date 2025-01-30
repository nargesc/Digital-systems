import os

video_file = "T3.2.mp4"


os.system("git add " + video_file)
os.system('git commit -m "Added video file"')
os.system("git push origin main")

