import InterfazConsola as ic
import CRUD

#Inicio de la aplicación
tareas = CRUD.Read()

mainloop = True
while mainloop:
    
    #Interacción
    opcion = ic.menuPrincipal()

    #Create    
    if opcion == 1:
        
        #Interacción 
        id,tarea = ic.formularioCrearTarea()

        #Lógica -> Create o adicionar tarea
        CRUD.Create(id,tarea,tareas)      
    
    #Read
    elif opcion == 2:

        #Interacción
        ic.mostrarTareas(tareas)        
    
    #Salida
    elif opcion == 3:

        #Lógica (persistencia)
        error = CRUD.Write(tareas)

        #Interacción
        if error:
            ic.mensaje('Error de escritura!')
        else:
            ic.mensaje('Cierre exitoso')
        mainloop = False
    
    #Entrada inválida o desconocida
    else:

        #Interacción
        ic.mensaje('Opción inválida')



    
