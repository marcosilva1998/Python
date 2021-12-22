try:
    import sys
    from playsound import playsound
    import PySimpleGUI as sg
    import random
    import csv
    from ScrabbleAR_py.Generadores import identificador_carpeta_error,corrector_paths,bloqueo_sonido
except ModuleNotFoundError:
    print("Error ,ejecute el  programa desde 'ScrabbleAR.py'")
    sys.exit()

Error_Op = True

def Primer_Cargar(values,window,Dicc_Bolsa,letra_Seleccionada):
    global Error_Op
    '''Carga por primera vez los datos de el Archivo_Opciones, devuelve values y Dicc_Bolsa'''
    arch = open(corrector_paths('ScrabbleAR_Datos\Archivo_Opciones.csv'),'r')
    reader = csv.reader(arch)
    Error_Op = False
    for row in reader:
        if (len(row) > 0):
            if (row[0] == 'True'):
                values[2] = row[2]
                values[3] = row[3]
                values[4] = row[4]
                if (values[2] == 'True'):
                    window['Facil'].update(values[0])
                elif(values[3] == 'True'):
                    window['Normal'].update(values[3])
                elif(values[4] == 'True'):
                    window['Dificil'].update(values[4])
                else:
                    window['Personalizado'].update(values[5])
                values[6] = row[6]
                window['Lote1'].update(values[6])
                values[7] = row[7]
                window['Lote2'].update(values[7])
                values[8] = row[8]
                window['Lote3'].update(values[8])
                values[9] = row[9]
                window['Lote4'].update(values[9])
                values[10] = row[10]
                window['Lote5'].update(values[10])
                values[11] = row[11]
                window['Lote6'].update(values[11])
                values[12] = row[12]
                window['Lote7'].update(values[12])
                values[13] = row[13]
                window['TT'].update(values[13])
                values[14] = row[14]
                window['TPR'].update(values[14])
                values[15] = row[15]
                window['Adjetivos'].update(True if values[15] != 'False' else False)
                values[16] = row[16]
                window['Sustantivos'].update(True if values[16] != 'False' else False)
                values[17] = row[17]
                window['Verbos'].update(True if values[17] != 'False' else False)
                a = 18
                for key in Dicc_Bolsa.keys():
                    Dicc_Bolsa[key] = int(row[a])
                    a = a + 1
                window['Cantidad'].update(Dicc_Bolsa[letra_Seleccionada])
                window['Usuario'].update(values[1])
    arch.close()
    return values,Dicc_Bolsa

def Cargar(values,window,Dicc_Bolsa,letra_Seleccionada):
    '''Carga los datos de el Archivo_Opciones, devuelve values'''
    arch = open(corrector_paths('ScrabbleAR_Datos\Archivo_Opciones.csv'),'r')
    reader = csv.reader(arch)
    for row in reader:
        if (len(row) > 0):
            if (row[1] == values['Usuario']):
                values['Facil'] = row[2]
                values['Normal'] = row[3]
                values['Dificil'] = row[4]
                if (values['Facil'] == 'True'):
                    window['Facil'].update(values['Facil'])
                elif(values['Normal'] == 'True'):
                    window['Normal'].update(values['Normal'])
                elif(values['Dificil'] == 'True'):
                    window['Dificil'].update(values['Dificil'])
                else:
                    window['Personalizado'].update(values['Personalizado'])
                values['Lote1'] = row[6]
                window['Lote1'].update(values['Lote1'])
                values['Lote2'] = row[7]
                window['Lote2'].update(values['Lote2'])
                values['Lote3'] = row[8]
                window['Lote3'].update(values['Lote3'])
                values['Lote4'] = row[9]
                window['Lote4'].update(values['Lote4'])
                values['Lote5'] = row[10]
                window['Lote5'].update(values['Lote5'])
                values['Lote6'] = row[11]
                window['Lote6'].update(values['Lote6'])
                values['Lote7'] = row[12]
                window['Lote7'].update(values['Lote7'])
                values['TT'] = row[13]
                window['TT'].update(values['TT'])
                values['TPR'] = row[14]
                window['TPR'].update(values['TPR'])
                values['Adjetivos'] = row[15]
                window['Adjetivos'].update(True if values['Adjetivos'] != 'False' else False)
                values['Sustantivos'] = row[16]
                window['Sustantivos'].update(True if values['Sustantivos'] != 'False' else False)
                values['Verbos'] = row[17]
                window['Verbos'].update(True if values['Verbos'] != 'False' else False)
                a = 18
                for key in Dicc_Bolsa.keys():
                    Dicc_Bolsa[key] = int(row[a])
                    a = a + 1
                window['Cantidad'].update(Dicc_Bolsa[letra_Seleccionada])
    arch.close()
    return values

