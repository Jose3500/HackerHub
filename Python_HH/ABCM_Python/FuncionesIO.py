
def Alta_Empleado(Emp,insert):
        Ingresar_Datos()
        Emp.Alta(Nombre,Apellidos,Profesion,Telefono,Github,Twitter,Facebook,NombreP,Tipo,Tecnologia,Repositorio,Sitio,Contribuidores,insert)    
    

def Baja_Empleado(Emp,delete,and_,User):
    
    Max = MAX_EMP(User)    
                    
    NE = int(raw_input("Ingrese el Numero de Empleado: "))
    #seleccionando el Ususario
    while NE < 0 or NE > Max:
        print "Usuario no Encontrado verifique el Numero de Empleado"
        NE = int(raw_input("Ingrese el Numero de Empleado: "))
        
    select = User.select(and_(User.c.id == NE)) 
    Emp_Select = select.execute()
    IMPRIMIR(Emp_Select)
    Mal = 1        
        
    while Mal == 1:
            
        Seg = raw_input("\n\nEsta Seguro de Querer Borrar este Resgistro (Responda SI/NO):")        
        if Seg == "NO":
            print "\nNINGUN REGISTRO SE BORRO"
            Mal = 0
        elif Seg <> "NO" and not Seg == "SI" or Seg <> "SI":
            print "Responda en Mayusculas SI o NO"
            Mal == 1
        elif Seg == "SI":
            delete = User.delete(and_(User.c.id == NE)) 
            delete.execute()            
            print "\nREGISTRO BORRADO"
            Mal = 0
    
    
    

def Consulta_Empleado(Emp,and_,User):
    
    Max = MAX_EMP(User)    
    try:       
            NE = int(raw_input("\nIngrese el Numero de Empleado: "))
    except ValueError:
            NE = -1
                    
    #seleccionando el Ususario
    while NE < 0 or NE > Max:
        print "Usuario no Encontrado verifique el Numero de Empleado"
        try:       
            NE = int(raw_input("\nIngrese el Numero de Empleado: "))
        except ValueError:
            NE = -1
        
    select = User.select(and_(User.c.id == NE)) 
    Emp_Select = select.execute()
    IMPRIMIR(Emp_Select)
    
        
def Modificacion_Empleado(Emp,and_,User,insert):
    Max = MAX_EMP(User)    
                        
    NE = int(raw_input("Ingrese el Numero de Empleado: "))
    #seleccionando el Ususario
    while NE < 0 or NE > Max:
        print "Usuario no Encontrado verifique el Numero de Empleado"
        NE = int(raw_input("Ingrese el Numero de Empleado: "))
            
    select = User.select(and_(User.c.id == NE)) 
    Emp_Select = select.execute()
    print "\nUsuario a Modificar\n"
    IMPRIMIR(Emp_Select)    
    
    print "\n\nIngrese TODOS los Datos Nuevamente)\n"
    Ingresar_Datos()

    
    Mal = 1        
    
    while Mal == 1:
            
            Seg = raw_input("\n\nEsta Seguro de Querer Modificar este Resgistro (Responda SI/NO):")        
            if Seg == "NO":
                    print "\nNINGUN REGISTRO SE MODIFICO"
                    Mal = 0
            elif Seg <> "NO" and not Seg == "SI" or Seg <> "SI":
                    print "Responda en Mayusculas SI o NO"
                    Mal == 1
            elif Seg == "SI":
                    delete = User.delete(and_(User.c.id == NE)) 
                    delete.execute()
                    insert.execute({'id':NE, 'Nombre': Nombre, 'Apellidos': Apellidos, 'Profesion': Profesion,'Telefono': Telefono,'Github': Github,'Twitter': Twitter,'Facebook': Facebook,'NombreP': NombreP,'Tipo': Tipo,'Tecnologia': Tecnologia,'Repositorio': Repositorio,'Sitio': Sitio,'Contribuidores': Contribuidores})
                    print "\nREGISTRO MODIFICADO"
                    Mal = 0

def MAX_EMP(User):
    select = User.select()
    Emp_Select = select.execute()
    for row in Emp_Select:
        MAX = row['id']
    print "**** Ingrese un Numero de Empleado MENOR a " + str(MAX) + " ****\n"
    return MAX  

