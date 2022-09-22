from ctypes.wintypes import INT

""" 1) Solicitar el nombre de los 4 equipos """
""" inscripcion de equipos """

team1 = input('equipo #1: ')
team2 = input('equipo #2: ')
team3 = input('equipo #3: ')
team4 = input('equipo #4: ')

""" se preparan las variables apra guardar los resultados """
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

puntos_team1 = 0
puntos_team2 = 0
puntos_team3 = 0
puntos_team4 = 0
 
puntajes = [
    puntos_team1,
    puntos_team2,
    puntos_team3,
    puntos_team4
]
""" se crea el diccionario donde viviran los resultados del campeonato """
grupo = {
    team1: [
        team1,
        pg1,
        pe1,
        pp1,
        gf1,
        gc1
    ],
    team2: [
        team2,
        pg2,
        pe2,
        pp2,
        gf2,
        gc2
    ],
    team3: [
        team3,
        pg3,
        pe3,
        pp3,
        gf3,
        gc3
    ],
    team4: [
        team4,
        pg4,
        pe4,
        pp4,
        gf4,
        gc4
    ]
}
""" Funcion que agrega los resultados de los partidos """
def resultados_partidos(equipo1, goles_equipo1, equipo2, goles_equipo2):
    """ eleccion de resultados de los partidos """
    if goles_equipo1 > goles_equipo2:
        grupo[equipo1][1] += 1
        grupo[equipo2][2] += 1
        grupo[equipo1][3] += goles_equipo1
        grupo[equipo1][5] -= goles_equipo2
        grupo[equipo2][4] += goles_equipo2
        grupo[equipo2][5] -= goles_equipo1
    if goles_equipo1 < goles_equipo2:
        grupo[equipo2][1] += 1
        grupo[equipo1][3] += 1
        grupo[equipo1][4] += goles_equipo1
        grupo[equipo1][5] -= goles_equipo2
        grupo[equipo2][4] += goles_equipo2
        grupo[equipo2][5] -= goles_equipo1
    if goles_equipo1 == goles_equipo2:
        grupo[equipo2][2] += 1
        grupo[equipo1][2] += 1
        grupo[equipo1][4] += goles_equipo1
        grupo[equipo1][5] -= goles_equipo2
        grupo[equipo2][4] += goles_equipo2
        grupo[equipo2][5] -= goles_equipo1

""" funcion para imprimir """
def imprimit_tabla(e, pj, pg, pp, pe, gf, gc, p):
    """ print('Equipo           |', 'Partidos jugados |', 'Partidos ganados |', 'Partidos perdidos |', 'Partidos empatados |', 'Goles a Favor |', 'Goles en Contra |', 'Puntos |') """
    print(e,'            ', pj,'                    ', pg,'               ', pp,'                  ', pe,'               ', gf,'            ', gc,'           ', p, '   ')

""" Funcion calculo de puntos """
def puntaje(equipo, ppg, ppe, ppp):
    pg = ppg*3
    pe = ppe*1
    pp = ppp*0
    PF = ppg + ppe + ppp
    if(equipo == grupo[team1]):
        puntajes[0] += PF
    if(equipo == grupo[team2]):
        puntajes[1] += PF
    if(equipo == grupo[team3]):
        puntajes[2] += PF
    if(equipo == grupo[team4]):
        puntajes[3] += PF


""" 2) Preguntar el resultado de cada partido. El formato será todos contra todos.
a. Cuando pregunte cada partido deberá al inicio la fecha que se esta 
jugando. Serian en total 3 fechas, dos partidos por fecha, seis partidos 
en total. """
""" procesamos los resultadosde la primera fecha """
partido1 = 1
ra_fecha = 'ra fecha'
da_fecha = 'da fecha'
print(partido1, ra_fecha)
partido1_fecha1 = team1 + ' vs ' + team2
partido2_fecha1 = team3 + ' vs ' + team4

fecha1team1_goles = input('¿cuantos goles hizo el equipo ' + team1 + ' en el partido ' + partido1_fecha1 + '? ')
fecha1team2_goles = input('¿cuantos goles hizo el equipo ' + team2 + ' en el partido ' + partido1_fecha1 + '? ')
fecha1team3_goles = input('¿cuantos goles hizo el equipo ' + team3 + ' en el partido ' + partido2_fecha1 + '? ')
fecha1team4_goles = input('¿cuantos goles hizo el equipo ' + team4 + ' en el partido ' + partido2_fecha1+ '? ')

