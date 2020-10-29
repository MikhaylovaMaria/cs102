def encrypt_vigenere(plaintext: str, keyword: str) -> str:
  ciphertext = ""
  a,b,c,k=len(plaintext),len(keyword),keyword,0
  if b<a:
    for i in range (a-b):
      keyword += c[k]
      k+=1
      if k>=b:
        k=0
  m=0
  keyword = keyword.upper()      
  for i in plaintext:
    b=keyword[m]
    m+=1
    a=ord(i)
    shift = ord(b)-65
    if shift == 0:
      ciphertext += chr(a)

    elif a+shift>90 and 65<=a<=90:
      ciphertext += chr(a + shift-26)
    elif a+shift>122 and 97<=a<=122:
      ciphertext += chr(a + shift-26)
    elif (a+shift<=90 and 65<=a<=90) or (a+shift<=122 and 97<=a<=122):
      ciphertext += chr(a + shift)
    else:
      ciphertext += chr(a)

  return ciphertext

def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
  plaintext = ""
  a,b,c,k=len(ciphertext),len(keyword),keyword,0
  if b<a:
    for i in range (a-b):
      keyword += c[k]
      k+=1
      if k>=b:
        k=0
  m=0      
  keyword = keyword.upper() 
  for i in ciphertext:
    b=keyword[m]
    
    m+=1
    a=ord(i)
    shift = ord(b)-65
    if shift == 0:
      plaintext += chr(a)
    
    
    elif a - shift < 65 and 65 <= a <= 90:
      plaintext += chr(a - shift + 26)
    elif a - shift < 97 and 97 <= a <= 122:
      plaintext += chr(a - shift +26 )
    elif (a - shift >= 65 and 65 <= a <= 90) or (a - shift >= 97 and 97 <= a <= 122):
      plaintext += chr(a - shift)
    else:
      plaintext += chr(a) 
  
  return plaintext

