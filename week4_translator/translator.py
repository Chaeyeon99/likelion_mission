from googletrans import Translator

#1. 번역기 생성
translator = Translator()

#2. 번역을 원하는 문장 입력
print('='*50)
sentence = input("번역할 문장을 입력해주세요: ")

#3. 언어를 감지한다.
detected = translator.detect(sentence)
print("감지된 입력 언어:", detected.lang)  #감지된 언어만 출력
print('='*50)

#3. 번역을 원하는 언어 설정 & 4. 번역
lang_list = ['en','fr', 'es']
lang = int(input("번역을 원하는 언어를 입력해주세요(0: 영어, 1: 프랑스어, 2: 스페인어): "))
result = translator.translate(sentence, lang_list[lang])
# print(result)
print(sentence,"를 번역하면, ",result.text)

#깔끔한 출력
print('='*50)
print(detected.lang, ": ", sentence)
print(result.dest, ": ", result.text)