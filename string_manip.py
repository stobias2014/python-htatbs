#!/bin/python3


sentence = "This is a sentence."

print(sentence)

print("\nEscape characters")

print("\tWhat is up yo\'s?\\")

print('''Dear blank,

        This is a multiline string by using triple quotes.

        Thank you,
        ST
        ''')

print("\nA slice of string")
print("sentence[0:4] = {0}".format(sentence[0:4]))

print("in operator")
if "is" in sentence:
    print("\'is\' is in the sentence: {0} ".format(sentence))
else:
    print("\'is\' is not in the sentence: {0} ".format(sentence))

print("\nString Interpolations")
name = "saul"
age = 21
print("name = %s ---- age = %d"%(name, age))

print("\nSentence lowered: {0} ----- Is it lowered? {1} ".format(sentence.lower(), sentence.lower().islower()))
print("Sentence uppered: {0} ----- Is it uppered? {1} ".format(sentence.upper(), sentence.upper().isupper()))



