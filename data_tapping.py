import pyautogui as pag
from time import sleep
from datetime import datetime,timedelta


def input_tanggal():
	hariini = (datetime.now().strftime("%d-%m-%Y"))
	tgl = pag.prompt(title="Masukan Tanggal", default=hariini)
	return tgl


sleep(3)
edge = pag.locateCenterOnScreen("edge.png")
print(edge)
pag.moveTo(edge)
pag.click(clicks=2, interval=0.25)


sleep(2)
user = pag.locateCenterOnScreen("userid.png")
print(user)
pag.moveTo(user)
pag.moveTo(user.x , user.y + 30)
pag.click()
pag.write("vu08a12")

password = pag.locateCenterOnScreen("password.png")
print(password)
pag.moveTo(password)
pag.moveTo(password.x , password.y + 30)
pag.click()
pag.write("yamaha06*")

loginbutton = pag.locateCenterOnScreen("login.png")
print(loginbutton)
pag.moveTo(loginbutton)
pag.click()

sleep(2)
attendance = pag.locateCenterOnScreen("attendance.png")
print(attendance)
pag.moveTo(attendance)
pag.click()

attendance = pag.locateCenterOnScreen("attend-time.png")
print(attendance)
pag.moveTo(attendance)
pag.click()

sleep(2)
if __name__ == "__main__":
	tglawal = input_tanggal()

sleep(1)
dated = pag.locateCenterOnScreen("date.png")
print(dated)
pag.moveTo(dated)
pag.moveTo(dated.x + 150, dated.y)
pag.click()
pag.press("backspace", presses=10)
pag.write(tglawal)
	

sleep(1)
dated = pag.locateCenterOnScreen("date.png")
print(dated)
pag.moveTo(dated)
pag.moveTo(dated.x + 330, dated.y)
pag.click()
pag.press("backspace", presses=10)
pag.write(tglawal)

sleep(1)
dated = pag.locateCenterOnScreen("date.png")
print(dated)
pag.moveTo(dated)
pag.moveTo(dated.x + 195, dated.y + 30 )
pag.click()


sleep(1)
alll = pag.locateCenterOnScreen("26548.png")
print(alll)
pag.moveTo(alll)
pag.moveTo(alll.x - 60, alll.y)
pag.click()

confirm = pag.locateCenterOnScreen("confirm.png")
print(confirm)
pag.moveTo(confirm)
pag.click()

sleep(2)
retrive = pag.locateCenterOnScreen("retrive.png")
print(retrive)
pag.moveTo(retrive)
pag.click()

sleep(5)
export = pag.locateCenterOnScreen("export.png")
print(export)
pag.moveTo(export)
pag.click()

sleep(1)
confir = pag.locateCenterOnScreen("exit.png")
pag.moveTo(confir)
pag.click()