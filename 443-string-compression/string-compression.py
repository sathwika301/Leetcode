
class Solution:
    def compress(self, chars: list[str]) -> int:
        i = 0          # Read pointer
        write = 0      # Write pointer
        
        while i < len(chars):
            x = chars[i]
            count = 0
            
          
            while i < len(chars) and chars[i] == x:
                count += 1
                i += 1
                
        
            chars[write] = x
            write += 1
            
           
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
                    
        return write

        