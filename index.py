import Read_tech
import Write_tech

	
def AppointmentIndexInTechDataBase (Client_ID) :
	for i in Tech_DataBase :
		for j in Tech_DataBase[i] :							
			if str(Client_ID) == str(j[0]) :
				Appointment_index = Tech_DataBase[i].index(j)
				return Appointment_index,i

print("********************************************************************")
print("*                                                                  *")
print("*             Welcome to ICX Systems Management System             *")
print("*             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~             *")
print("********************************************************************")
	
	
tries = 0
tries_flag = ""
while tries_flag != "Close the program" :

		Client_DataBase = Read_tech.Read_Client_DataBase()
		Tech_DataBase  = Read_tech.Read_Tech_DataBase()
				
		print("-----------------------------------------")
		print("|Enter 1 for Admin mode			|\n|Enter 2 for User mode			|")
		print("-----------------------------------------")
		Admin_user_mode = input("Enter your mode : ") 
		

		if Admin_user_mode == "1" :																			#Admin mode
				print("*****************************************\n|         Welcome to admin mode         |\n*****************************************")
				Password = input("Please enter your password : ")
				while True :
					
					if Password == "No2002" :
						print("-----------------------------------------")
						print("|To manage Clients Enter 1 		|\n|To manage Techs Enter 2	 	|\n|To manage appointments Enter 3 	|\n|To be back Enter E		   |")
						print("-----------------------------------------")
						AdminOptions = input ("Enter your choice : ")
						AdminOptions = AdminOptions.upper()
						
						if AdminOptions == "1" :															#Admin mode --> Pateints Management
								print("-----------------------------------------")
								print("|To add new Client Enter 1	  	|")
								print("|To display Client Enter 2	  	|")
								print("|To delete Client data Enter 3   |")
								print("|To edit Client data Enter 4    	|")
								print("|To Back enter E      			|")
								print("-----------------------------------------")
								Admin_choice = input ("Enter your choice : ")
								Admin_choice = Admin_choice.upper()
								
								if Admin_choice == "1" : 										#Admin mode --> Pateints Management --> Enter new Client data
											try :		#To avoid non integer input
												Client_ID = int(input("Enter Client ID : "))
												while Client_ID in Client_DataBase :		#if Admin entered used ID
													Client_ID = int(input("This ID is unavailable, please try another ID : "))					
												Department=input("Enter Client department                : ")
												TechName=input("Enter name of tech following the ticket  : ")
												Name      =input("Enter Client name                      : ")
												Address   =input("Enter Client address                   : ")
												Client_DataBase[Client_ID]=[Department,TechName,Name,Address]
												print("----------------------Client added successfully----------------------")
											except :
												print("Client ID should be an integer number")
										
								elif Admin_choice == "2" :										#Admin mode --> Pateints Management --> Display Client data
											try :		#To avoid non integer input
												Client_ID = int(input("Enter Client ID : "))
												while Client_ID not in Client_DataBase :
													Client_ID = int(input("Incorrect ID, Please Enter Client ID : "))
												print("\nClient name        : ",Client_DataBase[Client_ID][2])
												print("Client address     : ",Client_DataBase[Client_ID][5])
												print("Client is in "+Client_DataBase[Client_ID][0]+" department")
												print("Client is followed by Tech : "+Client_DataBase[Client_ID][1])
											except :
												print("Client ID should be an integer number")
								
								elif Admin_choice == "3" :										#Admin mode --> Pateints Management --> Delete Client data
											try :		#To avoid non integer input
												Client_ID = int(input("Enter Client ID : "))
												while Client_ID not in Client_DataBase :
													Client_ID = int(input("Incorrect ID, Please Enter Client ID : "))
												Client_DataBase.pop(Client_ID)
												print("----------------------Client data deleted successfully----------------------")
											except :
												print("Client ID should be an integer number")
										
								elif Admin_choice == "4" :						 				#Admin mode --> Pateints Management --> Edit Client data
											try :		#To avoid non integer input
												Client_ID=int(input("Enter Client ID : "))
												while Client_ID not in Client_DataBase :
													Client_ID = int(input("Incorrect ID, Please Enter Client ID : "))
												while True :
													print("------------------------------------------")
													print("|To Edit Client Department Enter 1 :    |")
													print("|To Edit Tech following ticket Enter 2 :|")
													print("|To Edit Client Name Enter 3 :          |")
													print("|To Edit Client Address Enter 4 :       |")
													print("|To be Back Enter E                     |")
													print("-----------------------------------------")
													Admin_choice = input("Enter your choice : ")
													Admin_choice = Admin_choice.upper()
													if Admin_choice == "1" :
														Client_DataBase[Client_ID][0]=input("\nEnter Client department : ")
														print("----------------------Client Department edited successfully----------------------")
														
													elif Admin_choice == "2" :
														Client_DataBase[Client_ID][1]=input("\nEnter Tech following ticket : ")
														print("----------------------Tech following ticketedited successfully----------------------")
										
													elif Admin_choice == "3" :
														Client_DataBase[Client_ID][2]=input("\nEnter Client name : ")
														print("----------------------Client name edited successfully----------------------")
													elif Admin_choice == "4" :
														Client_DataBase[Client_ID][5]=input("\nEnter Client address : ")
														print("----------------------Client address edited successfully----------------------")
													elif Admin_choice == "E" :
														break
														
													else :
														print("Please Enter a correct choice")
											except :
												print("Client ID should be an integer number")
																				
								elif Admin_choice == "E" :										#Admin mode --> Pateints Management --> Back
											break
								
								else :
											print("Please enter a correct choice\n")
											
						elif AdminOptions == "2" :															#Admin mode --> Tech Management
							print("-----------------------------------------")
							print("|To add new Tech Enter 1              |")
							print("|To display Tech Enter 2              |")
							print("|To delete Tech data Enter 3          |")
							print("|To edit Tech data Enter 4            |")
							print("|To be back enter E                     |")
							print("-----------------------------------------")
							Admin_choice = input ("Enter your choice : ")
							Admin_choice = Admin_choice.upper()
							
							if Admin_choice == "1" : 											#Admin mode --> Tech  Management --> Enter new Tech data
									try :		#To avoid non integer input
										Tech_ID = int(input("Enter Tech ID : "))
										while Tech_ID in Tech_DataBase :			#if Admin entered used ID
											Tech_ID = int(input("This ID is unavailable, please try another ID : "))
										
										Department=input("Enter Tech department : ")
										Name      =input("Enter Tech name       : ")
										Address   =input("Enter Tech address    : ")
										Tech_DataBase[Tech_ID]=[[Department,Name,Address]]
										print("----------------------Tech added successfully----------------------")
									except :
										print("Tech ID should be an integer number")
								
							elif Admin_choice == "2" : 											#Admin mode --> Techs Management --> Display Tech data
									try :		#To avoid non integer input
										Tech_ID = int(input("Enter Tech ID : "))
										while Tech_ID not in Tech_DataBase :
											Tech_ID = int(input("Incorrect ID, Please Enter Tech ID : "))
										print("Tech name    : ",Tech_DataBase[Tech_ID][0][1])
										print("Tech address : ",Tech_DataBase[Tech_ID][0][2])
										print("Tech is in "+Tech_DataBase[Tech_ID][0][0]+" department")
									except :
										print("Tech ID should be an integer number")
							
							elif Admin_choice == "3" :											#Admin mode --> Tech Management --> Delete Tech data
									try :		#To avoid non integer input
										Tech_ID = int(input("Enter Tech ID : "))
										while Tech_ID not in Tech_DataBase :
											Tech_ID = int(input("Incorrect ID, Please Enter Tech ID : "))
										Tech_DataBase.pop(Tech_ID)
										print("/----------------------Tech data deleted successfully----------------------/")
									except :
										print("Tech ID should be an integer number")

							elif Admin_choice == "4" :											#Admin mode --> Techs Management --> Edit Tech data
									try :		#To avoid non integer input	
										Tech_ID=input("Enter Tech ID : ")
										while Tech_ID not in Tech_DataBase :
											DTech_ID = int(input("Incorrect ID, Please Enter Tech ID : "))
										print("-----------------------------------------")
										print("|To Edit Tech's department Enter 1    |")
										print("|To Edit Tech's name Enter 2          |")
										print("|To Edit Tech's address Enter 3       |")
										print("To be Back Enter E                      |")
										print("-----------------------------------------")
										Admin_choice=input("Enter your choice : ")
										Admin_choice = Admin_choice.upper()
										if Admin_choice == "1" :
											Tech_DataBase[Tech_ID][0][0]=input("Enter Tech's Department : ")
											print("/----------------------Tech's department edited successfully----------------------/")
											
										elif Admin_choice == "2" :
											Tech_DataBase[Tech_ID][0][1]=input("Enter Tech's Name : ")
											print("----------------------Tech's name edited successfully----------------------")
											
										elif Admin_choice == "3" :
											Tech_DataBase[Tech_ID][0][2]=input("Enter Tech's Address : ")
											print("----------------------Tech's address edited successfully----------------------")
										
										elif Admin_choice == "E" :
											break
										
										else :
											print("\nPlease enter a correct choice\n")
											
									except :
										print("Tech ID should be an integer number")
											
							elif Admin_choice == "E" :											#Back
										break
									
							else :
								print("\nPlease enter a correct choice\n")
											
						elif AdminOptions == "3" :															#Admin mode --> Appointment Management
							print("-----------------------------------------")
							print("|To book an appointment Enter 1         |")
							print("|To edit an appointment Enter 2         |")
							print("|To cancel an appointment Enter 3       |")
							print("|To be back enter E                     |")
							print("-----------------------------------------")
							Admin_choice = input ("Enter your choice : ")
							Admin_choice = Admin_choice.upper()
							if Admin_choice == "1" :												#Admin mode --> Appointment Management --> Book an appointment							
								try :		#To avoid non integer input
										Tech_ID = int(input("Enter the ID of Tech : "))
										while Tech_ID not in Tech_DataBase :
											Tech_ID = int(input("Tech ID incorrect, Please enter a correct Tech ID : "))
										print("---------------------------------------------------------")
										print("|For book an appointment for an exist Client Enter 1   |\n|For book an appointment for a new Client Enter 2      |\n|To be Back Enter E                                     |")
										print("---------------------------------------------------------")
										Admin_choice = input ("Enter your choice : ")
										Admin_choice = Admin_choice.upper()
										if Admin_choice == "1" :
												Client_ID = int(input("Enter Client ID : "))
												while Client_ID not in Tech_DataBase :		#if Admin entered incorrect ID
													Client_ID = int(input("Incorrect ID, please Enter a correct Client ID : "))	
										
											
										elif Admin_choice == "2" :
											Client_ID = int(input("Enter Client ID : "))
											while Client_ID in Client_DataBase :		#if Admin entered used ID
												Client_ID = int(input("This ID is unavailable, please try another ID : "))					
											Department=Tech_DataBase[Tech_ID][0][0]
											TechName=Tech_DataBase[Tech_ID][0][1]
											Name      =input("Enter Client name    : ")
											Address   =input("Enter Client address : ")
											Client_DataBase[Client_ID]=[Department,TechName,Name,Address]
										
										elif Admin_choice == "E" :
											break
											
										Session_Start = input("Session starts at : ")
										while Session_Start[ :2] == "11" or Session_Start[ :2] == "12" :
											Session_Start = input("Appointments should be between 01:00PM to 10:00PM, Please enter a time between working hours : ")
											
										for i in Tech_DataBase[Tech_ID] :
											if type(i[0])!=str :
												while Session_Start >= i[1] and Session_Start < i[2] :
													Session_Start = input("This appointment is already booked, Please Enter an other time for start of session : ")
										Session_End   = input("Session ends at : ")
										
										New_Appointment=list()
										New_Appointment.append(Client_ID)
										New_Appointment.append(Session_Start)
										New_Appointment.append(Session_End)
										Tech_DataBase[Tech_ID].append(New_Appointment)								
										print("/----------------------Appointment booked successfully----------------------/")
								except :
										print("Tech ID should be an integer number")
					
							elif Admin_choice == "2" :												#Admin mode --> Appointment Management --> Edit an appointment
									try :		#To avoid non integer input
										Client_ID = int(input("Enter Client ID : "))						
										while Client_ID not in Client_DataBase :
											Client_ID = int(input("Incorrect Id, Please Enter correct Client ID : "))
										try :   #To avoid no return function
												AppointmentIndex,PairKey = AppointmentIndexInTechDataBase(Client_ID)
												Session_Start = input ("Please enter the new start time : ")
												while Session_Start[ :2] == "11" or Session_Start[ :2] == "12" :
													Session_Start = input("Appointments should be between 01:00PM to 10:00PM, Please enter a time between working hours : ")
													
												for i in Tech_DataBase[Tech_ID] :
													if type(i[0])!=str :
														while Session_Start >= i[1] and Session_Start < i[2] :
															Session_Start = input("This appointment is already booked, Please Enter an other time for start of session : ")
												Session_End = input ("Please enter the new end time : ")
												Tech_DataBase[PairKey][AppointmentIndex]=[Client_ID,Session_Start,Session_End]							
												print("/----------------------appointment edited successfully----------------------/")
										except :
												print("No Appointment for this Client")
									except :
										print("Tech ID should be an integer number")
						
							elif Admin_choice == "3" :												#Admin mode --> Appointment Management --> Cancel an appointment
									try :		#To avoid non integer input
										Client_ID = int(input("Enter Client ID : "))
										while Client_ID not in Client_DataBase :
											Client_ID = int(input("Invorrect ID, Enter Client ID : "))
										try :
												AppointmentIndex,PairKey = AppointmentIndexInTechDataBase(Client_ID)						
												Tech_DataBase[PairKey].pop(AppointmentIndex)
												print("/----------------------appointment canceled successfully----------------------/")
										except :
												print("No Appointment for this Client")
									except :	 #To avoid no return function
										print("Client ID should be an integer number")
							
							elif Admin_choice == "E" :												#Back
										break
							
							else :
										print("please enter a correct choice")
						
						elif AdminOptions == "E" :															#Back
							break
						
						else :
							print("Please enter a correct option")
					
				
					elif Password != "1234" :
						if tries < 2 :
							Password = input("Password incorrect, please try again : ")
							tries += 1
						else :
							print("Incorrect password, no more tries")
							tries_flag = "Close the program"
							break
				
					Write_tech.Write_Client_DataBase(Client_DataBase)
					Write_tech.Write_Tech_DataBase(Tech_DataBase)
					
					
		elif Admin_user_mode == "2" :																		#User mode
			print("****************************************\n|         Welcome to user mode         |\n****************************************")
			while True :
				print("\n-----------------------------------------")
				print("|To view ICX's departments Enter 1 |")
				print("|To view ICX's techs Enter 2     |")
				print("|To view clients' residents Enter 3    |")
				print("|To view client's details Enter 4      |")
				print("|To view Tech's appointments Enter 5  |")
				print("|To be Back Enter E                     |")
				print("-----------------------------------------")
				UserOptions = input("Enter your choice : ")
				UserOptions = UserOptions.upper()
				
				if   UserOptions == "1" :											#User mode --> view icx's departments
							print("ICX's departments :")
							for i in Tech_DataBase :
								print("	"+Tech_DataBase[i][0][0])
					
				elif UserOptions == "2" :											#User mode --> view icx's Tech
							print("ICX's techs :")
							for i in Tech_DataBase :
								print("	"+Tech_DataBase[i][0][1]+" in "+Tech_DataBase[i][0][0]+" department, from "+Tech_DataBase[i][0][2])
								
				elif UserOptions == "3" :											#User mode --> view Clients' residents
					for i in Client_DataBase :
						print("	Client : "+Client_DataBase[i][2]+" in "+Client_DataBase[i][0]+" department and followed by "+Client_DataBase[i][1]+", age : "+Client_DataBase[i][3]+", from : "+Client_DataBase[i][5]+", RoomNumber : "+Client_DataBase[i][6])
				
				elif UserOptions == "4" :											#User mode --> view Client's details
					try :				#To avoid non integer input
						Client_ID = int(input("Enter Client's ID : "))
						while Client_ID not in Client_DataBase :
							Client_ID = int(input("Incorrect Id, Please enter Client ID : "))
						print("	Client name        : ",Client_DataBase[Client_ID][2])
						print("	Client address     : ",Client_DataBase[Client_ID][5])
						print("	Client is in "+Client_DataBase[Client_ID][0]+" department")
						print("	Client is followed by Tech : "+Client_DataBase[Client_ID][1])
					except :
						print("Client ID should be an integer number")
							
				elif UserOptions == "5" :											#User mode --> view Tech's appointments
					try :				#To avoid non integer input
						Tech_ID = int(input("Enter Tech's ID : "))
						while Tech_ID not in Tech_DataBase :
							Tech_ID = int(input("Incorrect Id, Please enter Tech ID : "))
						print(Tech_DataBase[Tech_ID][0][1]+" has appointments :")
						for i in Tech_DataBase[Tech_ID] :
							if type(i[0])==str :
								continue
							else :
								print("	from : "+i[1]+"    to : "+i[2])
					except :
						print("Tech ID should be an integer number")
					
				elif UserOptions == "E" :											#Back
					break
					
				else :
					print("Please Enter a correct choice")
					
					
		else :
			print("Please choose just 1 or 2")
