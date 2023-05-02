import random
from flask import Flask, jsonify, request, render_template

class MyNumber:
    def __init__(self):
        self.generated_numbers = []
        self.min_value = 1
        self.max_value = 100
        self.number = self.generate_number()

    def reset(self):
        self.min_value = 1
        self.max_value = 100
        self.generated_numbers = []
        self.number = random.randint(self.min_value, self.max_value)
    
    def generate_number(self):
        number = random.randint(self.min_value, self.max_value)
        while number in self.generated_numbers:
            number = random.randint(self.min_value, self.max_value)
        self.generated_numbers.append(number)
        return number

    def check_guess(self, guess):
        if guess == 'more':
            self.min_value = self.number + 1
            self.number = self.generate_number()
            return f"Number is {self.number}. Next guess?"
        elif guess == 'less':
            self.max_value = self.number - 1
            self.number = self.generate_number()
            return f"Number is {self.number}. Next guess?"
        elif guess == 'equals':
            return f'I`m won! Number of attempts: {len(self.generated_numbers)}'

num_mag:list = [] # список в котором хранится сгенерированное число
attempt:list=[] # список в котором хранятся все (цифры) попытки. 
game = MyNumber()

app = Flask(__name__) # присвоение переменой app объекта Flask(__name__) 


@app.route('/') # декоратор для обработки Главной страницы
def index():
    resetNumber() # при обновлении страницы сбрасываем все счетчики и перегенерируем число
    return render_template('index.html') # загружаем страницу HTML

@app.route('/number1')
def number1():
    resetNumber() # при обновлении страницы сбрасываем все счетчики и перегенерируем число
    return render_template('number1.html', attempt=len(attempt)) # загружаем страницу HTML

@app.route('/number2')
def number2():
    resetNumber() # при обновлении страницы сбрасываем все счетчики и перегенерируем число
    return render_template('number2.html', gener_value=num_mag[0]) # загружаем страницу HTML

@app.route('/process_number1', methods=['POST'])  # декоратор для обработки POST-запроса с введеным числом
def process_text():
    text = request.form['text'] # получаем из поля "text" значение 
    result = youwish(int(text)) # передаем его в функцию для обработки и ждем результат которыей будет присвоен перененной result
    return jsonify({'result': result}) # возвращаем на форму полученные данные 

@app.route('/iPick', methods=['POST'])
def iPick():
    
    ret_val=game.check_guess(request.form.get('action'))
    return jsonify({'result': ret_val})


def resetNumber():# сброс счетчиков и перегенерация нового числа
    game.reset()
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
                return f"You win!!!  Your attempts {len(attempt)}<br> list variants {txt_att}" 
            elif value < num:
                return f"Attempt {len(attempt)}. Number is less"
            elif value > num:
                return f"Attempt {len(attempt)}. Number is more"
    except Exception as e:
        # если возникнут ошибки вернет "Error!!!! - и ошибку"
        return f"Error!!!!  {str(e)}"



if __name__ == '__main__':
    
    app.run(debug=True)