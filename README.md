# Sistema Municipal de Gestión de Trámites  
### Proyecto POO – Primer Parcial  
### Grupo 11: Gestión de Servicios de Municipio / Trámites  

## 👥 Integrantes
- Collaguari Israel  
- Macias Brithany  
- Suarez Yanina  

---

# 📌 Descripción del Proyecto

Este proyecto implementa un **Sistema Municipal de Gestión de Trámites**, aplicando conceptos de **Programación Orientada a Objetos (POO)**:

- Encapsulamiento  
- Herencia  
- Polimorfismo  
- Validaciones  
- Uso de listas polimórficas  
- Buenas prácticas PEP8  

El sistema permite gestionar trámites comunes realizados en un municipio, como:

- Emisión de cédula (primera vez o renovación)  
- Permisos de funcionamiento para negocios  

El usuario puede registrar ciudadanos, generar trámites, obtener reportes y calcular totales.

---

# 🏗 Estructura del Sistema

El proyecto está compuesto por **5 clases mínimo**, cumpliendo los requisitos del parcial.

## **1️⃣ Superclase**
### `Tramite`
Contiene atributos comunes:
- descripción
- costo base  

Métodos:
- `calcular_costo()` (polimórfico)
- `__str__()`  
Además, aplica **encapsulamiento** usando `@property` y validaciones.

---

## **2️⃣ Subclases (Herencia)**

### `TramiteCedula`  
Hereda de `Tramite`.  
Atributos extra:
- `es_renovacion` (booleano)

Reglas:
- Si es renovación → 20% de descuento  

Sobrescribe:
- `calcular_costo()` (polimorfismo)

---

### `PermisoFuncionamiento`  
Hereda de `Tramite`.  
Atributos extra:
- `tipo_negocio` (comercial, industrial, otro)

Reglas:
- Comercial → +$50  
- Industrial → +$100  
- Otro → sin recargo  

Sobrescribe:
- `calcular_costo()` (polimorfismo)

---

## **3️⃣ Clases Extra**

### `Ciudadano`
Representa a un ciudadano con:
- nombre
- cédula  

### `GestorTramites`
Contiene métodos **polimórficos obligatorios**:

- `calcular_totales(lista_tramites)`  
- `generar_reporte(lista_tramites)`  

Ambos reciben una **lista polimórfica** con objetos de diferentes tipos de trámites.

---

# ▶ Ejecución del Programa

El archivo **main.py** contiene un menú interactivo:

1. Registrar ciudadano
2. Crear trámite de cédula
3. Crear permiso de funcionamiento
4. Calcular costo total
5. Generar reporte
6. Mostrar ciudadanos registrados
7. Salir

El usuario puede registrar ciudadanos, generar distintos trámites y ver reportes detallados.

---

# 🟢 Instrucciones para Ejecutar

1. Clonar o descargar el repositorio.  
2. Abrir la carpeta en PyCharm / VSCode.  
3. Ejecutar:
4. Usar el menú interactivo.

---

# ✔ Conclusión

Este proyecto demuestra correctamente:

- Encapsulamiento  
- Herencia  
- Polimorfismo  
- Uso de clases bien estructuradas  
- Menú interactivo completo  
- Validaciones  
- Buenas prácticas PEP8  

El sistema cumple con **todos los requisitos del Primer Parcial**.



---

# ✔ Conclusión

Este proyecto demuestra correctamente:

- Encapsulamiento  
- Herencia  
- Polimorfismo  
- Uso de clases bien estructuradas  
- Menú interactivo completo  
- Validaciones  
- Buenas prácticas PEP8  

El sistema cumple con **todos los requisitos del Primer Parcial**.

---

# 🔗🎥 Link del video

 

---

# 📊 Diagrama UML
          
![WhatsApp Image 2025-12-09 at 21 02 22](https://github.com/user-attachments/assets/4d2f7142-34c4-43a1-88b2-0cced2fa96d1)

---

# 📸 Capturas de la ejecución

![WhatsApp Image 2025-12-09 at 20 23 32](https://github.com/user-attachments/assets/ba70feb3-0713-480e-8e58-39afa36bd6ab)
![WhatsApp Image 2025-12-09 at 20 24 11](https://github.com/user-attachments/assets/be06fb8b-218d-4756-91e9-f818394e98f5)
![WhatsApp Image 2025-12-09 at 20 24 26](https://github.com/user-attachments/assets/d034a7f2-a712-40b0-9f17-e4b5837e357e)
![WhatsApp Image 2025-12-09 at 20 24 46](https://github.com/user-attachments/assets/31cc4df2-64f3-4bce-a649-a8b1cfc2c088)
![WhatsApp Image 2025-12-09 at 20 25 07](https://github.com/user-attachments/assets/5bb7e96d-ede3-4768-a71f-29b1626ce69f)

---



