from estructuras_de_datos import ArrayStack;
from estructuras_de_datos import ArrayQueue;
from puerto import Puerto;


if __name__ == '__main__':
    Cargo_Imaginary_Company = Puerto(False);
    modo = 'container';
    print('Bienvenido al control de inventario de Cargo Imaginary Company');
    print('¿Desea inicializar el puerto con 988 contenedores y 369 autos?');
    print('YES');
    print('NO');
    while True:
        yesnoquestion = input();

        if yesnoquestion == 'YES':
            Cargo_Imaginary_Company._inicializar();
            break;
        elif yesnoquestion == 'NO':
            break;

        else:
            print('Ingrese YES o NO, por favor');

    while True:
        if modo == 'container':
            estructura = 'pila'
            display = 'contenedor';
            change = 'automovil'
        else:
            estructura = 'cola'
            display = 'automovil';
            change =  'contenedor';

        print('Comandos:');
        print('-e entregar un ' + display);
        print('-r recibir un ' + display);
        print('-v ver una ' + estructura + ' en particular');
        print('-s buscar ' + display + ' por numero de serial')
        print('-n numero de contenedores y automoviles');


        print('[Modo ' + display + ']');
        print('-C cambiar a modo ' + change);

        comando = input();
        if comando == '-e':
            print('Ingrese el serial del ' + display);
            print('Ingrese -q para volver');
            while True:
                command = input();

                if command == '-q':
                    break;

                try:
                    command = int(command);
                except:
                    print('Por favor, ingrese un numero entero');
                    continue;

                if modo == 'container':
                    Cargo_Imaginary_Company.desapilar(command);
                    break;
                else:
                    Cargo_Imaginary_Company.desencolar(command);
                    break;

        elif comando == '-r':
            print('Ingrese el serial del ' + display);
            print('Ingrese -q para volver');
            while True:
                command = input();

                try:
                    command = int(command);
                except:
                    print("Ingrese un numero entero, por favor");
                    continue;

                if command == '-q':
                    break;

                if modo == 'container':
                    Cargo_Imaginary_Company.apilar(command);
                    break;
                else:
                    Cargo_Imaginary_Company.encolar(command);
                    break;

        elif comando == '-v':
            print('Ingrese el serial de la ' + estructura + ' a observar');
            print('Ingrese -q para volver');
            while True:
                command = input();

                if command == '-q':
                    break;

                try:
                    command = int(command);
                except:
                    print('Por favor, ingrese un numero entero');
                    continue;

                if modo == 'container':
                    try:
                        assert command >= 1;
                        assert command <= 200;
                    except:
                        print('Por favor, ingrese un numero entre 1 y 200');
                        continue;
                else:
                    try:
                        assert command >= 1;
                        assert command <= 25;
                    except:
                        print('Por favor, ingrese un numero entre 1 y 25');
                        continue;

                if modo == 'container':
                    Cargo_Imaginary_Company.observar_pila(command - 1);
                    break;
                else:
                    Cargo_Imaginary_Company.observar_cola(command - 1);
                    break;

        elif comando == '-s':
            print('Ingrese el serial del ' + display + ' que desea buscar');
            print('Ingrese -q para volver');
            while True:
                command = input();

                if command == '-q':
                    break;

                try:
                    command = int(command);
                except:
                    print("Ingrese un numero entero, por favor");
                    continue;

                if modo == 'container':
                    Cargo_Imaginary_Company.buscar_serial_pilas(command);
                    break;
                else:
                    Cargo_Imaginary_Company.buscar_serial_colas(command);
                    break;

        elif comando == '-n':
            Cargo_Imaginary_Company.total();

        elif comando == '-C':
            if modo == 'container':
                modo = 'car';
            else:
                modo = 'container';

        else:
            print('Inserta un comando valido, por favor')
