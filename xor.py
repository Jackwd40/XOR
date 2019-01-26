import string
import binascii
import matplotlib.pyplot as plt
import numpy as np
import re

def xor(message, key):
	index = 0
	output = ''
	for x in message:
		new = ord(message[index]) ^ ord(key[index % len(key)])
		# removes the first 2 0x from every iteration so it's not 0xA0xB0xC --> ABC
		output += hex(new)[2:]
		index += 1
	return(output)

def freq_analysis(ciphertext, graph):
	# used later for histogram
	total_alphabetical_freq = {'A': 8.167, 'B': 1.492, 'C': 2.782, 'D': 4.253, 'E': 12.702, 'F': 2.228, 'G': 2.015, 'H': 6.094, 'I': 6.966, 'J': 0.153, 'K': 0.772, 'L': 4.025, 'M': 2.406, 'N': 6.749, 'O': 7.507, 'P': 1.929, 'Q': 0.095, 'R': 5.987, 'S': 6.327, 'T': 9.056, 'U': 2.758, 'V': 0.978, 'W': 2.360, 'X': 0.150, 'Y': 1.974, 'Z': 0.074, ' ': 16.523}
	saved_count = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0, ' ': 0, '.': 0, ',': 0, '?': 0, '!': 0,}
	saved_percents = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0, ' ': 0, '.': 0, ',': 0, '?': 0, '!': 0,}

	# ciphertext = re.sub(r"^[\s.?!0-9\s]*$", "", ciphertext)
	cipher_upper = ciphertext.upper()
	cipher_len = len(ciphertext)

	if cipher_len == 0:
		raise Exception("Can not have an input of nothing!")

	for letter in cipher_upper:
		# Thanks for like actually being cool python. PS: if the letter selected from the cipher text is in the cipher text then well add it (it always will be since it's pulled straight from the cipher text)
		if letter in cipher_upper:
			# add that bad boy
			saved_count[letter] += 1

	for item in saved_percents:
		saved_percents[item] = (saved_count[item] / cipher_len) * 100

	if graph == 'y':
		ax = plt.subplot(111)
		ax.bar(list(total_alphabetical_freq.keys()), list(total_alphabetical_freq.values()), align='edge', color='g', width=0.5)
		ax.bar(list(saved_percents.keys()), list(saved_percents.values()), align='center', color='r', width=0.5)
		plt.title("Letters by frequency in english language")
		plt.xlabel('Letter')
		plt.ylabel('Frequency')
		plt.show()
	# print(saved_percents)
	# print(sorted(total_alphabetical_freq.values()))
	# return("Sentence letter count dict: {0}".format(saved_count))
	for key in sorted(total_alphabetical_freq.keys()):
		print("{0}:{1}".format(key, total_alphabetical_freq[key]))

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
	print(xor("jack", "fun"))
	print(freq_analysis("eeeeee", 'n'))
	# print(single_byte_xor("jesus", "a"))

if __name__ == '__main__':
	main()

