import os

from ScrabbleAR_py.Generadores import corrector_paths
'''
letras_rutas=['A1','A2','B2','B3','B4','C1','C2','C3','D1','D2','D3','E1','E2','F3','F4','F5','G1','G2','G3','H3','H4','H5','I1','I2','J5','J6','J7','K7','K8','K9','L1','L2','M2','M3','M4','N1','N2','O1','O2','P2','P3','P4','Q7','Q8','Q9','R1','R2','S1','S2','T1','T2','U1','U2','V3','V4','V5','W7','W8','W9','X7','X8','X9','Y3','Y4','Y5','Z10','Z11','Z9','Ñ7','Ñ8','Ñ9']
carpeta_imagen="ScrabbleAR_Imagenes_png"+chr(92)
ruta_imagen_B=sorted(os.listdir(carpeta_imagen+"FichasUsuario_B"))#Fichas Blancas
ruta_imagen_S=sorted(os.listdir(carpeta_imagen+"FichasUsuario_S"))
ruta_imagen_T=sorted(os.listdir(carpeta_imagen+"FichasUsuario_T"))
print(ruta_imagen_B)
Dicc_Rutas={}
x=0
for imagen in letras_rutas:
    Dicc_Rutas[imagen]=[corrector_paths(carpeta_imagen+"FichasUsuario_B"+chr(92)+ruta_imagen_B[x]),corrector_paths(carpeta_imagen+"FichasUsuario_S"+chr(92)+ruta_imagen_S[x]),corrector_paths(carpeta_imagen+"FichasUsuario_T"+chr(92)+ruta_imagen_T[x])]
    x=x+1
'''

'''
letras_rutas_CPU=['A1','A2','B2','B3','B4','C1','C2','C3','D1','D2','D3','E1','E2','F3','F4','F5','G1','G2','G3','H3','H4','H5','I1','I2','J5','J6','J7','K7','K8','K9','L1','L2','M2','M3','M4','N1','N2','O1','O2','P2','P3','P4','Q7','Q8','Q9','R1','R2','S1','S2','T1','T2','U1','U2','V3','V4','V5','W7','W8','W9','X7','X8','X9','Y3','Y4','Y5','Z10','Z11','Z9','Ñ7','Ñ8','Ñ9']
carpeta_imagen="ScrabbleAR_Imagenes_png"+chr(92)
ruta_imagen_CPU=sorted(os.listdir(carpeta_imagen+"FichasCPU"))#Fichas Negras
Dicc_Rutas_CPU={}
x=0
for imagen in letras_rutas_CPU:
    Dicc_Rutas_CPU[imagen]=corrector_paths(carpeta_imagen+"FichasCPU"+chr(92)+ruta_imagen_CPU[x])
    x=x+1
print(Dicc_Rutas_CPU)
'''
Dicc={}
#red,yellow,blue,green
Diseño1={"red":["0,2","0,12","2,0","2,14","5,7","7,5","7,9","9,7","12,0","12,14","14,2","14,12"],
        "yellow":["1,5","1,9","3,7","5,1","5,13","7,3","7,11","9,1","9,13","11,7","13,5","13,9"],
        "blue":["1,7","3,3","3,11","5,5","5,9","7,1","7,13","9,5","9,9","11,3","11,11","13,7"],
        "green":[ "0,4","0,10","1,1","1,13","2,6","2,8","4,0","4,14","6,2","6,12","8,2","8,12","10,0","10,14","12,6","12,8","13,1","13,13","14,4","14,10"]}
Diseño2={"red":[],"yellow":[],"blue":["2,2","2,12","3,3","3,11","4,4","4,9","10,4","10,10","11,3","11,11","12,2","12,12"],"green":["0,0","0,14","1,1","1,13","2,3","2,11","3,2","3,12","5,2","5,12","9,2","9,12","11,2","11,12","12,3","12,11","13,1","13,13","14,0","14,14"]}
Diseño3={"red":[],"yellow":[],"blue":[],"green":[]}
#Primero se ve cual diseño se va a usar
for x in range(15):         #por ejemplo
    for y in range(15):
        coordenada=str(x)+","+str(y)
        if(coordenada) in Diseño1["red"]:
            Dicc[coordenada]="red"
        elif(coordenada) in Diseño1["yellow"]:
             Dicc[coordenada]="yellow"
        elif(coordenada) in Diseño1["blue"]:
             Dicc[coordenada]="blue"
        elif(coordenada) in Diseño1["green"]:
             Dicc[coordenada]="green"
        else:
            Dicc[coordenada]="white"
print("Nuevo",Dicc)
