# Firemark
Have you ever been searching an image and found one with watermark/logo on left side, one with logo on right side, and you didn't find the original image? This script can remove the unwanted content for you. Simply follow these instructions:

`python firemark.py` Firemark is fully compatible with Python 2.7.
 
After you start the script, application will ask you for the first file name. `Image 1: `
 
Then, of course, for the second file name. Just enter the names of those images.
 
`Image 1: img1.png`
 
`Image 2: img2.png`
 
Now, the script is printing out almost every (JPEG compression changes the RGB a little bit, so it logs only "bigger" color differences) difference in color. You can see x,y position, RGB on first image and RGB on second image in the log.
 
When this finishes, you will see 4 values. First and last appearance of difference on both x and y axes, formatted like
 
`first on x`
 
`first on y`
 
`last on x`
 
`last on y`
 
Then, it will ask you for `xstart`,`ystart`,`xend` and `yend`. Basically, values above. **But**, these values don't have to be accurate. Because you can can have more differences than just a watermark. This basically ask you for coordinates of a frame, which will be replaced.
 
Then it asks for `img`. This asks for **image from which the pixels in range determined above are gonna be put into the final image**. _Type **pixelMap** for the **first** image and **pixelMap2** for the **second** image.
 
Finally, it asks you for the name of the final image it will save these changes to.
`Save to (.png): final.png`