""" print('resultado partido #1: ' + team1 + ' ' + fecha1team1_goles + ' - ' + fecha1team2_goles + ' ' + team2)
print('resultado pratido #2: ' + team3 + ' ' + fecha1team3_goles + ' - ' + fecha1team4_goles + ' ' + team4) """

fecha1team1_goles_int = int(fecha1team1_goles)
fecha1team2_goles_int = int(fecha1team2_goles)
fecha1team3_goles_int = int(fecha1team3_goles)
fecha1team4_goles_int = int(fecha1team4_goles)

resultados_partidos(team1, fecha1team1_goles_int, team2, fecha1team2_goles_int)
resultados_partidos(team3, fecha1team3_goles_int, team4, fecha1team4_goles_int)
""" print('Equipo ', 'Partidos jugados', 'Partidos ganados', 'Partidos perdidos', 'Partidos empatados', 'Goles a Favor', 'Goles en Contra', 'Puntos')
print(grupo[team1][0], ' ', partido1,'', grupo[team1][1],'', grupo[team1][2],'', grupo[team1][3],'', grupo[team1][4],'', grupo[team1][5],'', grupo[team1][0])
 """
puntaje(grupo[team1][0], grupo[team1][1], grupo[team1][2], grupo[team1][3])
puntaje(grupo[team2][0], grupo[team2][1], grupo[team2][2], grupo[team2][3])
puntaje(grupo[team3][0], grupo[team3][1], grupo[team3][2], grupo[team3][3])
puntaje(grupo[team4][0], grupo[team4][1], grupo[team4][2], grupo[team4][3])
print('Equipo          |', 'Partidos jugados |', 'Partidos ganados |', 'Partidos empatados |', 'Partidos perdidos  |', 'Goles a Favor |', 'Goles en Contra |', 'Puntos  ')
imprimit_tabla(grupo[team1][0], partido1, grupo[team1][1], grupo[team1][2], grupo[team1][3], grupo[team1][4], grupo[team1][5], puntajes[0])
imprimit_tabla(grupo[team2][0], partido1, grupo[team2][1], grupo[team2][2], grupo[team2][3], grupo[team2][4], grupo[team2][5], puntajes[1])
imprimit_tabla(grupo[team3][0], partido1, grupo[team3][1], grupo[team3][2], grupo[team3][3], grupo[team3][4], grupo[team3][5], puntajes[2])
imprimit_tabla(grupo[team4][0], partido1, grupo[team4][1], grupo[team4][2], grupo[team4][3], grupo[team4][4], grupo[team4][5], puntajes[3])

""" ingresamos resultados de la segunda fecha """
partido2 = 2
print(partido2, da_fecha)
partido1_fecha2 = team1 + ' vs ' + team3
partido2_fecha2 = team2 + ' vs ' + team4

fecha2team1_goles = input('¿cuantos goles hizo el equipo ' + team1 + ' en el partido ' + partido1_fecha2 + '? ')
fecha2team2_goles = input('¿cuantos goles hizo el equipo ' + team3 + ' en el partido ' + partido1_fecha2 + '? ')
fecha2team3_goles = input('¿cuantos goles hizo el equipo ' + team2 + ' en el partido ' + partido2_fecha2 + '? ')
fecha2team4_goles = input('¿cuantos goles hizo el equipo ' + team4 + ' en el partido ' + partido2_fecha2 + '? ')

""" print('resultado partido #1: ' + team1 + ' ' + fecha2team1_goles + ' - ' + fecha2team2_goles + ' ' + team3)
print('resultado pratido #2: ' + team2 + ' ' + fecha2team3_goles + ' - ' + fecha2team4_goles + ' ' + team4) """

fecha2team1_goles_int = int(fecha2team1_goles)
fecha2team2_goles_int = int(fecha2team2_goles)
fecha2team3_goles_int = int(fecha2team3_goles)
fecha2team4_goles_int = int(fecha2team4_goles)

resultados_partidos(team1, fecha2team1_goles_int, team3, fecha2team3_goles_int)
resultados_partidos(team2, fecha2team2_goles_int, team4, fecha2team4_goles_int)

