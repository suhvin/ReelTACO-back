# Flask 서버
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 모든 경로에 대해 CORS 정책 허용


@app.route('/api', methods=['POST'])
def index():
    req_data = request.get_json()  # POST 요청의 JSON 데이터 추출
    if not req_data or not isinstance(req_data, list):
        return jsonify({'error': 'Invalid request format'})

    response_data = req_data[:]  # 요청 데이터를 복사하여 response_data 초기화

    # 새로운 객체 생성 및 배열 맨 끝에 추가
    new_obj = {
        'type': 'recommender',
        'desc': 'hello'
    }
    response_data.append(new_obj)

    return jsonify(response_data)


# import tensorflow as tf
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import LSTM, Dense

# # 데이터 준비
# names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
# greetings = ['Hello', 'Hi', 'Hey', 'Greetings', 'Welcome']

# # 데이터 전처리
# name_to_greeting = dict(zip(names, greetings))

# # 모델 구성
# model = Sequential()
# model.add(LSTM(64, input_shape=(5, 1)))  # 입력 크기는 (시퀀스 길이, 1)
# model.add(Dense(len(greetings), activation='softmax'))
# model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# # 모델 학습
# X = []
# y = []
# for name, greeting in name_to_greeting.items():
#     X.append([ord(c) for c in name])  # 각 이름의 문자를 아스키 코드로 변환하여 입력 데이터에 추가
#     y.append(greetings.index(greeting))  # 해당 인사말의 인덱스를 타깃 데이터에 추가

# X = tf.keras.preprocessing.sequence.pad_sequences(X, padding='post', maxlen=5)  # 시퀀스 길이를 5로 맞추고 패딩
# X = tf.expand_dims(X, axis=-1)  # 차원 확장
# y = tf.keras.utils.to_categorical(y, num_classes=len(greetings))  # 원-핫 인코딩

# model.fit(X, y, epochs=10)

# @app.route('/', methods=['GET'])
# def index():
#     name = request.args.get('name', '')

#     if not name:
#         return jsonify({'error': 'Name is missing'})

    # 입력 데이터 전처리
    # x = [ord(c) for c in name]
    # x = tf.keras.preprocessing.sequence.pad_sequences([x], padding='post', maxlen=5)
    # x = tf.expand_dims(x, axis=-1)  # 차원 확장

    # # 모델 예측
    # prediction = model.predict(x)
    # predicted_greeting = greetings[prediction.argmax()]

    # response = {'greeting': predicted_greeting}



    # return jsonify(response)

if __name__ == '__main__':
    app.run(port=5001)