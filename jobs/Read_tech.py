def Read_Client_DataBase() :

	myfile = open("Databases/Client_DataBase.csv","r")

	Client_Dict = dict()
	Client_ID = ""
	Department = ""
	Tech_Name = ""
	Client_Name = ""
	Client_Address = ""
	flag = 0
	text = myfile.read()
		
	for i in text :
		if flag == 0 :
						if i != ";" :
							Client_ID = Client_ID + i
						elif i == ";" :
							flag = 1
							
		elif flag == 1 :
						if i != ";" :
							Department = Department + i
						elif i == ";" :
							flag = 2
							
		elif flag == 2 :
						if i != ";" :
							Tech_Name = Tech_Name + i
						elif i == ";" :
							flag = 3
							
		elif flag == 3 :
						if i != ";" :
							Client_Name = Client_Name + i
						elif i == ";" :
							flag = 4
       
		elif flag == 6 :
						if i != ";" :
							Client_Address = Client_Address + i
						elif i == ";" :
							flag = 7
							
		elif flag == 7 :
						if i != "\n" :
							RoomNumber = RoomNumber + i
						elif i == "\n" :
							Client_Dict[int(Client_ID)]=[Department,Tech_Name,Client_Name,Client_Address]
							Client_ID = ""
							Department = ""
							Tech_Name = ""
							Client_Name = ""
							Client_Address = ""
							flag = 0
							
		
	myfile.close()
	return Client_Dict
			
			
			
def Read_Tech_DataBase () :

	myfile = open ("Databases/Tech_DataBase.csv","r")

	Tech_Dict = dict()
	Tech_ID = ""
	Department = ""
	Tech_Name = ""
	Tech_Address = ""
	Client_ID = ""
	Session_Start = ""
	Session_End = ""
	flag = 0

	
	text = myfile.read()

	while text.count(";;") :
		text=text.replace(";;",";")
	
	for i in text :
		if flag == 0 :
					if i != ";" :
						Tech_ID = Tech_ID + i
					elif i == ";" :
						flag = 1
				
		elif flag == 1 :
					if i != ";" :
						Department = Department + i
					elif i == ";" :
						flag = 2
				
		elif flag == 2 :
					if i != ";" :
						Tech_Name = Tech_Name + i
					elif i == ";" :
						flag = 3
				
		elif flag == 3 :
					if i != ";" :
						Tech_Address = Tech_Address + i
					elif i == ";" :
						flag = 4
						Tech_Data_List = [Department,Tech_Name,Tech_Address]
						Tech_Dict[int(Tech_ID)]=[Tech_Data_List]
						
		elif flag == 4 :
					if i != ";" and i != "\n" :
						Client_ID = Client_ID + i
					elif i == ";" :
						flag = 5
					elif i == "\n" :
						flag = 0
						Tech_ID = ""
						Department = ""
						Tech_Name = ""
						Tech_Address = ""
						
		elif flag == 5 :
					if i != ";" :
						Session_Start = Session_Start + i
					elif i == ";" :
						flag = 6
		
		elif flag == 6 :
					if i != ";" and i != "\n" :
						Session_End = Session_End + i
					elif i == ";" :
						flag = 4
						Appointment_List = [int(Client_ID),Session_Start,Session_End]	
						Tech_Dict[int(Tech_ID)].append(Appointment_List)
						Client_ID = ""
						Session_Start = ""
						Session_End = ""
					elif i == "\n" :
						flag = 0
						Tech_ID = ""
						Department = ""
						Tech_Name = ""
						Tech_Address = ""

	myfile.close()
	return Tech_Dict