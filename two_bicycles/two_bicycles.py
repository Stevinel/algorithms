def days_buy(days_money, price, left, right):
    if right <= left:
        return -1
    if days_money[left] >= price:
        return left + 1

    mid = (left + right) // 2
    if days_money[mid - 1] < price <= days_money[mid]:
        return mid + 1
    elif price <= days_money[mid]:
        return  days_buy(days_money, price, left, mid)
    else:
        return days_buy(days_money, price, mid + 1, right)


if __name__ == '__main__':
    days_len = int(input())
    days_money = [int(i) for i in input().split()]
    price = int(input())
    x = (days_buy(days_money, price, left = 0, right = days_len))
    y = (days_buy(days_money, price * 2, left = 0, right = days_len))
    print(x, y)
