class Book:
    def __init__(self, title, author, price, stock, oid):
        self._title = title
        self._author = author
        self._price = price
        self._stock = stock
        self._oid = oid

    def get_info(self):
        return f"""\n Título: {self._title} \n Autor: {self._author} \n Precio: {self._price} \n Stock: {self._stock} \n ID: {self._oid}"""

    def set_title(self, new_title):
        self._title = new_title

    def get_title(self):
        return self._title

    def get_price(self):
        return self._price

    def set_price(self, new_price):
        if new_price > 0:
            self._price = new_price
        else:
            print('El precio de un libro no puede ser igual o menor a cero.')

#ENCAPSULAMIENTO:
#público -> accesible para todos
#protegido -> solo debería accederse desde la propia clase y sus subclases ---- SINTAXIS: _
#private -> solo es accesible por su propia clase ---- SINTAXIS: __

#Getters/Setters
#get -> obtener una propiedad (lectura)
#set -> setear/establecer valores (escritura)

class Comic(Book):
    def __init__(self, title, author, price, stock, oid, illustrators, vol):
        super().__init__(title, author, price, stock, oid)
        self._illustrators = illustrators
        self._vol = vol

    def get_info(self):
        info = super().get_info()
        str_illustrators = ', '.join(self._illustrators)
        return info + f"""\n Ilustradores: {str_illustrators} \n Volumen: {self._vol} """
#instanciar
book1 = Book('Así habló Zaratustra', 'Nietzche', 250.0, 100, 1)
book2 = Book('1984', 'G. Orwell', 150.0, 50, 2)
comic1 = Comic('Batman: The Killing Joke', 'nomeacuerdo', 100, 10, 1, ['Ilustrador 1', 'Ilustrador 2'], 147)

#print(book1._title)
#print(book2._title)
#print(book1.get_info())
#print(book2.get_title())
print(comic1.get_info())
