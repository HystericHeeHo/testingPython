l2 = ["s","f","p","g"]
    
l3 = ["n","v","f","h","s"]
    
for i in range(4):
    
  l2[i] = chr(ord(l2[i])-i)
    
  l3[i] = chr(ord(l3[i])-i)
    
result = ''.join(l2) + " " + ''.join(l3)
    
print(result)