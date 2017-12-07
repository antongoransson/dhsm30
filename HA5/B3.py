from random import randrange
def hex2(x):
  return  '{}{:x}'.format('0' * (len(hex(x)) % 2), x)
  # x = format(n, 'x')
  # return ('0' * (len(x) % 2)) + x
# def b_64_encode(x):
#   p = 2530368937, q = 2612592767 and e = 65537
def TLV_DER_encode_int(i):
  l = (i.bit_length() + 7 // 8) // 8 + 1
  l_str = hex2(l)
  if l > 2**7  // 4:
    l_str += '8' + str(len(l_str) // 2)
  return '02' + l_str + '00' +  hex2(i)



if __name__ == '__main__':
  p = 2530368937
  q = 2612592767
  e = 65537
  print(TLV_DER_encode_int(p))
  print(TLV_DER_encode_int(q))
  print(TLV_DER_encode_int(1498103913))
  i = 2530368937
  #96d25da9
  # print(TLV_DER_encode_int(i))
  # print('02050096d25da9')
  # print(TLV_DER_encode_int(161863091426469985001358176493540241719547661391527305133576978132107887717901972545655469921112454527920502763568908799229786534949082469136818503316047702610019730504769581772016806386178260077157969035841180863069299401978140025225333279044855057641079117234814239380100022886557142183337228046784055073741))
  # print(TLV_DER_encode_int(32317006071311007300714876688669951960444102669715484032130345427524655138867890893197201411522913463688717960921898019494119559150490921095088152386448283120630877367300996091750197750389652106796057638384067568276792218642619756161838094338476170470581645852036305042887575891541065808607552399123930385521914333389668342420684974786564569494856176035326322058077805659331026192708460314150258592864177116725943603718461857357598351152301645904403697613233287231227125684710820209725157101726931323469678542580656697935045997268352998638215525166389437335543602135433229604645318478604952148193555853611059596230650))