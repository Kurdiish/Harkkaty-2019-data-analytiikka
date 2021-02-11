######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä:Arash Niroumand
# Opiskelijanumero: 0543243
# Päivämäärä: 14.11.2019
# Yhteistyö ja lähteet, nimi ja yhteistyön muoto: opettajan opas ja assarit
# HUOM! KAIKKI KURSSIN TEHTÄVÄT OVAT HENKILÖKOHTAISIA!
######################################################################

import datetime
import sys

class Data: #luokka, jolla on jäsenmuuttujia ja ne käytetään olioiden kanssa
    
    pvm = ''
    paiste = 0
    havainto_asema = ''
    vuosi = 0
    nimi = ''

def valikko(): 
    
    print("Mitä haluat tehdä:")
    print("1) Anna havaintoasema ja vuosi")
    print("2) Lue säätilatiedosto")
    print("3) Analysoi päivittäiset säätilatiedot")
    print("4) Tallenna päivittäiset säätilatiedot")
    print("0) Lopeta")
    while True:
        try:
            valinta = int(input("Valintasi: "))
            break
        
        except ValueError:
            print("Anna valinta kokonaislukuna.")
    return valinta

def datan_asema_ja_vuosi(nimi):
    data = Data()
    
    try:    
        data.havainto_asema=input("Anna havaintoaseman nimi: ")
        data.vuosi=int(input("Anna analysoitava vuosi: "))
        return data
    
    except ValueError: # jos vuosiluku ei ole kokonaisluku, tämä viesti tulostuu
        print("Anna vuosiluku kokonaislukuna.")
    return None


def lue(lista,nimi): # lue funktio, jolla on kaksi parametria
    try:
        tnimi = nimi.havainto_asema + str(nimi.vuosi) + '.txt' # tiedoston nimi, vuosi ja '.txt' pääte 
        tiedosto = open(tnimi,"r") # avataan tiedosto luettavaksi
        lkm = 0		# alustetaan lukumäärä 0
        tiedosto.readline() # otsikko rivi luettu ja pois listasta
        lkm += 1 # rivi lukumäärä on nyt 1
        try:
            while True:
                
                rivit = tiedosto.readline() #luetaan rivi kerralla
                rivit = rivit[:-1]  #rivivaihtomerkki poistetaan
                lkm += 1 # jokaisen loopin jälkeen lisätään rivien määrä
                if (len(rivit) == 0): # kun kaikki rivit on luettu poistutaan loopista
                    break
                data=Data()
                rivit = rivit.split(";") # data splitataan puolipisteen kohdalla
                data.pvm=datetime.datetime.strptime(rivit[0],'%Y-%m-%d')# listan ensimmäisessä indeksissa on päivämäärät
                data.aika=datetime.datetime.strptime(rivit[1],'%H:%M') #tunti on listan toisessa indeksissa
                data.paiste=rivit[2] #paisteaika on listan 3. indeksissa
                lista.append(data)  # listassa on kaikki tiedoston sisältämät tiedot
                
            print("Tiedosto '{}' luettu. Tiedostossa oli {} riviä.".format(tnimi,lkm)) # tulostetaan luetun tiedostonnimi ja rivien lukumäärä
            tiedosto.close() # tiedosto suljetaan
            return lista	# palautetaan lista
        except OSError:
            print("Tiedoston '{}' lukeminen epäonnistui.".format(tnimi))
    
    except OSError: # poikeustenkäsittely
        print("Tiedoston '{}' avaaminen epäonnistui.".format(tnimi))# jos ei ole annettu tiedosto olemassa, printataan printissa oleva viesti
        sys.exit(0) # ja sitten poistutaan
        
    except AttributeError: # jos käyttäjä syöttää heti 2, tämä estää kaatumista
        print("Valitse havaintoasema ja vuosi ennen tiedostonlukua.")
        return lista
		
def analysoi(lista):
    
    if len(lista) == 0: # jos käyttäjä syöttää heti 3, tämä viesti estää kaatumista
        print("Lista on tyhjä. Lue ensin tiedosto.")
        return lista
    
    data=Data() #luodaan uusi olio
    summa = 0 #alustetaan summa
    lst=[]  # tyhjä lista päiväkohtainen ja summan tallentamiseen
    nykyinenPv = lista[0].pvm # päivämääräolio on listan indeksissä 0
    
    for i in lista: # kkäydään läpi listaa
        if nykyinenPv == i.pvm: #verrataan päivämäärät, jos ne on samapäivä
            summa += int(i.paiste) 
            
        else:
            data = Data() # luodaan uusi olio
            data.pv=nykyinenPv 
            data.paiste= summa #päiväkohtainen summa
            lst.append(data) #lisätään datat listaan
            nykyinenPv = i.pvm
            summa = int(i.paiste) # kun pv muuttuu summataan uuden pvn paisteajat
    data = Data() # luodaan uusi olio, toistetaan else:n sisällä oleva koodia jotta saadaan 31.12.2018 mukana
    data.pv=nykyinenPv 
    data.paiste= summa #päiväkohtainen summa
    lst.append(data)
	
    print("Data analysoitu ajalta {} - {}.".format(lista[0].pvm.strftime('%d.%m.%Y'),lista[-1].pvm.strftime('%d.%m.%Y'))) #päivämäärän muotoilu ja analysointi
    return lst # palautetaan llista

def tallenna(lista,data):
    
    if len(lista) == 0: # jos käyttäjä syöttää heti 4, tämä viesti tulostuu
        print("Lista on tyhjä. Analysoi data ennen tallennusta.")
        return lista
    
    try:
        nimi = input("Anna tulostiedoston nimi: ") #kysytään kirjoitettaban tiedoston niim
        tiedosto = open(nimi,"w")    #avataan tiedoston
        tiedosto.write('Pvm')

        for i in lista: #käydään lista läpi jossa on päivämäärät 
            tiedosto.write(';'+str(i.pv.strftime('%d.%m.%Y')))   # 
        tiedosto.write('\n')
        summa = 0
        
        tiedosto.write(data.havainto_asema) # kirjoitetaan havaintoasema tiedostoon
        for j in lista:
            summa += j.paiste # kumulaatiivinen summa
            tiedosto.write(';'+str(int(summa/60))) # kirjoitetaan kumSumma tiedostoon jaetaan 60:lla ja 
        tiedosto.write('\n')
        print("Paisteaika tallennettu tiedostoon '{}'.".format(nimi))
        tiedosto.close()
        
    except IOError:
         print("Tiedoston '{}' avaaminen epäonnistui.".format(nimi))
         sys.exit(0)
    return None
    
