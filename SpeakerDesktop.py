from tkinter import Tk,Entry,Button, Menu, messagebox
import pyttsx3 
import speech_recognition as sr
from translate import Translator

#Traductor
traductor = Translator (
    from_lang="english",
    to_lang="spanish"
)
#Función de traducción
def traduccion():
    texto = input.get()
    resultado = traductor.translate(texto)
    input.delete(0, "end")
    input.insert(0, resultado)
    
#Función de eliminar texto
def eliminar():
    input.delete(0, "end")

#Opción de hablar
motor = pyttsx3.init()
motor.setProperty("rate", 180)

#Función de hablar
def hablar():
    texto = input.get()
    motor.say(texto)
    motor.runAndWait()
#Función de escuchar/posteriormente hablar
def escuchar():
    listen = sr.Recognizer() 
    with sr.Microphone() as source:
        voz = listen.listen(source)
    try:
        audio = listen.recognize_google(voz, language="ES-es")
        input.delete(0, "end")
        input.insert(0, audio)
    except:
        pass
    

def mensaje():
    messagebox.showinfo("Información", "Esta aplicación es de uso libre y gratuito, la cual fue desarrollada para personas que necesiten traducción, escuchar un texto y el poder escribir con la voz.")

def contacto():
    messagebox.showinfo("Contacto", "gmail:jd288868@gmail.com\n\nLinkedin:https://www.linkedin.com/in/juan-pereyra-507aa8252\n\nGithub:https://github.com/Juancito15?tab=repositories\n\nInstagram:https://www.instagram.com/juan_pereyra20")

def copyright():
    messagebox.showinfo("Derechos de autor", "Copyright--2023--Juan Pereyra")

def cerrar():
    quit()
    
#Ventana principal
ventana = Tk()
ventana.geometry("290x280")
ventana.title("Speaker Desktop")
ventana.config(bg="#3f8880") 

#Menu de aplicación
menuBarra = Menu(ventana)
ventana.config(menu=menuBarra)
menuInformacion = Menu(menuBarra, tearoff=0)
menuContacto = Menu(menuBarra, tearoff=0)
menuDerecho = Menu(menuBarra, tearoff=0)
menu_Salir = Menu(menuBarra, tearoff=0)

menuBarra.add_cascade(label="Información", menu=menuInformacion)

menuInformacion.add_cascade(label="Más información", command=mensaje)
menuInformacion.add_cascade(label="Copyright", command=copyright)
menuInformacion.add_cascade(label="Cerrar", command=cerrar)

menuBarra.add_cascade(label="Contacto", menu=menuContacto)
menuContacto.add_cascade(label="Links", command=contacto)

#Entrada de texto
input = Entry(ventana)
input.place(relx=0.1, rely=0.2, relheight=0.1,relwidth=0.8)
#Boton de leet
boton = Button(ventana)
boton.config(text="Leer", command=hablar, bg="#6aa3b4")
boton.place(relx=0.1, rely=0.4, relheight=0.1, relwidth=0.2)
#boton escuchar
boton_escuchar = Button(ventana)
boton_escuchar.config(text="Escuchar", command=escuchar, bg="#6aa3b4")
boton_escuchar.place(relx=0.1, rely=0.6, relheight=0.1, relwidth=0.2)
#Boton traducción
boton = Button(ventana)
boton.config(text="Traducir", command=traduccion, bg="#6aa3b4")
boton.place(relx=0.6,rely=0.4,relwidth=0.3,relheight=0.1)
botonBorrar = Button(ventana)
botonBorrar.config(text="Eliminar", command=eliminar, bg="#6aa3b4")
botonBorrar.place(relx=0.6,rely=0.6,relwidth=0.3,relheight=0.1)
#Boton exit
boton_Exit = Button(ventana)
boton_Exit.config(text="Salir", command= quit, bg="#ff6961")
boton_Exit.place(relx=0.4, rely=0.8, relheight=0.1, relwidth=0.2)
ventana.mainloop()