def AgregarDatos(values):
    '''Agrega los datos de un usuario nuevo ingresado a Archivo_Opciones'''
    arch = open(corrector_paths('ScrabbleAR_Datos\Archivo_Opciones.csv'),'a')
    writer = csv.writer(arch)
    writer.writerow([True,values['Usuario'].strip(),values['Facil'],values['Normal'],values['Dificil'],values['Personalizado'],int(values['Lote1']),int(values['Lote2']),int(values['Lote3']),int(values['Lote4']),int(values['Lote5']),int(values['Lote6']),int(values['Lote7']),values['TT'],values['TPR'],values['Adjetivos'],values['Sustantivos'],values['Verbos'],values['A'],values['B'],values['C'],values['D'],values['E'],values['F'],values['G'],values['H'],values['I'],values['J'],values['K'],values['L'],values['M'],values['N'],values['Enie'],values['O'],values['P'],values['Q'],values['R'],values['R'],values['S'],values['T'],values['U'],values['V'],values['W'],values['X'],values['Y'],values['Z']])
    arch.close()

def GuardarDatos(lista):
    '''Guarda los datos de un usuario'''
    arch = open(corrector_paths('ScrabbleAR_Datos\Archivo_Opciones.csv'),'w')
    writer = csv.writer(arch)
    writer.writerow(['Actual','Usuario','Facil','Normal','Dificil','Personalizado','Lote1','Lote2','Lote3','Lote4','Lote5','Lote6','Lote7','TT','TPR','Adjetivos','Sustantivos','Verbos','A','B','C','D','E','F','G','H','I','J','K','L','M','N','Enie','O','P','Q','R','S','T','U','V','W','X','Y','Z'])
    for row in lista:
        writer.writerow([row['Actual'],row['Usuario'].strip(),row['Facil'],row['Normal'],row['Dificil'],row['Personalizado'],int(row['Lote1']),int(row['Lote2']),int(row['Lote3']),int(row['Lote4']),int(row['Lote5']),int(row['Lote6']),int(row['Lote7']),row['TT'],row['TPR'],row['Adjetivos'],row['Sustantivos'],row['Verbos'],row['A'],row['B'],row['C'],row['D'],row['E'],row['F'],row['G'],row['H'],row['I'],row['J'],row['K'],row['L'],row['M'],row['N'],row['Enie'],row['O'],row['P'],row['Q'],row['R'],row['R'],row['S'],row['T'],row['U'],row['V'],row['W'],row['X'],row['Y'],row['Z']])
    arch.close()

def LeerDatos():
    '''Lee los datos de el Archivo_Opciones y los retorna en forma de lista con diccionarios.'''
    arch = open(corrector_paths('ScrabbleAR_Datos\Archivo_Opciones.csv'),'r')
    reader = csv.reader(arch)
    datos = []
    index = 0
    for row in reader:
        if (len(row) > 0):
            if (index == 0):
                claves = row
                index = index + 1
            else:
                dicc = {}
                [dicc.setdefault(claves[i],row[i]) for i in range(len(claves))]
                datos.append(dicc.copy())
    arch.close()
    return datos

