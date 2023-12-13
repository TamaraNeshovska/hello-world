class Produkt: 
    def __init__(self, ime, seriski_broj, cena, tip, kolicina = None):
        self.ime = ime
        self.seriski_broj = seriski_broj
        self.cena = cena
        self.tip = tip 
        self.kolicina = kolicina
    
    def __str__(self):
        return (f"Produkt {self.ime}, Seriski broj: {self.seriski_broj}, Cena: {self.cena}, Tip: {self.tip}, Kolicina: {self.kolicina}")

class Prodavnica:
    def __init__(self, ime, seriski_broj):
        self.ime = ime
        self.seriski_broj = seriski_broj
        self.dostapni_produkti = []

    def dodaj_produkt(self, produkt:Produkt):
        #ovde sakam da napravam da mozam i ako sakam da ja smenam kolicinata na istiot produkt
        self.dostapni_produkti.extend([produkt.ime, produkt.kolicina])
        # self.dostapni_produkti.append(produkt)

    def pecati_produkti(self):
        print(self.dostapni_produkti)

    # def otstrani(self, produkt:Produkt): 
    #    pozicija = self.dostapni_produkti.find(produkt.ime)
    #    self.dostapni_produkti[pozicija+1] = produkt.kolicina - 1
       
    def __str__(self):
        return f"Prodavnica: {self.ime}, Seriski broj: {self.seriski_broj}"

class Kupuvac:
    def __init__(self, ime, prezime, dostapni_paricni_sredstva):
        self.ime = ime
        self.prezime = prezime
        self.dostapni_paricni_sredstva = dostapni_paricni_sredstva
        self.pazari = []
    
    def kosnica(self, produkt:Produkt, prodavnica:Prodavnica, kolicina:Produkt):
        if produkt.ime not in prodavnica.dostapni_produkti:
            print(f"Ne e dostapen ovoj proizvod {produkt.ime} momentalno")
        else:
            self.pazari.extend([produkt.ime, produkt.cena])
            if self.dostapni_paricni_sredstva >= produkt.cena:
                self.dostapni_paricni_sredstva = self.dostapni_paricni_sredstva - produkt.cena
                # prodavnica.otstrani(produkt)
                #TUKA SAKAV DA JA POVIKAM FUNKCIJATA OD GORE NO NE ZNAM KAKO DA GI POVRZAM DVETE 
                
            else:
                print(f"Nemate dovolno paricni sredstva za {produkt.ime}")


    def __str__(self):
        return (f"Kupuvac : {self.ime.title()} {self.prezime.title()}. Sostojba: {self.dostapni_paricni_sredstva} denari")
    

kupuvac1 = Kupuvac("tamara", "neshovska", 100)
print(kupuvac1)
kupuvac2 = Kupuvac("NekojKupuvac","SoNekoePrezime",500)
kupuvac3 = Kupuvac("magdalena", "Magdalenkoska", 3500)
kupuvac4 = Kupuvac("Andrej", "Andre", 300)

produkt_cia = Produkt("Cia", 1000, 50, "zdrava hrana", 10 )
print(produkt_cia)
produkt_mleko = Produkt("Mleko", 1001, 70, "mlecni proizvodi", 20)
produkt_malini = Produkt("Malini", 1002, 120, "ovosje", 15)
produkt_kaskaval = Produkt("Kaskaval",1003, 200, "mlecni proizvodi", 30)
produkt_morkovi = Produkt("Morkovi", 1004, 30, "zelencuk", 40)


prodavnica1 = Prodavnica("Tinex",1200)
print(prodavnica1)
prodavnica2 = Prodavnica("Kam",1202)

prodavnica1.dodaj_produkt(produkt_cia)
prodavnica1.dodaj_produkt(produkt_mleko)
prodavnica1.dodaj_produkt(produkt_malini)

prodavnica2.dodaj_produkt(produkt_morkovi)
prodavnica2.dodaj_produkt(produkt_mleko)
prodavnica2.dodaj_produkt(produkt_kaskaval)
print(prodavnica1.dostapni_produkti)
# prodavnica1.pecati_produkti()
# prodavnica2.pecati_produkti()

# prodavnica1.vo_kosnica(produkt_kaskaval)
# kupuvac1.kosnica(produkt_cia)
kupuvac1.kosnica( produkt_kaskaval, prodavnica1, 2)
kupuvac1.kosnica( produkt_malini, prodavnica1, 1)
kupuvac1.kosnica( produkt_mleko, prodavnica1, 3)
# prodavnica1.pecati_produkti()
print(kupuvac1.pazari)
print(kupuvac1.dostapni_paricni_sredstva)
