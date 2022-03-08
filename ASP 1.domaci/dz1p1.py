
def menu():
    print('     ___MENI___')
    print('1. dodavanje polinoma\n2. brisanje polinoma\n3. dodavanje clana\n4. brisanje clana\n5. stampanje polinoma\n6. sabiranje polinoma\n7. mnozenje polinoma\n8. prikaz svih polinoma\n9. izracuvanje vrednosti polinoma\n10. izlaz iz programa\n')
    print(' -------------------')
    n = int(input('Unesi broj opcije: '))
    print()
    return n
class Node:
    def __init__(self,coef = None,exp = None,next = None):
        self.exp = exp
        self.coef = coef
        self.next = next
class Header:
    def __init__(self,len = 0,first = None):
        self.len = len
        self.first = first

class Polynomial:
    def __init__(self,head = None,tail = None):
        self.head = head
        self.tail = tail
        self.header = Header()

    def append(self, coef, exp):
        new = Node(coef, exp)
        '''
        dodaje clanove na kraju
        '''
        if self.header.first is None:
            self.head = new
            self.tail = new
            self.head.next = self.tail
            self.tail.next = self.head
            self.header.first = self.head
            self.header.len += 1
            return
        self.tail.next = new
        self.tail = new
        self.tail.next = self.head
        self.header.len += 1
        return
    def print(self):
        pointer = self.head
        if pointer is None:
            print()
            return
        if pointer.coef == 1:
            print('x^{:-d}'.format(pointer.exp),end='')
        else:
            if float(pointer.coef).is_integer():
                print('{:-d}x^{:d}'.format(pointer.coef,pointer.exp),end='')
            else:
                print('{:-.2f}x^{:d}'.format(pointer.coef,pointer.exp),end='')

        pointer = pointer.next
        while pointer is not self.head:
            if pointer.exp == 1 or pointer.exp == -1:
                if float(pointer.coef).is_integer():
                    if pointer.coef == 1:
                        print('+x'.format(pointer.exp), end='')
                    elif pointer.coef == -1:
                        print('+x'.format(pointer.exp), end='')
                    else:
                        print('{:+d}x'.format(pointer.coef, pointer.exp),end='')

                else:
                    print('{:+.2f}x'.format(pointer.coef, pointer.exp),end='')

            elif pointer is not self.tail:
                if float(pointer.coef).is_integer():
                    if pointer.coef == 1:
                        print('+x^{:d}'.format(pointer.exp), end='')
                    elif pointer.coef == -1:
                        print('+x^{:d}'.format(pointer.exp), end='')
                    else:
                        print('{:+d}x^{:d}'.format(pointer.coef, pointer.exp),end='')

                else:
                    print('{:+.2f}x^{:d}'.format(pointer.coef, pointer.exp),end='')
            else:
                if float(pointer.coef).is_integer():
                    print('{:+d}'.format(pointer.coef),end='')
                else:
                    print('{:+.2f}'.format(pointer.coef),end='')
            pointer = pointer.next
        print()

    def len(self):
        pointer = self.head
        if pointer is None:
            return 0
        if pointer == self.tail:
            return 1
        pointer = pointer.next
        counter = 1
        while pointer is not self.head:
            pointer = pointer.next
            counter += 1
        return counter

    def cal(self,var):
        pointer = self.head
        if pointer is None:
            return 0
        value = pointer.coef * (var**pointer.exp)
        pointer = pointer.next
        while pointer is not self.head:
            value += pointer.coef * (var**pointer.exp)
            pointer = pointer.next
        return value
    def search(self,exponent):
        pointer = self.head
        if self.header.first is None:
            return False
        if exponent > pointer.exp:
            return False
        if pointer.exp == exponent:
            return True
        pointer = pointer.next
        while pointer is not self.head:
            if pointer.exp == exponent:
                return True
            pointer = pointer.next
        return False

    def add(self,coefi,exponent):
        pointer = self.head
        new = Node(coefi, exponent)
        if self.search(exponent) is False:
            if exponent > self.head.exp:
                '''
                dodavanje na pocetak
                '''
                new.next = self.head
                self.head = new
                self.tail.next = new
                self.header.first = self.head
            elif exponent < self.tail.exp:
                '''
                dodavanje na kraj
                '''
                self.append(coefi,exponent)
            else:
                '''
                dodavanje na ostalim mestima
                '''
                while pointer.next.exp > exponent:
                    pointer = pointer.next
                new.next = pointer.next
                pointer.next = new
            self.header.len += 1
        else:
            while True:
                if pointer.exp == exponent:
                    pointer.coef = pointer.coef + coefi
                    break
                pointer = pointer.next

    def delete(self, exponent):
        if self.search(exponent) is False:
            print('Izabrani eksponent ne postoji u polinomu')
            return None
        pointer = self.head
        if self.header.len == 1:
            self.header.first = None
            self.head = None
            self.tail = None
            self.header.len = 0
            return
        if exponent == pointer.exp:
            '''
            brisanje na pocetku
            '''
            self.head = self.head.next
            self.tail.next = self.head
            self.header.first = self.head
        elif exponent == self.tail.exp:
            '''
            brisanje na kraju
            '''
            while pointer.next is not self.tail:
                pointer = pointer.next
            self.tail = pointer
            pointer.next = self.head

        else:
            '''
            brisanje na ostalim mestima
            '''
            while pointer.next.exp is not exponent:
                pointer = pointer.next
            pointer.next = pointer.next.next
        self.header.len -= 1

    def additionPolynomial(self,polynomial2):
        new_polynomial = Polynomial()
        first_pointer = self.head
        second_pointer = polynomial2.head
        while first_pointer.next is not self.head or second_pointer.next is not polynomial2.head:
            if first_pointer.exp > second_pointer.exp:
                new_polynomial.append(first_pointer.coef, first_pointer.exp)
                first_pointer = first_pointer.next
            elif first_pointer.exp < second_pointer.exp:
                new_polynomial.append(second_pointer.coef, second_pointer.exp)
                second_pointer = second_pointer.next
            else:
                new_polynomial.append(first_pointer.coef + second_pointer.coef, first_pointer.exp)
                first_pointer = first_pointer.next
                second_pointer = second_pointer.next

        if first_pointer.next is self.head and second_pointer.next is polynomial2.head:
            if first_pointer.exp == second_pointer.exp:
                new_polynomial.append(second_pointer.coef+first_pointer.coef, second_pointer.exp)
            elif first_pointer.exp > second_pointer.exp:
                new_polynomial.append(first_pointer.coef,first_pointer.exp)
                new_polynomial.append(second_pointer.coef,second_pointer.exp)
            elif first_pointer.exp < second_pointer.exp:
                new_polynomial.append(second_pointer.coef,second_pointer.exp)
                new_polynomial.append(first_pointer.coef,first_pointer.exp)
        elif second_pointer.next is polynomial2.head:
            while first_pointer is not self.head:
                new_polynomial.append(first_pointer.coef, first_pointer.exp)
                first_pointer = first_pointer.next
        elif first_pointer.next is self.head:
            while second_pointer is not polynomial2.head:
                new_polynomial.append(second_pointer.coef,second_pointer.exp)
                second_pointer = second_pointer.next

        new_polynomial.header.first = new_polynomial.head
        new_polynomial.header.len = new_polynomial.len()

        return new_polynomial

    def sort(self):
        pointer = self.head
        if pointer is None:
            return None
        if pointer.next.exp > pointer.exp:
            pointer.coef , pointer.exp , pointer.next.coef, pointer.next.exp = pointer.next.coef, pointer.next.exp,pointer.coef,pointer.exp
        pointer = pointer.next
        while pointer is not self.tail:
            temp = pointer.next
            while temp is not self.head:
                if temp.exp > pointer.exp:
                    pointer.coef, pointer.exp, temp.coef, temp.exp = temp.coef, temp.exp, pointer.coef, pointer.exp
                temp = temp.next
            pointer = pointer.next
        self.print()

    def mulPolynomial(self,polynomial2):
        first_pointers = self.head
        second_pointers = polynomial2.head
        new_polynomial = Polynomial()
        t = 0
        s = 0
        while True:
            if first_pointers is self.head:
                t += 1
            if t>1: break
            while True:
                if second_pointers is polynomial2.head:
                    s += 1
                if s > 1: break
                new_polynomial.append( first_pointers.coef * second_pointers.coef, first_pointers.exp + second_pointers.exp)
                new_polynomial.header.len += 1
                second_pointers = second_pointers.next
            second_pointers = polynomial2.head
            s = 0
            first_pointers = first_pointers.next

        first_pointers = new_polynomial.head
        t = 0

        while True:
            if first_pointers is new_polynomial.head:
                t += 1
            if t > 1: break
            second_pointers = first_pointers

            while second_pointers.next is not first_pointers:
                if first_pointers.exp == second_pointers.next.exp:
                    first_pointers.coef = first_pointers.coef + second_pointers.next.coef
                    second_pointers.next = second_pointers.next.next
                    new_polynomial.header.len += (-1)
                second_pointers = second_pointers.next
            first_pointers = first_pointers.next


        new_polynomial.header.first = new_polynomial.head
        new_polynomial.header.len = new_polynomial.len()
        new_polynomial.sort()
        #new_polynomial.print()

        return new_polynomial

