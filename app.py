import random
from flask import Flask, jsonify, request, render_template



num_mag:list = []
attempt:list=[]

app = Flask(__name__)

@app.route('/')
def index():
    resetNumber()
    # num_mag.clear()
    # attempt.clear()
    # num_mag.append(random.randint(1, 100))
    return render_template('index.html', attempt=len(attempt))

@app.route('/process_text', methods=['POST'])
def process_text():
    text = request.form['text']
    # здесь можно обработать текст и получить результат
    result = youwish(int(text))
    return jsonify({'result': result})


def resetNumber():
    attempt.clear()
    num_mag.clear()
    num_mag.append(random.randint(1, 100))

def youwish(num:int = 0,):
    # value: int = random.randint(1, 100)
    value=num_mag[0]
    # cnt = 0
    try:
        while True:
            attempt.append(str(num))
            if num == 7777:
                return f"You are a cheater, the answer is {value}" 
            if value == num:
                txt_att=",".join(attempt)
                # value: int = random.randint(1, 100)
                return f"You win!!!  Your attempts {len(attempt)} \n list variants {txt_att}" 
            elif value < num:
                return f"Attempt {len(attempt)}. Number is less"
                print("Number is less")
            elif value > num:
                return f"Attempt {len(attempt)}. Number is more"
                print("Number is more")
    except Exception as e:
        return f"Error!!!!  {str(e)}"
    # num: int = int(input(f"Probe {cnt} \nMy number: "))
    # return("You win!")


def iwish():
    pass
if __name__ == '__main__':
    
    app.run(debug=True)