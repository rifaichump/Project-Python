from time import sleep
import socket
device_name = "RIFAI BELAJAR PYTHON"

def menu_message():
  style = "#" * (len(device_name) + 6)
  print(style)
  print(f"## {device_name} ##")
  print(style)
  
def exit_message():
  print("Program akan di hentikan..")
  sleep(1)
  print("3..")
  sleep(1)
  print("2..")
  sleep(1)
  print("1...")
  sleep(1)
  print("Program berhenti!")
  exit()
  
if __name__ == "__main__":
  menu_message()
  exit_message()