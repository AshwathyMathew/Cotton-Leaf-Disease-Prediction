import cv2
image=cv2.imread("Coloured_image.jpeg")
cv2.imshow("Coloured Image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
gray_image=cv2.imread("Coloured_image.jpeg", 0)
cv2.imshow("Gray Image", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()