from cliente_dao import ClienteDAO
from cliente import Cliente
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


class AppZonaFit(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('900x550')
        self.resizable(False, False)
        self.iconbitmap('icono.ico')
        self.configure(background='#424342')
        self.title('Zona Fit GUI')
        self.crearComponentes()
        self.frameFormulario()
        self.frameTabla()
        self.frameBotones()
        
    def crearComponentes(self):
        tituloEtiqueta = ttk.Label(self, text='Zona Fit (GYM)', background='#E8E6E0')
        tituloEtiqueta.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)
        
        
    def frameBotones(self):
        estilo = ttk.Style()
        estilo.configure('Botones.TFrame', background='6c757d')
        self.botonesFrame = ttk.Frame(self, style='Botones.TFrame', width=500, height=100)
        self.botonesFrame.grid(row=3, column=0, columnspan=2, padx=50, pady=10)
        self.botonesFrame.grid_propagate(False)
        self.contenidoBotones()
        
    def contenidoBotones(self):
        botonesEtiqueta = ttk.Label(text='Botones', foreground='black', 
                                    background='#E8E6E0', anchor='center', border=1)
        botonesEtiqueta.grid(row=2, column=0, columnspan=2)
        
        guardarBoton = ttk.Button(self.botonesFrame, text='Guardar', command=self.guardar)
        guardarBoton.grid(row=0, column=0, pady=33, padx=20)
        
        eliminarBoton =  ttk.Button(self.botonesFrame, text='Eliminar', command=self.eliminar)
        eliminarBoton.grid(row=0, column=1)
        
        limpiarBoton = ttk.Button(self.botonesFrame, text='Limpiar', command=self.limpiar)
        limpiarBoton.grid(row=0, column=2)

        
        self.botonesFrame.columnconfigure(0, weight=1)
        self.botonesFrame.columnconfigure(1, weight=1)
        self.botonesFrame.columnconfigure(2, weight=1)
        
    def guardar(self):
        cliente_insertado = Cliente(nombre = self.entryNombre.get(), apellido = self.entryApellido.get(), memebresia = self.entryMembresia.get())
        insertado = ClienteDAO.insertar(cliente_insertado)
        showinfo(title='Cliente Guardado', message=f'{cliente_insertado}')
        self.contenidoTabla()
        self.limpiar()
    
    def eliminar(self):
        seleccion = self.tabla.selection()
        if seleccion:
            item = self.tabla.item(seleccion[0])
            cliente_id = item['values'][0]
            ClienteDAO.eliminar(cliente_id)
            showinfo("Cliente eliminado", f"Cliente con ID {cliente_id} fue eliminado.")
            self.tabla.delete(seleccion[0])  # Elimina directamente del Treeview
            self.limpiar()
        else:
            showinfo("Selecciona un cliente", "Primero debes seleccionar un cliente de la tabla.")

            
    def mostrar_registro_seleccionado(self, event):
        seleccion = self.tabla.selection()
        if seleccion:
            item = self.tabla.item(seleccion[0])
            datos = item['values']
            self.entryNombre.delete(0, tk.END)
            self.entryNombre.insert(0, datos[1])
            self.entryApellido.delete(0, tk.END)
            self.entryApellido.insert(0, datos[2])
            self.entryMembresia.delete(0, tk.END)
            self.entryMembresia.insert(0, datos[3])
            
            self.usuarioSeleccionado = datos[0]



    
    def limpiar(self):
        self.entryNombre.delete(0, tk.END)
        self.entryApellido.delete(0, tk.END)
        self.entryMembresia.delete(0, tk.END)

    def frameFormulario(self):
        # Creamos un estilo para el ttk.Frame
        style = ttk.Style()
        style.configure('Formulario.TFrame', background='#E8E6E0')  # Definimos el color de fondo

        # Usamos el ttk.Frame con el estilo creado y especificamos tamaño
        self.formulario = ttk.Frame(self, style='Formulario.TFrame', width=400, height=300)
        self.formulario.grid(row=1, column=0, sticky='w', padx=10, pady=10)

        self.formulario.grid_propagate(False)  # Evita que el tamaño cambie por el contenido
        self.formulario.columnconfigure(0, weight=1) # Hacemos que la 1ra columna se expanda
        self.formulario.columnconfigure(1, weight=2)

        labelFormulario = ttk.Label(self.formulario, text='Formulario', foreground='white', background='#424342', anchor='center', border=1)
        labelFormulario.grid(row=0, column=0, pady=5, columnspan=2)
        self.contenidoFormulario()
        
    def frameTabla(self):
        style = ttk.Style()
        style.configure('Formulario.TFrame', background='#E8E6E0')  # Definimos el color de fondo
        self.tablaFrame = ttk.Frame(self, style='Formilario.TFrame', width=400, height=300)
        self.tablaFrame.grid(row=1, column=1, sticky='w', padx=10, pady=10)
        self.contenidoTabla()
        
    def contenidoTabla(self):
        estilos = ttk.Style()
        estilos.theme_use('clam')
        estilos.configure('Treeview', background='black', foreground='white', fieldbackground='black'
                          , rowheight=30)
        estilos.map('Treeview', background=[('selected', '#3a86ff')])
        
        columnas = ('Id', 'Nombre', 'Apellido','Membresia')
        self.tabla = ttk.Treeview(self.tablaFrame, columns=columnas, show='headings')
        
        self.tabla.heading('Id', text='Id', anchor=tk.CENTER)
        self.tabla.heading('Nombre', text='Nombre', anchor=tk.W)
        self.tabla.heading('Apellido', text='Apellido', anchor=tk.W)
        self.tabla.heading('Membresia', text='Membresia', anchor=tk.W)


        self.tabla.column('Id', width=80)
        self.tabla.column('Nombre', width=120)
        self.tabla.column('Apellido', width=120)
        self.tabla.column('Membresia', width=120)
        
        self.clientes = ClienteDAO.seleccionar()
        for cliente in self.clientes:
            self.tabla.insert(parent='', index=tk.END, values=(cliente.id, cliente.nombre, cliente.apellido, cliente.membresia))



        scrollbar = ttk.Scrollbar(self.tablaFrame, orient='vertical', command=self.tabla.yview)
        self.tabla.configure(yscrollcommand= scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky=tk.NS)
        # Asociamos un evento select de la tabla
        self.tabla.bind('<<TreeviewSelect>>', self.mostrar_registro_seleccionado)
        # Publicamos la tabla
        self.tabla.grid(row=0, column=0, sticky=tk.NSEW)
        
