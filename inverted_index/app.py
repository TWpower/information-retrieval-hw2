import re

# regex pattern - space로 구분된 단어만 뽑아옵니다
pattern = re.compile('(\w+)')

# word들을 저장하는 list 선언
words = []

# Inverted Index를 저장하는 Dictionary
inverted_index = {}

# 1.txt ~ 4.txt를 읽으면서 단어를 words에 추가
# 여기서 i는 Document ID라고 정의합니다.
for document_id in range(1,5):

	with open(str(document_id) + '.txt', 'r') as txt_file:

		txt = txt_file.read()
		result = pattern.findall(txt)

		for word in result:

			word = word.lower()

			if word not in words:
				words.append(word)
				inverted_index[word] = [document_id]
			else:
				if document_id not in inverted_index[word]:
					inverted_index[word].append(document_id)

		words.sort()

# 이제 하나하나 단어들을 보면서 출력을 합니다.

for word in words:
	print(word + ' : ', end='')
	for id in inverted_index[word]:
		print(str(id) + str(' '), end='')
	print()




