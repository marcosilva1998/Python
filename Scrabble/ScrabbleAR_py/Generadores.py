import string
import random
import sys
import traceback
import tkinter
import PySimpleGUI as sg
import platform
import os
def bloqueo_sonido():
    if platform.system() == "Linux":
        return True
    else:
        return False
def corrector_paths(path):
    sistema_Operativo=platform.system()
    path_base=os.getcwd()
    path_add=path.split(chr(92))
    path=os.path.join(path_base,*path_add)
    return(path)


def identificador_carpeta_error(ProgramaPrincipal):
    event=""
    try:
        event=ProgramaPrincipal()
    except FileNotFoundError:
        tb = sys.exc_info()[2]
        tbinfo = traceback.format_tb(tb)[2]
        ruta_archivo_error=tbinfo[tbinfo.find("(")+1:tbinfo.find(")")].strip(",'r'")
        ruta_archivo_error=ruta_archivo_error.strip("corrector_paths('")
        ruta_carpeta=ruta_archivo_error[:ruta_archivo_error.find(os.sep)]
        sg.popup_error("Error al intentar acceder al archivo de la siguiente ruta :",corrector_paths(ruta_archivo_error),"\nRevise que el archivo se encuentre en la carpeta",ruta_carpeta,"\nError en : ",tbinfo,title='Error')
    except tkinter.TclError:
        Direciones_error={"inicio":corrector_paths(r'ScrabbleAR_Imagenes_png\icono_inicio.png'),"yellow":corrector_paths(r'ScrabbleAR_Imagenes_png\icono3.png'),"red":corrector_paths(r'ScrabbleAR_Imagenes_png\icono_x2.png'),
        "green":corrector_paths(r'ScrabbleAR_Imagenes_png\icono_-3.png'),"blue":corrector_paths(r'ScrabbleAR_Imagenes_png\icono_-2.png'),"white":corrector_paths(r'ScrabbleAR_Imagenes_png\modelo_ficha.png')}
        tb = sys.exc_info()[2]
        tbinfo = traceback.format_tb(tb)[3]
        if("window[coord].update" in tbinfo):

            ruta_archivo_error=tbinfo[tbinfo.find("(")+1:tbinfo.find(")")].strip(",'r'")
            ruta_archivo_error=ruta_archivo_error[:ruta_archivo_error.find(",")]
            ruta_archivo_error=ruta_archivo_error[ruta_archivo_error.find("=")+1:]
            ruta_carpeta=Direciones_error[ruta_archivo_error]
            ruta_capeta=ruta_carpeta.split(str(os.sep))
            sg.popup_error("Error al intentar acceder a la imagen de la siguiente ruta :",Direciones_error[ruta_archivo_error] ,"\nRevise que la imagen se encuentre el la carpeta: ",ruta_capeta[len(ruta_capeta)-2] ,"\nError en : ",tbinfo ,title='Error')
        else:
            sg.popup_error("Hubo un error con PySimpleGUI\nError en : ",tbinfo,title='Error')#Tambien puede ser un error con PySimpleGUI
    except UnicodeDecodeError:
        tb = sys.exc_info()[2]
        tbinfo = traceback.format_tb(tb)[1]
        if "playsound" in tbinfo:
            ruta_archivo_error=tbinfo[tbinfo.find("(")+1:tbinfo.find(")")].strip(",'r'")
            ruta_archivo_error=ruta_archivo_error.strip("corrector_paths('")
            ruta_carpeta=ruta_archivo_error[:ruta_archivo_error.find(os.sep)]
            sg.popup_error("Error al intentar acceder al archivo de audio de la siguiente ruta :",corrector_paths(ruta_archivo_error),"\nRevise que el archivo de audio se encuentre el la carpeta: ",ruta_carpeta,"\nError en : ",tbinfo ,title='Error')
        else:
            sg.popup_error("Falta un archivo de audio , revise la carpeta ScrabbleAR_Sonidos\nError en : ",tbinfo,title='Error')
#    except:
#        tb = sys.exc_info()[2]
#        tbinfo = traceback.format_tb(tb)
#        sg.popup_error("Ah ocurrido un error desconocido\nInfo de error :",tbinfo,title='Error')
    return(event)



def Selector_de_coordenadas_disponibles(conjunto):
    x=random.randint(0,(len(conjunto)-1))
    conjunto=list(conjunto)
    return(tuple(conjunto[x]))
