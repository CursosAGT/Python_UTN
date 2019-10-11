from Estructura import *
nuevo(0,"inicio");
#################################################################
def Ej_ya_hechos():
	#Con tab colocaremos aqui las prácticas hechas
	pass
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║              Unidad 5 - MySQL, Parte 1                                      ║
║                 * INSERT, UPDATE, DELETE, SELECT                            ║
║                 * FECHAS Y HORAS                                            ║
║                 * %LIKE%                                                    ║
║                 * JOIN                                                      ║
║                                                                             ║
║              Unidad 6 - MySQL, Parte 2                                      ║
║                 * MySQL en Python                                           ║
║                 * Cursor y verificación de consultas                        ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║                              manejo de imagennes                            ║
║                                                                             ║
║                              libreria opencv2                               ║
║                                                                             ║
║                              ROI, Region of Image                           ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║              Unidad 8 - OPEN cv2                                            ║
║                 * Procesamiento de imágenes en Opencv2                      ║
║                 * Detección y descripción de imágenes                       ║
║                 * Detección de objetos                                      ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
pip install numpy
pip install opencv-python
pip install matplotlib
pip install Pillow==2.2.2
pip install imutils




https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_setup/py_setup_in_windows/py_setup_in_windows.html

https://docs.opencv.org/master/d6/d00/tutorial_py_root.html
# si da error copiar y pegar en un buscador y rastrear el link

https://opencv-python-tutroals.readthedocs.io/en/latest/

https://docs.python.org/3/library/sched.html
https://www.quora.com/How-do-I-install-Python-packages-in-Anaconda
https://docs.python.org/2/library/sched.html
https://pypi.org/project/opencv2-python/
https://docs.opencv2.org/3.0-beta/doc/py_tutorials/py_tutorials.html
https://docs.opencv2.org/trunk/d5/de5/tutorial_py_setup_in_windows.html
https://www.pyimagesearch.com/2018/07/19/opencv-tutorial-a-guide-to-learn-opencv/
https://pythonprogramming.net/loading-images-python-opencv-tutorial/
https://github.com/jrosebr1/imutils");
https://www.pyimagesearch.com/2015/11/09/pedestrian-detection-opencv/

