
import copy
import itertools

result = []

def calculate(number:int) -> list:
    global result
    result.clear()
    numbers_list = list("9876543210")

    slice_recursive(numbers_list, [], number)
    return(result)

def slice_recursive(numbers_list, list_of_slice, target_num):
    if len(numbers_list) == 0:
        global result
        for variation in list(map(''.join, itertools.product('+-', repeat=len(list_of_slice)-1))):
            buf_list = copy.copy(list_of_slice)
            buf_variation_list = list(variation)
            slice_result = []
            while len(buf_variation_list) > 0:
                slice_result.append(buf_list.pop(0))
                slice_result.append(buf_variation_list.pop(0))
            slice_result.append(buf_list.pop(0))

            if eval("".join(slice_result)) == target_num:
                result.append("".join(slice_result))
        return
    
    for slice_pointer in reversed(list(range(len(numbers_list)))):
        buf_list = copy.copy(list_of_slice)
        buf_list.append("".join(numbers_list[:(slice_pointer + 1)]))
        slice_recursive(copy.copy(numbers_list[slice_pointer + 1:len(numbers_list)]), buf_list, target_num)

    
if __name__ == "__main__":
    print(calculate(200))