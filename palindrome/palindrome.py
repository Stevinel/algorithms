def palindrome(data):
    string = [char for char in data.lower() if char.isalnum()]
    string = ''.join(string)
    if string == string[::-1]:            
        return True
    else:
        return False


if __name__ == "__main__":
    data = input()
    print(palindrome(data))
