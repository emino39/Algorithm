# 자릿수의 합을 더해야 함 더하다보면 올림이 되는 경우가 있으니까!
N = int(input())
words = []
alpabet_value = {}

for n in range(N):
    word = input()
    words.append(word)
    word_len = len(word)

    for w in range(word_len):
        if word[w] not in alpabet_value:
            alpabet_value[word[w]] = 10 ** (word_len - w - 1)
        else:
            alpabet_value[word[w]] += 10 ** (word_len - w - 1)

alpabet_value = sorted(alpabet_value.items(), key=lambda x: x[1], reverse=True)

number = 9
total = 0

for alpabet in alpabet_value:
    total += alpabet[1] * number
    number -= 1

print(total)
"""
N = int(input())
word_dict = {}
numbers = []

for n in range(N):
    word = input()
    word_len = len(word)
    numbers.append([word, word_len-1])

    for l in range(word_len):
        if word[l] in word_dict:
            word_dict[word[l]]['p'] = max(word_dict[word[l]]['p'], word_len - l - 1)
            word_dict[word[l]]['cnt'] += 1
        else:
            word_dict[word[l]] = {
                'p': word_len - l - 1,
                'cnt': 1
            }

word_dict = sorted(word_dict.items(), key=lambda x: (x[1]['p'], x[1]['cnt']), reverse=True)
word_num = {}
num = 9
for w in word_dict:
    word_num[w[0]] = num
    num -= 1

total = 0
for number, cnt in numbers:
    for c in range(cnt+1):
        total += word_num[number[c]] * (10 ** (cnt - c))

print(total)
"""