http://acodigo.blogspot.com/2017/08/deteccion-de-contornos-con-opencv-python.html");
https://www.learnopencv.com/invisibility-cloak-using-color-detection-and-segmentation-with-opencv/"
https://www.youtube.com/watch?time_continue=18&v=YLnP2Ge65MU"
\n\n\nen especial\nhttps://pythonprogramming.net/drawing-writing-python-opencv-tutorial/?completed=/loading-video-python-opencv-tutorial/
https://foro.elhacker.net/scripting/vision_artificial_con_python-t467756.0.html
https://github.com/CAChemE/curso-opencv-python
""");

import numpy as np
import cv2
from matplotlib import pyplot as plt
import imutils
import os
limpiar();

#################################################################
#Clase_openCV_01
# Make an array of 120,000 random bytes.
random_byte_array = bytearray(os.urandom(120000))
flat_numpy_array = np.array(random_byte_array)

# Convert the array to make a 400x300 grayscale image.
gray_image = flat_numpy_array.reshape(300, 400)
cv2.imshow('Random gray', gray_image)

# Convert the array to make a 400x100 color image.
bgr_image = flat_numpy_array.reshape(100, 400, 3)
cv2.imshow('Random color', bgr_image)

cv2.waitKey(1000)
cv2.destroyAllWindows()
imagen = cv2.imread("brazo_robotico.png")
nuevo(1);
#################################################################
#Clase_openCV_02

cv2.imshow("ej016_1", imagen)
cv2.waitKey(1500)
cv2.destroyAllWindows()
nuevo(2);
#################################################################
#Clase_openCV_03
print("Inicio ej016_2 - ");
imagen2 = (255-imagen)
print("Hay un caso especial en que puedes crear una ventana y cargar la imagen posteriormente. En ese caso, puedes especificar si la ventana es redimensionable o no. Esto se realiza con la función cv2.namedWindow(). Por defecto, el indicador (o bandera) es cv2.WINDOW_AUTOSIZE. Pero si se especifica la que el indicador sea  cv2.WINDOW_NORMAL, puedes cambiar el tamaño de la ventana. Esto será útil cuando las dimensiones de la imagen sean muy grandes y se añada una barra de seguimiento (o un scroll).")
cv2.namedWindow('imagen2', cv2.WINDOW_NORMAL)
cv2.namedWindow('imagen2', cv2.WINDOW_AUTOSIZE)
cv2.imshow("WINDOW_AUTOSIZE", imagen)
cv2.imshow("WINDOW_AUTOSIZE", imagen2)
cv2.waitKey(1500)
cv2.destroyAllWindows()
nuevo(3);
#################################################################
#Clase_openCV_04

rimagen=imagen.copy()
rimagen=cv2.flip(imagen,1)

fimagen=imagen.copy()
fimagen=cv2.flip(imagen,0)
cv2.imshow("Original", imagen)
cv2.imshow("vertical flip", rimagen)
cv2.imshow("horizontal flip", fimagen)
cv2.waitKey(1500)
cv2.destroyAllWindows()
nuevo(4);
#################################################################
#Clase_openCV_05
frame = cv2.imread("brazo_robotico.png")
if frame is None:
    print('Error no encontre la imagen brazo_robotico.png')
    exit()
rows = frame.shape[0]
cols = frame.shape[1]
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV);
for i in range(0, cols):
    for j in range(0, rows):
        hsv[j, i][1] = 255;
frame = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR);
cv2.imshow("chau blanco", frame)
cv2.waitKey(1500)
cv2.destroyAllWindows()
nuevo(5);
#################################################################
#Clase_openCV_06
img = cv2.imread("brazo_robotico.png")
res = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)

cv2.imshow("apmlio x2 ", res)
cv2.waitKey(1500)
cv2.destroyAllWindows()
nuevo(6);
#################################################################
#Clase_openCV_07
img = cv2.imread("brazo_robotico.png")
height, width, depth = img.shape
circle_img = np.zeros((height, width), np.uint8)
mask = cv2.circle(circle_img, (int(width / 2), int(height / 2)), 50, 1, thickness=-1)
masked_img = cv2.bitwise_and(img, img, mask=circle_img)
cv2.imshow("masked", masked_img)
cv2.waitKey(1500)
cv2.destroyAllWindows()
nuevo(7);
#################################################################
#Clase_openCV_08

img = cv2.imread("brazo_robotico.png")
# make sure that you have saved it in the same folder
# Averaging
# You can change the kernel size as you want
avging = cv2.blur(img,(10,10))

cv2.imshow('Averaging',avging)
cv2.waitKey(1500)

# Gaussian Blurring
# Again, you can change the kernel size
gausBlur = cv2.GaussianBlur(img, (5,5),0)
cv2.imshow('Gaussian Blurring', gausBlur)
cv2.waitKey(1500)

# Median blurring
medBlur = cv2.medianBlur(img,5)
cv2.imshow('Media Blurring', medBlur)
cv2.waitKey(1500)

# Bilateral Filtering
bilFilter = cv2.bilateralFilter(img,9,75,75)
cv2.imshow('Bilateral Filtering', bilFilter)
cv2.waitKey(1500)
cv2.destroyAllWindows()
nuevo(8);
#################################################################
#Clase_openCV_09
img = cv2.imread("brazo_robotico.png")
nemo = cv2.imread('nemo.png')
cv2.imshow("masked", nemo)
cv2.waitKey(1000)
cv2.destroyAllWindows()
nemo = cv2.cvtColor(nemo, cv2.COLOR_BGR2RGB)
cv2.imshow("masked", nemo)
cv2.waitKey(1500)
cv2.destroyAllWindows()
nuevo(9);
#################################################################
#Clase_openCV_010
imagen = cv2.imread('opencv_logo.png')
imagenA =  cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
cv2.imshow('Ej 016_9 Amarillo', imagenA)
cv2.waitKey(1500)
cv2.destroyAllWindows()
nuevo(10);
#################################################################
#Clase_openCV_011
# Algoritmo de deteccion de colores multiples
# Por Glar3
# www.robologs.net
#
# Busca los píxeles rojos, verdes y azules de una imagen


imagen = cv2.imread('opencv_logo.png')
imagen_copy = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

#Rango de colores detectados:
#Verdes:
verde_bajos = np.array([49,50,50])
verde_altos = np.array([107, 255, 255])
#Azules:
azul_bajos = np.array([100,65,75], dtype=np.uint8)
azul_altos = np.array([130, 255, 255], dtype=np.uint8)
#Rojos:
rojo_bajos1 = np.array([0,65,75], dtype=np.uint8)
rojo_altos1 = np.array([12, 255, 255], dtype=np.uint8)
rojo_bajos2 = np.array([240,65,75], dtype=np.uint8)
rojo_altos2 = np.array([256, 255, 255], dtype=np.uint8)

#Crear las mascaras
mascara_verde = cv2.inRange(imagen_copy, verde_bajos, verde_altos)
mascara_rojo1 = cv2.inRange(imagen_copy, rojo_bajos1, rojo_altos1)
mascara_rojo2 = cv2.inRange(imagen_copy, rojo_bajos2, rojo_altos2)
mascara_azul = cv2.inRange(imagen_copy, azul_bajos, azul_altos)

#Juntar todas las mascaras
mask = cv2.add(mascara_rojo1, mascara_rojo2)
mask = cv2.add(mask, mascara_verde)
mask = cv2.add(mask, mascara_azul)

#Mostrar la mascara final y la imagen
cv2.imshow('Finale', mask)
cv2.imshow('Imagen', imagen)

#Salir con ESC
cv2.waitKey(1500)
cv2.destroyAllWindows()
nuevo(11);
#################################################################
#Clase_openCV_012

print("https://nbviewer.jupyter.org/github/CAChemE/opencv-python/blob/master/opencv-and-python.ipynb#3.-Manejo-de-ficheros,-c%C3%A1maras-e-interfaces-gr%C3%A1ficas-de-usuario")
img =  cv2.imread("brazo_robotico.png")

kernel = np.ones((5, 3), np.float32) / 9
dst = cv2.filter2D(src=img, ddepth=+8, kernel=kernel)
# Blur
k = 5
blur = cv2.blur(img, (k, k))
sigma = 0
GaussianBlur = cv2.GaussianBlur(img, (k, k), sigma)
# Sobel
k = 3
sobelx = cv2.Sobel(img, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=k)
sobely = cv2.Sobel(img, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=k)

# Show
cv2.imshow('Original', img)
cv2.imshow('filter2D', dst)
cv2.imshow('blur', blur)
cv2.imshow('GaussianBlur', GaussianBlur)
cv2.imshow('Sobel X', sobelx)
cv2.imshow('Sobel Y', sobely)
cv2.waitKey(1500)
cv2.destroyAllWindows()
nuevo(12);
#################################################################
#Clase_openCV_013
img =  cv2.imread("brazo_robotico.png")

# RGB -> Grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Input image should be grayscale and float32 type
gray = np.float32(gray)

# Corner detection
dst = cv2.cornerHarris(gray, blockSize=2, ksize=3, k=0.04)

# Threshold for an optimal value, it may vary depending on the image.
img[dst>0.01*dst.max()]=[0,0,255]

# Show
cv2.imshow('dst', img)

cv2.waitKey(1500)
cv2.destroyAllWindows()
nuevo(13);
#################################################################
#Clase_openCV_014
# Initiate ORB detector
if cv2.__version__.startswith('2.4'):
    orb = cv2.ORB()
else:
    orb = cv2.ORB_create()

# Find the keypoints and descriptors with ORB
kp, des = orb.detectAndCompute(img, None)

# Draw only keypoints location, not size and orientation
img2 = cv2.drawKeypoints(img, kp, None, color=(0, 255, 0), flags=0)
cv2.imshow('Keypoints', img2)
cv2.waitKey(1500)
cv2.destroyAllWindows()
nuevo(14);
#################################################################
#Clase_openCV_015
imagen = cv2.imread("brazo_robotico.png")
img2gray = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
(h, w, d) = imagen.shape
print("width={}, height={}, depth={}".format(w, h, d))
cv2.imshow("Ej 016_2", img2gray)
cv2.waitKey(1500)
cv2.destroyAllWindows()
nuevo(15);
#################################################################
#Clase_openCV_016
resized = cv2.resize(imagen, (200, 200))
cv2.imshow("Fixed Resizing", resized)
cv2.waitKey(1500)
cv2.destroyAllWindows()
nuevo(16);
#################################################################
#Clase_openCV_017
r = 800.0 / w
dim = (800, int(h * r))
resized = cv2.resize(imagen, dim)
cv2.imshow("Aspect Ratio Resize", resized)
cv2.waitKey(1500)
cv2.destroyAllWindows()
nuevo(17);
#################################################################
#Clase_openCV_018
resized = imutils.resize(imagen, width=600)
cv2.imshow("Imutils Resize", resized)
cv2.waitKey(1500)
cv2.destroyAllWindows()
nuevo(18);
#################################################################
#Clase_openCV_019
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, -45, 1.0)
rotated = cv2.warpAffine(imagen, M, (w, h))
cv2.imshow("Opencv2 Rotation", rotated)
cv2.waitKey(1500)
cv2.destroyAllWindows()
nuevo(19);
#################################################################
#Clase_openCV_020
rotated = imutils.rotate(imagen, 45)
cv2.imshow("Imutils Rotation", rotated)
cv2.waitKey(1500)
cv2.destroyAllWindows()
nuevo(20);
#################################################################
#Clase_openCV_021
blurred = cv2.GaussianBlur(imagen, (11, 11), 0)
cv2.imshow("Blurred", blurred)
cv2.waitKey(1500)
cv2.destroyAllWindows()
nuevo(21);
#################################################################
#Clase_openCV_022
print("grabo ");
# cargar el archivo PNG indicado
print("cargar el archivo PNG indicado");
img = cv2.imread('image.png', cv2.IMREAD_GRAYSCALE)
# guardar la imagen en formato JPG
print("guardar la imagen en formato JPG");
cv2.imwrite('save.jpg', img)
nuevo(22);
#################################################################
#Clase_openCV_023
output = imagen.copy()
cv2.rectangle(output, (10, 120), (100, 250), (0, 0, 255), 2)
cv2.imshow("Rectangle", output)
cv2.waitKey(1500)
cv2.destroyAllWindows()
nuevo(23);
#################################################################
#Clase_openCV_024
output = imagen.copy()
cv2.circle(output, (200, 200), 50, (255, 0, 0), -1)
cv2.imshow("Circle", output)
cv2.waitKey(1500)
cv2.destroyAllWindows()
nuevo(24);
#################################################################
#Clase_openCV_025
output = imagen.copy()
cv2.putText(output, "UTN 2019 en Opencv2!!!", (10, 25),
cv2.FONT_HERSHEY_SIMPLEX, 0.7, (55, 55, 255), 2)
cv2.imshow("Texto", output)
cv2.waitKey(1500)
cv2.destroyAllWindows()
nuevo(25);
#################################################################
#Clase_openCV_026
imagen = cv2.imread("brazo_robotico.png",cv2.IMREAD_GRAYSCALE)
cv2.imshow("Escalas de grices", imagen)
cv2.waitKey(1500)
cv2.destroyAllWindows()
nuevo(26);
#################################################################
#Clase_openCV_027
img1 = cv2.imread("brazo_robotico.png")
img2 = cv2.imread('brazo_robotico_marco.png')
add = img2+img1
cv2.imshow('add',add)
cv2.waitKey(1500)
cv2.destroyAllWindows()
nuevo(27);
#################################################################
#Clase_openCV_028
img = cv2.imread("brazo_robotico.png")
retval, threshold = cv2.threshold(img, 112, 155, cv2.THRESH_BINARY)
cv2.imshow('original',img)
cv2.imshow('threshold',threshold)
cv2.waitKey(1500)
cv2.destroyAllWindows()
nuevo(28);
#################################################################
#Clase_openCV_029
imagen = cv2.imread("brazo_robotico.png",cv2.IMREAD_COLOR)
cv2.line(imagen,(0,0),(150,150),(100,25,200),15)
cv2.imshow('image',imagen)
cv2.waitKey(1500)
cv2.destroyAllWindows()
nuevo(29);
#################################################################
#Clase_openCV_030
imagen = cv2.imread("brazo_robotico.png",cv2.IMREAD_COLOR)
#referenciamos un sector en especial via ROI,  Region of Image,:
px = imagen[100:150,100:150]
print(px)
#ponemos en ROJO el ROI elegido:
imagen[100:150,100:150] = [0,0,255]
#Referencias y caracteristicas de la image:
print(imagen.shape)
print(imagen.size)
print(imagen.dtype)
#operamos copiamos y pegamos:
celu = imagen[120:251,10:100]
imagen[0:131,160:250] = celu

cv2.imshow('image',imagen)
cv2.waitKey(1500)
cv2.destroyAllWindows()
nuevo(30);
#################################################################
#Clase_openCV_031
img1 = cv2.imread("brazo_robotico.png")
img2 = cv2.imread('icono.png')
# I want to put logo on top-left corner, So I create a ROI
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols ]
# Now create a mask of logo and create its inverse mask
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
# add a threshold
ret, mask = cv2.threshold(img2gray, 255, 25, cv2.THRESH_BINARY_INV)
mask_inv = cv2.bitwise_not(mask)
# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)
dst = cv2.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst
cv2.imshow('res',img1)
cv2.waitKey(1500)
cv2.destroyAllWindows()
nuevo(31);
#################################################################

#Clase_openCV_032
print("Inicio ej016_30 - ");
print("1. Umbral binario (THRESH_BINARY)");
print("Si la intensidad del pixel es mayor al umbral establecido el pixel de destino a establece al máximo valor definido, en caso contrario se establece a cero:");
gray = cv2.imread("brazo_robotico.png", cv2.IMREAD_GRAYSCALE)
t, dst = cv2.threshold(gray, 70, 155, cv2.THRESH_BINARY)
cv2.imshow('umbral', gray)
cv2.imshow('result', dst)
cv2.waitKey(1500)
cv2.destroyAllWindows()
print("2. Umbral binario invertido (THRESH_BINARY_INV)");
print("Similar al anterior, solo que aplicado al inverso, si la intensidad supera el umbral definido el valor resultante será establecido a cero, en caso contrario se establecerá al máximo valor definido.");

gray = cv2.imread("brazo_robotico.png")
t, dst = cv2.threshold(gray, 170, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('umbral', gray)
cv2.imshow('result', dst)
cv2.waitKey(1500)
cv2.destroyAllWindows()

print("3. Truncar (THRESH_TRUNC)");
print("En este caso si la intensidad del pixel es superior al umbral entonces el pixel destino se establece a el valor del umbral, en caso contrario el valor será igual al original, en otras palabras, cualquier pixel que supere el umbral tomará el valor del mismo, los demás permanecen igual.");
gray = cv2.imread("brazo_robotico.png", cv2.IMREAD_GRAYSCALE)
t, dst = cv2.threshold(gray, 170, 255, cv2.THRESH_TRUNC)
cv2.imshow('umbral', gray)
cv2.imshow('result', dst)
cv2.waitKey(1500)
cv2.destroyAllWindows()
print("4. Ajustar a cero (THRESH_TOZERO)");
print("Cualquier pixel cuya intensidad no supere el umbral se establecerá a cero, se define de la siguiente manera:");
gray = cv2.imread("brazo_robotico.png")
t, dst = cv2.threshold(gray, 170, 255, cv2.THRESH_TOZERO)
cv2.imshow('umbral', gray)
cv2.imshow('result', dst)
cv2.waitKey(1500)
cv2.destroyAllWindows()
print("5. Ajuste a cero invertido (THRESH_TOZERO_INV)");
print("Similar al anterior, pero al inverso, esta vez, si la intensidad supera el umbral establecido el valor de salida se ajustará acero.");
gray = cv2.imread("brazo_robotico.png")
t, dst = cv2.threshold(gray, 170, 255, cv2.THRESH_TOZERO_INV)
cv2.imshow('umbral', gray)
cv2.imshow('result', dst)
cv2.waitKey(1500)
cv2.destroyAllWindows()

nuevo(32);
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                    ver tema librerias y si finaliza mal,                    ║
║                    reveer anulando el ejercicio                             ║
║                                                                             ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝""")
#################################################################
#Clase_openCV_033
cap = cv2.VideoCapture('video-using-opencv.mp4',0)
while(cap.isOpened()):
  ret, frame = cap.read()
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  cv2.imshow('frame',gray)
  if cv2.waitKey(1) & 0xFF == ord('q'):
      break
