def count_sheep(n):
    return ''.join(map(lambda x: f"{x+1} sheep...", range(n)))
        
if __name__ == "__main__":
    print(count_sheep(3))