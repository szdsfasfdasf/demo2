
# for i range(100):
for i in range(101):
    if i % 7 == 0:
        continue
    elif i % 10 == 7:
        continue
    elif i // 10 == 7:
        continue
    else:
        print(i)
