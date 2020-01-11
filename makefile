
input = "EMPTY"


PY	 = python 
MAIN = data_processing/main.py

all: 
	${PY} $(MAIN) $(input)
