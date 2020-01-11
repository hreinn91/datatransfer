
db = "HELLO"
PY	 = python 

MAIN = data_processing/main.py

all: 
	${PY} $(MAIN) $(db)
