# numbers = [12, 45, 56, 45, 12, 89]
marks = {"physics": 12, "chemistry": 45, "math": 56}
marks['math'] = 56.5
marks['english'] = 89
# del marks['chemistry']
print(marks)

mark_keys = marks.keys()
mark_values = marks.values()
mark_items = marks.items()


print(mark_items)
