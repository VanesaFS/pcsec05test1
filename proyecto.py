#MenuGasolineraJaguar
TanqueRegular = 40.00
TanqueSuper = 40.00
TanqueDiesel = 40.00
MaxGalonesTanque = 80.00
MinGalonesTanque = 5.00
EmpleadoJornadadDiurna = 1
EmpleadoJornadadVespertina = 1
EmpleadoJornadadNocturna = 1
SalarioEmpleadoJornadadDiurna = 14.00
SalarioEmpleadoJornadadVespertina = 14.50
SalarioEmpleadoJornadadNocturna = 15.50
CompraporGalonDiesel = 0
CompraporGalonRegular = 0
CompraporGalonSuper = 0
VentaGDiesel = 0
VentaGRegular = 0
Preciosuper = 30.00
Precioregular = 29.00
Preciodiesel = 26.50
Galonpordinero = 0.00
VentaGSuper = 0
TotGalonesDiesel = 0
TotGalonesRegular = 0
TotGalonesSuper = 0
Contingresos = 0.00
Costoalmacenamientodiesel = 6.00
Costoalmacenamientoregular = 7.00
Costoalmacenamientosuper = 8.00
Costofijo = 10
OpcionMenu = 5
Seguir = 1
while True:
    print("Menu Gasolinera Jaguar")
    print("1. Gestión de Inventario")
    print("2. Venta de Combustible")
    print("3. Gestión de Turnos")
    print("4. Reporte de Rentabilidad")
    print("5. Salir del Menú")
    #Menu gestión de inventarios
    OpcionMenu = int(input("Seleccione la opción que desea utilizar: "))
    if OpcionMenu == 1:
        print("Usted seleccionó Gestión de Inventario")
        print("El nivel del Tanque Regular en galones es:", TanqueRegular-VentaGRegular)
        print("El nivel del Tanque Diesel en galones es:", TanqueDiesel-VentaGDiesel)
        print("El nivel del Tanque Super en galones es:", TanqueSuper-VentaGSuper)
        OpcionAgregar = input("Desea agregar combustible? (s/n) ")
        if OpcionAgregar == "s":
            OpcionTanque = int(input("Ingrese cuantos galones de combustible desea agregar al tanque de Diesel:"))
            TotGalonesDiesel = OpcionTanque + TanqueDiesel
            if TotGalonesDiesel <= MaxGalonesTanque:
             TanqueDiesel = TanqueDiesel + OpcionTanque
             CostoTotalDiesel = TotGalonesDiesel*Costoalmacenamientodiesel
             print("La cantidad de galones para el Tanque Diesel es:", TotGalonesDiesel)
             print("Su costo equivalente en Quetzales es:", CostoTotalDiesel)
            else:
                print("La cantidad ingresada sobrepasa la capacidad del tanque.")
            OpcionTanque = int(input("Ingrese cuantos galones de combustible desea agregar al tanque de Regular:"))
            TotGalonesRegular = OpcionTanque + TanqueRegular
            if TotGalonesRegular <= MaxGalonesTanque:
             TanqueRegular = TanqueRegular + OpcionTanque
             CostoTotalRegular = TotGalonesRegular*Costoalmacenamientoregular
             print("La cantidad de galones para el Tanque Regular es:", TotGalonesRegular)
             print("Su costo equivalente en Quetzales es:", CostoTotalRegular)
            else:
                print("La cantidad ingresada sobrepasa la capacidad del tanque.")
            OpcionTanque = int(input("Ingrese cuantos galones de combustible desea agregar al tanque de Super:"))
            TotGalonesSuper = OpcionTanque + TanqueSuper
            if TotGalonesSuper <= MaxGalonesTanque:
             TanqueSuper = TanqueSuper + OpcionTanque
             CostoTotalSuper = TotGalonesSuper*Costoalmacenamientosuper
             print("La cantidad de galones para el Tanque Super es:", TotGalonesSuper)
             print("Su costo equivalente en Quetzales es:", CostoTotalSuper)
            else:
                print("La cantidad ingresada sobrepasa la capacidad del tanque.")
    #Menu Venta de Combustible
    if OpcionMenu == 2:
        print("Usted selecionó Venta de Combustible")
        print("La cantidad de galones disponibles para el Tanque de Diesel es:", TanqueDiesel-CompraporGalonDiesel)
        print("Su precio equivalente en Quetzales es: Q.26.50")
        print("La cantidad de galones disponibles para el Tanque de Regular es:", TanqueRegular-CompraporGalonRegular)
        print("Su precio equivalente en Quetzales es: Q.29.00")
        print("La cantidad de galones disponibles para el Tanque de Super es:", TanqueSuper-CompraporGalonSuper)
        print("Su precio equivalente en Quetzales es: Q.30.00")
        print("Seleccione el tipo de combustible que desee")
        print("Para Diesel presione 1")
        print("Para Regular presione 2")
        print("Para Super presione 3")
        OpcionCombustible = int(input("Seleccione su opción: "))
        if OpcionCombustible == 1: 
            print("Seleccione 1 si desea comprar por galón.")
            print("Seleccione 2 si desea comprar por cantidad de dinero.")
            OpcionCompra = int(input("Ingrese su opción"))
            if OpcionCompra == 1:
                CompraporGalonDiesel = int(input("Ingrese la cantidad de galones que desee comprar: "))
                VentaGDiesel = TanqueDiesel - CompraporGalonDiesel
                if CompraporGalonDiesel*Preciodiesel <= 5:
                    print("La operación no es valida debido a bajo inventario.")
                else:
                    print("El total en Quetzales es: ", CompraporGalonDiesel * Preciodiesel)
                    Nombrecl = input("Ingrese su nombre completo: ")
                    Nit = input("Ingrese su número de NIT")
                    print(Nombrecl) 
                    print(Nit)        
                    print("Datos de la factura:  Nombre completo:", Nombrecl)     
                    print("Nit ingresado:", Nit)  
                    print("Galones comprados:", CompraporGalonDiesel)
                    print("Total a pagar:", CompraporGalonDiesel*Preciodiesel)     
                    Contingresos += CompraporGalonDiesel*Preciodiesel    
            if OpcionCompra == 2:
                Compra_por_Dinero_Diesel = int(input("Ingrese la cantidad de dinero que desea gastar: "))
                Galonpordinero = round (Compra_por_Dinero_Diesel/Preciodiesel, 2)
                if TanqueDiesel-Galonpordinero < 5:
                    print("La operación no es valida debido a bajo inventario.")
                else:
                    print("El total en galones es:", Galonpordinero)
                    TanqueDiesel -= Galonpordinero
                    Nombrecl = input("Ingrese su nombre completo:  ")
                    Nit = input("Ingrese su número de NIT:  ")
                    print(Nombrecl)
                    print(Nit)   
                    print("Datos de la factura:  Nombre completo:", Nombrecl)     
                    print("Nit ingresado:", Nit)  
                    print("Galones comprados:", Galonpordinero)
                    #print("Total a pagar:", Compra_por_Dinero_Diesel)     
                    Contingresos += Compra_por_Dinero_Diesel
        if OpcionCombustible == 2: 
            print("Seleccione 1 si desea comprar por galón.")
            print("Seleccione 2 si desea comprar por cantidad de dinero.")
            OpcionCompra = int(input("Ingrese su opción"))
            if OpcionCompra == 1:
                CompraporGalonRegular = int(input("Ingrese la cantidad de galones que desee comprar: "))
                VentaGRegular = TanqueRegular - CompraporGalonRegular
                if CompraporGalonRegular*Precioregular <= 5:
                    print("La operación no es valida debido a bajo inventario.")
                else:
                    print("El total en Quetzales es:", CompraporGalonRegular*Precioregular)
                    Nombrecl = input("Ingrese su nombre completo: ")
                    Nit = input("Ingrese su número de NIT: ")
                    print(Nombrecl) 
                    print(Nit)        
                    print("Datos de la factura:  Nombre completo:", Nombrecl)     
                    print("Nit ingresado:", Nit)  
                    print("Galones comprados:", CompraporGalonRegular)
                    print("Total a pagar:", CompraporGalonRegular*Precioregular)   
                    Contingresos += CompraporGalonRegular*Precioregular   
            if OpcionCompra == 2:
                Compra_por_Dinero_Regular = int(input("Ingrese la cantidad de dinero que desea gastar: "))
                Galonpordinero = round (Compra_por_Dinero_Regular/Precioregular, 2)
                if TanqueRegular-Galonpordinero < 5:
                    print("La operación no es valida debido a bajo inventario.")
                else:
                    print("El total en galones es:", Galonpordinero)
                    TanqueRegular -= Galonpordinero
                    Nombrecl = input("Ingrese su nombre completo: ")
                    Nit = input("Ingrese su número de NIT: ")
                    print(Nombrecl)
                    print(Nit)   
                    print("Datos de la factura:  Nombre completo:", Nombrecl)     
                    print("Nit ingresado: ", Nit)  
                    print("Galones comprados: ", Galonpordinero)
                    print("Total a pagar:", Compra_por_Dinero_Regular)
                    Contingresos += Compra_por_Dinero_Regular  
        if OpcionCombustible == 3: 
            print("Seleccione 1 si desea comprar por galón.")
            print("Seleccione 2 si desea comprar por cantidad de dinero.")
            OpcionCompra = int(input("Ingrese su opción:"))
            if OpcionCompra == 1:
                CompraporGalonSuper = int(input("Ingrese la cantidad de galones que desee comprar: "))
                VentaGSuper = TanqueSuper - CompraporGalonSuper
                if CompraporGalonSuper*Preciosuper <= 5:
                    print("La operación no es valida debido a bajo inventario.")
                else:
                    print("El total en Quetzales es: ", CompraporGalonSuper*Preciosuper)
                    Nombrecl = input("Ingrese su nombre completo: ")
                    Nit = input("Ingrese su número de NIT: ")
                    print(Nombrecl) 
                    print(Nit)        
                    print("Datos de la factura:  Nombre completo: ", Nombrecl)     
                    print("Nit ingresado:", Nit)  
                    print("Galones comprados: ", CompraporGalonSuper)
                    print("Total a pagar:", CompraporGalonSuper*Preciosuper)
                    Contingresos += CompraporGalonSuper*Preciosuper         
            if OpcionCompra == 2:
                Compra_por_Dinero_Super = int(input("Ingrese la cantidad de dinero que desea gastar: "))
                Galonpordinero = round (Compra_por_Dinero_Super/Preciosuper, 2)
                if TanqueSuper-Galonpordinero < 5:
                    print("La operación no es valida debido a bajo inventario.")
                else:
                    print("El total en galones es:", Galonpordinero)
                    TanqueSuper -= Galonpordinero
                    Nombrecl = input("Ingrese su nombre completo:  ")
                    Nit = input("Ingrese su número de NIT:  ")
                    print(Nombrecl)
                    print(Nit)   
                    print("Datos de la factura:  Nombre completo:", Nombrecl)     
                    print("Nit ingresado:", Nit)  
                    print("Galones comprados:", Galonpordinero)
                    print("Total a pagar:", Compra_por_Dinero_Super)
                    Contingresos += Compra_por_Dinero_Super                                  
    if OpcionMenu == 3:
        print("Usted seleccionó Gestión de Turnos")
        print("Los empleados disponibles para la Jornada Diurna son: ", EmpleadoJornadadDiurna)
        print("Los empleados disponibles para la Jornada Vespertina son: ", EmpleadoJornadadVespertina)
        print("Los empleados disponibles para la Jornada Nocturna son: ", EmpleadoJornadadNocturna)
        Empleadosagregar = int(input("Agregue la cantidad de empleados que desea agregar para la jornada diurna: "))
        if Empleadosagregar > 0:
            EmpleadoJornadadDiurna += Empleadosagregar
        Empleadosagregar = int(input("ingrese la cantidad de empleados que desea agregrar para la jornada vespertina: "))
        if Empleadosagregar > 0:
            EmpleadoJornadadVespertina += Empleadosagregar
        Empleadosagregar = int(input("Ingrese la cantidad de empleados que dese agregar a la joranda Nocturna: "))
        if Empleadosagregar > 0:
            EmpleadoJornadadNocturna += Empleadosagregar
        
        Empleadosquitar = int(input("Agregue la cantidad de empleados que desea quitar para la jornada diurna: "))
        if Empleadosquitar > 0: 
            if EmpleadoJornadadDiurna - Empleadosquitar >= 1:
                EmpleadoJornadadDiurna -= Empleadosquitar 
            else:
                print("No es posible quitara los empleados")
            
        Empleadosquitar = int(input("ingrese la cantidad de empleados que desea quitar para la jornada vespertina: "))
        if Empleadosquitar > 0:
            EmpleadoJornadadVespertina -= Empleadosquitar
        Empleadosquitar = int(input("Ingrese la cantidad de empleados que dese quitar a la joranda Nocturna: "))
        if Empleadosquitar > 0:
            EmpleadoJornadadNocturna -= Empleadosquitar
        
               
    if OpcionMenu == 4:
        print("Usted Seleccionó Reporte de Rentabilidad")
        print("Ingresos totales",Contingresos)
        Matprima = 0
        print("Materia prima")
        print("Costo combustible Diesel: ", TanqueDiesel*Costoalmacenamientodiesel)
        Matprima += TanqueDiesel*Costoalmacenamientodiesel
        print("Costo combustible Regular: ", TanqueRegular*Costoalmacenamientoregular)
        Matprima += TanqueRegular*Costoalmacenamientoregular
        print("Costo combustible super:", TanqueSuper*Costoalmacenamientosuper)
        Matprima += TanqueSuper*Costoalmacenamientosuper
        print("costo fijo:", Costofijo)
        print("Mano de obra:")
        Manobra = 0
        print("Salario Jornada diurna:", EmpleadoJornadadDiurna*SalarioEmpleadoJornadadDiurna)
        Manobra += EmpleadoJornadadDiurna*SalarioEmpleadoJornadadDiurna
        print("Salariojornada vespertina:", EmpleadoJornadadVespertina*SalarioEmpleadoJornadadVespertina)
        Manobra += EmpleadoJornadadVespertina*SalarioEmpleadoJornadadVespertina
        print("Salario Jornada nocturna:", EmpleadoJornadadNocturna*SalarioEmpleadoJornadadNocturna)
        Manobra += EmpleadoJornadadNocturna*SalarioEmpleadoJornadadNocturna
        print("Utilidad Bruta:", Contingresos-Matprima-Manobra-Costofijo)
        print("Salir") 
