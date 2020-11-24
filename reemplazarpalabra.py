class phrase:
    def __init__(self,cadena):
        self.cadena = cadena
    
    def buscar(self, search):
        newlist = self.cadena.split()
        state = False
        pos = 0
        for word in newlist:
            if word.lower() == search.lower():
                state = True
                break
            pos += 1
        if state == False:
            pos = None
        return pos
    
    def reemplazar(self, palabra):
        pos = self.buscar(input("Qué palabra quiere reemplazar?: "))
        if pos == None:
            print("no se encontraron resultados")
            return 
        newlist = self.cadena.split()
        newlist[pos] = palabra
        newcadena = ""
        for word in newlist:
           newcadena+=(" "+word)
        print(newcadena) 

test = phrase(input("Escriba una frase: "))
test.reemplazar(input("Qué palabra quiere poner: "))