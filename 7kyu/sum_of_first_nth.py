# Task:
# Your task is to write a function which returns the sum of following series upto nth term(parameter).

# Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...
# Rules:
# You need to round the answer to 2 decimal places and return it as String.

# If the given value is 0 then it should return 0.00

# You will only be given Natural Numbers as arguments.

# Examples:(Input --> Output)
# 1 --> 1 --> "1.00"
# 2 --> 1 + 1/4 --> "1.25"
# 5 --> 1 + 1/4 + 1/7 + 1/10 + 1/13 --> "1.57"

# def series_sum(n):

#     result = "0.00" if n == 0 else 1
#     if result == 1:
#         divisor = 4
#         for i in range(n-1):
#             result += 1/divisor
#             divisor += 3

#     return f"{float(result):.2f}"    


def series_sum(n):
    return f"{1+sum(list(map(lambda x: 1/x , [4 + 3 * i for i in range(n-1)]))):.2f}" if n > 0 else "0.00"

if __name__ == "__main__":
    t = [0,1,2,5]
    for n in t:
        print(series_sum(n))