
# we don't need to build the python version of sis
TARGET_APP=sis-cxx 

all::
	chmod +x sis-java sis-python

sis-cxx: codingsis.o

