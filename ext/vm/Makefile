FLAGS = -W -pedantic -std=c++17 -O3 -I/usr/local/include

.PHONY = all clean cleanall

all: maszyna-wirtualna maszyna-wirtualna-cln

maszyna-wirtualna: lexer.o parser.o mw.o main.o
	$(CXX) $^ -o $@
	strip $@

maszyna-wirtualna-cln: lexer.o parser.o mw-cln.o main.o
	$(CXX) $^ -o $@ -l cln
	strip $@

%.o: %.cc
	$(CXX) $(FLAGS) -c $^

lexer.cc: lexer.l parser.hh
	flex2 -o $@ $<

parser.cc parser.hh: parser.y
	bison3 -Wall -d -o parser.cc $^

clean:
	rm -f *.o parser.cc parser.hh lexer.cc

cleanall: clean
	rm -f maszyna-wirtualna maszyna-wirtualna-cln
