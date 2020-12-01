# Proyecto de Simulación

## Lógica Difusa

## Marcos Antonio Maceo Reyes, Grupo 2

## Principales ideas seguidas para la implementación del sistema 

Para la implementación del sistema difusa nos basamos en varias clases y archivos organizados de forma tal que se 
agruparan las funcionalidades de nuestro sistema de inferencia difusa. 

Se definieron los operadores `Max`, `Min`, `Or` y `And` además para la inferencia de cada regla se implementaron los 
metodos `Mamdani` y `Larsen`.

Se definieron las siguientes clases para la solucion del sistema de inferencia difuso:

- `LinguisticVar`: Defines las variables lingüísticas.
- `Rule`: Define las reglas planteadas como guías del problema. Esta compuesta por un Antecedente y un Precedente.
- `Antecedent`: Define la parte izquierda de la implicación de las reglas definidas anteriormente.
- `Consequence`: Representa la parte derecha de la implicación de las reglas defindas.
- `FuzzySet`: Representa un conjunto difuso.

Se implemento además una clase `FuzzyInferenceSystem` que representa el sistema de inferencia difusa. Este implementa 
como se dijo anteriormente `Mamdani` y `Larsen`, además de los métodos de desdifusificación `Centroide`, `Bisección` y 
`Media de Máximos`.

## Propuesta del Problema

Las emisiones nocivas que provienen de los vehículos representan una de las principales fuentes de contaminación. El 
exceso de agentes contaminantes en la atmósfera es uno de los mayores problemas a los que nos enfrentamos en la 
actualidad. En este trabajo se estudia como representar el comportamiento de varios conductores de acuerdo a los 
estilos de conducción (ecológica, agresiva) mediante lógica difusa, para evaluar la eficiencia energética en un vehículo.

## Variables y funciones de inferencia del problema propuesto

`Aceleración` La aceleración se clasifica en positiva y negativa.
`Consumo` El consumo de combustible se clasifica en alto y bajo.
`Eficiencia` Esta se clasifica en alta o baja.

Todas las variables linguisticas antes descritas se representan mediante un conjunto difuso. Las funciones de 
pertenencia usadas son triangulares, las cuales tienen como objetivo brindar un enfoque lo mas simplificado posible del 
problema. 

## Reglas del problema

Las reglas definidas a continuación represetan al problema,las cuales seran utilizadas posteriormente en algoritmos 
de logica difusa, estas se encuentran definidas en base a las basadas en las variables definidas anteriormente:

1. Si el consumo es bajo => la eficiencia es alta
2. Si el consumo es alta => la eficiencia es baja
3. Si la aceleración es negativa y el consumo es bajo => eficiencia alta
4. Si la aceleración es positiva y el consumo es alto => eficiencia baja


## Consideraciones obtenidas

Para validar las implementación y la respectiva solución aplicando los algoritmos de lógica difusa, se realizaron 
varios ejemplos, donde se puede observar un nivel de aceptación aceptable. 

Basándonos en las variables definidas, tomamos como ejemplos conductores que tienen estilos de conducción ecológicas, es
decir que mantuviera bajos niveles de aceleracion y consumo de combustible. Efectivamente el modelo nos brindo una 
solución que cumplía con ser un condutor eficiente.

Aproximadamente lo mismo paso con otros ejemplos que utilizamos, exceptuando las condiciones fronteras, que era díficil 
definir cuando un conductor era ecológico o agresivo.
