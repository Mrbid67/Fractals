Para el desarrollo de esta práctica se han creado los siguientes programas en python (se ha elegido cambiar la plataforma de desarrollo de Unity a python debido a que mi método de 
implementación anterior resultaría muy poco eficiente para un alto número de puntos en pantalla) recursivo.py, mandelbrotyJulia.py y IFS_Fractals.py.

Recursivo (sierpinsky): Siguiendo el consejo de mi compañero David Gómez se ha utilizado (para el fractal recursivo de sierpinsky) una librería visual llamada turtle, que ofrece una
representación visual en tiempo real del dibujo que se está llevando a cabo. El fractal de sierpinsky es generado ejecutando el código recursivo.py. En dicho código
existe una variable global: PartyMode, si se pusiera a "True" generaría el fractal con un color aleatorio para cada triángulo.

Mandelbrot y Julia: El archivo mandelbrotyJulia se encarga de generar ambos fractales. Debido a la similaritud entre ambos se ha decidido fusionar el código en este mismo archivo. 
Cambiando el valor de las variables globales hacerMandel y hacerJulia se puede decidir que fractales generará el código.

IFS_Fractals: Contiene el código necesario para generar un triángulo de sierpinsky y un fractal de Fern mediante IFS. El código se ejecuta de forma secuencial, mostrando primero
el triángulo y despúes Fern. La forma de funcionamiento es: Se crean los arrays con las transformaciones dadas en las diapositivas de la asignatura, se calculan las probabilidades
par cada matriz a partir de los determinantes y se llama a la funcion IFS común que se encarga de generar los puntos. Especial agradecimiento a mi compañero Juan Becerro, ya que me ayudó a
reformular el planteamiento de mi código para su correcto funcionamiento basándonos en su implementación en Unity (recibí ayuda, especialmente, en la forma de calcularlas probabilidades).