#    def mostrar_registro_seleccionado(self, event):
#        elemento_seleccionado = self.tabla.selection()[0]
#        if elemento_seleccionado:
#            elemento = self.tabla.item(elemento_seleccionado)
#            persona = elemento['values']
#            showinfo(title='registro', message=f'id: {persona[0]}, Nombre: {persona[1]}, Apellido: {persona[2]}, Membresia: {persona[3]}')
        
        
    def contenidoFormulario(self):
        etiquetaNombre = ttk.Label(self.formulario, text='Nombre:', foreground='white',
                                   background='#424342', anchor='center')
        etiquetaNombre.grid(row=1, column=0, sticky=tk.EW, pady=10)
        self.entryNombre = ttk.Entry(self.formulario)
        self.entryNombre.configure(width=40)
        self.entryNombre.grid(row=1, column=1, sticky=tk.W, padx=10)
        
        etiquetaApellido = ttk.Label(self.formulario, text='Apellido:', foreground='white',
                                     background='#424342', anchor='center')
        etiquetaApellido.grid(row=2, column=0, sticky=tk.EW, pady=10)
        self.entryApellido = ttk.Entry(self.formulario)
        self.entryApellido.configure(width=40)
        self.entryApellido.grid(row=2, column=1, sticky=tk.W, padx=10)
        
        etiquetaMembresia = ttk.Label(self.formulario, text='Membresia:', foreground='white',
                                      background='#424342', anchor='center')
        etiquetaMembresia.grid(row=3, column=0, sticky=tk.EW, pady=10)
        self.entryMembresia = ttk.Entry(self.formulario)
        self.entryMembresia.configure(width=40)
        self.entryMembresia.grid(row=3, column=1, sticky=tk.W, padx=10)
        
        
if __name__ == '__main__':
    app = AppZonaFit()
    app.mainloop()
