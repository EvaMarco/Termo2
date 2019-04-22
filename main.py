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
        self.tempertaura = StringVar(value='')
        # Cada vez q se hace una modificación llama a la función. Asi se mantiene la traza del texto.
        self.trace('w', self.validatet)
        self.tipounidad = StringVar(value='C')

        self.createlayout()

    def validatet(self, *args):
        nuevovalor = self.temperatura.get()
        try:
            float(nuevovalor)
            self.__temperaturaanterior = nuevovalor
        except:
            self.temperatura.set(self.__temperaturaanterior)

    def createlayout(self):
        self.entrada = ttk.Entry(self, textvariable=self.tempertaura).place(x=10, y=10)
        self.lblunidad = ttk.Label(self, text='Grados:').place(x=10, y=45)
        self.rb1 = ttk.Radiobutton(self, text='Fahrenheit', variable=self.tipounidad, value='F').place(x=20, y=70)
        self.rb2 = ttk.Radiobutton(self, text='Celsius', variable=self.tipounidad, value='C').place(x=20, y=95)

    # Hacemos que aparezca. Es el ciclo principal.
    def start(self):
        self.mainloop()


if __name__ == '__main__':
    app = MainApp()
    app.start()
