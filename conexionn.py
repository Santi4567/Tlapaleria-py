import mysql.connector

class Registro_datos():

    def __init__(self):
        self.conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='',
            db='tlapaleria'
        )


    def inserta_producto(self,codigo, nombre, marca, precio, porcentaje, publico, prove):
        self.curso = self.conexion.cursor()
        sql="""INSERT INTO productos (Clave_Produc, Nombre_Produc, Marca_Produc, Precio_Provedor, Ganacia_Produc, Precio_Publico_Produc,  provedor) 
        values(%s, %s, %s, %s, %s, %s, %s);"""
        data = (codigo, nombre, marca, precio, porcentaje, publico, prove)
        self.curso.execute(sql, data)
        self.conexion.commit()    
        self.curso.close()

    def mostrar_productos(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM productos ORDER BY Nombre_Produc  " 
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def busca_productoA(self, nombre_producto):
        self.curso = self.conexion.cursor()
        sql = "SELECT * FROM productos WHERE Nombre_Produc = %s OR  Clave_Produc = %s"
        data = nombre_producto 
        self.curso.execute(sql, (data, data))
        nombreX = self.curso.fetchall()
            
        return nombreX 
    
    def busca_producto(self, nombre_producto):
        self.curso = self.conexion.cursor()
        sql = "SELECT Clave_Produc, Nombre_Produc, Marca_Produc,Precio_Publico_Produc FROM productos WHERE Nombre_Produc LIKE LOWER(%s) OR  Clave_Produc LIKE LOWER(%s) ORDER BY Nombre_Produc"
        data = "%"+ nombre_producto +"%"
        self.curso.execute(sql, (data, data))
        nombreX = self.curso.fetchall()
            
        return nombreX 




    def elimina_productos(self,nombre):
        self.curso = self.conexion.cursor()
        sql='''DELETE FROM productos WHERE Nombre_Produc = %s'''
        self.curso.execute(sql, (nombre,))
        self.conexion.commit()
  
    def actualiza_productos(self,nombre, marca, precio, porcen ,public, codigo, prove):
        self.curso = self.conexion.cursor()
        sql="""UPDATE productos SET  Marca_Produc =%s , Precio_Provedor=%s, Ganacia_Produc=%s, Precio_Publico_Produc=%s, Nombre_Produc=%s, provedor=%s WHERE Clave_Produc=%s"""
        data = (marca, precio, porcen, public,nombre,prove, codigo)
        self.curso.execute(sql, data,)
        self.conexion.commit()
