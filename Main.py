from email import message
from tkinter import  Tk, Button, Entry, Label, messagebox, ttk, PhotoImage
from tkinter import  StringVar,Scrollbar,Frame, DoubleVar, IntVar
from conexionn import*
import time
class Ventana(Frame):
	def __init__(self, master, *args):
		super().__init__( master,*args)

		self.menu = True
		self.color = True

		#Para los productos

		self.codigo = StringVar()
		self.nombre = StringVar()
		self.marc = StringVar()
		self.precio = DoubleVar()
		self.porcen = IntVar()
		self.precio_public = DoubleVar()
		self.provedor = StringVar()
		self.precio_Publictotal = DoubleVar()
      

		#Buscadores y mas
		self.buscar = StringVar()
		self.buscar_actualiza =  StringVar()
		self.id = StringVar()

		self.base_datos = Registro_datos()
		self.total = 0

		self.frame_inicio = Frame(self.master, bg='#FF5733', width=50, height=45)
		self.frame_inicio.grid_propagate(0)
		self.frame_inicio.grid(column=0, row = 0, sticky='nsew')
		self.frame_menu = Frame(self.master, bg='#FF5733', width = 50)
		self.frame_menu.grid_propagate(0)
		self.frame_menu.grid(column=0, row = 1, sticky='nsew')
		self.frame_top = Frame(self.master, bg='#581845', height = 50)
		self.frame_top.grid(column = 1, row = 0, sticky='nsew')
		self.frame_principal = Frame(self.master, bg='#581845')
		self.frame_principal.grid(column=1, row=1, sticky='nsew')
		self.master.columnconfigure(1, weight=1)
		self.master.rowconfigure(1, weight=1)
		self.frame_principal.columnconfigure(0, weight=1)
		self.frame_principal.rowconfigure(0, weight=1)


		self.widgets()
		

	def pantalla_inicial(self):
		self.paginas.select([self.frame_uno])

	def pantalla_datos(self):
		self.paginas.select([self.frame_dos])
		self.frame_dos.columnconfigure(0, weight=1)
		self.frame_dos.columnconfigure(1, weight=1)
		self.frame_dos.rowconfigure(2, weight=1)
		self.frame_tabla_uno.columnconfigure(0, weight=1)
		self.frame_tabla_uno.rowconfigure(0, weight=1)

	def pantalla_escribir(self):
		self.paginas.select([self.frame_tres])
		self.frame_tres.columnconfigure(0, weight=1)
		self.frame_tres.columnconfigure(1, weight=1)

	def pantalla_actualizar(self):
		self.paginas.select([self.frame_cuatro])	
		self.frame_cuatro.columnconfigure(0, weight=1)
		self.frame_cuatro.columnconfigure(1, weight=1)

	def pantalla_buscar(self):
		self.paginas.select([self.frame_cinco])
		self.frame_cinco.columnconfigure(0, weight=1)
		self.frame_cinco.columnconfigure(1, weight=1)
		self.frame_cinco.columnconfigure(2, weight=1)
		self.frame_cinco.rowconfigure(2, weight=1)
		self.frame_tabla_dos.columnconfigure(0, weight=1)
		self.frame_tabla_dos.rowconfigure(0, weight=1)
		self.frame_tabla_tres.columnconfigure(0, weight=1)
		self.frame_tabla_tres.rowconfigure(0, weight=1)

	def pantalla_ajustes(self):
		self.paginas.select([self.frame_seis])

	def menu_lateral(self):
		if self.menu is True:
			for i in range(50,200,10):				
				self.frame_menu.config(width= i)
				self.frame_inicio.config(width= i)
				self.frame_menu.update()
				clik_inicio = self.bt_cerrar.grid_forget()
				if clik_inicio is None:		
					self.bt_inicio.grid(column=0, row=0, padx =10, pady=10)
					self.bt_inicio.grid_propagate(0)
					self.bt_inicio.config(width=i)
					self.pantalla_inicial()
			self.menu = False
		else:
			for i in range(170,50,-10):
				self.frame_menu.config(width=  i)
				self.frame_inicio.config(width= i)
				self.frame_menu.update()
				clik_inicio = self.bt_inicio.grid_forget()
				if clik_inicio is   None:
					self.frame_menu.grid_propagate(0)		
					self.bt_cerrar.grid(column=0, row=0, padx =10, pady=10)
					self.bt_cerrar.grid_propagate(0)
					self.bt_cerrar.config(width=i)
					self.pantalla_inicial()
			self.menu = True

	def cambiar_color(self):
		if self.color == True:
			self.bt_color['image'] = self.dia
			self.titulo.config(fg='deep sky blue')
			self.frame_seis.config(bg= '#616A6B')
			self.text_ajustes.config(bg='#616A6B')
			self.bt_color.config(bg='#616A6B',activebackground='#616A6B')	
			self.color = False	
		else:
			self.bt_color['image'] = self.noche
			self.titulo.config(fg='DarkOrchid1')
			self.frame_seis.config(bg= 'white')
			self.text_ajustes.config(bg='white')

			self.bt_color.config(bg='white',activebackground='white')	
			self.color = True

	def widgets(self):
		self.imagen_inicio = PhotoImage(file ='POR SI NO ALCANZO/inicio.png')
		self.imagen_menu = PhotoImage(file ='POR SI NO ALCANZO/menu.png')
		self.imagen_datos = PhotoImage(file ='POR SI NO ALCANZO/datos.png')
		self.imagen_registrar = PhotoImage(file ='POR SI NO ALCANZO/registrar.png')
		self.imagen_actualizar = PhotoImage(file ='POR SI NO ALCANZO/actualizar.png')
		self.imagen_buscar = PhotoImage(file ='POR SI NO ALCANZO/venta.png')
		self.imagen_ajustes = PhotoImage(file ='POR SI NO ALCANZO/configuracion.png')

		self.logo = PhotoImage(file ='POR SI NO ALCANZO/logo.png')
		self.imagen_uno = PhotoImage(file ='POR SI NO ALCANZO/imagen_uno.png')
		self.imagen_dos= PhotoImage(file ='POR SI NO ALCANZO/imagen_dos.png')
		self.dia = PhotoImage(file ='POR SI NO ALCANZO/dia.png')
		self.noche= PhotoImage(file ='POR SI NO ALCANZO/noche.png')

		self.bt_inicio = Button(self.frame_inicio, image= self.imagen_inicio, bg='#FF5733',activebackground='#FF5733', bd=0, command = self.menu_lateral)
		self.bt_inicio.grid(column=0, row=0, padx=5, pady=10)
		self.bt_cerrar = Button(self.frame_inicio, image= self.imagen_menu, bg='#FF5733',activebackground='#FF5733', bd=0, command = self.menu_lateral)
		self.bt_cerrar.grid(column=0, row=0, padx=5, pady=10)	

		#BOTONES Y ETIQUETAS DEL MENU LATERAL 
		Button(self.frame_menu, image= self.imagen_datos, bg='#FF5733', activebackground='#FF5733', bd=0, command = self.pantalla_datos).grid(column=0, row=1, pady=20,padx=10)
		Button(self.frame_menu, image= self.imagen_registrar, bg='#FF5733',activebackground='#FF5733', bd=0, command =self.pantalla_escribir ).grid(column=0, row=2, pady=20,padx=10)
		Button(self.frame_menu, image= self.imagen_actualizar, bg= '#FF5733',activebackground='#FF5733', bd=0, command = self.pantalla_actualizar).grid(column=0, row=3, pady=20,padx=10)
		Button(self.frame_menu, image= self.imagen_buscar, bg= '#FF5733',activebackground='#FF5733', bd=0, command = self.pantalla_buscar).grid(column=0, row=4, pady=20,padx=10)		
		Button(self.frame_menu, image= self.imagen_ajustes, bg= '#FF5733',activebackground='#FF5733', bd=0, command = self.pantalla_ajustes).grid(column=0, row=5, pady=20,padx=10)
		
		Label(self.frame_menu, text= 'PRODUCTOS', bg= '#FF5733', fg= 'white', font= ('Lucida Sans', 12, 'bold')).grid(column=1, row=1, pady=20, padx=2)
		Label(self.frame_menu, text= 'REGISTRAR', bg= '#FF5733', fg= 'white', font= ('Lucida Sans', 12, 'bold')).grid(column=1, row=2, pady=20, padx=2)
		Label(self.frame_menu, text= ' ACTUALIZAR', bg= '#FF5733', fg= 'white', font= ('Lucida Sans', 12, 'bold')).grid(column=1, row=3, pady=20, padx=2)
		Label(self.frame_menu, text= 'VENTA', bg= '#FF5733', fg= 'white', font= ('Lucida Sans', 12, 'bold')).grid(column=1, row=4, pady=20, padx=2)	
		Label(self.frame_menu, text= 'AJUSTES', bg= '#FF5733', fg= 'white', font= ('Lucida Sans', 12, 'bold')).grid(column=1, row=5, pady=20, padx=2)


		#############################  CREAR  PAGINAS  ##############################
		estilo_paginas = ttk.Style()
		estilo_paginas.configure("TNotebook", background='#581845', foreground='black', padding=0, borderwidth=0)
		estilo_paginas.theme_use('default')
		estilo_paginas.configure("TNotebook", background='#581845', borderwidth=0)
		estilo_paginas.configure("TNotebook.Tab", background="#581845", borderwidth=0)
		estilo_paginas.map("TNotebook", background=[("selected", '#581845')])
		estilo_paginas.map("TNotebook.Tab", background=[("selected", '#581845')], foreground=[("selected", 'black')]);

		#CREACCION DE LAS PAGINAS 
		self.paginas = ttk.Notebook(self.frame_principal , style= 'TNotebook') #, style = 'TNotebook'
		self.paginas.grid(column=0,row=0, sticky='nsew')
		self.frame_uno = Frame(self.paginas, bg='#E9E9E9')
		self.frame_dos = Frame(self.paginas, bg='#E9E9E9')
		self.frame_tres = Frame(self.paginas, bg='#E9E9E9')
		self.frame_cuatro = Frame(self.paginas, bg='#E9E9E9')
		self.frame_cinco = Frame(self.paginas, bg='#E9E9E9')
		self.frame_seis = Frame(self.paginas, bg='#E9E9E9')
		self.paginas.add(self.frame_uno)
		self.paginas.add(self.frame_dos)
		self.paginas.add(self.frame_tres)
		self.paginas.add(self.frame_cuatro)
		self.paginas.add(self.frame_cinco)
		self.paginas.add(self.frame_seis)


		##############################         PAGINAS       #############################################

		######################## FRAME TITULO #################
		self.titulo = Label(self.frame_top,text= 'Bienvenido', bg='#581845', fg= 'white', font= ('Imprint MT Shadow', 15, 'bold'))
		self.titulo.pack(expand=1)

		######################## VENTANA PRINCIPAL #################

		
		Label(self.frame_uno ,image= self.logo).pack(expand=2)


		######################## MOSTRAR TODOS LOS PRODUCTOS #################
		Label(self.frame_dos, text= 'PRODUCTOS', bg='white', fg= 'DarkOrchid1', font= ('Comic Sans MS', 12, 'bold')).grid(column =0, row=0)
		Button(self.frame_dos, text='MOSTRAR',fg='black' ,font = ('Arial', 11,'bold'), command= self.datos_totales, bg = 'green2', borderwidth=2).grid(column=1, row=0, pady=5)
		Button(self.frame_dos,command = self.eliminar_fila, text='ELIMINAR', font=('Arial',11,'bold'), bg='red',borderwidth=2).grid(column = 2, row=0,pady=10)
		Button(self.frame_dos,command = self.actualiza_btn, text='ACTUALIZAR', font=('Arial',11,'bold'), bg='#2ECC71',borderwidth=2).grid(column = 3, row=0,pady=5)


		#ESTILO DE LAS TABLAS DE DATOS TREEVIEW
		estilo_tabla = ttk.Style()
		estilo_tabla.configure("Treeview", font= ('Helvetica', 10, 'bold'), foreground='black',  background='white')  #, fieldbackground='yellow'
		estilo_tabla.map('Treeview',background=[('selected', 'DarkOrchid1')], foreground=[('selected','black')] )		
		estilo_tabla.configure('Heading',background = '#E9E9E9', foreground='navy',padding=3, font= ('Arial', 10, 'bold'))
		estilo_tabla.configure('Item',foreground = '#E9E9E9', focuscolor ='DarkOrchid1')
		estilo_tabla.configure('TScrollbar', arrowcolor = 'DarkOrchid1',bordercolor  ='black', troughcolor= 'DarkOrchid1',background ='#E9E9E9')


		#TABLA UNO 
		self.frame_tabla_uno = Frame(self.frame_dos, bg= 'gray90')
		self.frame_tabla_uno.grid(columnspan=4, row=2, sticky='nsew')		
		self.tabla_uno = ttk.Treeview(self.frame_tabla_uno) 
		self.tabla_uno.grid(column=0, row=0, sticky='nsew')
		ladox = ttk.Scrollbar(self.frame_tabla_uno, orient = 'horizontal', command= self.tabla_uno.xview)
		ladox.grid(column=0, row = 1, sticky='ew') 
		ladoy = ttk.Scrollbar(self.frame_tabla_uno, orient ='vertical', command = self.tabla_uno.yview)
		ladoy.grid(column = 1, row = 0, sticky='ns')

		self.tabla_uno.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set)
		self.tabla_uno['columns'] = ('Nombre', 'Marca', 'Precio_pro','Ganancia', 'Precio', 'Provedor')
		self.tabla_uno.column('#0', minwidth=100, width=120, anchor='center')
		self.tabla_uno.column('Nombre', minwidth=100, width=130 , anchor='center')
		self.tabla_uno.column('Marca', minwidth=100, width=120, anchor='center' )
		self.tabla_uno.column('Precio_pro', minwidth=100, width=120 , anchor='center')
		self.tabla_uno.column('Ganancia', minwidth=100, width=105, anchor='center')
		self.tabla_uno.column('Precio', minwidth=100, width=105, anchor='center')
		self.tabla_uno.column('Provedor', minwidth=100, width=105, anchor='center')

		self.tabla_uno.heading('#0', text='Codigo', anchor ='center')
		self.tabla_uno.heading('Nombre', text='Nombre', anchor ='center')
		self.tabla_uno.heading('Marca', text='Marca', anchor ='center')
		self.tabla_uno.heading('Precio_pro', text='Precio_pro', anchor ='center')
		self.tabla_uno.heading('Ganancia', text='Ganancia', anchor ='center')
		self.tabla_uno.heading('Precio', text='Precio', anchor ='center')
		self.tabla_uno.heading('Provedor', text='Provedor', anchor ='center')

		self.tabla_uno.bind("<<TreeviewSelect>>", self.obtener_fila) 

		######################## REGISTRAR  NUEVOS PRODUCTOS #################
		self.precio_public.set("")
		self.porcen.set("")
		self.precio.set("")
		Label(self.frame_tres, text = 'Agregar Nuevos Productos',fg='purple', bg ='#E9E9E9', font=('Kaufmann BT',24,'bold')).grid(columnspan=2, column=0,row=0, pady=5)
		Label(self.frame_tres, text = 'Codigo',fg='navy', bg ='#E9E9E9', font=('Rockwell',13,'bold')).grid(column=0,row=1, pady=15, padx=5)
		Label(self.frame_tres, text = 'Nombre',fg='navy', bg ='#E9E9E9', font=('Rockwell',13,'bold')).grid(column=0,row=2, pady=15)
		Label(self.frame_tres, text = 'Marca',fg='navy', bg ='#E9E9E9', font=('Rockwell',13,'bold')).grid(column=0,row=3, pady=15)
		Label(self.frame_tres, text = 'Precio_pro', fg='navy',bg ='#E9E9E9', font=('Rockwell',13,'bold')).grid(column=0,row=4, pady=15)
		Label(self.frame_tres, text = 'Porcentaje',fg='navy', bg ='#E9E9E9', font=('Rockwell',13,'bold')).grid(column=0,row=5, pady=15)  
		Label(self.frame_tres, text = 'Precio Publico',fg='navy', bg ='#E9E9E9', font=('Rockwell',13,'bold')).grid(column=0,row=6, pady=15)
		Label(self.frame_tres, text = 'Provedor',fg='navy', bg ='#E9E9E9', font=('Rockwell',13,'bold')).grid(column=0,row=7, pady=15)

		Entry(self.frame_tres, textvariable=self.codigo , font=('Comic Sans MS', 12),highlightbackground = "DarkOrchid1", highlightcolor= "green2", highlightthickness=5).grid(column=1,row=1)
		Entry(self.frame_tres, textvariable=self.nombre , font=('Comic Sans MS', 12),highlightbackground = "DarkOrchid1", highlightcolor= "green2", highlightthickness=5).grid(column=1,row=2)
		Entry(self.frame_tres, textvariable=self.marc , font=('Comic Sans MS', 12),highlightbackground = "DarkOrchid1", highlightcolor= "green2", highlightthickness=5).grid(column=1,row=3)
		Entry(self.frame_tres, textvariable=self.precio , font=('Comic Sans MS', 12),highlightbackground = "DarkOrchid1", highlightcolor= "green2", highlightthickness=5).grid(column=1,row=4)
		Entry(self.frame_tres, textvariable=self.porcen , font=('Comic Sans MS', 12),highlightbackground = "DarkOrchid1", highlightcolor= "green2", highlightthickness=5).grid(column=1,row=5)
		Entry(self.frame_tres, textvariable=self.precio_public ,state="disable", font=('Comic Sans MS', 12),highlightbackground = "DarkOrchid1", highlightcolor= "green2", highlightthickness=5).grid(column=1,row=6)
		Entry(self.frame_tres, textvariable=self.provedor , font=('Comic Sans MS', 12),highlightbackground = "DarkOrchid1", highlightcolor= "green2", highlightthickness=5).grid(column=1,row=7)

		Button(self.frame_tres,command= self.agregar_datos, text='REGISTRAR', font=('Arial',10,'bold'), bg='magenta2').grid(column=3,row=6, pady=10, padx=4)
		Button(self.frame_tres,command= self.calcular, text='CALCULAR', font=('Arial',10,'bold'), bg='magenta2').grid(column=3,row=7, pady=10, padx=4)
		Label(self.frame_tres, image= self.imagen_uno, bg= '#E9E9E9').grid(column= 3, rowspan= 5, row = 0, padx= 50)
		self.aviso_guardado = Label(self.frame_tres, bg= '#E9E9E9', font=('Comic Sans MS', 12), fg='black')
		self.aviso_guardado.grid(columnspan= 2 , column =0, row = 6, padx= 5)

		########################   ACTUALIZAR LOS PRODUCTOS REGISTRADOS     #################
		Label(self.frame_cuatro, text = 'Actualizar Datos',fg='purple', bg ='#E9E9E9', font=('Kaufmann BT',24,'bold')).grid(columnspan=4, row=0)		
		Label(self.frame_cuatro, text = 'Ingrese el nombre del producto a actualizar',fg='black', bg ='#E9E9E9', font=('Rockwell',12)).grid(columnspan=2,row=1)
		Entry(self.frame_cuatro, textvariable= self.buscar_actualiza , font=('Comic Sans MS', 12), highlightbackground = "magenta2", width=12, highlightthickness=5).grid(column=2,row=1, padx=5)
		Button(self.frame_cuatro, command= self.actualizar_datos, text='BUSCAR', font=('Arial',12,'bold'), bg='deep sky blue').grid(column=3,row=1, pady=5, padx=15)
		self.aviso_actualizado = Label(self.frame_cuatro, fg='black', bg ='#E9E9E9', font=('Arial',12,'bold'))
		self.aviso_actualizado.grid(columnspan= 2, row=7, pady=10, padx=5)

		Label(self.frame_cuatro, text = 'Codigo',fg='navy', bg ='#E9E9E9', font=('Rockwell',13,'bold')).grid(column=0,row=2, pady=15, padx=10)
		Label(self.frame_cuatro, text = 'Nombre',fg='navy', bg ='#E9E9E9', font=('Rockwell',13,'bold')).grid(column=0,row=3, pady=15)
		Label(self.frame_cuatro, text = 'Modelo',fg='navy', bg ='#E9E9E9', font=('Rockwell',13,'bold')).grid(column=0,row=4, pady=15)
		Label(self.frame_cuatro, text = 'Precio', fg='navy',bg ='#E9E9E9', font=('Rockwell',13,'bold')).grid(column=0,row=5, pady=15)
		Label(self.frame_cuatro, text = 'Porcentaje',fg='navy', bg ='#E9E9E9', font=('Rockwell',13,'bold')).grid(column=0,row=6, pady=15)  ##E65561
		Label(self.frame_cuatro, text = 'Precio Publico',fg='navy', bg ='#E9E9E9', font=('Rockwell',13,'bold')).grid(column=0,row=7, pady=15)
		Label(self.frame_cuatro, text = 'Provedor',fg='navy', bg ='#E9E9E9', font=('Rockwell',13,'bold')).grid(column=0,row=8, pady=15)

		Entry(self.frame_cuatro, textvariable=self.codigo ,state="disabled", font=('Comic Sans MS', 12), highlightbackground = "deep sky blue", highlightcolor= "green", highlightthickness=5).grid(column=1,row=2)
		Entry(self.frame_cuatro, textvariable=self.nombre , font=('Comic Sans MS', 12), highlightbackground = "deep sky blue", highlightcolor= "green", highlightthickness=5).grid(column=1,row=3)
		Entry(self.frame_cuatro, textvariable=self.marc , font=('Comic Sans MS', 12), highlightbackground = "deep sky blue", highlightcolor= "green", highlightthickness=5).grid(column=1,row=4)
		Entry(self.frame_cuatro, textvariable=self.precio , font=('Comic Sans MS', 12), highlightbackground = "deep sky blue", highlightcolor= "green", highlightthickness=5).grid(column=1,row=5)
		Entry(self.frame_cuatro, textvariable=self.porcen , font=('Comic Sans MS', 12), highlightbackground = "deep sky blue", highlightcolor= "green", highlightthickness=5).grid(column=1,row=6)
		Entry(self.frame_cuatro, textvariable=self.precio_public ,state="disabled", font=('Comic Sans MS', 12),highlightbackground = "deep sky blue", highlightcolor= "green", highlightthickness=5).grid(column=1,row=7)
		Entry(self.frame_cuatro, textvariable=self.provedor , font=('Comic Sans MS', 12),highlightbackground = "deep sky blue", highlightcolor= "green", highlightthickness=5).grid(column=1,row=8)


		Button(self.frame_cuatro,command= self.actualizar_tabla, text='ACTUALIZAR', font=('Arial',12,'bold'), bg='magenta2').grid(column=2, columnspan= 2 ,row=7, pady=2)
		Button(self.frame_cuatro, command= self.calcular, text='CALCULAR', font=('Arial',12,'bold'), bg='magenta2').grid(column=2,columnspan= 2 , row=6, pady=5, padx=15)
		Button(self.frame_cuatro, command= self.limpiar_datos, text='LIMPIAR', font=('Arial',12,'bold'), bg='magenta2').grid(column=2,columnspan= 2 , row=5, pady=5, padx=15)
		Label(self.frame_cuatro, image= self.imagen_dos, bg='#E9E9E9').grid(column= 2,columnspan= 2, rowspan= 5, row = 1, padx=2)

		######################## venta  #################
		Label(self.frame_cinco, text = 'VENTA',fg='purple', bg ='#E9E9E9', font=('Kaufmann BT',24,'bold')).grid(columnspan= 4,  row=0,sticky='nsew',padx=2)
		Entry(self.frame_cinco, textvariable= self.buscar , font=('Comic Sans MS', 12),highlightbackground = "DarkOrchid1", highlightcolor= "deep sky blue", highlightthickness=5).grid(column=0,row=1,sticky='nsew', padx=2)
		Button(self.frame_cinco,command = self.buscar_nombre, text='BUSCAR POR NOMBRE', font=('Arial',8,'bold'), bg='deep sky blue').grid(column = 1, row=1, sticky='nsew', padx=2)		
		Button(self.frame_cinco,command = self.agregar_tab, text='Agregar', font=('Arial',8,'bold'), bg='deep sky blue').grid(column = 2, row=1, sticky='nsew',padx=2)
		Button(self.frame_cinco,command=self.limpiarT, text='LIMPIAR', font=('Arial',8,'bold'), bg='deep sky blue').grid(column = 3, row=1, sticky='nsew',padx=2)
		Button(self.frame_cinco,command = self.eliminarfi, text='Eliminar', font=('Arial',8,'bold'), bg='red').grid(column = 4, row=1, sticky='nsew',padx=2)
		Label(self.frame_cinco, text = 'TOTAL',fg='purple', bg ='#E9E9E9', font=('Kaufmann BT',12,'bold')).grid(column=3,  row=3,sticky='nsew',padx=2)
		Entry(self.frame_cinco, textvariable=self.precio_Publictotal,state="disabled", font=('Comic Sans MS', 12),highlightbackground = "DarkOrchid1", highlightcolor= "deep sky blue", highlightthickness=5).grid(column=3,row=4,sticky='ew', padx=2)
		self.indica_busqueda= Label(self.frame_cinco, width= 15,text = '',fg='purple', bg ='#E9E9E9', font=('Arial',12,'bold'))
		self.indica_busqueda.grid(column = 0,  row=0,padx=2)

		#TABLA DOS
		self.frame_tabla_dos = Frame(self.frame_cinco, bg= 'gray90')
		self.frame_tabla_dos.grid(columnspan=4, row=2, sticky='nsew')

		self.tabla_dos = ttk.Treeview(self.frame_tabla_dos) 
		self.tabla_dos.grid(column=0, row=0, sticky='nsew')
		ladox = ttk.Scrollbar(self.frame_tabla_dos, orient = 'horizontal', command= self.tabla_dos.xview)
		ladox.grid(column=0, row = 1, sticky='ew') 
		ladoy = ttk.Scrollbar(self.frame_tabla_dos, orient ='vertical', command = self.tabla_dos.yview)
		ladoy.grid(column = 1, row = 0, sticky='ns')

		self.tabla_dos.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set,)
		self.tabla_dos['columns'] = ('Nombre', 'Marca','Precio Unidad','Cantidad','Total')
		self.tabla_dos.column('#0', minwidth=100, width=120, anchor='center')
		self.tabla_dos.column('Nombre', minwidth=100, width=130 , anchor='center')
		self.tabla_dos.column('Marca', minwidth=100, width=120, anchor='center' )
		self.tabla_dos.column('Precio Unidad', minwidth=100, width=105, anchor='center')
		self.tabla_dos.column('Cantidad',minwidth=100, width=105, anchor='center')
		self.tabla_dos.column('Total',minwidth=100, width=105, anchor='center')
	

		self.tabla_dos.heading('#0', text='Codigo', anchor ='center')
		self.tabla_dos.heading('Nombre', text='Nombre', anchor ='center')
		self.tabla_dos.heading('Marca', text='Marca', anchor ='center')
		self.tabla_dos.heading('Precio Unidad', text='Precio Unidad', anchor ='center')
		self.tabla_dos.heading('Cantidad', text='Cantidad', anchor ='center')
		self.tabla_dos.heading('Total', text='Total', anchor ='center')

		self.tabla_dos.bind("<<TreeviewSelect>>", self.obtener_fila) 

		#      tabla 3

		self.frame_tabla_tres = Frame(self.frame_cinco, bg= 'gray90')
		self.frame_tabla_tres.grid(columnspan=3, row=3,rowspan=3, sticky='nsew')

		self.tabla_tres = ttk.Treeview(self.frame_tabla_tres) 
		self.tabla_tres.grid(column=0, row=1, sticky='nsew')
		ladox = ttk.Scrollbar(self.frame_tabla_tres, orient = 'horizontal', command= self.tabla_tres.xview)
		ladox.grid(column=0, row = 2, sticky='ew') 
		ladoy = ttk.Scrollbar(self.frame_tabla_tres, orient ='vertical', command = self.tabla_tres.yview)
		ladoy.grid(column = 1, row = 1, sticky='ns')

		self.tabla_tres.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set,)
		self.tabla_tres['columns'] = ('Nombre', 'Marca','Precio')
		self.tabla_tres.column('#0', minwidth=100, width=120, anchor='center')
		self.tabla_tres.column('Nombre', minwidth=100, width=130 , anchor='center')
		self.tabla_tres.column('Marca', minwidth=100, width=120, anchor='center' )
		self.tabla_tres.column('Precio', minwidth=100, width=105, anchor='center')
	

		self.tabla_tres.heading('#0', text='Codigo', anchor ='center')
		self.tabla_tres.heading('Nombre', text='Nombre', anchor ='center')
		self.tabla_tres.heading('Marca', text='Marca', anchor ='center')
		self.tabla_tres.heading('Precio', text='Precio', anchor ='center')

		self.tabla_tres.bind("<<TreeviewSelect>>", self.obtener_fila)  
	 
	
	
		######################## AJUSTES #################
		self.text_ajustes = Label(self.frame_seis, text = 'Configuracion',fg='purple', bg ='#E9E9E9', font=('Kaufmann BT',28,'bold'))
		self.text_ajustes.pack(expand=1)
		self.bt_color = Button(self.frame_seis, image = self.noche , command= self.cambiar_color, bg = '#E9E9E9', bd=0, activebackground='#E9E9E9')
		self.bt_color.pack(expand=1)

		self.a = 0



	def datos_totales(self):
		datos = self.base_datos.mostrar_productos()
		self.tabla_uno.delete(*self.tabla_uno.get_children())
		i = -1
		for dato in datos:
			i= i+1
			self.tabla_uno.insert('',i, text = datos[i][1:2], values=datos[i][2:8])


	def agregar_datos(self):
		codigo = self.codigo.get()
		nombre = self.nombre.get()
		marca = self.marc.get()
		precio = self.precio.get()
		porcentaje = self.porcen.get()
		publico = self.precio_public.get()
		prove = self.provedor.get()

		datos = (nombre, marca, precio, porcentaje, publico, prove )
		if codigo and nombre and marca and precio and porcentaje and publico and prove !='':
			self.tabla_uno.insert('',0, text = codigo, values=datos)
			self.base_datos.inserta_producto(codigo, nombre, marca, precio, porcentaje, publico, prove)
			self.aviso_guardado['text'] = 'Datos Guardados'
			self.limpiar_datos()
			self.aviso_guardado.update()						
			time.sleep(1) 
			self.aviso_guardado['text'] = ''						
		else:
			self.aviso_guardado['text'] = 'Ingrese todos los datos'
			self.aviso_guardado.update()
			time.sleep(1) 
			self.aviso_guardado['text'] = ''

	def actualizar_datos(self):
		dato = self.buscar_actualiza.get()
		nombre_buscado = self.base_datos.busca_productoA(dato)
		print(nombre_buscado)

		if nombre_buscado == []:
			self.aviso_actualizado['text'] = 'No existe'			
			self.indica_busqueda.update()						
			time.sleep(1) 
			self.limpiar_datos()
			self.aviso_actualizado['text'] = ''
		else:
			i = -1
			for dato in nombre_buscado:
				i= i+1

				self.codigo.set(nombre_buscado[i][1])
				self.nombre.set(nombre_buscado[i][2])
				self.marc.set(nombre_buscado[i][3])
				self.precio.set(nombre_buscado[i][4])
				self.porcen.set(nombre_buscado[i][5])
				self.precio_public.set(nombre_buscado[i][6])
				self.provedor.set(nombre_buscado[i][7])


	def actualizar_tabla(self):	 	
		codigo = self.codigo.get()
		nombre = self.nombre.get()
		marca = self.marc.get()
		precio = self.precio.get()
		porcent = self.porcen.get()
		publico = self.precio_public.get()
		prove = self.provedor.get()
		datos = (nombre, marca, precio, porcent, publico, prove )
		if codigo and nombre and marca and precio and porcent and publico and prove !='':
			self.calcular()
			try:
				self.base_datos.actualiza_productos(nombre, marca, precio, porcent, publico, codigo,  prove)
				self.tabla_uno.delete(*self.tabla_uno.get_children())
				self.tabla_uno.insert('',0, text = codigo, values=datos)		
				self.aviso_actualizado['text'] = 'Datos Actualizados'			
				self.indica_busqueda.update()						
				time.sleep(1) 
				self.aviso_actualizado['text'] = ''
				self.limpiar_datos()
				self.buscar_actualiza.set('')
			except:
				messagebox.showerror(message="Error no se actualizo")
		else:
			self.aviso_actualizado['text'] = 'Ingres todos los datos'

				
	def limpiar_datos(self):
		self.codigo.set('')
		self.nombre.set('')
		self.marc.set('')
		self.precio.set('')
		self.porcen.set('')
		self.precio_public.set('')
		self.provedor.set('')

	def buscar_nombre(self):
		nombre_producto = self.buscar.get()
		nombre_buscado = self.base_datos.busca_producto(nombre_producto)
		self.tabla_tres.delete(*self.tabla_tres.get_children())

		if nombre_buscado == []:
			self.indica_busqueda['text'] = 'No existe'
			self.indica_busqueda.update()						
			time.sleep(1) 
			self.indica_busqueda['text'] =''

		i = -1
		for dato in nombre_buscado:
			i= i+1
			self.tabla_tres.insert('',i, text = nombre_buscado[i][0:1], values=nombre_buscado[i][1:4])
			self.indica_busqueda["text"]=f'Resultados {i+1}' 


	def eliminar_fila(self):
		fila = self.tabla_uno.selection()
		if len(fila) !=0:
			self.tabla_uno.delete(fila)
			nombre =self.nombre_borrar
			self.base_datos.elimina_productos(nombre)
			self.indica_busqueda['text'] = 'Eliminado'
			self.indica_busqueda.update()						
			self.tabla_uno.delete(*self.tabla_dos.get_children())
			time.sleep(1)
			self.indica_busqueda['text'] =''
			self.limpiar_datos()
		else:
			self.indica_busqueda['text'] = 'No se Elimino'
			self.indica_busqueda.update()
			self.tabla_uno.delete(*self.tabla_uno.get_children())						
			time.sleep(1) 
			self.indica_busqueda['text'] =''
			self.buscar.set('')
			self.limpiar_datos()

	def obtener_fila(self, event):
		current_item = self.tabla_uno.focus()
		if not current_item:
			return
		data = self.tabla_uno.item(current_item)
		self.nombre_borrar = data['values'][0]

	def calcular(self):
			precio = float(self.precio.get())
			porcen = int(self.porcen.get())
			public = float(((porcen/100)+1)*precio)
			self.precio_public.set(public) 

	def actualiza_btn(self):
		selecion = self.tabla_uno.focus()
		if not selecion:
			return
		data = self.tabla_uno.item(selecion)
		self.nombre_buscarbtn = data['text']
		self.pantalla_actualizar()
		self.buscar_actualiza.set(self.nombre_buscarbtn)

	def obtener_ver1(self):
		total = 0
		for item in self.tabla_dos.get_children():
			total +=1
			print(total)
			data = self.tabla_dos.item(item)
			print(data)

	def agregar_tab(self):
		fila = self.tabla_tres.selection()
		current_item = self.tabla_tres.focus()
		if not current_item:
			return
		data = self.tabla_tres.item(fila)
		codigo = data['text']
		print(f"tabla tres {data}")
		sentencia = self.base_datos.busca_producto(codigo)
		a = 0
		for dato in sentencia:
				self.tabla_dos.insert('',0, text = codigo, values=sentencia[a][1:4])
				self.precioT = float(data["values"][2])
				self.lista()	

	def lista(self):
		self.total = self.total + self.precioT
		self.precio_Publictotal.set(self.total)

	def eliminarfi(self):
		fila = self.tabla_dos.selection()
		current_item = self.tabla_dos.focus()
		if not current_item:
			return
		data = self.tabla_dos.item(current_item)
		self.borrar = data['values'][0]
		if len(fila) !=0:

			self.tabla_dos.delete(fila)
			menos = data['values'][2]
			menosT = (float(menos))
			self.precioT = menosT*-1
			self.lista()

	def limpiarT(self):
		self.tabla_dos.delete(*self.tabla_dos.get_children())
		self.precio_Publictotal.set('')	

        
			

				
		




if __name__ == "__main__":
	ventana = Tk()
	ventana.title('')
	ventana.minsize(height= 475, width=795)
	ventana.geometry('1000x500+180+80')
	ventana.call('wm', 'iconphoto', ventana._w, PhotoImage(file='POR SI NO ALCANZO/logo.png'))	
	app = Ventana(ventana)
	app.mainloop()