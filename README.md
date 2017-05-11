# Grietas
Códigos en Python para detección de grietas en carretera

+ *Canny*: Ejemplo que usé como base para hacer el Canny Threshold. Autor original Abid K. (abidrahman2@gmail.com)

+ *ROI*: Region of interest, código para seleccionar una región cuadrada de una imagen y trabajar sólo sobre ella, para usar, correr el programa, una ventana nueva con la imagen con algunos filtros ya puestos aparecerá. Seleccionar con el mouse el área de interés seleccionando y arrastrando. Un cuadrado verde aparecerá en el área seleccionada, cerrar la ventana y volverá a aparecer la misma ventana pero sin el cuadrado, presionar la tecla "C" para hacer el crop y aparecerá una ventana nueva sólo con el área seleccionadda originalmente.  La imagen nueva se guarda localmente en la computadora, tiene bugs de comportamiento (como tener que cerrar la ventana para que vuelva a aparecer y hacer el crop).

+ *Skeletonize*: Intento de mejorar el código de ejemplo de Canny, aplicando más filtros y en un orden diferente para obtener resultados diferentes, guarda las imágenes después de cada filtro aplicado si se desea.



Todos los scripts usan la librería de OpenCV y la de numpy, mientras que la de ROI también usa la librería de SciPy.
