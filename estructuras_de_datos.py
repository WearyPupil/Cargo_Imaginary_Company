class ArrayStack:
    """Implemetación LIFO de una pila,
    usando una lista de Python como almacenamiento."""

    def __init__(self):
        """Crear un stack vacío."""
        self._data = list();

    def __len__(self):
        """Devuelve el número de elementos en la pila."""
        return len(self._data);

    def __str__(self):

        return "[" + str(len(self._data)) + "]"

    def is_empty(self):
        """Devuelve True si la pila está vacía."""
        return len(self._data) == 0;

    def push(self, elemento):
        """Agrega el elemento a lo más alto de la pila."""
        self._data.append(elemento);

    def top(self):
        """Devuelve, mas no regresa el elemento más alto de la pila.
        Genera una excepción si la pila está vacía."""
        if self.is_empty():
            raise Empty('La pila está vacía');
        return self._data[-1];

    def pop(self):
        """Devuelve y regresa el elemento más alto de la pila, es decir LIFO.
        Se genera una excepción si la pila está vacía."""
        if self.is_empty():
            raise Empty('La pila está vacía');
        return self._data.pop();

class ArrayQueue:
    """Implemetación FIFO de una cola usando una lista de Python
    como almacenamiento."""
    def __init__(self):
        """Crear una cola vacía."""
        self._data = list();

    def __len__(self):
        """Devuelve el número de elementos en la cola."""
        return len(self._data);

    def __str__(self):
        """Imprime el número de elementos en la cola con el formato {x}"""
        return "{" + str(self._size) + "}"

    def is_empty(self):
        """Devuelve True si la cola está vacía."""
        return len(self._data) == 0;

    def first(self):
        """Devuelve, pero no remueve el elemento en el frente de la cola
        Genera una excepción si la cola está vacía."""
        if self.is_empty():
            raise Empty('Queue is empty');
        return self._data[0];

    def dequeue(self):
        """Remueve y devuelve el primer elemento de la cola, es decir FIFO
        Genera una excepción si la cola está vacía."""
        if self.is_empty():
            raise Empty('Queue is empty');
        answer = self._data.pop(0);
        return answer;

    def enqueue(self, elemento):
        """Agrega un elemento al final de la cola."""
        self._data.append(elemento);
