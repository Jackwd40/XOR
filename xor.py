import string
import binascii
import matplotlib.pyplot as plt
import numpy as np
import re
import codecs





def xor(message, key):
	index = 0
	output = ''
	for x in message:
		new = ord(message[index]) ^ ord(key[index % len(key)])
		# print(new)
		output += hex(new)[2:].zfill(2)
		index += 1
	return(output)

def freq_analysis(ciphertext, graph):
	print(len(ciphertext))
	ready_string_or_ascii_input = codecs.decode(ciphertext.strip(), "hex").decode("utf-8")
	total_alphabetical_freq = {'A': 8.167, 'B': 1.492, 'C': 2.782, 'D': 4.253, 'E': 12.702, 'F': 2.228, 'G': 2.015, 'H': 6.094, 'I': 6.966, 'J': 0.153, 'K': 0.772, 'L': 4.025, 'M': 2.406, 'N': 6.749, 'O': 7.507, 'P': 1.929, 'Q': 0.095, 'R': 5.987, 'S': 6.327, 'T': 9.056, 'U': 2.758, 'V': 0.978, 'W': 2.360, 'X': 0.150, 'Y': 1.974, 'Z': 0.074, ' ': 16.523}
	saved_count = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
	saved_percents = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
	if len(ciphertext) == 0:
		raise Exception("Can not have an input of nothing!")
	
	if graph == 'y':
		ax = plt.subplot(111)
		ax.bar(list(total_alphabetical_freq.keys()), list(total_alphabetical_freq.values()), align='edge', color='g', width=0.5)
		ax.bar(list(saved_percents.keys()), list(saved_percents.values()), align='center', color='r', width=0.5)
		plt.title("Letters by frequency in english language")
		plt.xlabel('Letter')
		plt.ylabel('Frequency')
		plt.show()


	residuals = saved_percents = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

	key_to_res = dict()
	for i in range(256):
		# print("i >> {0}".format(i))
		# print("ready_string >> {0}".format(ready_string_or_ascii_input))
		final_pushback = 0
		tester = xor(ready_string_or_ascii_input, chr(i))
		# fails in string length somewhere
		ready_to_go = codecs.decode(tester, "hex")
		given = bytearray(bytes.fromhex(tester))

		tester_countable = str(given)

		test_key = i
		
		for letter in tester_countable:
			if letter in tester_countable:
				if letter.isalpha():
					saved_count[letter.upper()] += 1
					print(saved_count)
			
		
		for item in saved_percents:
			saved_percents[item] = (saved_count[item] / len(ready_string_or_ascii_input)) * 100

		for item in residuals:
			# print("SAVED PERCENTS")
			# print(saved_percents[item])
			residuals[item] = total_alphabetical_freq[item] - saved_percents[item]
			# print("ITEM RES")
			# print(residuals[item])
			
		for key in residuals:
			final_pushback += residuals[key]
		
		key_to_res[i] = final_pushback ** 2
	
	# print(key_to_res)
	import operator
	sorted_x = sorted(key_to_res.items(), key=operator.itemgetter(1))
	# print("final?")
	# print(sorted_x[0])
	

def single_byte_xor(message, key):
	if len(key) != 1:
		raise Exception('The key should only be 1 character long')
	return xor(message, key)


# # determine key length
# def hamming(in1, in2):
# 	# hamming distance is the number of discrepencies they have between then
# 	hammingdist = xor(in1, in2)
# 	return bin( int(hammingdist, 16) ).count('1')

# print(hamming("attackatdawn", "key"))

def main():
	# print(xor("jesus", "x"))
	print(freq_analysis("121d0b0d0b", 'n'))
	# print(single_byte_xor("jesus", "a"))
	

if __name__ == '__main__':
	main()

