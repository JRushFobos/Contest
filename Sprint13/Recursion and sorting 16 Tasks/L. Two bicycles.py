# Два велосипеда
def binarySearch(money, price, left, right):
    if right <= left:  # промежуток пуст
        return -1
    # промежуток не пуст
    mid = (left + right) // 2
    if (mid == 0 and price <= money[mid]) or (
        money[mid] >= price > money[mid - 1]
    ):  # центральный элемент — искомый
        return mid + 1
    elif price <= money[mid]:  # искомый элемент меньше центрального
        # значит следует искать в левой половине
        return binarySearch(money, price, left, mid)
    else:  # иначе следует искать в правой половине
        return binarySearch(money, price, mid + 1, right)


# days = int(input())
# money = list(map(int, input().split()))
# price = int(input())

days = 7  # n число дней копим
money = [1, 1, 4, 4, 4, 4, 8]  # накопили за каждый день
price = 3  # цена велосипеда

result_list = []
# изначально мы запускаем двоичный поиск на всей длине массива
first_day = binarySearch(money, price, left=0, right=days)
second_day = binarySearch(money, price * 2, left=0, right=days)
print(str(first_day) + ' ' + str(second_day))
