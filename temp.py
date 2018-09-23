# def task():
#     print('#'*40)
#     print('Specify the task - Regression or Classification ')
#     task=int(input('''
# Enter 1 for Classification
# Enter 2 for Regression
# Enter 3 to automatically detect the task \n'''))
#     try:
#         try:
#             assert(type(task))!= type(1)
#         except ValueError:
#             print('please enter numeric values')
#             print('#'*40)
#     except AssertionError:
#             if task not in [1,2,3]:
#                 print('please renter the specified number')
#                 task()
#     print("You selected :",task)
#
#     return task

def task():
        task=0
        while task not in [1,2,3]:
            try:
                task=int(input('''
            Enter 1 for Classification
            Enter 2 for Regression
            Enter 3 to automatically detect the task \n'''))
            except ValueError:
                print("########## Please Enter Specified Numeric Values ############")
                task=0
        print("You selected :",task)
        return task


print(task())