def RestablecerPredeterminado(values,window,Dicc_Bolsa,letra_Seleccionada):
    '''Restablece en predeterminado todos los valores de el menu opciones'''
    values['Facil'] = False
    window['Facil'].update(values['Facil'])
    values['Normal'] = True
    window['Normal'].update(values['Normal'])
    values['Dificil'] = False
    window['Dificil'].update(values['Dificil'])
    values['Personalizado'] = False
    window['Personalizado'].update(values['Personalizado'])
    values['Lote1'] = 1
    window['Lote1'].update(values['Lote1'])
    values['Lote2'] = 2
    window['Lote2'].update(values['Lote2'])
    values['Lote3'] = 3
    window['Lote3'].update(values['Lote3'])
    values['Lote4'] = 4
    window['Lote4'].update(values['Lote4'])
    values['Lote5'] = 6
    window['Lote5'].update(values['Lote5'])
    values['Lote6'] = 8
    window['Lote6'].update(values['Lote6'])
    values['Lote7'] = 10
    window['Lote7'].update(values['Lote7'])
    values['TT'] = 45
    window['TT'].update(values['TT'])
    values['TPR'] = 45
    window['TPR'].update(values['TPR'])
    values['Adjetivos'] = False
    window['Adjetivos'].update(values['Adjetivos'])
    values['Sustantivos'] = True
    window['Sustantivos'].update(values['Sustantivos'])
    values['Verbos'] = True
    window['Verbos'].update(values['Verbos'])
    Dicc_Bolsa={"A":11,"B":3,"C":4,"D":4,"E":11,"F":2,"G":2,"H":2,"I":6,"J":2,"K":1,"L":4,"M":3,"N":5,
                      "Enie":1,"O":8,"P":2,"Q":1,"R":4,"S":7,"T":4,"U":6,"V":2,"W":1,"X":1,"Y":1,"Z":1}

    window['Cantidad'].update(Dicc_Bolsa[letra_Seleccionada])
    Cant_Fichas_Total = Contabilizar_Fichas(Dicc_Bolsa)
    window['FichasTotales'].update('Fichas totales:'+str(Cant_Fichas_Total))
    return values,Dicc_Bolsa,Cant_Fichas_Total

def Layout_Columna():
    '''Construye y devuelve un layout'''

    frame1 = [[sg.Text('Tiempo total:',key='Texto_TT'),sg.Input(pad=((55,0),(5,2)),size=(6,6),key='TT'),sg.Text('Minutos',key='Texto_Minutos')],
              [sg.Text('Tiempo por ronda:',key='Texto_TPR'),sg.Input(pad=((10,0),(2,5)),size=(6,6),key='TPR'),sg.Text('Segundos',key='Texto_Segundos')]]

    frame2 = [[sg.Text('LETRAS',key='Texto_Letra'),sg.Slider(range=(0,26),orientation="v",pad=((5,3),(5,0)),size=(6,10),disable_number_display=True,enable_events=True,key='Letras'),sg.Text('A',key='Letra_Pantalla',font=('Default',80),pad=(20,3))],
    [sg.Slider(range=(1,15),orientation="h",pad=((90,3),(0,3)),key='Cantidad',enable_events=True,size=(12,10))],
    [sg.Text('CANTIDAD',key='Texto_Cantidad',pad=((110,3),(5,12)))],
    [sg.Text('Fichas totales:0000',key='FichasTotales')]]

    frame3 = [[sg.Checkbox('Adjetivos',key='Adjetivos'),sg.Checkbox('Sustantivos',key='Sustantivos'),sg.Checkbox('Verbos',key='Verbos')]]

    layout = [[sg.Frame('Tiempo',frame1,pad=((5,5),(54,12)))],
              [sg.Frame('Tipos de palabra',frame3)],
              [sg.Frame('Cantidad de fichas por letra',frame2,pad=((60,0),(15,0)))],
              [sg.Exit('Salir',pad=((320,0),(80,0)))]]
    return layout

