from lru_cache import LruCache
from cache_calculator import CacheCalculator
from calculation import Calculation

# student 1: Yonatan Shirman id: 208870246
# student 2: Reut Dayan      id: 318879210

# creating cache with the size of 3 and inserting values with the calculate function
my_cal1=CacheCalculator(3)
result,is_cached_used = my_cal1.calculate(5,7,'mul')
print(f'the result is {result} ,is_cached_used1 {is_cached_used}')
result,is_cached_used = my_cal1.calculate(5,7,'sum')
print(f'the result is {result} ,is_cached_used1 {is_cached_used}')
result,is_cached_used = my_cal1.calculate(5,7,'div')
print(f'the result is {result} ,is_cached_used1 {is_cached_used}')
print("my cache is")
print(my_cal1)

# checking the get and put functions
print('*'*20)
p=my_cal1.get("5*7")
print(f'the value of key 5*7 is {p}')
my_cal1.calculate(6,8,'sub')
my_cal1.get("5/7")
my_cal1.put(1,'a')
print(f'the cache is ')
print(my_cal1)
print('*'*20)

# making new cahce with different size and inserting values with calculate function
my_cal2 = CacheCalculator(7)
result1,is_cached_used1 = my_cal2.calculate(5,7,'mul')
print(f' the result is {result1} ,is_cached_used1 {is_cached_used1}')
result1,is_cached_used1 = my_cal2.calculate(5,7,'sum')
print(f' the result is {result1} ,is_cached_used1 {is_cached_used1}')
result1,is_cached_used1 = my_cal2.calculate(5,0,'div')
print(f' the result is {result1} ,is_cached_used1 {is_cached_used1}')
result1,is_cached_used1 = my_cal2.calculate(5,1,'div')
print(f' the result is {result1} ,is_cached_used1 {is_cached_used1}')
result1,is_cached_used1 = my_cal2.calculate(5,8,'sub')
print(f' the result is {result1} ,is_cached_used1 {is_cached_used1}')
result1,is_cached_used1 = my_cal2.calculate(5,6,'mul')
print(f' the result is {result1} ,is_cached_used1 {is_cached_used1}')
result1,is_cached_used1 = my_cal2.calculate(5,7,'mul')
print(f' the result is {result1} ,is_cached_used1 {is_cached_used1}')
print(f'the cache is ')
print(my_cal2)
print('*'*20)

# using get and put functions to showcase that both of them work on the two caches we made before
print(my_cal1.get(7*8))
print(my_cal2.get(5*6))
my_cal2.put(3,'reut')
my_cal2.put(4,'yoni')
print (my_cal2)
print(my_cal1.get('5+7'))
print(my_cal1.get('6-8'))
my_cal1.calculate(6,6,'sub')
print(f'the cache is ')
print(my_cal1)





