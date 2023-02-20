#/usr/share/python3
import psutil
import os

def colsw(col):
	colors = {
		0: "\033[01;97m",	# white?
		5: "\033[0;0m",		# default terminal color
		1: "\033[01;31m",	# red
		2: "\033[01;92m",	# green
		3: "\033[01;94m",	# blue
		4: "\033[01;93m",	# yellow
	}
	print(colors[col],end='')

colsw(3)
print('''
⡏⠙⠻⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''',end="")
colsw(0)
print('''⢀⣤⠶⠟⠛⠿⠗⣦⣄⠀⠀⠀⠀''',end="")
colsw(3)
print('''
⡇⠀⠀⠀⠀⠙⠦⣄⠀⠀⠀⠀⠀⠀⠀''',end="")
colsw(0)
print('''⢀⣴⠋⠀⠀⠀⠀⠀⠀⠀⠉⢧⡀''',end="")
colsw(3)
print('''⠀⠀
⠙⢄⠀⠀⠀⠀⠀⠙⠲⢦⣀⠀⠀⠀⠀''',end="")
colsw(0)
print('''⣸⠋⠀⠀⠀''',end="")
colsw(1)
print("⢠⣤",end="")
colsw(0)
print('''⠀⠀⠀⠀⠘⢳⡀⠀
''',end="")
colsw(3)
print('''⠀⠈⠳⣀⠀⠀⠀⠀⠀⠀⠉⠻⢦⡀''',end="")
colsw(4)
print("⣼⠴⠖⠒⣄⠀",end="")
colsw(1)
print("⠈⠉",end="")
colsw(0)
print('''⠀⠀⠀⠀⠀⠈⣵⠀
''',end="")
colsw(3)
print('''⠀⠀⠀⠈⠳⣄⠀⠀⠀⠀⠀⠀''',end="")
colsw(4)
print("⢀⣿⠋⠀⠀⠀⠈⢆",end="")
colsw(0)
print('''⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣
''',end="")
colsw(3)
print('''⠀⠀⠀⠀⠀⠈⠳⢦⡀⠀⠀⠀''',end="")
colsw(4)
print("⣸⠁⠀⠀⠀⠀⣠⣼",end="")
colsw(0)
print('''⣷⡤⢤⣄⠀⠀⠀⠀⠀⣻
''',end="")
colsw(3)
print('''⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⣤''',end="")
colsw(4)
print("⣴⠋⠀⠀⠀⢀⣴",end="")
colsw(3)
print('''⣿⣄  ''',end="")
colsw(0)
print('''⢘⣻⠀⠀⠀⠀⠀⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''',end="")
colsw(4)
print("⠻⣔⣢⣲⣼⡿",end="")
colsw(3)
print('''⣿⠟⠁ ''',end="")
colsw(0)
print('''⠀⢸⠾⠀⠀⠀⠀⠀⢸
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ⠀⠀⠀⠀⣾⡇⠀⠀⠀⠀⠀⠀ ''', end="")
if open("/sys/devices/virtual/dmi/id/product_name", "r"): host=open("/sys/devices/virtual/dmi/id/product_name", "r").read().strip()
colsw(2)
print ("\tHost: ",end="")
colsw(5)
print(host, end="")
colsw(0)
print('''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠇''',end="")
colsw(2)
print("\tKernel: ",end="")
colsw(5)
print(os.uname()[2])
colsw(0)
print ('''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿ ''',end="")
cpu = os.popen('lscpu | grep "Model name"').readlines()[0].split("  ")[-1]
colsw(2)
print("\tCPU: ",end="")
colsw(5)
print(f"{cpu.split('TM')[0]}{os.cpu_count()}{str(cpu.split('TM')[1]).split('CPU @')[0]}{str(cpu.split('TM')[1]).split('CPU @')[-1]}",end="")
colsw(0)
print('''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡏⠀⠀⠀⠀⠀⠀⠀ ''',end="")
gpu = os.popen('lspci | grep "VGA compatible controller: "').readlines()[0].split(": ")[-1].split(" (")[0].split(" [")[0]
colsw(2)
print("\tGPU: ",end="")
colsw(5)
print(f"{gpu}")
colsw(0)
print ('''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡏⠀⠀⠀⠀⠀⠀⠀ ''',end="")
colsw(2)
memo = psutil.virtual_memory()
print ("\tMemory: ",end="")
colsw(5)
print(f"{str(round(memo[3]/1000000, 0)).split('.')[0]}MiB / {str(round(memo[0]/1000000, 0)).split('.')[0]}MiB")
print()
colsw(5)
