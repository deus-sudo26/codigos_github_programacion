reglas_recomendaciones =[
{"condiciones": [("edad",">",18),("genero","==","Terror")],
"texto": "Los juegos de terror suelen ser para mayores de 18. Juegalos con supervisión de un adulto 😖."
},
{"condiciones": [("edad","<",13),("modalidad","==","Multiplayer")],
"texto": "Activa el control parental y limita el chat con desconocidos al jugar en multijugador 🙂."
},
{"condiciones": [("experiencia","==","Amateur"),("dificultad","==","Dificil")],
"texto": "Elegiste dificultad difícil siendo amateur: empieza en medio y sube cuando domines los controles 👍."
},
{"condiciones": [("experiencia","==","Experto"),("dificultad","==","Facil")],
"texto": "Eres experto y elegiste fácil: prueba dificultad media o difícil para tener un verdadero reto 😋."
},
{"condiciones": [("preferencia_duracion_juego","==","Largo"),("dias_para_completar",">",30)],
"texto": "Considera uno corto si quieres terminarlo pronto 😫."},
{"condiciones": [("capacidad_almacenamiento_disponible", "<=", 50)],
"texto": "Revisa cuánto espacio necesita el videojuego y conserva almacenamiento libre para futuras actualizaciones 📦."
},
{"condiciones": [("capacidad_almacenamiento_disponible", ">", 50)],
"texto": "Revisa cuánto espacio necesita el videojuego y si puedes instala mínimo 2 juegos e intercala entre ellos para una mejor experiencia 📦."
},
{"condiciones": [("tiempo_disponible_al_dia", ">=", 3)],
"texto": "Haz una pausa de 10 minutos cada hora y cuida tu postura y tu vista 😒."
},
{"condiciones": [("genero", "==", "Accion")],
"texto": "En los juegos de acción, practica los reflejos y aprende los movimientos de combate para mejorar tu rendimiento ⚔️."
},
{"condiciones": [("genero", "==", "Aventura")],
"texto": "Explora los escenarios y revisa los caminos secundarios, podrías encontrar objetos y recompensas ocultas 🗺️."
},
{"condiciones": [("genero", "==", "Deportes")],
"texto": "Practica los controles y conoce las habilidades de cada jugador o equipo para mejorar tus resultados 🏆."
},
{"condiciones": [("genero", "==", "Rpg")],
"texto": "Investiga las estadísticas que más le favorecen a tu personaje y los posibles objetos ocultos."
},
{"condiciones": [("genero", "==", "Rpg"),("modalidad", "==", "Solo")],
"texto": "Es divertido jugar solo, aun así prueba jugar con amigos y mejorará la experiencia de rol."
},
{"condiciones": [("genero", "==", "Rpg"),("dificultad", "==", "Dificil")],
"texto": "Prueba juegos del mismo desarrollador que Elden Ring, suelen tener dificultades altas."
},
{"condiciones": [("presupuesto_disponible", "<", 20000)],
"texto": "Tu presupuesto es bajo: espera ofertas o busca juegos gratuitos (como Genshin Impact) 😢."
},
{"condiciones": [("presupuesto_por_hora_libre", ">", 2500),("plataforma", "==", "Xbox")],
"texto": "Con tu presupuesto te conviene una suscripción (Xbox Game Pass) para probar varios juegos sin comprarlos 😉."
},
{"condiciones": [("presupuesto_por_hora_libre", ">", 2500),("plataforma", "==", "Play station")],
"texto": "Con tu presupuesto te conviene una suscripción (PlayStation Plus) para probar varios juegos sin comprarlos 😉."
},
{"condiciones": [("capacidad_almacenamiento_disponible", "<", 25)],
"texto": "Tienes poco espacio libre: prioriza juegos livianos (de otros géneros, como Peak u Outlast) o libera espacio antes de instalar ☹️."
},
{"condiciones": [("plataforma", "==", "Movil"),("dificultad", "==", "Dificil")],
 "texto": "En móvil las experiencias de dificultad alta son más limitadas: para un reto real considera PC o consola 😉."
},
{"condiciones": [("modalidad", "==", "Multiplayer"),("cantidad_jugadores", ">=", 5)],
"texto": "Con {cantidad_jugadores} jugadores pocos juegos funcionan bien: divide al grupo en equipos o juega por turnos ☹️."
},
{"condiciones": [("experiencia", "==", "Amateur")],
"texto": "Como estás comenzando, busca juegos con tutoriales que te enseñen las mecánicas básicas 🎮."
},
{"condiciones": [("experiencia", "==", "Amateur"),("modalidad", "==", "Multiplayer")],
"texto": "Comienza jugando partidas casuales antes de participar en modos competitivos 🙂."
},
{"condiciones": [("experiencia", "==", "Amateur"),("modalidad", "==", "Multiplayer"),("cantidad_jugadores", ">=", 4)],
"texto": "Antes de comenzar, asegúrate de que todos los participantes conozcan las reglas y los controles del juego 🤝."
},
{"condiciones": [("experiencia", "==", "Experto"),("modalidad", "==", "Multiplayer")],
"texto": "Aprovecha tu experiencia para coordinar estrategias y comunicarte con tus compañeros de equipo 🎯."
},
{"condiciones": [("modalidad", "==", "Solo")],
"texto": "Si juegas en solitario, busca juegos con una buena campaña o historia para disfrutar la experiencia 😎 (por ejemplo: Outlast/Resident Evil)."
},
{"condiciones": [("genero", "==", "Terror"),("modalidad", "==", "Solo"),("experiencia", "==", "Amateur")],
"texto": "Para empezar en terror, juega con la luz de la habitación prendida o acompañado 😖."
},
{"condiciones": [("presupuesto_disponible", "<", 20000)],
"texto": "Compara precios antes de comprar y revisa las ofertas de las tiendas digitales 💰."
},
{"condiciones": [("presupuesto_disponible", ">=", 100000)],
"texto": "Aprovecha tu presupuesto para comparar ediciones especiales, pero revisa si sus contenidos adicionales realmente te interesan 💰."
},
{"condiciones": [("plataforma", "==", "Pc")],
"texto": "Comprueba los requisitos mínimos y recomendados antes de instalar el videojuego 💻."
},
{"condiciones": [("plataforma", "==", "Pc"),("capacidad_almacenamiento_disponible", "<", 50)],
        "texto": "En PC puedes revisar el tamaño de instalación y desinstalar juegos que ya no utilices para liberar espacio 💻."
},
{"condiciones": [("plataforma", "==", "Xbox")],
"texto": "Comprueba que el videojuego sea compatible con tu modelo de consola antes de comprarlo 🎮."
},
{"condiciones": [("plataforma", "==", "Play station")],
"texto": "Comprueba que el videojuego sea compatible con tu modelo de consola antes de comprarlo 🎮."
},
{"condiciones": [("tiempo_disponible_al_dia", "<", 2)],
"texto": "Como tienes poco tiempo disponible, busca juegos que permitan guardar la partida en cualquier momento ⏰."
}
]

