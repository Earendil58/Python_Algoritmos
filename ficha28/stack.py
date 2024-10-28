class Stack:
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def is_empty(self):
        longitud_pila = len(self.items)
        return longitud_pila == 0

    def peek(self):
        x = None
        if not self.is_empty():
            frente = -1
            x = self.items[frente]
        return x

    def push(self,x):
        self.items.append(x)

    def pop(self):
        x = None
        if not self.is_empty():
            frente = -1
            x = self.items[frente]
            del self.items[frente]
        return x



def main():
    pila = Stack()
    pila.push(5)
    pila.push(7)
    pila.push(2)
    pila.push(4)

    print(f'Estado actual de la pila: {pila}')

    elemento_removido = pila.pop()
    print(f'Elemento removido de la pila: {elemento_removido}')
    print(f'Nuevo estado de la pila: {pila}')

    ultimo_elemento = pila.peek()
    print(f'El último elemento de la pila es: {ultimo_elemento}')


if __name__ == '__main__':
    main()





