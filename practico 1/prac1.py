
#duraciones promedio de otros cursos

otros_cursos_min = 2.5
otros_cursos_max= 7
otros_cursos_promedio=4
curso_actual=1.5

#1. diferenecias entre cursos porcentual

diferencia_con_min = 100 - curso_actual / otros_cursos_min * 100 
diferencia_con_max = 100 - curso_actual / otros_cursos_max * 100 
diferencia_con_promedio = 100 - curso_actual / otros_cursos_promedio * 100 

print(f"La diferencia del curso actual con el minimo es de {diferencia_con_min}%\n"
      f"La diferencia del curso actual con el maximo es de {round(diferencia_con_max,1)}%\n"
      f"La diferencia del curso actual con el promedio es de {diferencia_con_promedio}%\n")

#2. duracion de crudo

crudo_promedio = 5
crudo_actual = 3.5

diferencia_crudos = 100 - otros_cursos_promedio / crudo_promedio * 100
diferencia_crudos_actual = 100 - curso_actual / crudo_actual * 100

print(f"La diferencia de tiempos con el curso promedio es de un {diferencia_crudos}%\n"
      f"La diferencia de tiempos con el curso actual es de un {round(diferencia_crudos_actual,1)}%\n")

#3. diferencias de ver 10 horas con el curso actual

print(f"ver 10 horas del curso actual corresponde a ver {round(otros_cursos_promedio / crudo_actual * 10,1)} horas de otros cursos en promedio")

