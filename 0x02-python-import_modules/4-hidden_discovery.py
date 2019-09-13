#!/usr/bin/python3
if __name__ == "__main__":
   import hidden_4
   dire = dir(hidden_4)
   a = 0
   while a < len(dire):
      if dire[a][0] != '_':
         print(dire[a])
      a = a + 1