def Layout_Main():
    '''Constuye y devuelve un layout'''
    frame = [[sg.Text('A E O S I U N L R T:'),sg.Slider(range=(1,2),orientation="h",size=(6,10),pad=((5,3),(0,22)),default_value=1,key='Lote1')],
            [sg.Text('C D G :'),sg.Slider(range=(1,3),orientation="h",size=(6,10),pad=((108,3),(0,22)),default_value=2,key='Lote2')],
            [sg.Text('M B P:'),sg.Slider(range=(2,4),orientation="h",size=(6,10),pad=((109,3),(0,22)),default_value=3,key='Lote3')],
            [sg.Text('F H V Y:'),sg.Slider(range=(3,5),orientation="h",size=(6,10),pad=((96,3),(0,22)),default_value=4,key='Lote4')],
            [sg.Text('J:'),sg.Slider(range=(5,7),orientation="h",size=(6,10),pad=((150,3),(0,22)),default_value=6,key='Lote5')],
            [sg.Text('K Ñ Q W X:'),sg.Slider(range=(7,9),orientation="h",size=(6,10),pad=((70,3),(0,22)),default_value=8,key='Lote6')],
            [sg.Text('Z:'),sg.Slider(range=(9,11),orientation="h",size=(6,10),pad=((146,3),(0,22)),default_value=10,key='Lote7')]]

    frame_Dificultad = [[sg.Radio('Facil','Dificultad',key='Facil',enable_events=True,tooltip='En "Facil" se aplicaran los siguientes cambios:\n_____________\nSe aceptaran: Adjetivos, Sustantivos y Verbos\nTiempo por ronda: 60sg \nTiempo Total: 60Min',pad=(8,3)),
    sg.Radio('Normal','Dificultad', default='1',key='Normal',enable_events=True,tooltip='En "Normal" se aplicaran los siguientes cambios:\n_____________\nSe aceptaran: Adjetivos y Verbos\nTiempo por ronda: 45sg \nTiempo Total: 45Min',pad=(8,3))],
    [sg.Radio('Dificil','Dificultad',key='Dificil',enable_events=True,tooltip='En "Dificil" se aplicaran los siguientes cambios:\n_____________\nSe aceptaran: Adjetivos y Verbos(De forma Aleatoria)\nTiempo por ronda: 30sg \nTiempo Total: 30Min',pad=(8,3)),sg.Radio('Personalizado','Dificultad',key='Personalizado',enable_events=True,tooltip='Puedes cambiar la configuracion a tu antojo',pad=(8,3))]]

    layout = [[sg.Text('Usuario:'),sg.Input(size=(15, 6),key='Usuario',default_text='Default'),sg.OK('Cargar perfil',key='Cargar')],
            [sg.Frame('Dificultad:',frame_Dificultad,pad=(5,10))],
            [sg.Frame('Cantidad de puntos por ficha',frame)],
            [sg.Save('Guardar'),sg.OK('Restablecer predeterminado')]]
    return layout

def Poner_Todos_En_Falso(lista):
    '''Reemplaza el valor actual por False a todos los usuarios ingresados en el Archivo_Opciones'''
    arch = open(corrector_paths('ScrabbleAR_Datos\Archivo_Opciones.csv'),'w')
    writer = csv.writer(arch)
    writer.writerow(['Actual','Usuario','Facil','Normal','Dificil','Personalizado','Lote1','Lote2','Lote3','Lote4','Lote5','Lote6','Lote7','TT','TPR','Adjetivos','Sustantivos','Verbos','A','B','C','D','E','F','G','H','I','J','K','L','M','N','Enie','O','P','Q','R','S','T','U','V','W','X','Y','Z'])
    i = 0
    for row in lista:
        lista[i]['Actual'] = False
        writer.writerow([False,row['Usuario'].strip(),row['Facil'],row['Normal'],row['Dificil'],row['Personalizado'],int(row['Lote1']),int(row['Lote2']),int(row['Lote3']),int(row['Lote4']),int(row['Lote5']),int(row['Lote6']),int(row['Lote7']),row['TT'],row['TPR'],row['Adjetivos'],row['Sustantivos'],row['Verbos'],row['A'],row['B'],row['C'],row['D'],row['E'],row['F'],row['G'],row['H'],row['I'],row['J'],row['K'],row['L'],row['M'],row['N'],row['Enie'],row['O'],row['P'],row['Q'],row['R'],row['R'],row['S'],row['T'],row['U'],row['V'],row['W'],row['X'],row['Y'],row['Z']])
        i = i + 1
    arch.close()

def Importar_Datos():
    '''Importa de Archivo_Opciones los datos del usuario activo'''
    arch = open(corrector_paths('ScrabbleAR_Datos\Archivo_Opciones.csv'),'r')
    reader = csv.reader(arch)
    index = 0
    for row in reader:
        if (len(row) > 0):
            if (index != 0):
                if (row[0] == 'True'):
                    arch.close()
                    return row
            else:
                index = index + 1

def Transformar_Values(values,Dicc_Bolsa):
    '''Tranforma values en un diccionario mas preciso para poder exportarlo luego a Archivo_Opciones'''
    values.pop('Letras')
    values.pop('Cantidad')
    for key,elem in Dicc_Bolsa.items():
        values[key] = elem

def Infomar_Error_Usuario(evento,mensaje,colorOriginal,window):
    '''Informa al usuario que inconveniente se presenta'''
    window[evento].update(background_color='red')
    playsound(corrector_paths(r'ScrabbleAR_Sonidos\Error_Opciones.mp3'),block=bloqueo_sonido())
    sg.popup(mensaje,background_color='#B91B1B',title='Aviso',keep_on_top=True)
    window[evento].update(background_color=colorOriginal)

