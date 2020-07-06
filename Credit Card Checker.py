credit_card_number = [5,4,9,6,2,7,4,1,4,3,1,4,1,5,2,2]

def cc_checker_function(credit_card_number):
    after_doubling_number = []
    for index in range(len(credit_card_number)):
        if index % 2 == 0:
            after_doubling_number.append(credit_card_number[index] * 2)
        else:
            after_doubling_number.append(credit_card_number[index])
    
    #print(after_doubling_number)
    
    after_subtracting_list = []
    for index1 in range(len(after_doubling_number)):
        if index1 % 2 == 0 and after_doubling_number[index1] > 9:
            nine_subtraction_value = after_doubling_number[index1] - 9
            after_subtracting_list.append(nine_subtraction_value)
        else:
            after_subtracting_list.append(after_doubling_number[index1])

    #print(after_subtracting_list)

    list_to_number = ""
    for index2 in range(len(credit_card_number)):
        list_to_number += str(credit_card_number[index2])

    sum_of_final_list = sum(after_subtracting_list)        
    
    if sum_of_final_list % 10 == 0:
        print("VALID!!")
        print(list_to_number)
    else:
        print("INVALID")
        print(list_to_number)

cc_checker_function(credit_card_number)




