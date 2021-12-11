class SolutionLongestPalindrome:

    @classmethod
    def longest_palindrome(cls, s: str) -> str:
        s_len = len(s)
        result = s[0] if len(s) else ""

        for i in range(s_len):
            left, right = i, i
            result_odd = cls._look_while(left, right, s, s_len, result)
            left, right = i, i+1
            result_even = cls._look_while(left, right, s, s_len, result_odd)
            result = result_odd if len(result_odd) > len(result_even) else result_even

        return result

    @staticmethod
    def _look_while(left, right, base_string, base_string_len, res):
        while left >= 0 and right < base_string_len and base_string[left] == base_string[right]:
            if len((new_result := base_string[left:right + 1])) >= len(res):
                res = new_result
            left -= 1
            right += 1
        return res
