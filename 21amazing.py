class tweentyone:

    def __init__(self):
        self.number = []
        self.compund = []
        self.lucky = []
        self.block = []
        self.fibonacci = []
        self.start()

    def pullNumber(self):
        for i in range(21):
            self.number.append(i+1)

    def compundNumber(self):
        for i in self.number:
            # Para que empiece de 2
            num=i+1 
            divisores = 0
            # Obtener los divisores de cada numero
            for d in range(num):
                check = num % (d+1)
                if check == 0:
                    divisores+=1
            if divisores > 2:
                self.compund.append(num)
                divisores = 0

    def compundNumberShow(self):
        pos = 0
        for n in self.compund:
            pos+=1
            if n == 21:
                print("\n {}) {} \n".format(pos,n))
            else:
                print("{}) {}".format(pos,n))

    def pullFibonacci(self):
        a=1
        b=0
        for i in range(10):
            c = a +b
            a = b
            b = c
            self.fibonacci.append(c)

    def delMulnumber(self,delete,blockmul):
        block = []
        for i in range(len(blockmul)):
            pos = i+1
            if pos % delete == 0:
                if i == len(blockmul):
                    break
            else:
                block.append(blockmul[i])
        return block

    def luckyNumber(self,numbers):
        block = numbers.copy()
        first = self.delMulnumber(block[self.fibonacci[0]],block.copy())
        second = self.delMulnumber(first[self.fibonacci[1]],first.copy())
        three = self.delMulnumber(second[self.fibonacci[2]],second.copy())
        self.lucky.extend([first,second,three])

    def start(self):
        self.pullNumber()
        self.compundNumber()
        print("\n{} Is a compund number {}\n{}\n{}".format('-'*15,'-'*15,self.compund,'-'*50))
        print("\nIf we invert the digits of 21 , we will realize that the result is same position that it occupies\n")
        self.compundNumberShow()
        self.pullFibonacci()
        self.luckyNumber(self.number)
        print("\n{} Is also a lucky number {}\n{}\n{}".format('-'*15,'-'*15,self.lucky[2],'-'*55))
        print("Sifting process to get the lucky number\n{}".format(self.number))
        print("First we eliminate the integers\n{}".format(self.lucky[0]))
        print("Since the 3 survived, we eliminate its multiples in places \n{}".format(self.lucky[1]))
        print("Now since 7 survived, you also remove its multiples in places\n{}".format(self.lucky[2]))

if __name__ == "__main__":
    print("Let me show you, because 21 is an amazing number")
    response = input("Continue? (y/n): ")
    if response == 'y':
        vone = tweentyone()
        print("{} I told you, the number 21 is amazing {}".format('-'*5,'-'*5))
    else:
        print("You don't know what you're missing")