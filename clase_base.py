# Integrantes:
# - Collaguari Israel
# - Macias Brithany
# - Suarez Yanina

#clase principal para realizar tramites
class Tramite:

# Contador de clase (compartido entre todas las instancias)
    _contador = 0

    def __init__(self, descripcion, costo_base, prefijo="TRM"):
        # Generar código automático
        Tramite._contador += 1
        codigo_auto = f"{prefijo}{Tramite._contador:04d}"  # TRM0001, TRM0002, etc.

        self.codigo = codigo_auto
        self.descripcion = descripcion
        self.costo_base = costo_base

    # ---- Encapsulamiento ----
    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        try:
            if not valor:
                raise ValueError("El código no puede estar vacío.")
            self._codigo = valor

        except ValueError:
            raise
        except Exception as e:
            raise ValueError(f"Error al procesar el código: {str(e)}")

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, valor):
        try:
            if not valor:
                raise ValueError("La descripción no puede estar vacía.")
            self._descripcion = valor

        except ValueError:
            raise
        except Exception as e:
            raise ValueError(f"Error al procesar la descripción: {str(e)}")

    @property
    def costo_base(self):
        return self._costo_base

    @costo_base.setter
    def costo_base(self, valor):
        try:
            # Validar que sea numérico
            if not isinstance(valor, (int, float)):
                raise ValueError("El costo base debe ser un número.")

            # Validar que no sea negativo
            if valor < 0:
                raise ValueError("El costo base no puede ser negativo.")

            self._costo_base = valor

        except ValueError:
            raise
        except Exception as e:
            raise ValueError(f"Error al procesar el costo base: {str(e)}")

    # ---- Métodos a sobrescribir (polimórficos) ----
    def calcular_costo(self):
        return self.costo_base

    def __str__(self):
        return f"Trámite {self.codigo}: {self.descripcion} - Costo base: ${self.costo_base}"


