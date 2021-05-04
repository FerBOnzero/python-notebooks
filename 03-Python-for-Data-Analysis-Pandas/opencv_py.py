import cv2

image = cv2.imread('/Users/omar/Documents/Baby_Yoda', 1)

cv2.imshow('Baby', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
