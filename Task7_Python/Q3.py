class py_program:
 def threeSum(self, numbers):
        numbers, result, i = sorted(numbers), [], 0
        while i < len(numbers) - 2:
            a, b = i + 1, len(numbers) - 1
            while a < b:
                if numbers[i] + numbers[a] + numbers[b] < 0:
                    a += 1
                elif numbers[i] + numbers[a] + numbers[b] > 0:
                    b -= 1
                else:
                    result.append([numbers[i], numbers[a], numbers[b]])
                    a, b = a + 1, b - 1
                    while a < b and numbers[a] == numbers[a - 1]:
                        a += 1
                    while a < b and numbers[b] == numbers[b + 1]:
                        b -= 1
            i += 1
            while i < len(numbers) - 2 and numbers[i] == numbers[i - 1]:
                i += 1
        return result

print(py_program().threeSum([-25, -10, -7, -3, 2, 4, 8, 10]))
