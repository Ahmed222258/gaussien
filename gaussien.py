import cv2




image=cv2.imread('img/620c0292e79375ecd81ce99b_Example of luminance noise zoomed.jpg')










gaussian_blur = cv2.GaussianBlur(image, (7,7), 2)



cv2.imshow("gaussianblur",gaussian_blur)

cv2.waitKey(0)