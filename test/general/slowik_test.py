from test.utils import *


class TestSlowik:
    def test_zero(self):
        simple_program_string = """
        DECLARE
    a, b, c, d, e, f, g, h, x
BEGIN
    READ a;
    READ b;
    READ c;
    READ d;
    READ e;
    READ f;
    READ g;
    READ h;
    x ASSIGN 0;
    FOR i FROM 1 TO a DO
        FOR j FROM -1 DOWNTO b DO
            FOR k FROM 1 TO c DO
                FOR l FROM -1 DOWNTO d DO
                    FOR m FROM 1 TO e DO
                        FOR n FROM -1 DOWNTO f DO
                            FOR o FROM 1 TO g DO
                                FOR p FROM -1 DOWNTO h DO
                                    x ASSIGN x PLUS 1;
                                ENDFOR
                            ENDFOR
                        ENDFOR
                    ENDFOR
                ENDFOR
            ENDFOR
        ENDFOR
    ENDFOR
END
                                 """
        a = b'10 20 30 40 50 60 70 80'
        out, err, asm, cost = run_vm(simple_program_string, input=a)
        assert err is b''
        print(" ")
        for o in out:
            print(o)
        print('\ntest-zero, cost: ', cost)

    def test_one(self):
        simple_program_string_first = """
        DECLARE
    j, k
BEGIN
    READ k;
    FOR i FROM 0 TO k DO
        IF i EQ 1 THEN
            j ASSIGN 1;
        ENDIF
        IF i GE 1 THEN
            j ASSIGN j TIMES 2;
        ENDIF
    ENDFOR
    IF k GEQ 1 THEN
        WRITE j;
    ENDIF
END
                                """

        simple_program_string_second = """
        DECLARE
    j, k
BEGIN
    READ k;
    FOR i FROM 0 TO k DO
        IF i GE 1 THEN
            j ASSIGN j TIMES 2;
        ENDIF
        IF i EQ 1 THEN
            j ASSIGN 1;
        ENDIF
    ENDFOR
    IF k GEQ 1 THEN
        WRITE j;
    ENDIF
END
        """

        simple_program_string_third = """
        DECLARE
    j, k
BEGIN
    READ k;
    FOR i FROM 1 TO k DO
        IF i EQ 1 THEN
            j ASSIGN 1;
        ELSE
            j ASSIGN j TIMES 2;
        ENDIF
    ENDFOR
    IF k GEQ 1 THEN
        WRITE j;
    ENDIF
END
        """
        simple_program_string_fourth = """
        DECLARE
    j, k
BEGIN
    READ k;
    FOR i FROM 1 TO k DO
        IF i GE 1 THEN
            j ASSIGN j TIMES 2;
        ELSE
            j ASSIGN 1;
        ENDIF
    ENDFOR
    IF k GEQ 1 THEN
        WRITE j;
    ENDIF
END
        """

        a = b'5'
        out, err, asm, cost = run_vm(simple_program_string_first, input=a)
        assert err is b''
        assert len(out) == 1
        result_a = int(out[0])
        print('\ntest-one, subtest a, cost: ', cost)

        out, err, asm, cost = run_vm(simple_program_string_second, input=a)
        assert err is b''
        assert len(out) == 1
        result_b = int(out[0])
        print('\ntest-one, subtest b, cost: ', cost)

        out, err, asm, cost = run_vm(simple_program_string_third, input=a)
        assert err is b''
        assert len(out) == 1
        result_c = int(out[0])
        print('\ntest-one, subtest c, cost: ', cost)

        out, err, asm, cost = run_vm(simple_program_string_fourth, input=a)
        assert err is b''
        assert len(out) == 1
        result_d = int(out[0])
        print('\ntest-one, subtest d, cost: ', cost)

        assert result_a == result_b
        assert result_b == result_c
        assert result_c == result_d

    def test_two(self):
        simple_program_string = """
        [ Rozklad liczby 340282367713220089251654026161790386200 na czynniki pierwsze ]
[ Oczekiwany wynik:
  2^3
  3
  5^2
  7
  13
  41
  61
  641
  1321
  6700417
  613566757
  715827883
]
DECLARE
    a(0:3),
    n, m, reszta, potega, dzielnik
BEGIN
    a(0) ASSIGN 4294967297;
    a(1) ASSIGN 4294967298;
    a(2) ASSIGN 4294967299;
    a(3) ASSIGN 4294967300;

    n ASSIGN a(0) TIMES a(1);
    n ASSIGN n TIMES a(2);
    n ASSIGN n TIMES a(3);

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
    UWAGA = "TEGO NIE KOMPILOWAC PRZEZ TEST HARNESS, ODPALIC RECZNIE (zeby bylo widac kilka poczatkowych wynikow ;)"