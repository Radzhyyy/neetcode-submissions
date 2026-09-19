class Solution:
    def compress(self, chars: List[str]) -> int:
        read_index = 0
        write = 0

        while read_index < len(chars):

            current_char = chars[read_index]
            count = 0

            while read_index < len(chars) and chars[read_index] == current_char:
                read_index += 1
                count += 1

            chars[write] = current_char
            write += 1

            if count > 1:
                for i in str(count):
                    chars[write] = i
                    write += 1

        return write