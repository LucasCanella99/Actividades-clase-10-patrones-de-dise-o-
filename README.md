# Actividades-clase-10-patrones-de-diseño-
Alumno: Lucas Daniel Canella
Comisión: 4

Ejercicio 1 — Críticas a los patrones de diseño(o desventajas)
1. Complejidad innecesaria
El problema más común es aplicar un patrón donde no hace falta. Si tenés una función que hace una sola cosa y nunca va a crecer, meterle Observer, Factory o cualquier otro patrón solo agrega clases y capas de abstracción que nadie va a entender seis meses después. El código termina siendo más difícil de leer que el problema original.
2. El Singleton arruina los tests
Es la crítica más documentada. Como hay una sola instancia global que persiste durante toda la ejecución, los tests se contaminan entre sí — lo que guarda un test lo ve el siguiente. Esto hace que los tests dependan del orden en que se ejecutan, que es exactamente lo que nunca debería pasar.
3. Patrones como fin en sí mismos
Algunos programadores los aplican "porque sí" para demostrar que los conocen, no porque resuelvan un problema real. Esto se llama over-engineering. El resultado es código que nadie entiende y que es más difícil de mantener que una solución simple.
4. Son dependientes del lenguaje
Muchos patrones nacieron para compensar limitaciones de Java y C++. En Python varios son innecesarios porque el lenguaje ya los tiene incorporados. El Iterator por ejemplo en Java requiere una clase entera, en Python es un for sobre cualquier lista.

Ejercicio 3 — Problemas de la vida diaria con patrones de diseño
1. Grupo de WhatsApp (Observer)
Cuando alguien manda un mensaje, todos los integrantes del grupo reciben la notificación. El grupo no sabe nada de cada persona, solo que estan "dentro de el" Si alguien sale del grupo, deja de recibir mensajes. Exactamente el mismo mecanismo que el Observer con inscribir y desinscribir(en mi ejemplo de codigo).
2. Adaptador de enchufes  (Adapter)
Cuando usas enchufes de 3 patitas, fase, neutro y tierra. Y en la pared hay para los de dos patas redondas. Compras un adaptador de tres patas a dos patas redondas
3. Pedido de comida personalizado (Builder)
Cuando pedis un kilo de helado vos elegis 3-4-5 sabores y listo. No tenes que ver una planilla de 15 opciones y poner si o no en cada uno de los sabores. Direcamente pedis lo que queres y necesitas. 

Ejercicio 4 — Tabla de nombres alternativos
| Observer | Publisher-Subscriber, Event Listener, Watcher |
| Adapter | Wrapper, Translator |
| Decorator | Wrapper, Enhanced Object |
| Factory Method | Virtual Constructor |
| Singleton | Instance Controller |
| Strategy | Policy, Algorithm Family |
| Prototype | Clone, Copy |
| Facade | Gateway, Simplifier |

Ejercicio 5 — Antipatrones de diseño
Son exactamente lo opuesto a los patrones: soluciones que parecen razonables pero que a largo plazo generan más problemas de los que resuelven.
*God Object* — una sola clase que hace absolutamente todo. En vez de tener Usuario, Carrito, Pago separados, tenés una clase Sistema con 50 métodos.
*Spaghetti Code* — código sin estructura donde todo llama a todo sin orden. 
*Copy-Paste Programming* — en vez de crear una función reutilizable, el mismo bloque de código aparece copiado en 10 lugares distintos. Cuando hay que corregir un bug, hay que corregirlo en los 10 lugares.
*Magic Numbers* — usar números literales en el código sin explicación.