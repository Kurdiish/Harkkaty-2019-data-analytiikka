import HT

def paaohjelma():
    
    
    nimi=''
    lista=[] 
    lista_kum=[]
    rivit=''
    
    while True:
        
        toiminto = HT.valikko() 
        if toiminto == 0:
            print("Kiitos ohjelman käytöstä.")
            break
        if toiminto == 1:
            nimi = HT.datan_asema_ja_vuosi(nimi)
        elif toiminto == 2:
            lista_kum=HT.lue(lista,nimi)
                
        elif toiminto == 3:
            rivit=HT.analysoi(lista_kum)

        elif toiminto == 4:
            HT.tallenna(rivit,nimi)
                
        else:
            print("Valintaa ei tunnistettu, yritä uudestaan.")
                
        print()
        
    return None
        
paaohjelma()
