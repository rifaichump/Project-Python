import random
import main

def start():
  while True:
    tebakan = random.randint(1, 4)
    bentuk_goa = "|_|"
    goa_kosong = [bentuk_goa] * 4
    goa = goa_kosong.copy()
    goa[tebakan - 1] = "|@|"
    goa_kosong = ' '.join(goa_kosong)
    goa = ' '.join(goa)
    print(f'''
    Coba perhatikan Kotak dibawah ini.
    {goa_kosong}
    ''')
    answer = int(input("Menurut kamu, kelinci itu di kotak nomor berapa? Ketik (1/2/3/4) : "))
    if answer == tebakan:
      print(f"{goa}, Selamat kamu menang!")
    else:
      print(str(f"{goa}, Maaf kamu kalah..., Kelinci itu berada di nomor {tebakan}"))
    again = input("\n\nApakah ingin bermain lagi? [y/n]: ")
    if again == "n":
      main.menu()

if __name__ == "__main__":
  start()