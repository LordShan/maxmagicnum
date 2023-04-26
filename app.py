import random
from flask import Flask, jsonify, request, render_template



num_mag:list = [] # список в котором хранится сгенерированное число
attempt:list=[] # список в котором хранятся все (цифры) попытки. 

app = Flask(__name__) # присвоение переменой app объекта Flask(__name__) 

@app.route('/') # декоратор для обработки Главной страницы
def index():
    resetNumber() # при обновлении страницы сбрасываем все счетчики и перегенерируем число
    return render_template('index.html', attempt=len(attempt)) # загружаем страницу HTML

@app.route('/number1')
def number1():
    resetNumber() # при обновлении страницы сбрасываем все счетчики и перегенерируем число
    return render_template('number1.html', attempt=len(attempt)) # загружаем страницу HTML

@app.route('/process_number1', methods=['POST'])  # декоратор для обработки POST-запроса с введеным числом
def process_text():
    text = request.form['text'] # получаем из поля "text" значение 
    result = youwish(int(text)) # передаем его в функцию для обработки и ждем результат которыей будет присвоен перененной result
    return jsonify({'result': result}) # возвращаем на форму полученные данные 

app.route('/process_number2', methods=['POST'])  # декоратор для обработки POST-запроса с введеным числом
def process_text():
    text = request.form['text'] # получаем из поля "text" значение 
    result = youwish(int(text)) # передаем его в функцию для обработки и ждем результат которыей будет присвоен перененной result
    return jsonify({'result': result}) # возвращаем на форму полученные данные 


def resetNumber():# сброс счетчиков и перегенерация нового числа
    attempt.clear() # сброс счетчиков попыток
    num_mag.clear() # сброс сгененрированного числа
    num_mag.append(random.randint(1, 100)) # перегенерация нового числа

def youwish(num:int = 0,): # функция для обработки полученного числа, по умолчанию оно равна=0
    value=num_mag[0] # присваиваем переменной value сгененрированное цисло из списка
    try: # обработчик ошибок 
        while True:
            # немного читерства, чтобы узнать правильные ответ
            attempt.append(str(num))
            if num == 7777:
                return f"You are a cheater, the answer is {value}" 
            # логика проверки числа, в зависимости от результата формируется ответ для страницы
            if value == num:
                txt_att=",".join(attempt)
                return f"You win!!!  Your attempts {len(attempt)} \n list variants {txt_att}" 
            elif value < num:
                return f"Attempt {len(attempt)}. Number is less"
            elif value > num:
                return f"Attempt {len(attempt)}. Number is more"
    except Exception as e:
        # если возникнут ошибки вернет "Error!!!! - и ошибку"
        return f"Error!!!!  {str(e)}"



def iwish():
    pass
if __name__ == '__main__':
    
    app.run(debug=True)