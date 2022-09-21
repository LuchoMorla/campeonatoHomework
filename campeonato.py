from ctypes.wintypes import INT

""" 1) Solicitar el nombre de los 4 equipos """
""" inscripcion de equipos """

team1 = input('equipo #1: ')
team2 = input('equipo #2: ')
team3 = input('equipo #3: ')
team4 = input('equipo #4: ')

""" 2) Preguntar el resultado de cada partido. El formato será todos contra todos.
a. Cuando pregunte cada partido deberá al inicio la fecha que se esta 
jugando. Serian en total 3 fechas, dos partidos por fecha, seis partidos 
en total. """
print('1ra fecha: ')
partido1_fecha1 = team1 + ' vs ' + team2
partido2_fecha1 = team3 + ' vs ' + team4

fecha1team1_goles = input('¿cuantos goles hizo el equipo ' + team1 + ' en el partido ' + partido1_fecha1 + '? ')
fecha1team2_goles = input('¿cuantos goles hizo el equipo ' + team2 + ' en el partido ' + partido1_fecha1 + '? ')
fecha1team3_goles = input('¿cuantos goles hizo el equipo ' + team3 + ' en el partido ' + partido2_fecha1 + '? ')
fecha1team4_goles = input('¿cuantos goles hizo el equipo ' + team4 + ' en el partido ' + partido2_fecha1+ '? ')

print('resultado partido #1: ' + team1 + ' ' + fecha1team1_goles + ' - ' + fecha1team2_goles + ' ' + team2)
print('resultado pratido #2: ' + team3 + ' ' + fecha1team3_goles + ' - ' + fecha1team4_goles + ' ' + team4)

fecha1team1_goles_int = int(fecha1team1_goles)
fecha1team2_goles_int = int(fecha1team2_goles)
fecha1team3_goles_int = int(fecha1team3_goles)
fecha1team4_goles_int = int(fecha1team4_goles)

""" ingresamos resultados de la segunda fecha """
print('2da fecha: ')
partido1_fecha2 = team1 + ' vs ' + team3
partido2_fecha2 = team2 + ' vs ' + team4

fecha2team1_goles = input('¿cuantos goles hizo el equipo ' + team1 + ' en el partido ' + partido1_fecha2 + '? ')
fecha2team2_goles = input('¿cuantos goles hizo el equipo ' + team3 + ' en el partido ' + partido1_fecha2 + '? ')
fecha2team3_goles = input('¿cuantos goles hizo el equipo ' + team2 + ' en el partido ' + partido2_fecha2 + '? ')
fecha2team4_goles = input('¿cuantos goles hizo el equipo ' + team4 + ' en el partido ' + partido2_fecha2 + '? ')

print('resultado partido #1: ' + team1 + ' ' + fecha2team1_goles + ' - ' + fecha2team2_goles + ' ' + team3)
print('resultado pratido #2: ' + team2 + ' ' + fecha2team3_goles + ' - ' + fecha2team4_goles + ' ' + team4)
fecha2team1_goles_int = int(fecha2team1_goles)
fecha2team2_goles_int = int(fecha2team2_goles)
fecha2team3_goles_int = int(fecha2team3_goles)
fecha2team4_goles_int = int(fecha2team4_goles)

""" ingresamos resultados de la tercera fecha """
print('3ra fecha: ')
partido1_fecha3 = team1 + ' vs ' + team4
partido2_fecha3 = team2 + ' vs ' + team3

fecha3team1_goles = input('¿cuantos goles hizo el equipo ' + team1 + ' en el partido ' + partido1_fecha3 + '? ')
fecha3team2_goles = input('¿cuantos goles hizo el equipo ' + team4 + ' en el partido ' + partido1_fecha3 + '? ')
fecha3team3_goles = input('¿cuantos goles hizo el equipo ' + team2 + ' en el partido ' + partido2_fecha3 + '? ')
fecha3team4_goles = input('¿cuantos goles hizo el equipo ' + team3 + ' en el partido ' + partido2_fecha3 + '? ')


print('resultado partido #1: ' + team1 + ' ' + fecha3team1_goles + ' - ' + fecha3team2_goles + ' ' + team4)
print('resultado pratido #2: ' + team2 + ' ' + fecha3team3_goles + ' - ' + fecha3team4_goles + ' ' + team3)

fecha2team1_goles_int = int(fecha2team1_goles)
fecha2team2_goles_int = int(fecha2team2_goles)
fecha2team3_goles_int = int(fecha2team3_goles)
fecha2team4_goles_int = int(fecha2team4_goles)

""" 3) Se deberá crear un diccionario que tenga la información de los equipos. La 
estructura de la información será la siguiente:
a. Cada elemento será un equipo
b. La llave de cada elemento será el nombre del Equipo(STR)
c. El valor de cada equipo será una lista que tendrá los siguientes 
valores:
i. Partidos Ganados (INT)
ii. Partidos Empatados (INT)
iii. Partidos Perdidos (INT)
iv. Goles a Favor(INT)
v. Goles en contra (INT) """
pg1 = 0
pe1 = 0
pp1 = 0
gf1 = 0
gc1 = 0

pe2 = 0
pp2 = 0
pg2 = 0
gf2 = 0
gc2 = 0

pg3 = 0
pe3 = 0
pp3 = 0
gf3 = 0
gc3 = 0

pg4 = 0
pe4 = 0
pp4 = 0
gf4 = 0
gc4 = 0
grupo = {
    team1: [
        pg1,
        pe1,
        pe1,
        gf1,
        gc1
    ],
    team2: [
        pg2,
        pe2,
        pe2,
        gf2,
        gc2
    ],
    team3: [
        pg3,
        pe3,
        pe3,
        gf3,
        gc3
    ],
    team4: [
        pg4,
        pe4,
        pe4,
        gf4,
        gc4
    ]
}

def resultados_partidos(equipo1, goles_equipo1, equipo2, goles_equipo2):
    """ eleccion de resultados de los partidos """
    if goles_equipo1 > goles_equipo2:
        grupo[equipo1[0]] += 1
        grupo[equipo2[2]] += 1
    if goles_equipo1 < goles_equipo2:
        grupo[equipo2[0]] += 1
        grupo[equipo1[2]] += 1
    if goles_equipo1 == goles_equipo2:
        grupo[equipo2[1]] += 1
        grupo[equipo1[1]] += 1

resultados_partidos(team1, fecha1team1_goles_int, team2, fecha1team2_goles_int)

print(grupo[team1])