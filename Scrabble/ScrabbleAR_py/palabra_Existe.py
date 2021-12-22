from pattern.es import spelling,lexicon,parse

Tipo= {'adj':["AO", "JJ","AQ","DI","DT"],
'sus':["NC", "NCS","NCP", "NNS","NP", "NNP","W"],#Borre el sus "NN" para que ande , sino , valida toda palabra  inexistente como "sus"
'verb':[ "VAG", "VBG", "VAI","VAN", "MD", "VAS" , "VMG" , "VMI", "VB", "VMM" ,"VMN" , "VMP", "VBN","VMS","VSG", "VSI","VSN", "VSP","VSS" ]
}
def verificar_Facil(palabra,existe):
    '''Para Facil ,Recibe una palabra , si existe(cumple con las condiciones) retorna Verdadero , sino retorna Falso'''
    if (palabra in spelling.keys() or palabra in lexicon.keys()):
        existe=True
    else:
        existe=False
    return(existe)
def verificar_Medio(palabra,existe):
    '''Para medio ,Recibe una palabra , si existe(cumple con las condiciones) retorna Verdadero , sino retorna Falso'''
    if palabra in spelling.keys() and palabra in lexicon.keys(): #Dificultad -> Medio(Sea adjetivo o verbo)
        if(parse(palabra).split("/")[1] in Tipo['verb']):
            existe=True
        elif(parse(palabra).split("/")[1] in Tipo['adj']):
            existe=True
        else:
            existe=False
    else:
        existe=False
    return(existe)
def verificar_Dificil_Personalizado(palabra,existe,Dificil_elegido):
    '''Para Dificil y Personalizado ,Recibe una palabra , si existe(cumple con las condiciones) retorna Verdadero , sino retorna Falso'''
    if palabra in spelling.keys() and palabra in lexicon.keys():
        for x in range(len(Dificil_elegido)):
            if(parse(palabra).split("/")[1] in Tipo[Dificil_elegido[x]]):
                existe=True
    else:
        existe=False
    return(existe)

def verificar_Palabra(palabra,dificultad,Dificil_elegido):
    '''Recibe una palabra , una dificiltad y para Dificil y Personalizado una lista de tipos de palabra y si la palabra es valida con las condiciones dadas
       retorna Verdadero , de lo contrario retorna Falso'''
    existe=False
    palabra=palabra.lower()
    if(len(palabra)>=2):
        if (dificultad=="Facil"):
            existe=verificar_Facil(palabra,existe)or verificar_Facil(palabra.upper(),existe)
        elif(dificultad=="Medio"):
            existe=verificar_Medio(palabra,existe) or verificar_Medio(palabra.upper(),existe)
        elif((dificultad=="Dificil") or (dificultad=="Personalizado")):
            existe=verificar_Dificil_Personalizado(palabra,existe,Dificil_elegido) or verificar_Dificil_Personalizado(palabra.upper(),existe,Dificil_elegido)
    return(existe)
 #---------Porgrama Principal---
if __name__ == '__main__':
    print(verificar_Palabra("FE","Facil",["sus","adj","verb"]))
