def Write_Client_DataBase (Client_DataBase) :
	myfile = open("Databases/Client_DataBase.csv","w")
	for i in Client_DataBase :
		myfile.write(str(i)+";"+Client_DataBase[i][0]+";"+Client_DataBase[i][1]+";"+Client_DataBase[i][2]+";"+Client_DataBase[i][3]+";"+Client_DataBase[i][4]+";"+Client_DataBase[i][5]+";"+Client_DataBase[i][6]+"\n")
	myfile.close()
	
	
	
def Write_Tech_DataBase (Tech_DataBase) :
	myfile = open("Databases/Tech_DataBase.csv","w")	
	for i in Tech_DataBase :
		myfile.write(str(i)+";")
		for j in Tech_DataBase[i] :
			myfile.write(str(j[0])+";"+j[1]+";"+j[2]+";")
		myfile.write("\n")
	
	myfile.close()