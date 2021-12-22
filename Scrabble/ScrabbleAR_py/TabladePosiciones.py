#!/usr/bin/env python
try:
    import sys
    import PySimpleGUI as sg
    import csv
    from playsound import playsound
    from ScrabbleAR_py.Generadores import identificador_carpeta_error,bloqueo_sonido,corrector_paths
except ModuleNotFoundError:
    print("Error ,ejecute el  programa desde 'ScrabbleAR.py'")
    sys.exit()
# Show CSV data in Table
sg.theme('DarkGrey2')

def Tabla():

    data_inicial = [[],[],[],[],[],[],[],[],[],[]]
    data_facil = []
    data_normal = []
    data_dificil = []
    data_personalizada = []
    header_list = []
    with open(corrector_paths(r'ScrabbleAR_Datos\Archivo_Puntajes.csv'), "r") as infile:
        reader = csv.reader(infile)
        header_list = next(reader)
        header_list.insert(0, 'N°')
        for row in reader:
            if (len(row) > 0):
                if row[3] == 'Facil':
                    data_facil.append(row)
                elif row[3] == 'Normal':
                    data_normal.append(row)
                elif row[3] == 'Dificil':
                    data_dificil.append(row)
                elif row[3] == 'Personalizado':
                    data_personalizada.append(row)
    for x in range(10):
        data_inicial[x].extend([["-"],["-"],["-"],["--/--/--"],["-"]])

    def DataTotal(window,*Lista):
        Total = []
        Merge = []
        for Dificultad in Lista:
            Merge.extend(Dificultad)
        Merge = sorted(Merge,key=lambda x:int(x[1]),reverse=True)
        for x in range(10):
            Total.append(Merge[x].copy()) #sirve el .copy() y el [:] , al estar pasando una lista de una lista , ambas direcciones eran las mismas
            Total[x].insert(0, x+1)
        window['info'].Update(Total)

    def DataMod(window,Lista):
        Lista = sorted(Lista,key=lambda x:int(x[1]),reverse=True)
        for x in range(len(Lista)):
            Lista[x].insert(0, x+1)
        window['info'].Update(Lista)
        for x in range(len(Lista)):
            Lista[x].remove(x+1)

    sg.set_options(element_padding=(0, 0))

    layout: list = [[sg.Button(button_text="Total",size=(17,2),pad=((0,14),(0,0)),key="Total"),sg.Button(button_text="Facil",size=(17,2),pad=((0,14),(0,0)),key="Facil"),sg.Button(button_text="Normal",size=(17,2),pad=((0,14),(0,0)),key="Normal"),sg.Button(button_text="Dificil",size=(17,2),pad=((0,14),(0,0)),key="Dificil"),sg.Button(button_text="Personalizada",size=(17,2),pad=((0,14),(0,0)),key="Personalizada")],
                     [sg.Table(values=data_inicial,
                            key='info',
                            headings=header_list,
                            def_col_width=17,
                            auto_size_columns=False,
                            hide_vertical_scroll=True,
                            display_row_numbers=False,
                            justification='center',
                            alternating_row_color='Brown',
                            row_height=50,
                            num_rows=10)],
                            [sg.Button(button_text="Salir",size=(20,2),key="Salir")]]


    window = sg.Window('Top',layout,location=(200,50),size=(797,600),finalize=True)
    while True:
        event, values = window.read()
        playsound(corrector_paths(r'ScrabbleAR_Sonidos\Click.mp3'),block=bloqueo_sonido())
        if(event in (None,"Salir")):
            playsound(corrector_paths(r'ScrabbleAR_Sonidos\Click.mp3'))
            break
        elif event == 'Total':
            DataTotal(window,data_facil,data_normal,data_dificil,data_personalizada)
        elif event in ('Facil',values):
            DataMod(window,data_facil)
        elif event == 'Normal':
            DataMod(window,data_normal)
        elif event == 'Dificil':
            DataMod(window,data_dificil)
        elif event == 'Personalizado':
            DataMod(window,data_personalizada)
    window.close()
    return event

#PROGRAMA PRINCIPAL
if __name__ == "__main__":
    identificador_carpeta_error(Tabla)
