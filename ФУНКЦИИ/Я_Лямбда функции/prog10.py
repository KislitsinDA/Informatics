def print_operation_table(operation, num_rows=9, num_columns=9):
    for i in range(1, num_rows + 1):
        print(*(operation(i, k) for k in range(1, num_columns + 1)), sep="\t")


print_operation_table(lambda x, y: y * x)
print("===========")
print_operation_table(lambda x, y: y * x, 5, 7)
