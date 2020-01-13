from test.utils import *


class TestGebalaSheet:
    def test_program_two(self):
        simple_program_string = """
        [ Rozklad liczby na czynniki pierwsze ]
DECLARE
    n, m, reszta, potega, dzielnik
BEGIN
    READ n;
    dzielnik ASSIGN 2;
    m ASSIGN dzielnik TIMES dzielnik;
    WHILE n GEQ m DO
        potega ASSIGN 0;
        reszta ASSIGN n MOD dzielnik;
        WHILE reszta EQ 0 DO
            n ASSIGN n DIV dzielnik;
            potega ASSIGN potega PLUS 1;
            reszta ASSIGN n MOD dzielnik;
        ENDWHILE
        IF potega GE 0 THEN [ czy znaleziono dzielnik ]
            WRITE dzielnik;
            WRITE potega;
        ELSE
            dzielnik ASSIGN dzielnik PLUS 1;
            m ASSIGN dzielnik TIMES dzielnik;
        ENDIF
    ENDWHILE
    IF n NEQ 1 THEN [ ostatni dzielnik ]
        WRITE n;
        WRITE 1;
    ENDIF
END

                                 """
        a = b'12345678901'
        out, err, asm, cost = run_vm(simple_program_string, input=a)
        assert err is b''
        print(" ")
        for o in out:
            print(o)
        print('\nprogram-two, subtest1, number: 12345678901, cost: ', cost)

        a = b'12345678903'
        out, err, asm, cost = run_vm(simple_program_string, input=a)
        assert err is b''
        print(" ")
        for o in out:
            print(o)
        print('\nprogram-two, subtest1, number: 12345678903, cost: ', cost)

    def test_program_one(self):
        simple_program_string = """
[ sito Eratostenesa ]
DECLARE
    n, j, sito(2:100)
BEGIN
    n ASSIGN 100;
    FOR i FROM n DOWNTO 2 DO
        sito(i) ASSIGN 1;
    ENDFOR
    FOR i FROM 2 TO n DO
        IF sito(i) NEQ 0 THEN
            j ASSIGN i PLUS i;
            WHILE j LEQ n DO
                sito(j) ASSIGN 0;
                j ASSIGN j PLUS i;
            ENDWHILE
            WRITE i;
        ENDIF
    ENDFOR
END
                                 """
        out, err, asm, cost = run_vm(simple_program_string)
        assert err is b''
        print(" ")
        for o in out:
            print(o)
        print('\nprogram-1, cost: ', cost)

    def test_program_zero(self):
        simple_program_string = """
         DECLARE
    a, b
BEGIN
    READ a;
    IF a GEQ 0 THEN
	WHILE a GE 0 DO
	    b ASSIGN a DIV 2;
	    b ASSIGN 2 TIMES b;
	    IF a GE b THEN 
                WRITE 1;
	    ELSE 
                WRITE 0;
	    ENDIF
	    a ASSIGN a DIV 2;
	ENDWHILE
    ENDIF
END

                                 """
        a = b'1345601'
        out, err, asm, cost = run_vm(simple_program_string, input=a)
        valid_number = "101001000100001000001"
        valid_number_reversed = valid_number[::-1]
        assert err is b''
        for i, o in enumerate(out):
            assert o == valid_number_reversed[i]
        print('\nprogram-0, cost: ', cost)

    def test_zero_div_mod(self):
        simple_program_string = """
                                 [ div-mod.imp 
                                      1 0
                                      1 0 0 0
                                    ]
                                    DECLARE
                                        a, b, c
                                    BEGIN
                                        READ a;
                                        READ b;
                                        c ASSIGN a DIV a;
                                        WRITE c;
                                        c ASSIGN a DIV b;
                                        WRITE c;
                                        c ASSIGN a MOD a;
                                        WRITE c;
                                        c ASSIGN a MOD b;
                                        WRITE c;
                                    END


                                 """
        a = b'1 0'
        out, err, asm, cost = run_vm(simple_program_string, input=a)
        assert err is b''
        assert int(out[0]) == 1
        assert int(out[1]) == 0
        assert int(out[2]) == 0
        assert int(out[3]) == 0
        print('\n0-div-mod, cost: ', cost)

    def test_one_numbers(self):
        simple_program_string = """
            [ numbers.imp - liczby ]
                DECLARE
                    a, b, c, t(-6:6), d, e, f, g, h, i, j, tab(-5:5)
                BEGIN
                    WRITE 0;
                    WRITE 1;
                    WRITE -2;
                    WRITE 10;
                    WRITE -100;
                    WRITE 10000;
                    WRITE -1234567890;
                
                    a ASSIGN 1234566543;
                    b ASSIGN -677777177;
                    c ASSIGN 15;
                    t(2) ASSIGN -555555555;
                    d ASSIGN 8888;
                    tab(-4) ASSIGN 11;
                    t(0) ASSIGN -999;
                    e ASSIGN 1111111111;
                    tab(0) ASSIGN 7777;
                    f ASSIGN -2048;
                    g ASSIGN -123;
                    t(-3) ASSIGN t(0);
                    tab(-5) ASSIGN a;
                    tab(-5) ASSIGN tab(0) DIV tab(-4);
                    t(-5) ASSIGN tab(0);
                
                    READ h;
                    i ASSIGN 1;
                    j ASSIGN h PLUS c;
                    
                    WRITE j; [ j = h + 15 ]
                    WRITE c; [ c = 15 ]
                    WRITE t(-3); [ -999 ]
                    WRITE t(2); [ -555555555 ]
                    WRITE t(-5); [ 7777 ]
                    WRITE t(0); [ -999 ]
                    WRITE tab(-4); [ 11 ]
                    WRITE tab(-5); [ 707 ]
                    WRITE tab(0); [ 7777 ]
                    END
                                 """
        h = -1337
        a = b'-1337'
        out, err, asm, cost = run_vm(simple_program_string, input=a)
        assert err is b''
        print('\n1-numbers, cost: ', cost)
        print('result: ')
        valid_result = [0, 1, -2, 10, -100, 10000, -1234567890, \
                        15 + h, 15, -999, -555555555, 7777, -999, 11, 707, 7777]
        for i, o in enumerate(out):
            assert int(o) == valid_result[i]

    def test_two_fib(self):
        simple_program_string = """
                   [ Fibonacci 26
? 1
> 121393
]
DECLARE
  tab(-987654321:1234567890),
  a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z
BEGIN
  READ tab(-121212121);
  a ASSIGN tab(-121212121);
  b ASSIGN a;
  c ASSIGN b PLUS a;
  d ASSIGN c PLUS b;
  e ASSIGN d PLUS c;
  f ASSIGN e PLUS d;
  g ASSIGN f PLUS e;
  h ASSIGN g PLUS f;
  i ASSIGN h PLUS g;
  j ASSIGN i PLUS h;
  k ASSIGN j PLUS i;
  l ASSIGN k PLUS j;
  m ASSIGN l PLUS k;
  n ASSIGN m PLUS l;
  o ASSIGN n PLUS m;
  p ASSIGN o PLUS n;
  q ASSIGN p PLUS o;
  r ASSIGN q PLUS p;
  s ASSIGN r PLUS q;
  t ASSIGN s PLUS r;
  u ASSIGN t PLUS s;
  v ASSIGN u PLUS t;
  w ASSIGN v PLUS u;
  x ASSIGN w PLUS v;
  y ASSIGN x PLUS w;
  z ASSIGN y PLUS x;
  a ASSIGN 10000 TIMES z;
  tab(a) ASSIGN z;
  WRITE tab(a);
END


                                 """
        a = b'1'
        out, err, asm, cost = run_vm(simple_program_string, input=a)
        assert err is b''
        assert int(out[0]) == 121393
        print('\n2-fib, cost: ', cost)

    def test_three_fib_factorial(self):
        simple_program_string = """
                        [ Silnia  PLUS  Fibonacci
? 20
> 2432902008176640000
> 6765
]
DECLARE
    f(0:100), s(0:100), i(0:100), n, k, l
BEGIN
    READ n;
    f(0) ASSIGN 0;
    s(0) ASSIGN 1;
    i(0) ASSIGN 0;
    f(1) ASSIGN 1;
    s(1) ASSIGN 1;
    i(1) ASSIGN 1;
    FOR j FROM 2 TO n DO
	k ASSIGN j MINUS 1;
        l ASSIGN k MINUS 1;
	i(j) ASSIGN i(k) PLUS 1;
	f(j) ASSIGN f(k) PLUS f(l);
        s(j) ASSIGN s(k) TIMES i(j);
    ENDFOR
    WRITE s(n);
    WRITE f(n);
END

                                   """
        a = b'20'
        out, err, asm, cost = run_vm(simple_program_string, input=a)
        assert err is b''
        assert int(out[0]) == 2432902008176640000
        assert int(out[1]) == 6765
        print('\n3-fib-factorial, cost: ', cost)

    def test_four_factorial(self):
        simple_program_string = """
 [ Silnia
? 20
> 2432902008176640000
]
DECLARE
  s(0:100), n, m, a, j
BEGIN
    READ n;
    s(0) ASSIGN 1;
    m ASSIGN n;
    FOR i FROM 1 TO m DO
		a ASSIGN i MOD 2;
		j ASSIGN i MINUS 1;
		IF a EQ 1 THEN
			s(i) ASSIGN s(j) TIMES m;
		ELSE
			s(i) ASSIGN m TIMES s(j);
		ENDIF
		m ASSIGN m MINUS 1;
    ENDFOR
    WRITE s(n);
END


                                       """
        a = b'20'
        out, err, asm, cost = run_vm(simple_program_string, input=a)
        assert err is b''
        assert int(out[0]) == 2432902008176640000
        print('\n4-factorial, cost: ', cost)

    def test_five_tab(self):
        simple_program_string = """
[ tab.imp ]
                        DECLARE
                            n, j, ta(0:25), tb(0:25), tc(0:25)
                        BEGIN
                            n  ASSIGN  25;
                            tc(0)  ASSIGN  n;
                            tc(n)  ASSIGN  n MINUS n;
                            FOR i FROM tc(0) DOWNTO tc(n) DO
                                ta(i)  ASSIGN  i;
                                tb(i)  ASSIGN  n MINUS i;
                            ENDFOR
                            FOR i FROM tc(n) TO tc(0) DO
                                tc(i)  ASSIGN  ta(i) TIMES tb(i);
                            ENDFOR
                            FOR i FROM 0 TO n DO
                                WRITE tc(i);
                            ENDFOR
                        END
                                           """
        out, err, asm, cost = run_vm(simple_program_string)
        assert err is b''
        print('\n5-tab, cost: ', cost)
        for o in out:
            print(o)

    def test_six_mod_mult(self):
        simple_program_string = """
            [ a ^ b mod c 
? 1234567890
? 1234567890987654321
? 987654321
> 674106858
]
DECLARE
    a, b, c, wynik, pot, wybor
BEGIN
    READ a;
    READ b;
    READ c;
    wynik ASSIGN 1;
    pot ASSIGN a MOD c;
    WHILE b GE 0 DO
		wybor ASSIGN b MOD 2;
		IF wybor EQ 1 THEN
			wynik ASSIGN wynik TIMES pot;
			wynik ASSIGN wynik MOD c;
		ENDIF
		b ASSIGN b DIV 2;
		pot ASSIGN pot TIMES pot;
		pot ASSIGN pot MOD c;
    ENDWHILE
    WRITE wynik;
END

                                               """
        a = b'1234567890 1234567890987654321 987654321'
        out, err, asm, cost = run_vm(simple_program_string, input=a)
        assert err is b''
        assert int(out[0]) == 674106858
        print('\n6-mod-mult, cost: ', cost)

    def test_seven_loop_three(self):
        simple_program_string = """
            [ loopiii.imp - zagniezdzone petle 
                0 0 0
                31000 40900 2222010
                
                1 0 2
                31001 40900 2222012
            ]
            DECLARE 
                a, b, c
            BEGIN
                READ a;
                READ b;
                READ c;
                FOR i FROM 111091 TO 111110 DO
                    FOR j FROM 209 DOWNTO 200 DO
                        FOR k FROM 11 TO 20 DO
                            a  ASSIGN  a PLUS k;
                        ENDFOR
                        b  ASSIGN  b PLUS j;
                    ENDFOR
                    c  ASSIGN  c PLUS i;
                ENDFOR
                WRITE a;
                WRITE b;
                WRITE c;
            END

         """
        a = b'0 0 0'
        out, err, asm, cost = run_vm(simple_program_string, input=a)
        assert err is b''
        assert int(out[0]) == 31000
        assert int(out[1]) == 40900
        assert int(out[2]) == 2222010
        print('\n7-loop-3, cost, first subtest: ', cost)

        a = b'1 0 2'
        out, err, asm, cost = run_vm(simple_program_string, input=a)
        assert err is b''
        assert int(out[0]) == 31001
        assert int(out[1]) == 40900
        assert int(out[2]) == 2222012
        print('\n7-loop-3, cost, second subtest: ', cost)

    def test_eight_for(self):
        simple_program_string = """
        [ for.imp 
  12 23 34
  507 4379 0
]
DECLARE
	a, b, c
BEGIN
	READ a;
	READ b;
	READ c;
	FOR i FROM 9 DOWNTO 0 DO
		FOR j FROM 0 TO i DO
			FOR k FROM 0 TO j DO
				a  ASSIGN  a PLUS k;
				c  ASSIGN  k TIMES j;
				c  ASSIGN  c PLUS i;
				b  ASSIGN  b PLUS c;
			ENDFOR
		ENDFOR
	ENDFOR
	WRITE a;
	WRITE b;
	WRITE c;
END

         """
        a = b'12 23 34'
        out, err, asm, cost = run_vm(simple_program_string, input=a)
        assert err is b''
        assert int(out[0]) == 507
        assert int(out[1]) == 4379
        assert int(out[2]) == 0
        print('\n8-for, cost: ', cost)

    def test_nine_sort(self):
        simple_program_string = """
        [ sort.imp 
]
DECLARE
	tab(-11:10), x, q, w, j, k, n, a, b
BEGIN
	a ASSIGN -11;
	b ASSIGN 10;
	n ASSIGN 23;
	q ASSIGN 5;
	w ASSIGN 1;
	[generowanie nieposortowanej tablicy]
	FOR i FROM b DOWNTO a DO
		w  ASSIGN  w TIMES q;
		w  ASSIGN  w MOD n;
		tab(i)  ASSIGN  w;
	ENDFOR
	[wypisywanie nieposortowanej tablicy]
	FOR i FROM a TO b DO
		WRITE tab(i);
	ENDFOR
	WRITE 1234567890;
	[sortowanie]
        q ASSIGN a PLUS 1;
	FOR i FROM q TO b DO
		x  ASSIGN  tab(i);
		j  ASSIGN  i;
		WHILE j GE a DO
			k  ASSIGN  j MINUS 1;
			IF tab(k) GE x THEN
				tab(j)  ASSIGN  tab(k);
				j  ASSIGN  j MINUS 1;
			ELSE
				k  ASSIGN  j;
				j  ASSIGN  a;
			ENDIF
		ENDWHILE
		tab(k)  ASSIGN  x;
	ENDFOR
	[wypisywanie posortowanej tablicy]
	FOR i FROM a TO b DO
		WRITE tab(i);
	ENDFOR
END

             """
        out, err, asm, cost = run_vm(simple_program_string)
        assert err is b''
        for o in out:
            print(o)
        print('\n9-sort, cost: ', cost)
