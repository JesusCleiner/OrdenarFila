TEMPERATURA = [
    [# QUITO
        [# SEMANA 1
            {"DIA": "LUNES", "TEMPERATURA": 33},
            {"DIA": "MARTES", "TEMPERATURA": 24},
            {"DIA": "MIÉRCOLES", "TEMPERATURA": 18},
            {"DIA": "JUEVES", "TEMPERATURA": 18},
            {"DIA": "VIERNES", "TEMPERATURA": 21},
            {"DIA": "SÁBADO", "TEMPERATURA": 19},
            {"DIA": "DOMINGO", "TEMPERATURA": 15}
        ],
        [# SEMANA 2
            {"DIA": "LUNES", "TEMPERATURA": 20},
            {"DIA": "MARTES", "TEMPERATURA": 22},
            {"DIA": "MIÉRCOLES", "TEMPERATURA": 19},
            {"DIA": "JUEVES", "TEMPERATURA": 17},
            {"DIA": "VIERNES", "TEMPERATURA": 16},
            {"DIA": "SÁBADO", "TEMPERATURA": 19},
            {"DIA": "DOMINGO", "TEMPERATURA": 19}
        ],
        [# SEMANA 3
            {"DIA": "LUNES", "TEMPERATURA": 19},
            {"DIA": "MARTES", "TEMPERATURA": 18},
            {"DIA": "MIÉRCOLES", "TEMPERATURA": 18},
            {"DIA": "JUEVES", "TEMPERATURA": 22},
            {"DIA": "VIERNES", "TEMPERATURA": 21},
            {"DIA": "SÁBADO", "TEMPERATURA": 21},
            {"DIA": "DOMINGO", "TEMPERATURA": 18}
        ],
        [# SEMANA 4
            {"DIA": "LUNES", "TEMPERATURA": 22},
            {"DIA": "MARTES", "TEMPERATURA": 14},
            {"DIA": "MIÉRCOLES", "TEMPERATURA": 15},
            {"DIA": "JUEVES", "TEMPERATURA": 17},
            {"DIA": "VIERNES", "TEMPERATURA": 15},
            {"DIA": "SÁBADO", "TEMPERATURA": 14},
            {"DIA": "DOMINGO", "TEMPERATURA": 16}
        ],
    ],
    [# GUAYAQUIL
        [# SEMANA 1
            {"DIA": "LUNES", "TEMPERATURA": 30},
            {"DIA": "MARTES", "TEMPERATURA": 28},
            {"DIA": "MIÉRCOLES", "TEMPERATURA": 36},
            {"DIA": "JUEVES", "TEMPERATURA": 22},
            {"DIA": "VIERNES", "TEMPERATURA": 32},
            {"DIA": "SÁBADO", "TEMPERATURA": 31},
            {"DIA": "DOMINGO", "TEMPERATURA": 34}
        ],
        [# SEMANA 2
            {"DIA": "LUNES", "TEMPERATURA": 30},
            {"DIA": "MARTES", "TEMPERATURA": 34},
            {"DIA": "MIÉRCOLES", "TEMPERATURA": 34},
            {"DIA": "JUEVES", "TEMPERATURA": 37},
            {"DIA": "VIERNES", "TEMPERATURA": 34},
            {"DIA": "SÁBADO", "TEMPERATURA": 39},
            {"DIA": "DOMINGO", "TEMPERATURA": 33}
        ],
        [# SEMANA 3
            {"DIA": "LUNES", "TEMPERATURA": 30},
            {"DIA": "MARTES", "TEMPERATURA": 28},
            {"DIA": "MIÉRCOLES", "TEMPERATURA": 36},
            {"DIA": "JUEVES", "TEMPERATURA": 22},
            {"DIA": "VIERNES", "TEMPERATURA": 32},
            {"DIA": "SÁBADO", "TEMPERATURA": 31},
            {"DIA": "DOMINGO", "TEMPERATURA": 34}
        ],
        [# SEMANA 4
            {"DIA": "LUNES", "TEMPERATURA": 30},
            {"DIA": "MARTES", "TEMPERATURA": 34},
            {"DIA": "MIÉRCOLES", "TEMPERATURA": 34},
            {"DIA": "JUEVES", "TEMPERATURA": 37},
            {"DIA": "VIERNES", "TEMPERATURA": 34},
            {"DIA": "SÁBADO", "TEMPERATURA": 39},
            {"DIA": "DOMINGO", "TEMPERATURA": 33}
        ],
    ],
    [# EL PUYO
        [# SEMANA 1
            {"DIA": "LUNES", "TEMPERATURA": 30},
            {"DIA": "MARTES", "TEMPERATURA": 28},
            {"DIA": "MIÉRCOLES", "TEMPERATURA": 36},
            {"DIA": "JUEVES", "TEMPERATURA": 22},
            {"DIA": "VIERNES", "TEMPERATURA": 32},
            {"DIA": "SÁBADO", "TEMPERATURA": 31},
            {"DIA": "DOMINGO", "TEMPERATURA": 34}
        ],
        [# SEMANA 2
            {"DIA": "LUNES", "TEMPERATURA": 30},
            {"DIA": "MARTES", "TEMPERATURA": 34},
            {"DIA": "MIÉRCOLES", "TEMPERATURA": 34},
            {"DIA": "JUEVES", "TEMPERATURA": 37},
            {"DIA": "VIERNES", "TEMPERATURA": 34},
            {"DIA": "SÁBADO", "TEMPERATURA": 39},
            {"DIA": "DOMINGO", "TEMPERATURA": 33}
        ],
        [# SEMANA 3
            {"DIA": "LUNES", "TEMPERATURA": 30},
            {"DIA": "MARTES", "TEMPERATURA": 28},
            {"DIA": "MIÉRCOLES", "TEMPERATURA": 36},
            {"DIA": "JUEVES", "TEMPERATURA": 22},
            {"DIA": "VIERNES", "TEMPERATURA": 32},
            {"DIA": "SÁBADO", "TEMPERATURA": 31},
            {"DIA": "DOMINGO", "TEMPERATURA": 34}
        ],
        [# SEMANA 4
            {"DIA": "LUNES", "TEMPERATURA": 30},
            {"DIA": "MARTES", "TEMPERATURA": 34},
            {"DIA": "MIÉRCOLES", "TEMPERATURA": 34},
            {"DIA": "JUEVES", "TEMPERATURA": 37},
            {"DIA": "VIERNES", "TEMPERATURA": 34},
            {"DIA": "SÁBADO", "TEMPERATURA": 39},
            {"DIA": "DOMINGO", "TEMPERATURA": 33}
        ],
    ],
]
LaCiudad = str()
def CalcularTemperatura(ciudad, semana):
    suma_temperatura = 0
    ciudad_seleccionada = TEMPERATURA[ciudad - 1]
    semana_seleccionada = ciudad_seleccionada[semana - 1]

    for dia in semana_seleccionada:
        suma_temperatura += dia["TEMPERATURA"]

    return suma_temperatura

# MENU DE CIUDADES
print("========================================================================")
print("************** CIUDADES **************")
print("< 1 >  QUITO")
print("< 2 >  GUAYAQUIL")
print("< 3 >  EL PUYO")
print("========================================================================")

# INGRESANDO INFORMACION REQUERIDA POR TECLADO
ciudad = int(input("SELECCIONE UNA CIUDAD: =====> "))
if ciudad == 1:
    LaCiudad = "QUITO"
if ciudad == 2:
     LaCiudad = "GUAYAQUIL"
if ciudad == 3:
     LaCiudad = "EL PUYO"
semana = int(input("INDIQUE LA SEMANA A PROMEDIAR; EL VALOR DEBE ESTAR ENTRE 1 Y 4: =====> "))

#LLAMADA A LA FUNCION Y ENTREGANDOLE 2 PARAMETROS CIUDAD Y SEMANA, PARA LOS CALCULOS SOLICITADOS
suma_total = CalcularTemperatura(ciudad, semana)

# IMPRESION DE RESULTADOS
print(f"LA SUMA DE LAS TEMPERATURAS DE LA  SEMANA {semana}, en la ciudad {LaCiudad} es: {suma_total}")

# FIN

