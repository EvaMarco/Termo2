from tkinter import *
from tkinter import ttk


class MainApp(Tk):

    # Aqui van los atributos.
    size = '210x150'
    entrada = None
    tipounidad = None
    __temperaturaanterior = ''

    # Creamos el constructor, aquí se define el self.
    def __init__(self):
        # Hacemos que nuestro init sea la propia pantalla de tkinter. LLamando al constructor de la clase padre.
        Tk.__init__(self)
        # Establecemos el tamaño y el nombre.
        self.geometry(self.size)
        self.title('Termometro')
        # Le podemos cambiar el aspecto.
        self.configure(bg='#ECECEC')
        self.resizable(0, 0)

        self.temperatura = StringVar(value='')
        # Cada vez q se hace una modificación llama a la función. Asi se mantiene la traza del texto.
        self.temperatura.trace('w', self.validatet)
        self.tipounidad = StringVar(value='C')

        self.createlayout()

    # Por si acaso la funcion que vamos a llamar tiene mas argumentos de los q le hemos mandado.
    def validatet(self, *args):
        nuevovalor = self.temperatura.get()
        print('Nuevo valor', nuevovalor, 'vs valoranterior', self.__temperaturaanterior)
        try:
            float(nuevovalor)
            self.__temperaturaanterior = nuevovalor
            print('fija valor anterior a', self.__temperaturaanterior)
        except:
            self.temperatura.set(self.__temperaturaanterior)
            print('Recupera valor anterior', self.__temperaturaanterior)

    def selected(self):
        toUnidad = self.tipounidad.get()
        grados = float(self.temperatura.get())

        if toUnidad == 'F':
            resultado = grados * 9/5 + 32
        elif toUnidad == 'C':
            resultado = (grados-32) *5/9
        else:
            resultado = grados
        self.temperatura.set(resultado)

    def createlayout(self):
        self.entrada = ttk.Entry(self, textvariable=self.temperatura).place(x=10, y=10)
        self.lblunidad = ttk.Label(self, text='Grados:').place(x=10, y=45)
        self.rb1 = ttk.Radiobutton(self, text='Fahrenheit', variable=self.tipounidad, value='F', command=self.selected).place(x=20, y=70)
        self.rb2 = ttk.Radiobutton(self, text='Celsius', variable=self.tipounidad, value='C', command=self.selected).place(x=20, y=95)

    # Hacemos que aparezca. Es el ciclo principal.
    def start(self):
        self.mainloop()


if __name__ == '__main__':
    app = MainApp()
    app.start()
