class Solution:

    def letterCombinations(self, digits: str) -> List[str]:
        *inpoo, = digits

        all_chars = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }


        out = []

        if len(inpoo) == 0:
            return out
        elif len(inpoo) == 1:
            return all_chars[inpoo[0]]

        elif len(inpoo) == 2:
            for i in all_chars[inpoo[0]]:
                for j in all_chars[inpoo[1]]:
                    out.append(i+j)
            return out
        elif len(inpoo) == 3:
            for i in all_chars[inpoo[0]]:
                for j in all_chars[inpoo[1]]:
                    for k in all_chars[inpoo[2]]:
                        out.append(i+j+k)
            return out
        else:
            for i in all_chars[inpoo[0]]:
                for j in all_chars[inpoo[1]]:
                    for k in all_chars[inpoo[2]]:
                        for l in all_chars[inpoo[3]]:
                            out.append(i+j+k+l)
            return out
                
