# ComputerVisionMiniProject1

## Making frames from videos:
1. Open anaconda
2. Go to folder where the videos are
3. Install ffmpeg: 
``conda install -c conda-forge ffmpeg``
4. Now make frames from the video by specfying how many fps are required:
```
ffmpeg -i Recording1.avi -vf fps=5 img_a_%d.jpg
```
