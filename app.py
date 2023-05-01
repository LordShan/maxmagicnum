import random
from flask import Flask, jsonify, request, render_template




num_mag:list = [] # список в котором хранится сгенерированное число
attempt:list=[] # список в котором хранятся все (цифры) попытки. 
list_genert=[1,100] # список в котором хранится range для random. 

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
    
    action = request.form.get('action')

    if action == 'more':
        list_genert[0] = num_mag[0]
        attempt.append(num_mag[0])
    elif action == 'less':
        list_genert[1] = num_mag[0]
        attempt.append(num_mag[0])
    elif action == 'equals':
        number = f"I winner!!!{len(attempt)}-attempts<br>Reload page for try again"
        list_genert=[1,100]
        return jsonify({'result': number})
        
    while True:
        if list_genert[0] - list_genert[1]==0: 
            yr_num = list_genert[0]
            list_genert=[1,100]
            return jsonify({'result': f"Your {yr_num} {len(attempt)}-attempts<br>Reload page for try again"})
        
        number = random.randint(list_genert[0], list_genert[1])
        if number not in attempt:
            number = random.randint(list_genert[0], list_genert[1])
            num_mag.insert(0,number)
        return jsonify({'result': f"My variant {number}"})

    
    number = random.randint(list_genert[0], list_genert[1])
    num_mag.insert(0,number)
    
    
    



def resetNumber():# сброс счетчиков и перегенерация нового числа
    attempt.clear() # сброс счетчиков попыток
    num_mag.clear() # сброс сгененрированного числа
    list_genert=[1,100]
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



if __name__ == '__main__':
    
    app.run(debug=True)