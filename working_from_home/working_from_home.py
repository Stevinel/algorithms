def run(num):
    bin_num = bin(num)
    slice_bin = bin_num[2::]
    return(slice_bin)

if __name__ == "__main__":
    num = int(input())
    print(run(num))
