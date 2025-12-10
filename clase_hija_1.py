# Integrantes:
# - Collaguari Israel
# - Macias Brithany
# - Suarez Yanina
from clase_base import Tramite

class TramiteCedula(Tramite):
    def __init__(self, descripcion, costo_base, es_renovacion):
        # Llamar al constructor padre con prefijo "CED"
        super().__init__(descripcion, costo_base, prefijo="CED")
        self.es_renovacion = es_renovacion

    @property
    def es_renovacion(self):
        return self._es_renovacion

    @es_renovacion.setter
    def es_renovacion(self, valor):
        try:
            if not isinstance(valor, bool):
                raise ValueError("es_renovacion debe ser booleano (True o False).")
            self._es_renovacion = valor

        except ValueError:
            raise
        except Exception as e:
            raise ValueError(f"Error al procesar es_renovacion: {str(e)}")

    # ---- Polimorfismo ----
    def calcular_costo(self):
        """Calcula el costo: renovación tiene 20% de descuento"""
        try:
            if self.es_renovacion:
                return self.costo_base * 0.8  # 20% descuento
            return self.costo_base  # Precio completo

        except Exception as e:
            print(f"Error al calcular costo: {e}")
            return self.costo_base

    def __str__(self):
        tipo = "Renovación" if self.es_renovacion else "Primera vez"
        return f"[Cédula] {self.codigo} - {tipo} - Total: ${self.calcular_costo()}"

