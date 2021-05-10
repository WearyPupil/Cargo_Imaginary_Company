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

    def __init__(self, display):
        """Iniciar datos del puerto"""
        self.pila_conte = [ArrayStack() for i in range(Puerto.MAX_CONTENEDORES)]
        self.cola_auto = [ArrayQueue() for i in range(Puerto.MAX_COLAS)];
        self.contenedores = 0
        self.autos = 0;
        self.puntero_pilas = 0;
        self.puntero_colas = 0;
        self.cuaderno_pilas = Puerto._Cuaderno();
        self.cuaderno_colas = Puerto._Cuaderno();
        self.display = display;

    def apilar(self, elemento):
        """Apilar un contenedor"""
        self.cuaderno_pilas._ordenar();
        if self.cuaderno_pilas._buscar(elemento):
            temp_1 = 'Ya existe ese serial en los contenedores';
            print('Ya existe ese serial en los contenedores');
            if self.display == True:
                return temp_1;
            else:
                print(temp_1);
                return None;

        if self.contenedores == Puerto.MAX_CONTENEDORES:
            temp_1 = 'Se ha llegado al 99% de ocupacion';
            temp_2 = 'No se puede agregar mas contenedores';
            if self.display:
                return temp_1, temp_2;
            else:
                print(temp_1);
                print(temp_2);
                return None;

        while len(self.pila_conte[self.puntero_pilas]) == 5:
            self.puntero_pilas += 1;
        self.pila_conte[self.puntero_pilas].push(elemento);
        self.contenedores += 1;
        # Agregar al cuaderno
        altura = len(self.pila_conte[self.puntero_pilas]);
        self.cuaderno_pilas._agregar(elemento, altura, self.puntero_pilas);
        # Imprimir tiempo y posicion
        temp_1 = 'Se ha recibido el contenedor con serial ' + str(elemento);
        temp_2 = 'Se apilo en 180 segundos';
        temp_3 = 'Se encuentra ubicado en la pila: ' + str(self.puntero_pilas + 1);
        temp_4 = 'Posicion en la pila es ' + str(altura);
        if self.display:
            return temp_1, temp_2, temp_3, temp_4;
        else:
            print(temp_1);
            print(temp_2);
            print(temp_3);
            print(temp_4);

    def desapilar(self, elemento):
        """Desapilar un contenedor"""
        self.cuaderno_pilas._ordenar();
        nota = self.cuaderno_pilas._buscar(elemento);
        if not nota:
            temp_1 = 'No se ha encontrado el serial en los contenedores';
            if self.display:
                return temp_1;
            else:
                print(temp_1);
                return None;
        temp_1 = 'El tiempo de entrega es ' + str(((len(self.pila_conte[nota[2]])-nota[1])*60)+240) + ' segundos';
        temp_2 = str(len(self.pila_conte[nota[2]]) - nota[1]) + ' contenedores se han movido a la pila 200';
        temp_3 = str(len(self.pila_conte[nota[2]]) - nota[1]) + ' contenedores han regresado a la pila ' + str(nota[2] +1);
        #[serial, posicion_en_pila, pila]
        for i in range(int(len(self.pila_conte[nota[2]])) - nota[1]):
            migrar = self.pila_conte[nota[2]].pop();
            borrar = self.cuaderno_pilas._buscar(migrar);
            self.cuaderno_pilas._quitar(borrar);
            self.pila_conte[199].push(migrar);
        # Entregando el contenedor requerido
        entrega = self.pila_conte[nota[2]].pop();
        entregado = self.cuaderno_pilas._buscar(entrega);
        self.cuaderno_pilas._quitar(entregado);
        # Se elimina resta un contenedor al puerto
        self.contenedores -= 1;
        temp_4 = 'Se ha hecho la entrega del contenedor con serial ' + str(entrega);
        temp_5 = 'El contenedor se ubicaba en la pila ' + str(nota[2]+1);
        # Regresando los contenedores anteriores a su lugar.
        for i in range(len(self.pila_conte[199])):
            migrar = self.pila_conte[199].pop();
            self.pila_conte[nota[2]].push(migrar);
            altura = len(self.pila_conte[nota[2]]);
            self.cuaderno_pilas._agregar(migrar, altura, nota[2]);

        # Reiniciando el puntero para llenar pilas vacías si existen.
        self.puntero_pilas = 0;

        if self.display:
            return temp_1, temp_2, temp_3, temp_4, temp_5;
        else:
            print(temp_1);
            print(temp_2);
            print(temp_3);
            print(temp_4);
            print(temp_5);

    def encolar(self, elemento):
        """Encolar un auto"""
        if self.autos == Puerto.MAX_AUTOS:
            temp_1 = 'Se ha llegado al 99% de ocupacio';
            temp_2 = 'No se puede agregar mas automoviles';
            if self.display:
                return temp_1, temp_2;
            else:
                print(temp_1);
                print(temp_2);
                return None;

        self.cuaderno_colas._ordenar();
        if self.cuaderno_colas._buscar(elemento):
            temp_1 = 'Ya existe ese serial en los automoviles';
            if self.display:
                return temp_1;
            else:
                print(temp_1);
                return None;

        while len(self.cola_auto[self.puntero_colas]) == 15:
            self.puntero_colas += 1;
        self.cola_auto[self.puntero_colas].enqueue(elemento);
        self.autos += 1;
        # Agregar al cuaderno
        altura = len(self.cola_auto[self.puntero_colas]);
        self.cuaderno_colas._agregar(elemento, altura, self.puntero_colas);
        # Imprimir tiempo y posicion
        temp_1 = 'Se ha recibido el automovil con serial ' + str(elemento);
        temp_2 = 'Se encolo en 120 segundos';
        temp_3 = 'Esta en la cola ' + str(self.puntero_colas + 1);
        temp_4 = 'Posicion en la cola es ' + str(altura);

        if self.display:
            return temp_1, temp_2, temp_3, temp_4;
        else:
            print(temp_1);
            print(temp_2);
            print(temp_3);
            print(temp_4);

    def desencolar(self, elemento):
        """Desencolar un auto"""
        self.cuaderno_colas._ordenar();
        nota = self.cuaderno_colas._buscar(elemento);
        if not nota:
            temp_1 = 'No se ha encontrado el serial en los autos';
            if self.display:
                return temp_1;
            else:
                print(temp_1);
                return None;

        temp_1 = 'El tiempo de entrega es ' + str((nota[1]*20) + 120) + ' segundos';
        #[serial, posicion_en_pila, cola]
        for i in range(int(nota[1] - 1)):
            migrar = self.cola_auto[nota[2]].dequeue();
            self.cola_auto[nota[2]].enqueue(migrar);
        temp_2 = 'Se han movido ' + str(nota[1] - 1) + ' automoviles a la cola ' + str(nota[2] + 1);
        # Entregando el automóvil requerido.
        entrega = self.cola_auto[nota[2]].dequeue();
        entregado = self.cuaderno_colas._buscar(entrega);
        self.cuaderno_colas._quitar(entregado);
        temp_3 = 'Se ha hecho la entrega del automovil con serial ' + str(entrega);
        temp_4 = 'El automovil se encontraba en la cola ' + str(nota[2] + 1);
        # Se elimina un automovil del puerto
        self.autos -= 1;

        # Actualizando posiciones
        posicion = 1
        for serial in self.cola_auto[nota[2]]._data:
            self.cuaderno_colas._ordenar();
            update = self.cuaderno_colas._buscar(serial);
            self.cuaderno_colas._quitar(update);
            self.cuaderno_colas._agregar(serial, posicion, nota[2]);
            posicion += 1;

        # Reiniciando el puntero para llenar colas vacías si existen.
        self.puntero_colas = 0;
        if self.display:
            return temp_1, temp_2, temp_3, temp_4;
        else:
            print(temp_1);
            print(temp_2);
            print(temp_3);
            print(temp_4);

    def observar_pilas(self, desde, hasta):
        """Observar la cantidad de elementos en las pilas requeridas"""
        for i in self.pila_conte[desde:hasta]:
            print(i);
        print(self.contenedores);

    def observar_pila(self, pila):
        """Observar una pila en particular"""
        if self.display:
            return self.pila_conte[pila]._data;
        else:
            for i in self.pila_conte[pila]._data[::-1]:
                print(f"[{i}]")

    def observar_colas(self, desde, hasta):
        """Observar la cantidad de elementos en las colas requeridas"""
        for i in self.cola_auto[desde:hasta]:
            print(i)
        print(self.autos);

    def observar_cola(self, cola):
        """Observar una cola en particular"""
        if self.display:
            return self.cola_auto[cola]._data[::-1];
        else:
            print(self.cola_auto[cola]._data[::-1]);

    def observar_ultima_pila(self):
        """Observar la ultima pila"""
        print(self.pila_conte[-1])

    def observar_ultima_cola(self):
        """Observar la ultima cola"""
        print(self.cola_auto[-1])

    def buscar_serial_pilas(self, elemento):
        """Buscar un contenedor"""
        self.cuaderno_pilas._ordenar();
        nota = self.cuaderno_pilas._buscar(elemento);
        if not nota:
            temp_1 = 'No se ha encontrado el serial en los contenedores';
            if self.display:
                return temp_1;
            else:
                print(temp_1);
                return None;

        temp_1 = 'El contenedor se encuentra en la pila ' + str(nota[2] + 1);
        temp_2 = 'La posicion en la pila es ' + str(nota[1]);

        if self.display:
            return temp_1, temp_2;
        else:
            print(temp_1);
            print(temp_2);

    def buscar_serial_colas(self, elemento):
        """Buscar un automovil"""
        self.cuaderno_colas._ordenar();
        nota = self.cuaderno_colas._buscar(elemento);
        if not nota:
            temp_1 = 'No se ha encontrado el serial en los automoviles';
            if self.display:
                return temp_1;
            else:
                print(temp_1);
                return None;

        temp_1 = 'El automovil se encuentra en la cola ' + str(nota[2] + 1);
        temp_2 = 'La posicion en la cola es ' + str(nota[1]);

        if self.display:
            return temp_1, temp_2;
        else:
            print(temp_1);
            print(temp_2);

    def total(self):
        """Imprime el numero de contenedores y automoviles en el puerto"""
        temp_1 = 'numero de contenedores: ' + str(self.contenedores);
        temp_2 = 'numero de automoviles: ' + str(self.autos);
        if self.display:
            return temp_1, temp_2;
        else:
            print(temp_1);
            print(temp_2);

    def _inicializar(self):
        for i in range(1, 989, 1):
            self.apilar(i);
        for i in range(1, 370, 1):
            self.encolar(i);
