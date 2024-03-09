from games import g_kelinci
from tools import kalkulator
from index import menu_message, exit_message

def menu():
  pilihan = int(input("Menu pilihan\n\n1. Game Kelinci\n2. Kalkulator (penambahan)\n3. Keluar\n\nIngin pilih nomor berapa?: "))
  if pilihan == 1:
    g_kelinci.start()
  elif pilihan == 2:
    kalkulator.start()
  elif pilihan == 3:
    exit_message()
  else:
    print("Hanya boleh pilih yang ada di menu!")
  
def main():
   menu_message()
   menu()
 
if __name__ == "__main__":
  main()