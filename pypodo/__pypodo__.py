from pathlib import Path

def help():
	help_txt = """\
	
NAME
       pypodo

SYNOPSIS
       pypodo is a todolist program who works with a .todo file at the root of the home directory
       pypodo [MODE] [PARAMETERS]...

       help : display this help
       list : print the todolist with an index for each task, with tag filtered on [PARAMETER]
              pypodo list #print the todolist
              pypodo list linux #print the todolist filtered on tag linux
       add : add [PARAMETER] to the todolist with an index autogenerated
              pypodo add "my first task" #add the task "my first task" to the todolist
       delete : delete the task identified with the index equals to [PARAMETER] from the todolist
              pypodo delete 3 #deletes the task identified by index equals 3	
       tag : add the tag [PARAMETER[2]] to the task the task identified with the index equals to [PARAMETER[1]]
              pypodo 3 linux #add the tag linux to the task identified with the index equals to 3
       untag : delete all tags from the task identified with the index equals to [PARAMETER]
              pypodo untag 3 #deletes all tags frome the task identified by index equals 3
       clear : reorder the todolist in consecutives index
              pypodo clear	
              			
	"""
	print(help_txt)

def list():
	import sys
	check()
	home = str(Path.home())
	if len(sys.argv) > 3:
		sys.exit("0 ou 1 parametre attendu pour pypodo list : le tag")
	with open(home+"/.todo", 'r') as f:
		for line in f.readlines():
			if len(sys.argv) == 2:
				print(line, end = '')	
			elif len(sys.argv) == 3:
				if '#'+sys.argv[2] in line:
					print(line, end = '')
					
def add():
	import sys
	check()
	home = str(Path.home())
	if len(sys.argv) != 3:
		sys.exit("1 et 1 seul parametre attendu pour pypodo add : la tache a ajouter") 
	else:
		with open(home+"/.todo", 'r') as f:
			lines = f.readlines()
		if len(lines) > 0:
			last_line = lines[len(lines)-1]
			index = int(last_line.split()[0])+1
		else:
			index = 1	
		with open(home+"/.todo", 'a') as f:
			f.write(str(index)+" "+sys.argv[2]+'\n')		

def delete():
	import sys
	import re
	check()
	home = str(Path.home())
	if len(sys.argv) == 3:
		if not re.findall("^\d+$",sys.argv[2]):
			sys.exit("1 et 1 seul parametre attendu pour pypodo del : l index a supprimer au format numerique")		
		with open(home+"/.todo", 'r') as f:
			lines = f.readlines()
		with open(home+"/.todo", 'w') as f:	    
			for line in lines:
				if not re.findall("^"+sys.argv[2]+' ',line):
					f.write(line)	
	else:
		sys.exit("1 et 1 seul parametre pour attendu pypodo del : l index a supprimer au format numerique")							

def clear():
	import sys
	import re
	check()
	if len(sys.argv) != 2:
		sys.exit("0 parametre attendu pour pypodo clear") 
	else:
		index=1
		home = str(Path.home())
		with open(home+"/.todo", 'r') as f:
			lines = f.readlines()
		with open(home+"/.todo", 'w') as f:	    
			for line in lines:
				replaced = re.sub("^\d+ ",str(index)+" ", line)
				index=index+1
				f.write(replaced)

def check():
	import sys
	import re
	import os
	index=1
	home = str(Path.home())
	file_exists = os.path.isfile(home+"/.todo") 
	if file_exists:
		with open(home+"/.todo", 'r') as f:
			for line in f.readlines():
				if not re.findall("^\d+ ",line):
					sys.exit("erreur : vérifier le fichier .todo")
	else:
		open(home+"/.todo", "w")

				
def untag():
	import sys
	import re
	check()
	home = str(Path.home())
	if len(sys.argv) == 3:
		if not re.findall("^\d+$",sys.argv[2]):
			sys.exit("1 et 1 seul parametre attendu pour pypodo untag : l index dont le tag doit etre supprime")		
		with open(home+"/.todo", 'r') as f:
			lines = f.readlines()
		with open(home+"/.todo", 'w') as f:	    
			for line in lines:
				if not re.findall("^"+sys.argv[2]+' ',line):
					f.write(line)
				if re.findall("^"+sys.argv[2]+' ',line):
					f.write(re.sub(" #.*" ,"", line))								
	else:
		sys.exit("1 et 1 seul parametre pour attendu pypodo untag : l index dont le tag doit etre supprime")	


def tag():
	import sys
	import re
	check()
	home = str(Path.home())
	if len(sys.argv) == 4:
		if not re.findall("^\d+$",sys.argv[2]):
			sys.exit("2 parametres attendus pour pypodo tag : l index de la tache au format numérique et le tag à ajouter")		
		with open(home+"/.todo", 'r') as f:
			lines = f.readlines()
		with open(home+"/.todo", 'w') as f:	    
			for line in lines:
				if not re.findall("^"+sys.argv[2]+' ',line):
					f.write(line)
				if re.findall("^"+sys.argv[2]+' ',line):
					f.write(line.rstrip('\n')+" #"+sys.argv[3]+"\n")							
	else:
		sys.exit("2 parametres attendus pour pypodo tag : l index de la tache au format numérique et le tag à ajouter")	

def pypodo():	
	import sys
	if len(sys.argv) == 1:
	    help()
	elif sys.argv[1] == "list":
	    list()
	elif sys.argv[1] == "add":
	    add()
	elif sys.argv[1] == "delete":
	    delete()
	elif sys.argv[1] == "clear":
	    clear()    
	elif sys.argv[1] == "help":
	    help()
	elif sys.argv[1] == "untag":
	    untag()
	elif sys.argv[1] == "tag":
	    tag()
	elif sys.argv[1] == "help":
	    tag() 
	else:
	     help()	
	      
