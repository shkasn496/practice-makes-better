'''
Description
Given a string str, we need to extract the symbols and words of the string in order.
Notice
The length of str does not exceed 10000.
The given str contains only lowercase letters, symbols, and spaces.

Example 1
Given str = "(hi (i am)bye)"，return ["(","hi","(","i","am",")","bye",")"].
Explanation:
Separate symbols and words.

Example 2
Given str = "#ok yes"，return ["#","ok","yes"]。
Explanation:
Separate symbols and words.

Example 3
Given str = "##s"，return ["#","#","s"]。
Explanation:
Separate symbols and words.

TC: O(N)
SC: O(W) W = len(max word)
'''

example1="(hi (i am)bye)"
example2="#ok yes"
example3="##s"

correct1=["(","hi","(","i","am",")","bye",")"]
correct2=["#","ok","yes"]
correct3=["#","#","s"]

def segment_string(input_data):
    output = []
    if not len(input_data):return output
    word = []
    for c in input_data:
        if c == ' ' or not c.isalpha():
            if len(word) != 0:
                output.append("".join(word))
                word=[]
            if c != ' ': output.append(c)
        elif c.isalpha():word.append(c)

    if len(word) != 0:output.append("".join(word))
    del word
    return output

output1 = segment_string(example1)
output2 = segment_string(example2)
output3 = segment_string(example3)
print(correct1==output1)
print(correct2==output2)
print(correct3==output3)