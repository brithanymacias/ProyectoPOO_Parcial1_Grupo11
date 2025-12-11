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

# 🔗🎥 Link del video

https://drive.google.com/file/d/1vaXwRA9qF4wJEwNTK-bnRa2UEoPHBKFT/view?usp=sharing

---

# 📊 Diagrama UML
          
![WhatsApp Image 2025-12-09 at 21 02 22](https://github.com/user-attachments/assets/4d2f7142-34c4-43a1-88b2-0cced2fa96d1)

---

# 📸 Capturas de la ejecución

[Capturas POO - Grupo 11.pdf](https://github.com/user-attachments/files/24084610/Capturas.POO.-.Grupo.11.pdf)


![WhatsApp Image 2025-12-09 at 20 23 32](https://github.com/user-attachments/assets/ee4b9f90-5f87-4871-a7b2-a92b379098b0)
![WhatsApp Image 2025-12-09 at 20 24 11](https://github.com/user-attachments/assets/2d15f34d-e043-4b48-a01d-a863f6d98595)
![WhatsApp Image 2025-12-09 at 20 24 26](https://github.com/user-attachments/assets/0f560eaa-a122-4c62-a008-cc6d67cd0dc3)
![WhatsApp Image 2025-12-09 at 20 24 46](https://github.com/user-attachments/assets/2b7622c8-cf1c-4af8-ac44-700ec4e3fcd9)
![WhatsApp Image 2025-12-09 at 20 25 07](https://github.com/user-attachments/assets/9aab6787-b51e-4eaa-ab20-a5a74963fa7b)


---



