# Proyecto de Simulacion

## Logica Difusa

## Marcos Antonio Maceo Reyes, Grupo 2

## Principales ideas seguidas para la implementacion del Sistema

Para la implementacion del sistema difusa nos basamos en varias clases y archivos organizados de forma tal que se 
agruparan las funcionalidades de nuestro sistema de inferencia difusa. 

Se definieron los operadores `Max`, `Min`, `Or` y `And` ademas para la inferencia de cada regla se implementaron los 
metodos `Mamdani` y `Larsen`.

Se definieron las siguientes clases para la solucion del sistema de inferencia difuso:

- `LinguisticVar`: Defines las variables linguisticas.
- `Rule`: Define las reglas planteadas como guias del problema. Esta compuesta por un Antecedente y un Precedente.
- `Antecedent`: Define la parte izquierda de la implicacion de las reglas definidas anteriormente.
- `Consequence`: Representa la parte derecha de la implicacion de las reglas defindas.
- `FuzzySet`: Representa un conjunto difuso.

Se implemento ademas una clase `FuzzyInferenceSystem` que representa el sistema de inferencia difusa. Este implementa 
como se dijo anteriormente `Mamdani` y `Larsen`, ademas de los metodos de desdifusificacion `Centroide`, `Biseccion` y 
`Media de Maximos`.

## Propuesta del Problema

Las emisiones nocivas que provienen de los vehículos representan una de las principales
fuentes de contaminación. El exceso de agentes contaminantes en la atmósfera es uno de los
mayores problemas a los que nos enfrentamos en la actualidad. En este trabajo se estudia
como representar el comportamiento de varios conductores de acuerdo a los estilos de
conducción (ecológica, normal, agresiva) mediante lógica difusa,
para evaluar la eficiencia energética en un vehículo.

## Variables y funciones de inferencia del problema propuesto

`Aceleracion` La aceleracion se clasifica en positiva y negativa.
`Consumo` El consumo de combustible se clasifica en alto y bajo.
`Eficiencia` Esta se clasifica en Alta o Baja.

Todas las variables antes linguisticas antes descritas se representan mediante un conjunto 
difuso. Las funciones de pertenencia usadas son triangulares  tiene como objetivo brindar un 
enfoque lo mas simplificado posible del problema. 

## Reglas del problema

Las reglas definidas sobre el problema para aplicar posteriormente los algoritmos de logica difusa
son las siguientes, basadas en las variables definidas anteriormente:

1. Si el consumo es bajo => la eficiencia es alta
2. Si el consumo es alta => la eficiencia es baja
3. Si la aceleracion es negativa y el consumo es bajo => eficiencia alta
4. Si la aceleracion es positiva y el consumo es alto => eficiencia baja


## Consideraciones obtenidas

Para validar las implementacion y la respectiva solucion aplicando los algoritmos de logica difusa, se realizaron 
varios ejemplos, donde se puede observar un nivel de aceptacion aceptable. 

Basandonos en las variables definidas, tomamos como ejemplos conductores que fueran estilos de conduccion ecologicas, es
decir que mantiviera bajos niveles de aceleracion y consumo de combustible. Efectivamente el modelo nos brindo una 
solucion que cumplia con ser un condutor eficiente.

Aproximadamente lo mismo paso con otros ejemplos que usamos, exceptuando las condiciones fronteras, que era dificil 
definir cuando un conductor era ecologico o agresivo.
