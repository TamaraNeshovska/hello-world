"""Zad1 """

class Employee:
    """
    Klasa za vraboteni.
    """
   
    def __init__(self, first_name:str, last_name:str, email:str, position:None, company:None, salary=None):
        """
        Inicijalizirame objekt od klasata Employee.
        :param first_name:str, ime 
        :param last_name:str, prezime 
        :param email:str, email
        :param position:str, pozicija vo kompanijata
        :param company:str, kompanija 
        :param salary: int, plata 
        """
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.position = position
        self.company = company 
        self.salary = salary 
        self.request = None
   
       #Ne znam kako da napravam od edna kompanija da se stavaat vo edna lista site vraboteni za da mozam da najdam sredna vrednost od platite

      
    def request_for_work(self, request):
        self.request = request
        print(f"Ponuda za rabota za {self.first_name} za pozicija {self.request}")
    
    def prifati(self, company, position, salary):
        if self.request:
            print(f"{self.first_name} ja prifakja ponudata {self.request}")
            self.company = company
            self.position = position 
            self.salary = salary
            self.request = None
        else:
            print("Nemate ponuda za rabota")

    def odbi(self):
        if self.request:
            print(f"{self.first_name} ja odbiva ponudata za rabota {self.request}")
            self.request = None
        else:
            print("Nemate ponuda za da ja odbiete :)")  
  
    def podnesuvanje_otkaz(self, den:str):
        self.den = den
        print(f"{self.first_name} uspesno podnese otkaz na den {self.den}")
    
         

class Company:
    """
    Klasa za kompanija.
    """
    def __init__(self, name:str, company_id:int, address:str ):
        """
        Inicijalizirame objekt od klasata Company.
        :param name: str, ime na kompanijata
        :param company_id: int, unikaten broj za edna kompanija 
        """
        self.name = name 
        self.company_id = company_id
        self.address = address 
        self.vraboteni = []
    
    def hire(self, employee: Employee, position:str, salary:int):
        """
        """
        # if not isinstance(employee,Employee):
        #     raise Exception(f"Kompanijata ne moze da vrati employee sto ne e od podatocen tip Employee.")
        # print(f"{self.name} go vrabotuva {employee.first_name}")
        employee.position = position
        employee.salary = salary 
        self.vraboteni.append(employee)
        
    def ponuda_za_rabota(self, employee: Employee, request:str):
        self.request = request
        employee.request_for_work(self.request)
        print(f"Ponuda za rabota ispratena na {employee.email} za pozicija {self.request}")
    

    


semos_mk = Company("Semos Makedonija", 1234,"adresa")
ime1 = Employee("Ime1", "Prezime1", "ime1@ime1.com", "developer","semos_mk")

# print(ime1.position, ime1.salary)
# semos_mk.hire(ime1,"support", 100000)
# print(ime1.position, ime1.salary)
semos_mk.ponuda_za_rabota(ime1,"DATA")
ime1.prifati("Semos Makedonija","Data", 100)
ime1.podnesuvanje_otkaz("24.10.2023")

# Da se napravat 2 instanci od klasata Company i 3 instanci od klasata Employee.
company1 = Company("ParametarsTracker", 1000, "st.Makedonija")
company2 = Company("AdAstra",10123,"st.Goce Delcev no. 26/b")

ime1 = Employee("Tamara","Neshovska", "tamara.neshovska@yahoo.com","assistant","AdAstra",10)
ime2 = Employee("Marija", "Jovkovska", "marija2020@gmail.com", "supervisor", "ParametarTracker",20)
ime3 = Employee("Nikita", "Nikitovski", "nikita123@outlook.com", "consultant", "ParametarTracker",20)

# zadaca 2
# Da se napravi sporedba za prosecnite salary costs za sekoja kompanija.
