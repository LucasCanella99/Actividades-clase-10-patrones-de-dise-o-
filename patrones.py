# Patron creacional prototype

import copy # Importe copy para que haga referencias y copie obviante al objeto original

class Auto:
    def __init__(self, marca, motor, color, techo_descapotable, asientos):
        self.marca = marca
        self.motor = motor
        self.color = color
        self.techo_descapotable = techo_descapotable
        self.asientos = asientos

    def __str__(self):
        return (f"{self.marca} | Motor: {self.motor} | Color: {self.color} "
                f"| Techo descapotable: {self.techo_descapotable} | Asientos: {self.asientos}")


# Auto base de fábrica
auto_base = Auto("Toyota Corolla", "1.8 naftero", "blanco", False, 5)

# Caso de uso, quiere el mismo auto pero rojo y con techo descapotable
auto_rojo = copy.copy(auto_base)
auto_rojo.color = "rojo"
auto_rojo.techo_descapotable = True

# Otro caso de uso, quiere el mismo pero negro y 7 asientos
auto_negro = copy.copy(auto_base)
auto_negro.color = "negro"
auto_negro.asientos = 7

print(auto_base)   # Toyota Corolla | Motor: 1.8 naftero | Color: blanco | Techo descapotable: False | Asientos: 5
print(auto_rojo)   # Toyota Corolla | Motor: 1.8 naftero | Color: rojo   | Techo descapotable: True  | Asientos: 5
print(auto_negro)  # Toyota Corolla | Motor: 1.8 naftero | Color: negro  | Techo descapotable: False | Asientos: 7

# El patron de prototype estaria en la parte que se usa el copy ya que copia el "prototipo" auto base con sus atributos y hacer referencia a ese y despues se lo modifica.

#Patron cracional adapter

import json

class SistemaViejo:
    def obtener_datos_xml(self):
        return "<datos>ventas</datos>"

class SistemaNuevo:
    def procesar(self, datos_json):
        print(f"Procesando JSON: {datos_json}")

class Adapter:
    def __init__(self, sistema_viejo):
        self.sistema_viejo = sistema_viejo

    def obtener_datos_json(self):
        xml = self.sistema_viejo.obtener_datos_xml()
        return json.dumps({"datos": "ventas"})  # traduce XML → JSON aca estaria el patron adapter

# Uso
adaptado = Adapter(SistemaViejo())
SistemaNuevo().procesar(adaptado.obtener_datos_json())

# La adaptacion es algo similar a lo que ocurre en django rest framework cuando se serializa del modelo de la db en python a json y cuando viene una peticion y se "deserializa" de json a python para poder ejecutar la vistas, hacer el modelo guardar que el orm traduzca nuevamente a sql y lo guarde en la db etc..

# Patron de comportamiento observer

# El problema que resuelve:
# Cuando una materia cambia de horario, todos los alumnos inscriptos
# tienen que enterarse. Sin Observer, la materia tendría que conocer
# a cada alumno — un desastre si hay 200.

class Materia:
    def __init__(self, nombre):
        self.nombre = nombre
        self.horario = None
        self._alumnos = []  # Lista donde estan los alumnos 

    def inscribir(self, alumno):
        self._alumnos.append(alumno)

    def desinscribir(self, alumno):
        self._alumnos.remove(alumno)

    def cambiar_horario(self, nuevo_horario):
        self.horario = nuevo_horario
        print(f"\n[{self.nombre}] Horario cambiado a: {nuevo_horario}")
        for alumno in self._alumnos:
            alumno.notificar(self.nombre, nuevo_horario)


class Alumno:
    def __init__(self, nombre):
        self.nombre = nombre

    def notificar(self, materia, horario):
        print(f"  → {self.nombre} recibió aviso: '{materia}' ahora es a las {horario}")


# --- Uso ---
prog_avanzada = Materia("Programación Avanzada")

lucas  = Alumno("Lucas")
juan  = Alumno("Juan")
martin = Alumno("Martín")

prog_avanzada.inscribir(lucas)
prog_avanzada.inscribir(juan)
prog_avanzada.inscribir(martin)

prog_avanzada.cambiar_horario("Jueves 18hs")

# Si Martín se da de baja, deja de recibir avisos
prog_avanzada.desinscribir(martin)
prog_avanzada.cambiar_horario("Viernes 20hs")

# Aca el patron de diseño esta aplicado puntualmente en el bucle for que recorre la lista de alumnos y les avisa uno por uno (simulando) que reciben la notificacion del nuevo horario de la materia.