from typing import List

PHONE_BUTTON_TO_LETTERS = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        output = []

        def process(created_comb, remaining_digits):
            if not remaining_digits:
                output.append(created_comb)
            else:
                for c in PHONE_BUTTON_TO_LETTERS[remaining_digits[0]]:
                    process(created_comb + c, remaining_digits[1:])

        if digits:
            process('', digits)
        return output


if __name__ == '__main__':
    print(Solution().letterCombinations('23'))
