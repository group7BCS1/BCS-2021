str = 'X-DSPAM-Confidence: 0.8475'
index = str.find(':')
new_index=(str[index+1:])
new_index = float(new_index)
print("Floating number: ", new_index)