def printAll(listofPolynomials):
    print()
    print('Polinomi: ')
    print()
    for index,polynomial in enumerate(listofPolynomials):
        print(index + 1,'.',sep = '',end = ' ')
        polynomial.print()
        print()

def addPolynomial():
    polynomial = Polynomial()
    n = int(input('Unesite red polinoma: '))
    for i in range(n,-1,-1):
        coef,exp = input('Unesite koeficijent i stepen clana: ').split()
        coef = int(coef)
        exp = int(exp)
        if coef == 0: continue
        polynomial.append(coef,exp)
    return polynomial

polinomi = []
while True:
    try:
        n = menu()

        if n ==1:
            '''
            dodavanje polinoma
            '''
            polinomi.append(addPolynomial())
            printAll(polinomi)
            print()

        elif n==2:
            '''
            brisanje polinoma
            '''
            printAll(polinomi)
            if len(polinomi) == 0: print('Ne postoji ni jedan polinom!'); continue
            k = int(input('Unesi koji polinom hocete da obrisete: '))

            if k > len(polinomi):
                print('Pogresno unet polinom! ')
                continue
            polinomi.pop(k-1)
            print('Uspesno obrisan polinom!')

        elif n==3:
            '''
            dodavanje clana u nekom polinomu
            '''
            if len(polinomi)==0:
                print('Nema unetih polinoma! ')
                continue
            printAll(polinomi)
            k = int(input('Izaberite polinom: '))
            if k> len(polinomi):
                print('Pogresno unet polinom!')
                continue
            coef,exp = input('Unesite koeficijent i eksponent koji zelite da dodate u polinomu: ').split()
            coef,exp = int(coef),int(exp)
            polinomi[k-1].add(coef,exp)
            print('Uspesno ste dodali clan!')
            print()

        elif n==4:
            '''
            brisanje clana u nekom polinomu
            '''
            if len(polinomi)==0:
                print('Nema unetih polinoma')
                continue
            printAll(polinomi)
            k = int(input('Izaberite polinom: '))
            if k> len(polinomi):
                print('Pogresno unet polinom')
                continue
            exp = int(input('Unesite koji eksponent zelite da obrisete'))
            polinomi[k-1].delete(exp)
            print()
            print('Uspesno ste obrisali eksponent')
            print()

        elif n==5:
            '''
            stampanje nekog polinoma
            '''
            k = int(input('Unesite redni broj polinoma koji hocete da stampate: '))
            if k > len(polinomi):
                print('Pogresno unet redni broj polinoma')
                continue
            polinomi[k-1].print()
            print()
        elif n==6:
            '''
            sabiranje polinoma
            '''
            printAll(polinomi)
            k1,k2 = input('Izaberite dva polinoma: ').split()
            k1, k2 = int(k1),int(k2)
            if k1 > len(polinomi) or k2 >len(polinomi) or k1 <=0 or k2<=0:
                print('Pogresno unet polinom!')
                continue
            polinomi.append(polinomi[k1-1].additionPolynomial(polinomi[k2-1]))
            polinomi[-1].print()
            print()
        elif n==7:
            printAll(polinomi)
            k1,k2 = input('Izaberite dva polinoma: ').split()
            k1, k2 = int(k1),int(k2)
            if k1 > len(polinomi) or k2 >len(polinomi) or k1 <=0 or k2<=0:
                print('Pogresno unet polinom!')
                continue
            polinomi.append(polinomi[k1-1].mulPolynomial(polinomi[k2-1]))
            print()
        elif n==8:
            printAll(polinomi)
        elif n == 9:
            '''
            izracuvanje vrednosti
            '''
            if len(polinomi)==0:
                print("Nema unetih polinoma")
                continue
            printAll(polinomi)
            k = int(input("Izaberite polinom: "))
            x = int(input("Unesite promenljivu x: "))
            print('Vrednost polinoma za promenljivu {} je {}'.format(x,polinomi[k-1].cal(x) ))
            print()

        elif n == 10:
            '''
            izlaz iz programa
            '''
            break
        else:
            print('Pogresno uneta opcija')

    except ValueError:
        print('Pogresno unete vrednosti!\n')
        continue

    except IndexError:
        print('Pogresno unet polinom! ')
        continue