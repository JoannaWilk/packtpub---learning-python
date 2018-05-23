test_list = [2, 5, 8, 0, 0, 1, 0]
print("test_list:", test_list)
print('-' * 10)
print("list(filter(None, test)):\n",
      list(filter(None, test_list)))
print('-' * 10)
print("list(filter(lambda x: x, test_list)):\n",
      list(filter(lambda x: x, test_list)))
print('-' * 10)
print("list(filter(lambda x: x > 4, test_list)):\n",
      list(filter(lambda x: x > 4, test_list)))

