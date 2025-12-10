def ft_count_harvest_recursive():
    day = int(input("Days until harvest: "))
    i = 1

    def harvest_count(i):
        print(f"Day: {i}")
        if i < day:
            harvest_count(i + 1)
    harvest_count(i)
    print("Harvest time!")
