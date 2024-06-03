# we are learning about exceptions, and error handling.
# try:
#     x = int(input("Enter the first number: "))
#     y = int(input("Enter the second number: "))
#     print(x/y)
# # except ValueError:
# #     print("Could not divide")
# except ZeroDivisionError:
#     print("Can not divide by zero")
# except:
#     raise ValueError("Something is wrong")
# # except is for when there comes an error in try.
# else:
#     print("Program successfully executed.")
# finally:
#     print("Not my headache...I will get printed anyhow")


# def assertion():
#     x = input("Enter a word: ")
#     assert len(x)>5,"Not even a proper word!!"
#     print("Now thats a word!")
#     print(x)
# assertion()


# def isPalindrome(s):
#  def toChars(s):
#     s = s.lower()
#     ans = ''
#     for c in s:
#         if c in 'abcdefghijklmnopqrstuvwxyz':
#            ans = ans + c
#     return ans
#  def isPal(s):
#     if len(s) <= 1:
#         return True
#     else:
#         return s[0] == s[-1] and isPal(s[1:-1])
#  return isPal(toChars(s))
# string = input("Enter the string you want to check:")
# print(isPalindrome(string))


def lyrics_to_frequencies(lyrics):
 myDict = {}
 list =lyrics.split()
 for word in list: 
    if word in myDict: 
        myDict[word] += 1
    else:
        myDict[word] = 1
 return myDict
lyrics = input("Enter the sentence: ")
a=lyrics_to_frequencies(lyrics)
print(a)

def most_common_words(freqs): 
 values = freqs.values()
 best = max(values)
 words = []
 for k in freqs:
    if freqs[k] == best:
        words.append(k)
 return (words, best)

print(most_common_words(a))
def words_often(freqs, minTimes):
 result = []
 done = False
 while not done:
    temp = most_common_words(freqs)
    if temp[1] >= minTimes:
        result.append(temp)
        for w in temp[0]:
            del(freqs[w])
    else:
        done = True
 return result
print(words_often(a,3))

