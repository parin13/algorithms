
def calculate_sum(number_list):
	sum = 0
	for single_num in number_list:
		sum = sum+single_num
	
	if not (len(str(sum)) == 1):
		return_list = [int(x) for x in str(sum)]
		sum = calculate_sum(return_list)
	return sum 


def algorith(dob):

	split_data_data_list = dob.split('-')


	total_numbers = []
	for split_num in split_data_data_list:
		data = [int(x) for x in str(split_num)]
		for single_num in data:
			total_numbers.append(single_num)

	return calculate_sum(total_numbers)



if __name__ == "__main__":
	print ('Inter date of Birth in this format : day-month-year')
	dob=str(input())
	enc_key = algorith(dob)
	print ('ANS: {}'.format(enc_key))
	print('As per algorith your encryption key for d.o.b {} would be {}'.format(dob, enc_key))