puntaje(grupo[team1][0], grupo[team1][1], grupo[team1][2], grupo[team1][3])
puntaje(grupo[team2][0], grupo[team2][1], grupo[team2][2], grupo[team2][3])
puntaje(grupo[team3][0], grupo[team3][1], grupo[team3][2], grupo[team3][3])
puntaje(grupo[team4][0], grupo[team4][1], grupo[team4][2], grupo[team4][3])
print('Equipo          |', 'Partidos jugados |', 'Partidos ganados |', 'Partidos empatados |', 'Partidos perdidos  |', 'Goles a Favor |', 'Goles en Contra |', 'Puntos  ')
imprimit_tabla(grupo[team1][0], partido1, grupo[team1][1], grupo[team1][2], grupo[team1][3], grupo[team1][4], grupo[team1][5], puntajes[0])
imprimit_tabla(grupo[team2][0], partido1, grupo[team2][1], grupo[team2][2], grupo[team2][3], grupo[team2][4], grupo[team2][5], puntajes[1])
imprimit_tabla(grupo[team3][0], partido1, grupo[team3][1], grupo[team3][2], grupo[team3][3], grupo[team3][4], grupo[team3][5], puntajes[2])
imprimit_tabla(grupo[team4][0], partido1, grupo[team4][1], grupo[team4][2], grupo[team4][3], grupo[team4][4], grupo[team4][5], puntajes[3])

""" ingresamos resultados de la tercera fecha """
partido3 = 3
print(partido3, ra_fecha)
partido1_fecha3 = team1 + ' vs ' + team4
partido2_fecha3 = team2 + ' vs ' + team3

fecha3team1_goles = input('¿cuantos goles hizo el equipo ' + team1 + ' en el partido ' + partido1_fecha3 + '? ')
fecha3team2_goles = input('¿cuantos goles hizo el equipo ' + team4 + ' en el partido ' + partido1_fecha3 + '? ')
fecha3team3_goles = input('¿cuantos goles hizo el equipo ' + team2 + ' en el partido ' + partido2_fecha3 + '? ')
fecha3team4_goles = input('¿cuantos goles hizo el equipo ' + team3 + ' en el partido ' + partido2_fecha3 + '? ')

""" print('resultado partido #1: ' + team1 + ' ' + fecha3team1_goles + ' - ' + fecha3team2_goles + ' ' + team4)
print('resultado pratido #2: ' + team2 + ' ' + fecha3team3_goles + ' - ' + fecha3team4_goles + ' ' + team3) """

fecha3team1_goles_int = int(fecha3team1_goles)
fecha3team2_goles_int = int(fecha3team2_goles)
fecha3team3_goles_int = int(fecha3team3_goles)
fecha3team4_goles_int = int(fecha3team4_goles)

resultados_partidos(team1, fecha3team1_goles_int, team4, fecha3team4_goles_int)
resultados_partidos(team2, fecha3team2_goles_int, team3, fecha3team3_goles_int)

puntaje(grupo[team1][0], grupo[team1][1], grupo[team1][2], grupo[team1][3])
puntaje(grupo[team2][0], grupo[team2][1], grupo[team2][2], grupo[team2][3])
puntaje(grupo[team3][0], grupo[team3][1], grupo[team3][2], grupo[team3][3])
puntaje(grupo[team4][0], grupo[team4][1], grupo[team4][2], grupo[team4][3])
print('Equipo          |', 'Partidos jugados |', 'Partidos ganados |', 'Partidos empatados |', 'Partidos perdidos  |', 'Goles a Favor |', 'Goles en Contra |', 'Puntos  ')
imprimit_tabla(grupo[team1][0], partido1, grupo[team1][1], grupo[team1][2], grupo[team1][3], grupo[team1][4], grupo[team1][5], puntajes[0])
imprimit_tabla(grupo[team2][0], partido1, grupo[team2][1], grupo[team2][2], grupo[team2][3], grupo[team2][4], grupo[team2][5], puntajes[1])
imprimit_tabla(grupo[team3][0], partido1, grupo[team3][1], grupo[team3][2], grupo[team3][3], grupo[team3][4], grupo[team3][5], puntajes[2])
imprimit_tabla(grupo[team4][0], partido1, grupo[team4][1], grupo[team4][2], grupo[team4][3], grupo[team4][4], grupo[team4][5], puntajes[3])
