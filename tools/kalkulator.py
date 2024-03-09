import main
def start():
  c = int(input("Masukan angka pertama: "))
  d = int(input("Masukan angka kedua: "))
  e = c + d
  str(print(f"\nHasil nya: {e}"))
  pilihan = str(input("\nIngin melanjutkan? Ketik [y/n] : "))
  if pilihan == "n":
    main.menu()
    
if __name__ == "__main__":
  start()