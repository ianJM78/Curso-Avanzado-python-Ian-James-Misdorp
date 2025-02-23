



class ReproductorMusica:
    def __init__(self):
        self.type = MP3()  # Store the audio type

    def reproducir(self) -> str:
        if self.type:
            return self.type.reproducir()
        return "No hay un formato de reproducción asignado."

    def change_type(self, obj) -> None:
        self.type = obj  


#! Por lo menos para MP3, no es posible que tenga herencia, ya que cuando se hace "self.typr = MP3" para que sea el defult, 
#! termina con un loop infinito llamando a MP3() y haciendo la herencia

class MP3():
    def reproducir(self) -> str:
        return "Reproduciendo en MP3"
    

class CD():
    def reproducir(self) -> str:
        return "Reproduciendo en CD"
    
class Consola():
    def reproducir(self) -> str:
        return "Reproduciendo en Consola"
    


#? MAIN

t = ReproductorMusica()

print(t.reproducir())  #Defult case test

t.change_type(CD())
print(t.reproducir())

t.change_type(Consola())
print(t.reproducir())

