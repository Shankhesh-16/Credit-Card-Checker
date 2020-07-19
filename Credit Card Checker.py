
def cc_checker_function():
    cc = input('Enter the credit card number: ')
    credit_card_number = []
    for digit in cc:
        credit_card_number.append(digit)

    if len(credit_card_number) > 0:

        after_doubling_number = []
        for index in range(len(credit_card_number)):
            if index % 2 == 0:
                after_doubling_number.append(int(credit_card_number[index]) * 2)
            else:
                after_doubling_number.append(int(credit_card_number[index]))

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

    else:
        print('Please check the length of the number.')


def rerun():
    for rerun in range(10000):
        cc_checker_function()

rerun()

#Some examples of valid
4539689887705798
1234567812345670

#Some of invalid
12345678123456
1234567812345678
4539689887705799





