class polinomio:
    def __init__(self):
        self.ecuacion =[]
        self.praices = []
        self.n=0

    def completar(self, n):
        self.n = n
        for i in range(n+1):
            self.ecuacion.append(int(input("Ingrese el valor del coeficiente de grado {}: ".format(n-i))))
    
    def divisores(self):
        Dn = []#DIvisores del último coeficiente
        Dcp = []#Divisores del coeficiente con mayor grado
        divtotale = []
        n = self.ecuacion[self.n]
        for i in range(1,abs(n)+1):
            if abs(n) % i == 0:
                Dn.append(i)
        cp = self.ecuacion[0]
        for i in range(1,abs(cp)+1):
            if abs(cp) % i == 0:
                Dcp.append(i)
        for i in Dcp:
            for j in Dn:
                if j % i == 0:
                    divtotale.append(j)
        return divtotale

    def obtener(self):
        divisores = self.divisores()
        d = 0
        for ps in divisores:
            i = 0
            for e in self.ecuacion:
                if i == 0:
                    d = e
                else:
                    d = e+(ps*d)
                i+=1
            if d == 0:
                self.praices.append(ps*(-1))
            else:
                i = 0
                for e in self.ecuacion:
                    if i == 0:
                        d = e
                    else:
                        d = e-(ps*d)
                    i+=1
                if d == 0:
                    self.praices.append(ps)

    def imprimir(self):
        j = 0
        Secuacion = ""
        for i in  self.ecuacion:
            Secuacion += "{}x{}\t".format(i,self.unicode_exp((self.n)-j))
            j+=1
        print(Secuacion)
        for i in self.praices:
            if i >= 0:
                print("(x+{})".format(i))
            else:
                print("(x{})".format(i))

    def unicode_exp(self,exp):
        if exp == 1:
            return chr(0xB9)
        if exp == 2 or exp == 3:
            return chr(0xB0 + exp)
        else:
            return chr(0x2070 + exp)
               

pol  = polinomio()
pol.completar(int(input("Ingrese el grado del polinomio: ")))
pol.obtener()
pol.imprimir()