reglas_videojuegos =[
  {"condiciones": [("edad",">=","edad_recomendada"),("modalidad","in","modalidad"),("dificultad","==","dificultad")],
   "puntos": +10},
  {"condiciones": [("modalidad","in","modalidad")],
   "puntos": +4},
  {"condiciones": [("plataforma","==","plataforma")],
   "puntos": +5,
  "segunda_regla": [("capacidad_almacenamiento_disponible",">=","almacenamiento_minimo")],
  "segundo_puntaje": +2},
  {"condiciones": [("experiencia","==","experiencia_requerida"),("dificultad","==","dificultad")],
   "puntos": +4},
  {"condiciones": [("experiencia","==","Amateur"),("dificultad","==","Dificil")],#evaluar
   "puntos": -4},
  {"condiciones": [("modalidad","not in","modalidad")],
   "puntos": -2},

 # {"condiciones": [("minutos_disponibles_al_dia","<","duracion.Minutos_recomendados")],
 #  "puntos": -1},
 # {"condiciones": [("minutos_disponibles_al_dia", ">=", "duracion.Minutos_recomendados")],
 #   "puntos": +2},

  {"condiciones": [("preferencia_duracion_juego", "in", "duracion")],
   "puntos": +3},
  {"condiciones": [("experiencia", "==", "Amateur")],
   "puntos" : 0,
   "segunda_regla": [("presupuesto_disponible", "<", "presupuesto_minimo"),("dificultad", "!=", "dificultad")],
   "segundo_puntaje": -2},
  {"condiciones": [("experiencia", "!=", "Amateur")],
   "puntos": 0,
   "segunda_regla": [("presupuesto_disponible", "<", "presupuesto_minimo"),("dificultad", "!=", "dificultad")],
   "segundo_puntaje": -1},
  {"condiciones": [("capacidad_almacenamiento_disponible", ">", "almacenamiento_minimo")],
   "puntos": +4},
  {"condiciones": [("capacidad_almacenamiento_disponible", "<=", "almacenamiento_minimo")],
   "puntos": -2}
]


        