def IMPRIMIR(Emp_Select):
    for row in Emp_Select:
            print "\nNumero de Empleado:",row['id']
            print "Nombre del Trabajador:" ,row['Nombre'], row['Apellidos']
            print "Profesion/Ocupacion:" ,row['Profesion']
            print "Telefono:" ,row['Telefono']
            print "Github:" ,row['Github']
            print "Twitter:" ,row['Twitter']
            print "Facebook:" ,row['Facebook']
            print "Nombre del Proyecto:" ,row['NombreP']
            print "Tipo:" ,row['Tipo']
            print "Tecnologia:" ,row['Tecnologia']
            print "Repositorio:" ,row['Repositorio']
            print "Sitio:" ,row['Sitio']
            print "Contribuidores:" ,row['Contribuidores']    
            
            
def Ingresar_Datos():
        global Nombre,Apellidos,Profesion,Telefono,Github,Twitter,Facebook,NombreP,Tipo,Tecnologia,Repositorio,Sitio,Contribuidores
        Nombre = raw_input("Ingrese el Nombre del Trabajador: ")
        Apellidos = raw_input("Ingrese los Apellidos del Trabajador: ")
        Profesion = raw_input("Ingrese la Profesion del Trabajador: ")
        Telefono = raw_input("Ingrese el Telefono del Trabajador: ")
    
        Mal = 1
        Red = "NO"
        Proy = "NO"
        
        while Mal == 1:
                
                Red = raw_input("Usted cuenta con GitHub (Responda SI/NO):")        
                if Red == "NO":
                        Github = "NO"
                        Mal = 0
                elif Red <> "NO" and not Red == "SI" or Red <> "SI":
                        print "Responda en Mayusculas SI o NO"
                        Mal == 1
                elif Red == "SI":
                        Github = raw_input("\nDigite su cuenta GitHub: ")
                        Mal = 0
                        
        Mal = 1        
                        
        while Mal == 1:
            
                Red = raw_input("Usted cuenta con Twitter (Responda SI/NO):")        
                if Red == "NO":
                        Twitter = "NO"
                        Mal = 0
                elif Red <> "NO" and not Red == "SI" or Red <> "SI":
                        print "Responda en Mayusculas SI o NO"
                        Mal == 1
                elif Red == "SI":
                        Twitter = raw_input("\nDigite su cuenta Twitter: ")
                        Mal = 0
    
        Mal = 1
          
        while Mal == 1:
            
                Red = raw_input("Usted cuenta con Facebook (Responda SI/NO):")        
                if Red == "NO":
                        Facebook = "NO"
                        Mal = 0
                elif Red <> "NO" and not Red == "SI" or Red <> "SI":
                        print "Responda en Mayusculas SI o NO"
                        Mal == 1
                elif Red == "SI":
                        Facebook = raw_input("\nDigite su cuenta Facebook: ")
                        Mal = 0                
            
        #Preguntando por Proyectos Personales
        Mal = 1
        
        while Mal == 1:
            
                Proy = raw_input("Usted Tiene algun Proyecto (Responda SI/NO):")        
                if Proy == "NO":
                        NombreP = "SIN PROYECTO"
                        Tipo = ""
                        Tecnologia = ""
                        Repositorio = ""
                        Sitio = ""
                        Contribuidores = ""
                        Mal = 0
                elif Proy <> "NO" and not Proy == "SI" or Proy <> "SI":
                        print "Responda en Mayusculas SI o NO"
                        Mal == 1
                elif Proy == "SI":
                        NombreP = raw_input("Nombre del Proyecto: ")
                        Tipo = raw_input("Tipo de Proyecto (Web, Desktop, Movil): ")
                        Tecnologia = raw_input("Tecnologia del Proyecto (Python, Andorid, C++, Etc): ")
                        Repositorio = raw_input("Repositorio del Proyecto (Si NO Tiene Repositorio solo de Enter): ")
                        Sitio = raw_input("Sitio del Proyecto (Si NO Tiene Sitio solo de Enter): ")
                        Contribuidores = raw_input("Contribuidores del Proyecto (Si NO Tiene Contribuidores solo de Enter): ")
                
                        if Repositorio == "":
                                Repositorio = "NO"
                    
                        if Sitio == "":
                                Sitio = "NO" 
     
                        if Contribuidores == "":
                                Contribuidores = "NO"  
                    
                        Mal = 0          