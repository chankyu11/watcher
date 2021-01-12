import cv2


src = cv2.imread("D:/googleImageDownloader-master/images/person/0 (1).jpg", cv2.IMREAD_COLOR)

h, w, c = src.shape

# 사이즈 확대
dst = cv2.pyrUp(src, dstsize=(w*2, h*2), borderType=cv2.BORDER_DEFAULT);

# 사이즈 축소
dst = cv2.pyrDown(src)

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()