def Comprobaciones(values,Cant_Fichas_Total,window):
    '''Se comprueba que no el usuario no haya ingresado algo que no debe'''
    TodoOk = True
    if values['Usuario'] != '':
        for L in values['Usuario']:
            if ((ord(L) < 48) or (ord(L) > 57) and (ord(L) < 65) or (ord(L) > 90) and (ord(L) < 97) or (ord(L) > 122)):
                Infomar_Error_Usuario('Usuario','Prueba con un usuario que tenga letras y/o numeros!','#F1D6AB',window)
                TodoOk = False
                break
    else:
        Infomar_Error_Usuario('Usuario','No puedes guardar un usuario vacio!','#F1D6AB',window)
        TodoOk = False

    if len(values['Usuario']) > 10:
        Infomar_Error_Usuario('Usuario','No puedes guardar un usuario con mas de 10 caracteres!','#F1D6AB',window)
        TodoOk = False

    for T in ['TT','TPR']:
        Es_numero = True
        if values[T] != '':
            for c in values[T]:
                if not(ord(c) >= 48 and ord(c) <= 57):
                    Infomar_Error_Usuario(T,'Prueba ingresar un numero valido!','#F1D6AB',window)
                    TodoOk = False
                    sonNumeros = False
                    break
                else:
                    sonNumeros = True
            if sonNumeros:
                if (T == 'TT') and (int(values[T]) > 120):
                    Infomar_Error_Usuario('TT','Intenta ingresar un numero menor a 120!','#F1D6AB',window)
                    TodoOk = False
                if (T == 'TPR') and (int(values[T]) > 600):
                    Infomar_Error_Usuario('TPR','Intenta ingresar un numero menor a 600!','#F1D6AB',window)
                    TodoOk = False

        else:
            Infomar_Error_Usuario(T,'Prueba ingresar un numero!','#F1D6AB',window)
            TodoOk = False

    if values['Adjetivos'] == False and values['Sustantivos'] == False and values['Verbos'] == False:
        window['Adjetivos'].update(background_color='red')
        window['Sustantivos'].update(background_color='red')
        window['Verbos'].update(background_color='red')
        playsound(corrector_paths(r'ScrabbleAR_Sonidos\Error_Opciones.mp3'),block=bloqueo_sonido())
        sg.popup('No puedes dejar las casillas vacias!',background_color='#B91B1B',title='Aviso',keep_on_top=True)
        window['Adjetivos'].update(background_color='#2B2B28')
        window['Sustantivos'].update(background_color='#2B2B28')
        window['Verbos'].update(background_color='#2B2B28')
        TodoOk = False

    if Cant_Fichas_Total < 99 or Cant_Fichas_Total > 200:
        Infomar_Error_Usuario('FichasTotales','Intenta que las fichas totales sean mayores a 99 y menores a 200!','#2B2B28',window)
        TodoOk = False

    return TodoOk

def Deshabilitar(Dificultad_Actual,window):
    '''Desabilita el tiempo\Tipos de palabra si no se elige la dificultad personalizado'''
    if Dificultad_Actual == 'Facil' or Dificultad_Actual == 'Normal' or Dificultad_Actual == 'Dificil':
        window['Texto_TT'].update(text_color='grey') #ADADAD = 'gris'
        window['Texto_TPR'].update(text_color='grey')
        window['TT'].update(text_color='grey')
        window['TPR'].update(text_color='grey')
        window['Texto_Minutos'].update(text_color='grey')
        window['Texto_Segundos'].update(text_color='grey')
        if Dificultad_Actual == 'Facil':
            window['TT'].update('60',disabled=True)
            window['TPR'].update('60',disabled=True)
            window['Adjetivos'].update(True,disabled=True)
            window['Sustantivos'].update(True,disabled=True)
            window['Verbos'].update(True,disabled=True)
        elif Dificultad_Actual == 'Normal':
            window['TT'].update('45',disabled=True)
            window['TPR'].update('45',disabled=True)
            window['Adjetivos'].update(True,disabled=True)
            window['Sustantivos'].update(False,disabled=True)
            window['Verbos'].update(True,disabled=True)
        elif Dificultad_Actual == 'Dificil':
            window['TT'].update('30',disabled=True)
            window['TPR'].update('30',disabled=True)
            Lista_random = ['Adjetivos','Verbos']
            random.shuffle(Lista_random)
            window[Lista_random[0]].update(True,disabled=True)
            window[Lista_random[1]].update(False,disabled=True)
            window['Sustantivos'].update(False,disabled=True)
    else:
        window['TT'].update(disabled=False)
        window['TPR'].update(disabled=False)
        window['Adjetivos'].update(disabled=False)
        window['Sustantivos'].update(disabled=False)
        window['Verbos'].update(disabled=False)
        window['Texto_TT'].update(text_color='white')
        window['Texto_TPR'].update(text_color='white')
        window['TT'].update(text_color='black')
        window['TPR'].update(text_color='black')
        window['Texto_Minutos'].update(text_color='white')
        window['Texto_Segundos'].update(text_color='white')


