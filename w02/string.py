#řetězce v pythonu
#reprezentovány UNICODE UTF8, UTF16 i UTF32
text = "Dvojité \"uvozovky\" musíme potlačit; 'jednoduché' jsou OK"
text = 'Jednoduché \'uvozovky\' musíme potlačit; "dvojité" jsou OK'
#speciální znaky
#\N{název} - znak se zadaným názvem ze zn. sady Unicode
print("\N{GREEK CAPITAL LETTER DELTA}")
#\ooo znak se zadanou osmičkovou hodnotou
print("\177")
#\xhh  - znak se zadanou 8bit hex hodnotou
print("\xfa")
#\uhhhh  - znak se zadanou 16bit hex hodnotou
print("\u0122")
#\Uhhhhhhhh  - znak se zadanou 32bit hex hodnotou
print("\U00000122")

# řezání řetězců - stejné jako u seznamů:
text = "Ostrý šíp"
print(text[1:3])
#každý druhý znak:
print(text[::2])
#každý druhý znak od zadu:
print(text[::-2])
#otočení textu
print(text[::-1])