Algoritmo Busqueda_Binaria_Iteractiva
	puntero<-1
	final<-10
	Dimension vec[10]
	vec[1]<- 10
	vec[2]<- 8
	vec[3]<- 5
	vec[4]<- 2
	vec[5]<- 3
	vec[6]<- 1
	vec[7]<- 7
	vec[8]<- 4
	vec[9]<- 9
	vec[10]<- 6
	encontro<-Falso
	Escribir "Ingresar el número a buscar: "
	Leer numero
	
	Mientras ( encontro=Falso y puntero<=final ) Hacer
		
		mitad<-trunc( (puntero+final) /2) 
		Si numero=vec[mitad] Entonces
			encontro<-Verdadero
		SiNo Si numero<vec[mitad] Entonces
				final<-mitad-1
			SiNo
				puntero <- mitad+1
			FinSi
		FinSi
	FinMientras
	Si (Encontro=Verdadero) Entonces
		Escribir "El dato se encuentra en la posición ", mitad
	SiNo
		Escribir "El dato NO se encuentra "
	FinSi
	
FinAlgoritmo
