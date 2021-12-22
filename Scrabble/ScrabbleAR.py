import json
import PySimpleGUI as sg
from ScrabbleAR_py.Opciones import Ventana_Opciones
from ScrabbleAR_py.TabladePosiciones import Tabla
from ScrabbleAR_py.Tablero import genero_Tablero
from ScrabbleAR_py.ventana_Ayuda import Ayuda
from ScrabbleAR_py.Generadores import identificador_carpeta_error,corrector_paths,bloqueo_sonido
from playsound import playsound
import csv


#Aca Arranca La Pantalla Principal----------------------------------------------------------------------------------------------------------------------------------------------

def obtengo_Perfil():                                #Busco el nombre del ultimo usuario registrado
    archivo_csv=open(corrector_paths(r'ScrabbleAR_Datos\Archivo_Opciones.csv'),'r')
    perfiles=csv.reader(archivo_csv)
    for perfil in perfiles:
        if((len(perfil))>0):
            perfil_Actual=perfil[1]
    archivo_csv.close()
    return(perfil_Actual)

def establezco_PP():
#Columnas
    columna_izquierda=[ [sg.Text("USUARIO",relief='groove',font=('default',15),text_color='orange',size=(27,1),pad=((6,5),(3,3)),justification='center')],
                        [sg.Frame('',[[sg.Text(obtengo_Perfil(),font=('default',19),size=(19,1),justification='center')]],relief="sunken",pad=((5,5),(3,30)))],
                        [sg.Image(corrector_paths(r'ScrabbleAR_Imagenes_png\Icono_Jugar.png')),
                        sg.Button(button_text="JUGAR",font=('impact',20),size=(18,1),pad=(0,20))],
                        [sg.Image(corrector_paths(r'ScrabbleAR_Imagenes_png\Icono_Opciones.png')),
                        sg.Button(button_text="OPCIONES",font=('impact',20),size=(18,1),pad=(0,20))],
                        [sg.Image(corrector_paths(r'ScrabbleAR_Imagenes_png\Icono_Top10.png')),
                        sg.Button(button_text="TOP 10",font=('impact',20),size=(18,1),pad=(0,20))],
                        [sg.Image(corrector_paths(r'ScrabbleAR_Imagenes_png\Icono_Instrucciones.png')),
                        sg.Button(button_text="INSTRUCCIONES",key="AYUDA",font=('impact',20),size=(18,1),pad=(0,20))],
                        [sg.Image(corrector_paths(r'ScrabbleAR_Imagenes_png\Icono_Salir.png'),pad=((5,5),(80,3))),
                        sg.Button(button_text="SALIR",font=('Impact',20),size=(9,1),pad=((5,5),(80,3)))]  ]

    Linea = [[sg.Image(corrector_paths(r'ScrabbleAR_Imagenes_png\Linea.png'))]]

    columna_derecha=[ [sg.Image(corrector_paths(r'ScrabbleAR_Imagenes_png\ScrabbleAR_Inicio.png'),pad=(50,0))] ]

#Diseño
    diseño=[        [sg.Column(columna_izquierda),
                    sg.Column(Linea),
                    sg.Column(columna_derecha)]       ]

#Aplico y muestro

    window = sg.Window('Pantalla Principal',diseño,location=(540,100),size=(800,650))
    boton_cliqueado,datos_ingresados=window.Read()
    playsound(corrector_paths(r'ScrabbleAR_Sonidos\Click.mp3'),block=bloqueo_sonido())
    while True:
        if boton_cliqueado in(None,'SALIR'):
            break
        elif boton_cliqueado == 'JUGAR':
            #Aca abro la nueva ventana en el mismo lugar que la anterior , luego de cerrar la principal
            window.close()
            if((genero_Tablero())in(None,'Salir','Rendirse')):
                establezco_PP()
            break
        elif boton_cliqueado =='TOP 10':
            #Aca abro la nueva ventana en el mismo lugar que la anterior , luego de cerrar la principal
            window.close()
            if((Tabla())in(None,'Salir')):
                establezco_PP()
            break
        elif boton_cliqueado =='OPCIONES':
            #Aca abro la nueva ventana en el mismo lugar que la anterior , luego de cerrar la principal
            window.close()
            if((Ventana_Opciones())in(None,'Salir')):
                establezco_PP()
            break
        elif boton_cliqueado=="AYUDA":
            window.close()
            if((Ayuda())in(None,'Salir')):
                establezco_PP()
            break

    return(boton_cliqueado)

#Programa Principal-----------------------------------------------------------------------------------------------
if __name__ == "__main__":
    identificador_carpeta_error(establezco_PP)
