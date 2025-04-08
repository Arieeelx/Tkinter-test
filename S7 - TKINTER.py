import tkinter as tk
from tkinter import messagebox

#Función para registrar estudiante

def registrar_estudiante():
    nombre_estudiante = entry_nombre.get()
    apellido_estudiate = entry_apellido.get()
    edad_estudiante = entry_edad.get()
    clase_estudiante = entry_clase.get()
    seccion_estudiante = entry_seccion.get()
    nivel_estudiante = var_nivel_estudiante.get()
    estado_inscripcion = var_estado_inscripcion.get()
    materias_estudiante = [var_matematicas.get(), var_lenguaje.get(), var_historia.get()]
    comentarios = text_comentarios.get("1.0", tk.END).strip()

    mensaje = (f"Estudiante registrado:\n\nNombre estudiante: {nombre_estudiante}\nApellido del estudiante: {apellido_estudiate}\nEdad {edad_estudiante}\nCurso: {clase_estudiante}\nLetra: {seccion_estudiante}\nNivel: {nivel_estudiante}\nEstado: {estado_inscripcion}\nMaterias optativas: {materias_estudiante}\nComentarios: {comentarios}")

    messagebox.showinfo("Registro exitoso", mensaje)

#Función para limpiar registro

def limpiar_formulario():
    entry_nombre.delete(0,tk.END)
    entry_apellido.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    entry_clase.delete(0, tk.END)
    entry_seccion.delete(0, tk.END)
    var_nivel_estudiante.set(None)
    var_estado_inscripcion.set(None)
    var_matematicas.set(0)
    var_lenguaje.set(0)
    var_historia.set(0)
    text_comentarios.delete("1.0", tk.END)

#Detalle de la Ventana
ventana = tk.Tk()
ventana.title("Registro Estudiante - Escuela InnovadoresX")
ventana.attributes("-alpha", 0.9)
ventana.configure(bg="gray91")


#Frames

frame_informacion_estudiante = tk.Frame(ventana)
frame_informacion_estudiante.pack(pady=10)

frame_detalle_academico = tk.Frame(ventana)
frame_detalle_academico.pack(pady=10)

frame_estado_inscripcion = tk.Frame(ventana)
frame_estado_inscripcion.pack(pady=10)

frame_materias_optativas = tk.Frame(ventana)
frame_materias_optativas.pack(pady=10)

frame_comentarios = tk.Frame(ventana)
frame_comentarios.pack(pady=10)

#Label's y entry's

    #Información estudiante
label_nombre = tk.Label(frame_informacion_estudiante, text="Nombre del estudiante:")
label_nombre.grid(row=0, column=0, padx=5, pady=5)
label_apellido = tk.Label(frame_informacion_estudiante, text="Apellido del estudiante:")
label_apellido.grid(row=1, column=0, padx=5, pady=5)
label_edad = tk.Label(frame_informacion_estudiante, text="Edad:")
label_edad.grid(row=2, column=0, padx=5, pady=5)

entry_nombre = tk.Entry(frame_informacion_estudiante)
entry_nombre.grid(row=0, column=1, padx=5, pady=5)
entry_apellido = tk.Entry(frame_informacion_estudiante)
entry_apellido.grid(row=1, column=1, padx=5, pady=5)
entry_edad = tk.Entry(frame_informacion_estudiante)
entry_edad.grid(row=2, column=1, padx=5, pady=5)

    #Detalle académico
label_clase = tk.Label(frame_detalle_academico, text="Curso:")
label_clase.grid(row=0, column=0, padx=5, pady=5)
label_seccion = tk.Label(frame_detalle_academico, text="Letra:")
label_seccion.grid(row=1, column=0, padx=5, pady=5)

entry_clase = tk.Entry(frame_detalle_academico)
entry_clase.grid(row=0, column=1, padx=5, pady=5)
entry_seccion = tk.Entry(frame_detalle_academico)
entry_seccion.grid(row=1, column=1, padx=5, pady=5)

    #Estado inscripción
var_estado_inscripcion = tk.StringVar()
label_estado_inscripcion = tk.Label(frame_estado_inscripcion, text="Estado inscripción:")
label_estado_inscripcion.grid(row=0, column=0, padx=5, pady=5)

radio_inscrito = tk.Radiobutton(frame_estado_inscripcion, text="Inscrito", variable=var_estado_inscripcion, value="Inscrito")
radio_inscrito.grid(row=0, column=1, padx=5, pady=5)

radio_no_inscrito = tk.Radiobutton(frame_estado_inscripcion, text="No inscrito", variable=var_estado_inscripcion, value="No inscrito")
radio_no_inscrito.grid(row=0, column=2, padx=5, pady=5)

    #Materias optativas
var_matematicas = tk.IntVar()
var_lenguaje = tk.IntVar()
var_historia = tk.IntVar()
label_materias_estudiante = tk.Label(frame_materias_optativas, text="Materias optativas:")
label_materias_estudiante.grid(row=0, column=0, padx=5, pady=5)

check_matematicas = tk.Checkbutton(frame_materias_optativas, text="Matemáticas", variable=var_matematicas)
check_matematicas.grid(row=0, column=1, padx=5, pady=5)

check_lenguaje = tk.Checkbutton(frame_materias_optativas, text="Lenguaje y Comunicación", variable=var_lenguaje)
check_lenguaje.grid(row=0, column=2, padx=5, pady=5)

check_historia = tk.Checkbutton(frame_materias_optativas, text="Historia", variable=var_historia)
check_historia.grid(row=0, column=3, padx=5, pady=5)

    #Comentario adicional
label_comentarios = tk.Label(frame_comentarios, text="Comentarios adicionales:")
label_comentarios.grid(row=0, column=0, padx=5, pady=5)
text_comentarios = tk.Text(frame_comentarios, height=5, width=30)
text_comentarios.grid(row=0, column=1, padx=5, pady=5)

    #Menu desplegable insertado en frame de detalle académico
nivel_estudiante = ["Básica", "Media"]
var_nivel_estudiante = tk.StringVar()
var_nivel_estudiante.set(nivel_estudiante[0])

label_nivel_estudiante = tk.Label(frame_detalle_academico, text="Nivel académico:")
label_nivel_estudiante.grid(row=2, column=1, padx=5, pady=5)

menu_nivel_estudiante = tk.OptionMenu(frame_detalle_academico, var_nivel_estudiante, *nivel_estudiante)
menu_nivel_estudiante.grid(row=2, column=2, padx=5, pady=5)

    #Botones
btn_registro_estudiante = tk.Button(ventana, text="Registrar estudiante", command=registrar_estudiante)
btn_registro_estudiante.pack(pady=10)

btn_limpiar_formulario = tk.Button(ventana, text="Limpiar", command=limpiar_formulario)
btn_limpiar_formulario.pack(pady=10)

ventana.mainloop()