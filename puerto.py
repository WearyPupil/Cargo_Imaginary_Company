from estructuras_de_datos import ArrayStack;
from estructuras_de_datos import ArrayQueue;

class Puerto:
    """Modelado del problema planteado."""
    # Constantes del problema
    MAX_CONTENEDORES = 990;
    MAX_AUTOS = 371;
    MAX_PILAS = 200;
    MAX_COLAS = 25;

    class _Cuaderno:
        """Clase liviana perteneciente a puerto para anotar la posición de
        los seriales para pilas y colas."""

        def __init__(self):
            """Crear un arreglo dinmámico para guardar los datos"""
            self._posiciones = list();

        def _agregar(self, elemento, altura, estructura):
            """Agregar un serial y su posición al cuaderno"""
            self._posiciones.append([elemento, altura, estructura]);

        def _quitar(self, elemento):
            """Eliminar un serial del cuaderno"""
            self._posiciones.remove(elemento);

        def _ordenar(self):
            """Ordenar el cuaderno"""
            self._posiciones = sorted(self._posiciones);

        def _buscar(self, elemento):
            """Implemetación de Búsqueda binaria para seriales"""
            low = 0;
            high = len(self._posiciones)-1;
            while low <= high:
                mid = (low + high) // 2;
                if elemento == self._posiciones[mid][0]:
                    return self._posiciones[mid];
                elif elemento < self._posiciones[mid][0]:
                    high = mid - 1;
                else:
                    low = mid + 1;
            return False;

        def _mostrar(self):
            """Mostrar los datos almacenados en el cuaderno"""
            print(self._posiciones);

    def __init__(self):
        """Iniciar datos del puerto"""
        self.pila_conte = [ArrayStack() for i in range(Puerto.MAX_CONTENEDORES)]
        self.cola_auto = [ArrayQueue() for i in range(Puerto.MAX_COLAS)];
        self.contenedores = 0
        self.autos = 0;
        self.puntero_pilas = 0;
        self.puntero_colas = 0;
        self.cuaderno_pilas = Puerto._Cuaderno();
        self.cuaderno_colas = Puerto._Cuaderno();

    def apilar(self, elemento):
        """Apilar un contenedor"""
        self.cuaderno_pilas._ordenar();
        if self.cuaderno_pilas._buscar(elemento):
            print('Ya existe ese serial en los contenedores');
            return None;

        if self.contenedores == Puerto.MAX_CONTENEDORES:
            print('Se ha llegado al 99% de ocupación');
            print('No se puede agregar mas contenedores');
            return None;

        while len(self.pila_conte[self.puntero_pilas]) == 5:
            self.puntero_pilas += 1;
        self.pila_conte[self.puntero_pilas].push(elemento);
        self.contenedores += 1;
        # Agregar al cuaderno
        altura = len(self.pila_conte[self.puntero_pilas]);
        self.cuaderno_pilas._agregar(elemento, altura, self.puntero_pilas);
        # Imprimir tiempo y posicion
        print(f"Se ha recibido el contenedor con serial {elemento}");
        print("Se apilo en 180 segundos");
        print(f"Se encuentra ubicado en la pila: {self.puntero_pilas + 1}");
        print(f"Posicion en la pila es: {altura}");

    def desapilar(self, elemento):
        """Desapilar un contenedor"""
        self.cuaderno_pilas._ordenar();
        nota = self.cuaderno_pilas._buscar(elemento);
        if not nota:
            print('No se ha encontrado el serial en los contenedores');
            return None;

        print(f"El tiempo de entrega es {(((5 - nota[1])*60)+60) + 180} segundos");
        #[serial, posicion_en_pila, pila]
        for i in range(int(len(self.pila_conte[nota[2]])) - nota[1]):
            migrar = self.pila_conte[nota[2]].pop();
            borrar = self.cuaderno_pilas._buscar(migrar);
            self.cuaderno_pilas._quitar(borrar);
            self.pila_conte[199].push(migrar);
        print(f"{5 - nota[1]} contenedores se han movido a la pila 200");
        print(f"{5 - nota[1]} contenedores se han movido a la pila {nota[2]+1}")
        # Entregando el contenedor requerido
        entrega = self.pila_conte[nota[2]].pop();
        entregado = self.cuaderno_pilas._buscar(entrega);
        self.cuaderno_pilas._quitar(entregado);
        # Se elimina resta un contenedor al puerto
        self.contenedores -= 1;
        print(f"Se ha hecho la entrega del contenedor con serial {entrega}");
        print(f"el contenedor se ubicaba en la pila {nota[2]+1}");

        # Regresando los contenedores anteriores a su lugar.
        for i in range(len(self.pila_conte[199])):
            migrar = self.pila_conte[199].pop();
            self.pila_conte[nota[2]].push(migrar);
            altura = len(self.pila_conte[nota[2]]);
            self.cuaderno_pilas._agregar(migrar, altura, nota[2]);

        # Reiniciando el puntero para llenar pilas vacías si existen.
        self.puntero_pilas = 0;

    def encolar(self, elemento):
        """Encolar un auto"""
        if self.autos == Puerto.MAX_AUTOS:
            print('Se ha llegado al 99% de ocupación');
            print('No se puede agregar mas automoviles')
            return None;

        self.cuaderno_colas._ordenar();
        if self.cuaderno_colas._buscar(elemento):
            print('Ya existe ese serial en los automoviles');
            return None;

        while len(self.cola_auto[self.puntero_colas]) == 15:
            self.puntero_colas += 1;
        self.cola_auto[self.puntero_colas].enqueue(elemento);
        self.autos += 1;
        # Agregar al cuaderno
        altura = len(self.cola_auto[self.puntero_colas]);
        self.cuaderno_colas._agregar(elemento, altura, self.puntero_colas);
        # Imprimir tiempo y posicion
        print(f"Se ha recibido el automovil con serial {elemento}");
        print("Se encolo en 120 segundos");
        print(f"Se encuentra ubicado en la cola: {self.puntero_colas + 1}");
        print(f"Posicion en la cola es: {altura}");

    def desencolar(self, elemento):
        """Desencolar un auto"""
        self.cuaderno_colas._ordenar();
        nota = self.cuaderno_colas._buscar(elemento);
        if not nota:
            print('No se ha encontrado el serial en los autos');
            return None;

        print(f"El tiempo de entrega es {(nota[1]*20) + 120} segundos");
        #[serial, posicion_en_pila, cola]
        for i in range(int(nota[1] - 1)):
            migrar = self.cola_auto[nota[2]].dequeue();
            self.cola_auto[nota[2]].enqueue(migrar);
        print(f"Se han movido {nota[1] - 1} vehiculos a la cola {nota[2] + 1}");
        # Entregando el automóvil requerido.
        entrega = self.cola_auto[nota[2]].dequeue();
        entregado = self.cuaderno_colas._buscar(entrega);
        self.cuaderno_colas._quitar(entregado);
        print(f"Se ha hecho la entrega del automovil con serial {entrega}");
        print(f"El automovil se encontraba en la cola {nota[2] + 1}");
        # Se elimina un automovil del puerto
        self.autos -= 1;

        # Actualizando posiciones
        posicion = 1
        for serial in self.cola_auto[nota[2]]._data:
            update = self.cuaderno_colas._buscar(serial);
            self.cuaderno_colas._quitar(update);
            self.cuaderno_colas._agregar(serial, posicion, nota[2]);
            posicion += 1;

        # Reiniciando el puntero para llenar colas vacías si existen.
        self.puntero_colas = 0;

    def observar_pilas(self, desde, hasta):
        """Observar la cantidad de elementos en las pilas requeridas"""
        for i in self.pila_conte[desde:hasta]:
            print(i);
        print(self.contenedores);

    def observar_pila(self, pila):
        """Observar una pila en particular"""
        for i in self.pila_conte[pila]._data[::-1]:
            print(f"[{i}]")

    def observar_colas(self, desde, hasta):
        """Observar la cantidad de elementos en las colas requeridas"""
        for i in self.cola_auto[desde:hasta]:
            print(i)
        print(self.autos);

    def observar_cola(self, cola):
        """Observar una cola en particular"""
        print(self.cola_auto[cola]._data[::-1]);

    def observar_ultima_pila(self):
        """Observar la ultima pila"""
        print(self.pila_conte[-1])

    def observar_ultima_cola(self):
        """Observar la ultima cola"""
        print(self.cola_auto[-1])

    def buscar_serial_pilas(self, elemento):
        """Buscar un contenedor"""
        nota = self.cuaderno_pilas._buscar(elemento);
        if not nota:
            print('No se ha encontrado el serial en los contenedores');
            return None;

        print(f"El contenedor se encuentra en la pila {nota[2] + 1}");
        print(f"La posicion en la pila es {nota[1]}");

    def buscar_serial_colas(self, elemento):
        """Buscar un automovil"""
        nota = self.cuaderno_colas._buscar(elemento);
        if not nota:
            print('No se ha encontrado el serial en los automoviles');
            return None;

        print(f"El automovil se encuentra en la cola {nota[2] + 1}");
        print(f"La posicion en la cola es {nota[1]}");

    def total(self):
        """Imprime el numero de contenedores y automoviles en el puerto"""
        print(f"numero de contenedores: {self.contenedores}");
        print(f"numero de automoviles: {self.autos}");

    def _inicializar(self):
        for i in range(1, 989, 1):
            self.apilar(i);
        for i in range(1, 370, 1):
            self.encolar(i);
