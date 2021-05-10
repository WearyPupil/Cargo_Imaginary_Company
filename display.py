import curses;
from estructuras_de_datos import ArrayQueue;
from estructuras_de_datos import ArrayStack;
from puerto import Puerto;
import time;

cargo_imaginary_company = Puerto(True);

def main(display):
    # Recuerda borrar esta mondá, manín.
    display = curses.initscr();
    # Recuerda borrar esta mondá
    # Clear screen
    display.clear();
    curses.curs_set(False);
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE);
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK);
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK);
    h, w = display.getmaxyx();
    max_y = h-1;
    max_x = w-1;
    mid_y = h//2;
    mid_x = w//2;
    curses.noecho();
    curses.cbreak();
    display.keypad(True);
    display.clear();

    arriba = 'Presione la tecla flecha arriba';
    display.addstr(mid_y, mid_x - len(arriba)//2, arriba);
    display.refresh();
    flecha_arriba = display.getch();

    display.clear();
    abajo = 'Presione la tecla flecha abajo';
    display.addstr(mid_y, mid_x - len(abajo)//2, abajo);
    display.refresh();
    flecha_abajo = display.getch();

    display.clear();
    enter = 'Presione la tecla enter';
    display.addstr(mid_y, mid_x - len(enter)//2, enter);
    display.refresh();
    enter = display.getch();

    display.clear();
    tabulador = 'presione la tecla tabulador';
    display.addstr(mid_y, mid_x - len(tabulador)//2, tabulador);
    tab = display.getch();
    display.refresh()


    def question():

        curses.noecho();
        curses.cbreak();
        display.keypad(True);
        display.clear();
        state = True;

        while True:
            display.clear();
            bienvenida = 'Bienvenido al control de inventario de Cargo Imaginary Company'
            pregunta = '¿Desea inicializar el puerto con 988 contenedores y 369 autos?'
            yes = 'SI';
            no = 'NO';
            display.addstr(mid_y - 1, mid_x - len(bienvenida)//2, bienvenida);
            display.addstr(mid_y, mid_x - len(pregunta)//2, pregunta);

            if state:
                display.attron(curses.color_pair(1));
                display.addstr(mid_y + 2, mid_x - len(yes)//2, yes);
                display.attroff(curses.color_pair(1));
                display.addstr(mid_y + 3, mid_x - len(no)//2, no);
            else:
                display.addstr(mid_y + 2, mid_x - len(yes)//2, yes);
                display.attron(curses.color_pair(1));
                display.addstr(mid_y + 3, mid_x - len(no)//2, no);
                display.attroff(curses.color_pair(1));

            display.refresh();

            key = display.getch();

            if key == flecha_abajo:
                state = False;
                continue;

            elif key == flecha_arriba:
                state = True;
                continue;

            elif key == 10:
                if state == True:
                    cargo_imaginary_company._inicializar();
                    break;
                else:
                    break;

    def main_menu():

        admin = 'user: varamir0';
        role = 'role: admin';
        modo = 'container';

        option = 1

        while True:
            curses.noecho();
            curses.cbreak();
            display.keypad(True);
            display.clear();
            curses.curs_set(False);
            if modo == 'container':
                estructura = 'pila';
                show = 'contenedor';
                change = 'automovil';
            else:
                estructura = 'cola';
                show = 'automovil';
                change = 'contenedor'

            mode = 'modo: [' + show +'] - presione TAB para cambiar a modo ' + change;
            entregar = 'entregar un ' + show;
            recibir = 'recibir un ' + show;
            ver = 'ver una ' + estructura + ' en particular';
            buscar = 'buscar ' + show + ' por numero de serial';

            display.attron(curses.color_pair(3));
            display.addstr(0, 0, admin);
            display.addstr(max_y, 0, mode);
            display.attroff(curses.color_pair(3));
            display.attron(curses.color_pair(2));
            display.addstr(1, 0, role);
            display.attroff(curses.color_pair(2));

            contenedores, automoviles = cargo_imaginary_company.total();
            if contenedores[-3:] == '990':
                display.attron(curses.color_pair(2));
                display.addstr(0, mid_x - len(contenedores)//2, contenedores);
                display.attroff(curses.color_pair(2));

            else:
                display.addstr(0, mid_x - len(contenedores)//2, contenedores);


            if automoviles[-3:] == '371':
                display.attron(curses.color_pair(2));
                display.addstr(1, mid_x - len(automoviles)//2, automoviles);
                display.attroff(curses.color_pair(2));

            else:
                display.addstr(1, mid_x - len(automoviles)//2, automoviles);

            if option == 1:
                display.attron(curses.color_pair(1));
                display.addstr(mid_y-2, mid_x - len(entregar)//2, entregar);
                display.attroff(curses.color_pair(1));
                display.addstr(mid_y-1, mid_x - len(recibir)//2, recibir);
                display.addstr(mid_y, mid_x - len(ver)//2, ver);
                display.addstr(mid_y+1, mid_x - len(buscar)//2, buscar);

            elif option == 2:
               display.addstr(mid_y-2, mid_x - len(entregar)//2, entregar);
               display.attron(curses.color_pair(1));
               display.addstr(mid_y-1, mid_x - len(recibir)//2, recibir);
               display.attroff(curses.color_pair(1));
               display.addstr(mid_y, mid_x - len(ver)//2, ver);
               display.addstr(mid_y+1, mid_x - len(buscar)//2, buscar);

            elif option == 3:
                display.addstr(mid_y-2, mid_x - len(entregar)//2, entregar);
                display.addstr(mid_y-1, mid_x - len(recibir)//2, recibir);
                display.attron(curses.color_pair(1));
                display.addstr(mid_y, mid_x - len(ver)//2, ver);
                display.attroff(curses.color_pair(1));
                display.addstr(mid_y+1, mid_x - len(buscar)//2, buscar);

            elif option == 4:
                display.addstr(mid_y-2, mid_x - len(entregar)//2, entregar);
                display.addstr(mid_y-1, mid_x - len(recibir)//2, recibir);
                display.addstr(mid_y, mid_x - len(ver)//2, ver);
                display.attron(curses.color_pair(1));
                display.addstr(mid_y+1, mid_x - len(buscar)//2, buscar);
                display.attroff(curses.color_pair(1));

            display.refresh();

            key = display.getch();

            if key == flecha_arriba:
                if option > 1:
                    option -= 1;
                continue;

            elif key == flecha_abajo:
                if option < 4:
                    option += 1;
                continue;

            elif key == tab:
                if modo == 'container':
                    modo = 'car';
                else:
                    modo = 'container';

            elif key == 10:
                if option == 1:
                    deliver(modo, show);
                if option == 2:
                    get(modo, show);
                if option == 3:
                    check(modo, estructura);
                if option == 4:
                    search(modo, show)

            elif key == curses.KEY_F5:
                break;


    def deliver(modo, show):
        curses.nocbreak();
        curses.echo();
        curses.curs_set(True);
        error = False;

        while True:
            display.clear();
            serial = 'Ingrese el serial del ' + show + ' a entregar';
            display.addstr(mid_y, mid_x - len(serial)//2, serial);
            if error:
                errorm = 'Por favor, ingrese un numero entero';
                display.attron(curses.color_pair(2));
                display.addstr(mid_y-1, mid_x - len(errorm)//2, errorm);
                display.attroff(curses.color_pair(2));
            display.refresh();
            entrada = display.getstr(mid_y+1, mid_x - len(serial)//2);

            try:
                entrada = int(entrada);
            except:
                error = True;
                continue;

            curses.cbreak();
            curses.noecho();
            curses.curs_set(False);
            display.clear();

            if modo == 'container':
                temp_0 = cargo_imaginary_company.desapilar(entrada);
                if len(temp_0) != 5:
                    display.attron(curses.color_pair(2));
                    display.addstr(mid_y, mid_x - len(temp_0)//2, temp_0);
                    display.attroff(curses.color_pair(2));
                else:
                    for i in range(5):
                        display.addstr(mid_y+(i-2), mid_x - len(temp_0[i])//2, temp_0[i]);
            else:
                temp_0 = cargo_imaginary_company.desencolar(entrada)
                if len(temp_0) != 4:
                    display.attron(curses.color_pair(2));
                    display.addstr(mid_y, mid_x - len(temp_0)//2, temp_0);
                    display.attroff(curses.color_pair(2));
                else:
                    for i in range(4):
                        display.addstr(mid_y+(i-2), mid_x - len(temp_0[i])//2, temp_0[i]);

            message = 'Presione cualquier tecla para continuar';
            display.addstr(max_y - 3, mid_x - len(message)//2, message, curses.A_BLINK);
            key = display.getch();
            break;

    def get(modo, show):
        curses.nocbreak();
        curses.echo();
        curses.curs_set(True);
        error = False;

        while True:
            display.clear();
            serial = 'Ingrese el serial del ' + show + ' a recibir';
            display.addstr(mid_y, mid_x - len(serial)//2, serial);
            if error:
                errorm = 'Por favor, ingrese un numero entero';
                display.attron(curses.color_pair(2));
                display.addstr(mid_y-1, mid_x - len(errorm)//2, errorm);
                display.attroff(curses.color_pair(2));
            display.refresh();
            entrada = display.getstr(mid_y+1, mid_x - len(serial)//2);

            try:
                entrada = int(entrada);
            except:
                error = True;
                continue;

            curses.cbreak();
            curses.noecho();
            curses.curs_set(False);
            display.clear();

            if modo == 'container':
                temp_0 = cargo_imaginary_company.apilar(entrada);
                if len(temp_0) == 4:
                    for i in range(4):
                        display.addstr(mid_y+(i-2), mid_x - len(temp_0[i])//2, temp_0[i]);

                elif len(temp_0) == 2:
                    for i in range(2):
                        display.attron(curses.color_pair(2));
                        display.addstr(mid_y+(i-2), mid_x - len(temp_0[i])//2, temp_0[i]);
                        display.attroff(curses.color_pair(2));

                else:
                    display.attron(curses.color_pair(2));
                    display.addstr(mid_y, mid_x - len(temp_0)//2, temp_0);
                    display.attroff(curses.color_pair(2));

            else:
                temp_0 = cargo_imaginary_company.encolar(entrada);
                if len(temp_0) == 4:
                    for i in range(4):
                        display.addstr(mid_y+(i-2), mid_x - len(temp_0[i])//2, temp_0[i]);

                elif len(temp_0) == 2:
                    for i in range(2):
                        display.attron(curses.color_pair(2));
                        display.addstr(mid_y+(i-2), mid_x - len(temp_0[i])//2, temp_0[i]);
                        display.attroff(curses.color_pair(2));

                else:
                    display.attron(curses.color_pair(2));
                    display.addstr(mid_y, mid_x - len(temp_0)//2, temp_0);
                    display.attroff(curses.color_pair(2));

            message = 'Presione cualquier tecla para continuar';
            display.addstr(max_y - 3, mid_x - len(message)//2, message, curses.A_BLINK);
            key = display.getch();

            break;

    def check(modo, estructura):
        curses.nocbreak();
        curses.echo();
        curses.curs_set(True);
        error = False;

        while True:
            display.clear();
            buscar = 'Ingrese el serial de la ' + estructura + ' a buscar';
            display.addstr(mid_y, mid_x - len(buscar)//2, buscar);
            if error:
                if modo == 'container':
                    umbral = '1 y 200';
                else:
                    umbral = '1 y 25';
                errorm = 'Por favor, ingrese un numero entero entre ' + umbral;
                display.attron(curses.color_pair(2));
                display.addstr(mid_y-1, mid_x - len(errorm)//2, errorm);
                display.attroff(curses.color_pair(2));
            display.refresh();
            entrada = display.getstr(mid_y+1, mid_x - len(buscar)//2);

            try:
                entrada = int(entrada);
                assert entrada >= 1;
                if modo == 'container':
                    assert entrada <= 200;
                else:
                    assert entrada <= 25;
            except:
                error = True;
                continue;


            curses.cbreak();
            curses.noecho();
            curses.curs_set(False);
            display.clear();

            if modo == 'container':
                temp_0 = cargo_imaginary_company.observar_pila(entrada - 1);
                for i in range(len(temp_0)):
                    tostring = '[' + str(temp_0[i]) + ']';
                    display.addstr(mid_y-i, mid_x - len(tostring)//2, tostring);

            else:
                temp_0 = cargo_imaginary_company.observar_cola(entrada - 1);
                cola = str(temp_0);
                display.addstr(mid_y, mid_x - len(cola)//2, cola);

            message = 'Presione cualquier tecla para continuar';
            display.addstr(max_y - 3, mid_x - len(message)//2, message, curses.A_BLINK);
            key = display.getch();
            break;

    def search(modo, show):
        curses.nocbreak();
        curses.echo();
        curses.curs_set(True);
        error = False;

        while True:
            display.clear();
            buscar = 'Ingrese el serial del ' + show + ' a buscar';
            display.addstr(mid_y, mid_x - len(buscar)//2, buscar);
            if error:
                errorm = 'Por favor, ingrese un numero entero'
                display.attron(curses.color_pair(2));
                display.addstr(mid_y-1, mid_x - len(errorm)//2, errorm);
                display.attroff(curses.color_pair(2));
            display.refresh();
            entrada = display.getstr(mid_y+1, mid_x - len(buscar)//2);

            try:
                entrada = int(entrada);
            except:
                error = True;
                continue

            curses.cbreak();
            curses.noecho();
            curses.curs_set(False);
            display.clear();

            if modo == 'container':
                temp_0 = cargo_imaginary_company.buscar_serial_pilas(entrada);
                if len(temp_0) == 2:
                    display.addstr(mid_y-1, mid_x - len(temp_0[0])//2, temp_0[0]);
                    display.addstr(mid_y, mid_x - len(temp_0[1])//2, temp_0[1]);

                else:
                    display.attron(curses.color_pair(2));
                    display.addstr(mid_y, mid_x - len(temp_0)//2, temp_0);
                    display.attroff(curses.color_pair(2));

            else:
                temp_0 = cargo_imaginary_company.buscar_serial_colas(entrada);
                if len(temp_0) == 2:
                    display.addstr(mid_y-1, mid_x - len(temp_0[0])//2, temp_0[0]);
                    display.addstr(mid_y, mid_x - len(temp_0[1])//2, temp_0[1]);

                else:
                    display.attron(curses.color_pair(2));
                    display.addstr(mid_y, mid_x - len(temp_0)//2, temp_0);
                    display.attroff(curses.color_pair(2));

            message = 'Presione cualquier tecla para continuar';
            display.addstr(max_y - 3, mid_x - len(message)//2, message, curses.A_BLINK);
            key = display.getch();
            break;

    question();
    main_menu();


curses.wrapper(main);