def Cual_Dificultad(Facil,Normal,Dificil,window):
    '''Devuelve la dificultad actual que el usuario eligio'''
    if Facil == 'True':
            dificultad = 'Facil'
    elif Normal == 'True':
            dificultad = 'Normal'
    elif Dificil == 'True':
            dificultad = 'Dificil'
    else:
        dificultad = 'Personalizado'
    return dificultad

def Contabilizar_Fichas(Dicc_Bolsa):
    '''Contabiliza la cantidad de fichas que hay en total en funcion a los cambios generados en menu opciones'''
    Cant_Total = 0
    for Cant in Dicc_Bolsa.values():
        Cant_Total = Cant_Total + Cant
    return Cant_Total

def Cargar_Perfil(Lista,Dicc_Bolsa,letra_Seleccionada,window):
    Lista_Usuarios = []
    for i in Lista:
        if (i['Actual'] != 'True'):
            Lista_Usuarios.append(i['Usuario'])
        else:
            Lista_Usuarios.append('*'+i['Usuario'])
    window_cargar = sg.Window('Cargar',[[sg.Listbox(Lista_Usuarios,size=(20, 10))],[sg.Button('Cargar'),sg.Button('Eliminar'),sg.Exit('Salir')]])
    while True:
        event_cargar,values_cargar = window_cargar.read()

        if event_cargar in (None, 'Salir'):
            playsound(corrector_paths(r'ScrabbleAR_Sonidos\Click.mp3'),block=bloqueo_sonido())
            break

        if values_cargar[0] != []: #Si selecciono algo:

            values_cargar[0][0] = values_cargar[0][0].strip('*')
            Jugador_Seleccionado = list(filter(lambda jug:values_cargar[0][0].strip() == jug['Usuario'],Lista))

            if (event_cargar == 'Cargar'):
                Lista.pop(Lista.index(Jugador_Seleccionado[0]))
                Jugador_Seleccionado[0]['Actual'] = True
                Poner_Todos_En_Falso(Lista)
                Lista.append(Jugador_Seleccionado[0])
                GuardarDatos(Lista)
                values = Cargar(Jugador_Seleccionado[0],window,Dicc_Bolsa,letra_Seleccionada)
                playsound(corrector_paths(r'ScrabbleAR_Sonidos\Click.mp3'),block=bloqueo_sonido())
            #Eliminar:
            else:
                if (len(Lista) > 1):
                    if Jugador_Seleccionado[0]['Actual'] == 'True':
                        Lista[0]['Actual'] = True
                    Lista.pop(Lista.index(Jugador_Seleccionado[0]))
                    GuardarDatos(Lista)
                    playsound(corrector_paths(r'ScrabbleAR_Sonidos\Exito_Opciones.mp3'),block=bloqueo_sonido())
                    sg.popup('El perfil se ha eliminado con exito!',background_color='#63B91B',title='Aviso',keep_on_top=True)
                else:
                    playsound(corrector_paths(r'ScrabbleAR_Sonidos\Error_Opciones.mp3'),block=bloqueo_sonido())
                    sg.popup('No puedes eliminar el ultimo perfil!',background_color='#B91B1B',title='Aviso',keep_on_top=True)
        else:
            playsound(corrector_paths(r'ScrabbleAR_Sonidos\Error_Opciones.mp3'),block=bloqueo_sonido())
            sg.popup('Tienes que seleccionar un perfil!',title='Aviso',background_color='#B91B1B',keep_on_top=True)
    window_cargar.close()

