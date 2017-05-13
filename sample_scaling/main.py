text_file_directory = 'data/'

text_file_number = 40031
text_file_name = str(text_file_number) + '.txt'

text_file = text_file_directory + text_file_name

f = open(text_file)

data = f.read()
data = """너에게 묻는다.
- 안도현 -
너에게 묻는다
연탄재 함부로 발로 차지 마라
너는 누구에게 한번이라도 뜨거운 사람이었느냐

반쯤 깨진 연탄
언젠가는 나도 활활 타오르고 싶을 것이다
나를 끝 닿는데까지 한번 밀어붙여 보고 싶은 것이다

타고왔던 트럭에 다시 실려 돌아가면
연탄, 처음으로 붙여진 나의 이름도 으깨어져
나의 존재도 까마득히 뭉개질 터이니
죽어도 여기서 찬란한 끝장을 보고 싶은 것이다

나를 기다리고 있는 찬란한 밑불위에
지금은 인정머리없는 차가운 내 몸을 얹고
아랫쪽부터 불이 건너와 옴겨 붙기를
시간의 바통을  내가 넘겨 받는 순간이 오기를
그리하여 서서히 온몸이 벌겋게 달아오르기를
나도 느껴보고 싶은 것이다
나도 보고 싶은 것이다

모두들 잠든 깊은 밤에 눈에 발갛게 불을 켜고
구들장 속이 얼마나 침침한지 손을 뻗어보고 싶은 것이다
나로 하여 푸근한 잠 자는 처녀의 등허리를
밤새도록 슬금슬금 만져도 보고 싶은 것이다
"""
filter_set = []
import scaling
filter_set= filter_set+scaling.filter_pronouns
scaled_data = scaling.filtering_data(data, filter_set)
print(type(scaled_data)) # <class 'list'>
print(type(scaled_data[0])) # <class 'str'>
print(scaled_data) # ['안도현', '연탄재', '발', '한번', '사람', '연탄', '끝', '한번', '트럭', '연탄', '처음', '이름', '뭉개질', '터', '여기', '끝장', '지금', '몸', '아랫쪽', '불', '옴겨', '시간', '바통', '순간', '오기', '온몸', '밤', '눈', '불', '구들장', '손', '처녀']

help(scaling.filtering_data)
