# Informe os segundos e converta em dias horas minutos e segundos

totalDesegundos = int(input('Por favor, entre com o número de segundos que deseja converter: '))

dias = totalDesegundos//86400
segundosRestantesAposDias = totalDesegundos%86400
horas = segundosRestantesAposDias//3600
segundosRestantesAposHoras = totalDesegundos %3600
minutos = segundosRestantesAposHoras//60
segundosRestantesAposMinutos = totalDesegundos%60


print(dias,'dias,',horas,'horas,',minutos,'minutos e',segundosRestantesAposMinutos,'segundos.')