def Ventana_Opciones ():
    '''Abre menu de opciones con todas sus funciones'''
    sg.theme('DarkGrey2')
    Lista_Letras = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Enie','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    Diseño = [ [sg.Column((Layout_Main())),
                sg.Column(Layout_Columna())] ]
    window = sg.Window('Opciones', Diseño,font='Cambria',size=(808, 667))
    window.Read(timeout=1)[1]
    Dicc_Bolsa={"A":11,"B":3,"C":4,"D":4,"E":11,"F":2,"G":2,"H":2,"I":6,"J":2,"K":1,"L":4,"M":3,"N":5,
                      "Enie":1,"O":8,"P":2,"Q":1,"R":4,"S":7,"T":4,"U":6,"V":2,"W":1,"X":1,"Y":1,"Z":1}
    values,Dicc_Bolsa = Primer_Cargar(Importar_Datos(),window,Dicc_Bolsa,'A')
    letra_Seleccionada = 'A'
    Dificultad_Actual = Cual_Dificultad(values[2],values[3],values[4],window)
    Ultima_Dificultad = 'Personalizado'
    Cant_Letra_Actual = Dicc_Bolsa['A']
    window['Cantidad'].update(Dicc_Bolsa['A'])
    while True:
        Cant_Fichas_Total = Contabilizar_Fichas(Dicc_Bolsa)
        window['FichasTotales'].update('Fichas totales:'+str(Cant_Fichas_Total))

        if (Ultima_Dificultad != Dificultad_Actual):
            Deshabilitar(Dificultad_Actual,window)

        event, values = window.read()

        if event in (None, 'Salir'):
            playsound(corrector_paths(r'ScrabbleAR_Sonidos\Click.mp3'))
            break

        if event == 'Letras':
            window['Cantidad'].update(Dicc_Bolsa[Lista_Letras[int(values['Letras'])]])
            if Lista_Letras[int(values['Letras'])] != 'Enie':
                window['Letra_Pantalla'].update(Lista_Letras[int(values['Letras'])])
            else:
                window['Letra_Pantalla'].update('Ñ')
            letra_Seleccionada = Lista_Letras[int(values['Letras'])]

        elif event == 'Cantidad':
            Cant_Letra_Actual = values['Cantidad']
            Dicc_Bolsa[letra_Seleccionada] = int(Cant_Letra_Actual)

        elif (event == 'Restablecer predeterminado'):
            playsound(corrector_paths(r'ScrabbleAR_Sonidos\Click.mp3'),block=bloqueo_sonido())
            values,Dicc_Bolsa,Cant_Fichas_Total = RestablecerPredeterminado(values,window,Dicc_Bolsa,letra_Seleccionada)

        elif (event == 'Guardar') or (event == 'Cargar'):
            playsound(corrector_paths(r'ScrabbleAR_Sonidos\Click.mp3'),block=bloqueo_sonido())
            Lista = LeerDatos()
            Transformar_Values(values,Dicc_Bolsa)
            if (event == 'Guardar'):
                if Comprobaciones(values,Cant_Fichas_Total,window):
                    existe = list(filter(lambda jug:values['Usuario'].strip() == jug['Usuario'],Lista))
                    if existe != []: #Reemplazo la configuracion del usuario existente
                        Lista.pop(Lista.index(existe[0]))
                        values['Actual'] = True
                        Lista.append(values)
                        GuardarDatos(Lista)
                        playsound(corrector_paths(r'ScrabbleAR_Sonidos\Exito_Opciones.mp3'),block=bloqueo_sonido())
                        sg.popup('El perfil se modifico exitosamente!',background_color='#63B91B',title='Aviso',keep_on_top=True)
                    else: #Simplemente lo agrego
                        Poner_Todos_En_Falso(Lista)
                        AgregarDatos(values)
                        playsound(corrector_paths(r'ScrabbleAR_Sonidos\Exito_Opciones.mp3'),block=bloqueo_sonido())
                        sg.popup('El perfil se guardo exitosamente!',background_color='#63B91B',title='Aviso',keep_on_top=True)

            else:           #Cargar Perfil
                Cargar_Perfil(Lista,Dicc_Bolsa,letra_Seleccionada,window)

        Ultima_Dificultad = Dificultad_Actual
        Dificultad_Actual = Cual_Dificultad(str(values['Facil']),str(values['Normal']),str(values['Dificil']),window)

    window.close()
    return event


#PROGRAMA PRINCIPAL
if __name__ == "__main__":
    identificador_carpeta_error(Ventana_Opciones)
