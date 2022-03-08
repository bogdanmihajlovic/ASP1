import random
def menu():
    print('\n1. Simulacija upisa studenata\n2. Provera da li je red pun\n3. Provera da li je red prazan\n4. Dodavanje studenata u listu\n5. Kraj programa\n')
    n = int(input('Unesite broj opcije: '))
    return n
def addToList():
    print('Unosite studente koji zelite da se upisu.')
    print('Unesite STOP kada zelite da prekinete unos\n')

    while True:
        info = unos()
        if info is False:
            break
        try:
            ime, prezime, brind, smer, godina = info[0], info[1], int(info[2]), info[3], int(info[4])
            lista_studenata.addStudent(ime, prezime, brind, smer, godina)
        except ValueError:
            print('Pogresno uneti podaci pokusajte ponovo: ')
            continue
        except IndexError:
            print('Pogresno uneti podaci')
            continue

def unos():

    info = input('Unesite ime, prezime, broj indeksa(ggbbbb), smer i godinu studenta: ')
    if info == 'stop' or info == 'Stop' or info == 'STOP':
        return False
    else: lista = info.split(', ')
    #ime, prezime, brind, smer, godina = info[0], info[1], int(info[2]), info[3], int(info[4])
    return lista

class Node:
    def __init__(self , ime = None, prezime = None, brindeksa = None, smer = None, godina = None, next = None):
        self.ime = ime
        self.prezime = prezime
        self.brindeksa = brindeksa
        self.smer = smer
        self.godina = godina
        self.next = next
class Header:
    def __init__(self,len = 0,first = None):
        self.len = len
        self.first = first

class Queue:
    def __init__(self,front = None,rear = None,len = 0):
        self.front = front
        self.rear = rear
        self.limit = 100
        self.header = Header()

    def add(self,student):
        self.header.len += 1
        if self.front is None:
            self.front = student
            self.rear = student
            self.front.next = self.rear
            self.rear.next = self.front
            self.header.first = self.front
            return

        self.rear.next = student
        self.rear = student
        self.rear.next = self.front

    def delete(self):
        if self.front is None:
            print('Red je prazan')
            return

        if self.header.len == 1:
            self.rear = None
            self.front = None
            self.header.len =- 0
            self.header.first = None
            return
        self.front = self.front.next
        self.rear.next = self.front
        self.header.first = self.front
        self.header.len -= 1

    def checkFull(self):
        if self.header.len >= self.limit:
            return True
        else:
            return False
    def checkEmpty(self):
        if self.header.len == 0:
            return True
        else:
            return False


class CirlularList:

    def __init__(self,head = None,tail = None,numEl = 0):
        self.head = head
        self.tail = tail
        self.numEl = numEl
        self.header = Header()

    def print(self):
        if self.head is None:
            print()
            return
        pointer = self.head
        while pointer.next is not self.head:
            print('{} {}'.format(pointer.ime,pointer.prezime))
            pointer = pointer.next
        print('{} {}'.format(pointer.ime,pointer.prezime))
        return


    def addStudent(self,ime,prezime,indeks,smer,godina):
        new_student = Node(ime,prezime,indeks,smer,godina)
        if self.header.len == 0:
            self.head = new_student
            self.tail = new_student
            self.tail.next = self.head
            self.head.next = self.tail
            self.header.first = self.head
            self.header.len += 1
            return
        self.tail.next = new_student
        self.tail = new_student
        self.tail.next = self.head
        self.header.len += 1
        return

    def pop(self,index):
        if self.header.len == 0:
            print('Nema studenata u listi')
            return None
        if self.header.len == 1:
            self.head = None
            self.tail = None
            self.header.first = None
            self.header.len = 0
            return
        if index == 0:
            self.head = self.head.next
            self.tail.next = self.head
            self.header.len -= 1
            self.header.first = self.head
            return

        elif index == self.header.len - 1 and self.header.len != 1 :
            pointer = self.head
            while pointer.next is not self.tail:
                pointer = pointer.next
            self.tail = pointer
            self.tail.next = self.head
            self.heaer.len -= 1
            return

        else:
            counter = 0
            pointer = self.head
            while counter + 1 != index:
                pointer = pointer.next
                counter += 1
            pointer.next = pointer.next.next
            self.header.len -= 1
            return


    def search(self,index):
        if index >= self.header.len or index < 0 :
            print("Out of range")
            return
        if index == 0: return self.head
        elif index == self.header.len - 1 : return self.tail
        counter = 1
        pointer = self.head.next
        while counter != index:
            pointer = pointer.next
            counter += 1
        return pointer

lista_studenata = CirlularList()
addToList()
brSt = lista_studenata.header.len
if brSt == 1:
    print('Dodat je 1 student')
elif brSt > 1:
    print('Dodato je {} studenta'.format(brSt))
else:
    print('Nije dodat ni jedan student')

queue = Queue()

while True:
    try:
        #brSt = lista_studenata.header.len
        opcija = menu()
        if opcija == 1:
            if lista_studenata.header.len == 0: print("Nema unetih studenata u listu"); continue
            brojOperacija = 0
            #dodavanje u red iz liste
            while lista_studenata.header.len != 1:
                redniBroj = random.randrange(1,lista_studenata.header.len,1)
                student = lista_studenata.search(redniBroj-1)
                new = Node(student.ime,student.prezime,student.brindeksa,student.smer,student.godina)
                queue.add(new)
                print('Student {} {}, {} je dodat u red'.format(student.ime,student.prezime,student.brindeksa,student.smer,student.godina))
                lista_studenata.pop(redniBroj-1)

            student = lista_studenata.search(0)
            queue.add(student)
            lista_studenata.pop(0)
            print('Student {} {}, {} je dodat u red'.format(student.ime, student.prezime, student.brindeksa, student.smer,student.godina))
            print()
            #upis studenata
            while queue.header.len != 0:
                broj = random.random()
                if broj <= 0.5:
                    #student sa fronta ide na rear
                    #zapamti prvog
                    new = queue.front
                    queue.delete()
                    queue.add(new)
                    #obrises ga
                    #stavis ga na kraj reda
                    pass
                else:
                    #student se upisuje
                    print('Upisan je student: {} {} {} {} {}'.format(queue.front.ime, queue.front.prezime, queue.front.brindeksa, queue.front.smer, queue.front.godina+1))
                    #zapamtis mu informacije
                    #obrises ga sa fronta
                    queue.delete()
                    pass
                brojOperacija += 1
            print()
            print('Izvrseno je',brojOperacija,'operacija')
        elif opcija == 2:
            if queue.checkFull():
                print("Red je pun")
            else:
                print("Red nije pun")
        elif opcija == 3:
            if queue.checkEmpty():
                print("Red je prazan")
            else:
                print("Red nije prazan")
        elif opcija == 4:
            addToList()
        elif opcija == 5:
            break
        else:
            print("Pogresno uneta opcija!")
    except ValueError:
        print("Pogresno uneta opcija!")
        continue



