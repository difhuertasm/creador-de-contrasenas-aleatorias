🔐 Password Maker 1.0
Password Maker 1.0 es un enerador de contraseñas seguras con interfaz gráfica usando Python y Tkinter. 
Permite crear claves robustas combinando caracteres especiales, palabras personalizadas y números aleatorios.

🧠 Características
1. Ventana de inicio con imagen personalizada.
2. Interfaz intuitiva para generar contraseñas seguras.
3. Estructura de clave: carácter-palabra-número-carácter.
4. Control de longitud mínima de la contraseña.
5. Posibilidad de guardar la contraseña generada en un archivo .txt.
6. Mensajes informativos mediante cuadros de diálogo (messagebox).

📦 Requisitos
1. Python 3.7 o superior
2. Tkinter (normalmente incluido con Python)
3. Archivo de imagen PW_M.png en la raíz del proyecto

🖼️ Interfaz
1. Puedes ingresar una palabra personalizada.
2. Escoger la longitud total de la contraseña.
3. Presionar el botón Crear contraseña para generarla.
4. Usar el menú para guardar la contraseña o ver información del autor.

🧮 Lógica de creación
La contraseña se crea siguiendo esta estructura:

1.Un carácter especial inicial.
2.Una palabra ingresada por el usuario, con la primera letra en mayúscula.
3.Una cadena de números aleatorios para cumplir con la longitud total requerida.
4.El mismo carácter especial al final.

Ejemplo: #Python123#

💾 Guardado
Si la contraseña es válida, se guarda en un archivo llamado contraseña.txt. Si no se genera correctamente (por ejemplo, si la longitud es insuficiente), se guarda como NULL.

👤 Autor
Proyecto desarrollado por el Ing. D. Fernando Huertas M. Contacto y sugerencias: difhuertasm@gmail.com
