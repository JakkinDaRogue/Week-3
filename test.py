def BinToDec():
      pass
      count = 0
      ans = 0
      binary = input("What binary number do you want to convert to decimal? ")
      binary_str = str(binary)
      binary = int(binary)
      while count <= len(binary_str):
          rem = binary % 2
          ans = rem*2**count + ans
          binary = int(binary / 10)
          count = count + 1
      print(ans)

BinToDec()