cap.release()
cv2.destroyAllWindows()
nuevo(33);

#################################################################
#Clase_openCV_034
captura = cv2.VideoCapture('video-using-opencv.mp4')
while(1):
    #Capturamos una imagen y la convertimos de RGB -> HSV
    _, imagen = captura.read()
    hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

    #Establecemos el rango de colores que vamos a detectar
    #En este caso de verde oscuro a verde-azulado claro
    verde_bajos = np.array([49,50,50], dtype=np.uint8)
    verde_altos = np.array([80, 255, 255], dtype=np.uint8)

    #Crear una mascara con solo los pixeles dentro del rango de verdes
    mask = cv2.inRange(hsv, verde_bajos, verde_altos)

    #Encontrar el area de los objetos que detecta la camara
    moments = cv2.moments(mask)
    area = moments['m00']

    #Descomentar para ver el area por pantalla
    #print area
    if(area > 2000000):
        #Buscamos el centro x, y del objeto
        x = int(moments['m10']/moments['m00'])
        y = int(moments['m01']/moments['m00'])

        #Mostramos sus coordenadas por pantalla
        print ("x = ", x)
        print ("y = ", y)

        #Dibujamos una marca en el centro del objeto
        cv2.rectangle(imagen, (x, y), (x+2, y+2),(0,0,255), 2)

    #Mostramos la imagen original con la marca del centro y
    #la mascara
    cv2.imshow('mask', mask)
    cv2.imshow('Camara', imagen)
    tecla = cv2.waitKey(5) & 0xFF
    if tecla == 27:
        break

