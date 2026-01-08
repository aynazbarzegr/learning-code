import random 
def start_game():
    print("be bazi hads adad khosh amdi")
    gaes_number =int (input("lottan hads khod ra vard konid(az 1 ta 100 )"))
    secret_number =random.randint(1,100)
    attempts = 0
    while True:
        attempts +=1
        if gaes_number > secret_number :
            print("biya paayintar")
            print(f"talash ={attempts}")
        elif gaes_number < secret_number :   
             print("boro balater")
        elif gaes_number == secret_number :
             print("hads shoma dorste")
             break
start_game()        