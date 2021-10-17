import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\\Tesseract-OCR\\tesseract.exe'

path = input('write path\n')


img = cv2.imread(path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

config = r'--oem 3 --psm 3'
print(pytesseract.image_to_string(img, config=config))

data = pytesseract.image_to_data(img, config=config)

for i, line in enumerate(data.splitlines()):
	if i == 0:
		continue

	line = line.split()

	try:
		x, y, w, h = int(line[6]), int(line[7]), int(line[8]), int(line[9])
		cv2.rectangle(img, (x, y), (w + x, h + y), (0, 0, 255), 1)
		cv2.putText(img, line[11], (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1)
	except IndexError:
		pass

cv2.imshow('Result', img)
cv2.waitKey(0)