cv2.destroyAllWindows()

nuevo(34);
#################################################################
#Clase_openCV_035
video_file = 'video-using-opencv.mp4'
cap = cv2.VideoCapture(video_file)

while (cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()

    if ret == True:
        # Operations on the frame
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        cv2.imshow('frame', gray)

        # Exit?
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
nuevo(36);
#################################################################
#Clase_openCV_037
cap = cv2.VideoCapture(video_file)

# Properties
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
color = (255,255,255)
thickness = 1

if cv2.__version__.startswith('2.4'):
    height_prop = cv2.cv.CV_CAP_PROP_FRAME_HEIGHT
else:
    height_prop = cv2.CAP_PROP_FRAME_HEIGHT

if cv2.__version__.startswith('2.4'):
    fps_prop = cv2.cv.CV_CAP_PROP_FPS
else:
    fps_prop = cv2.CAP_PROP_FPS

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        # Text position
        height = int(cap.get(height_prop))
        position = (50, height - 50)

        # Frames per second
        fps = "{0:.2f}".format(cap.get(fps_prop))
        text = "FPS: " + fps

        # Put text
        cv2.putText(frame, text, position, font, font_scale, color, thickness)

        # Display
        cv2.imshow("Video", frame)

        # Exit?
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
cv2.destroyAllWindows()
nuevo(37);
#################################################################
#Clase_openCV_038
# empty function called when
# any trackbar moves
def emptyFunction():
    pass
def main():
	# blackwindow having 3 color chanels
	image = np.zeros((512, 512, 3), np.uint8)
	windowName ="Open CV Color Palette"
	# window name
	cv2.namedWindow(windowName)
	# there trackbars which have the name
	# of trackbars min and max value
	cv2.createTrackbar('Blue', windowName, 0, 255, emptyFunction)
	cv2.createTrackbar('Green', windowName, 0, 255, emptyFunction)
	cv2.createTrackbar('Red', windowName, 0, 255, emptyFunction)
	# Used to open the window
	# till press the ESC key
	while(True):
		cv2.imshow(windowName, image)
		if cv2.waitKey(1) == 27:
			break
		# values of blue, green, red
		blue = cv2.getTrackbarPos('Blue', windowName)
		green = cv2.getTrackbarPos('Green', windowName)
		red = cv2.getTrackbarPos('Red', windowName)
		# merge all three color chanels and
		# make the image composites image from rgb
		image[:] = [blue, green, red]
		#print(blue, green, red)
	cv2.waitKey(3000)
	cv2.destroyAllWindows()
# Calling main()
if __name__=="__main__":
    main()
nuevo(38,"fin");
#################################################################

