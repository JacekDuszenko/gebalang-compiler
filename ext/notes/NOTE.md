## Ograniczenie na liczby

1. Każda stała liczba jawnie zapisana w kodzie musi być w zakresie [2^-63, 2^63 -1] , potem może być overflow ale to już nieważne.
Część overflow'ów dałoby się sprawdzić w trakcie kompilacji ale tego nie chcemy (bo na maszynie cln nie będzie overflow'ów)
To jest sprawdzane przez lexer

## Reszta z dzielenia

1. Mod div  - reszta Knutha z The Art of Computer Programming, a / b --> (sgn(b) == sgn(r))
 czyli a/b = _(a / b), A TAKŻE a = b * q + r <==> r = a - bq = a - (b * _(a /b)).
Czyli np. 5/2 = 2, ale 5/(-2) = -3 no i 5 % 2 = 1 , ale 5 % (-2) = 5 - ( (-2) * (-3)) = 5 - 6 = -1
Patologia...

## Sprawdzanie nieinicjalizacji w SA

1. Na razie sprawdzanie robi preorder na ast i dodaje dzieciom scope parenta. Jeżeli traverse dojdzie do  jakiegoś ASSIGN lub READ
przed użyciem zmiennej to nie oznaczy jej jako uninitialized i nie wywali się - powinno wystarczyć na testy. Jeśli nie wystarczy to dokończy się później, ale
nie ma sensu implementować całego interpreted inference.