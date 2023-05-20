from flask import Flask, render_template, request, redirect, url_for
from service import line_bot, kintone

app = Flask(__name__)

@app.route('/', methods=['GET'])
def init():
    return redirect('/shop')

@app.route('/shop', methods=['GET'])
def shop_list():
    # kintoneからselect
    # line_bot.send_ticket('sample')
    return render_template('shop/list.html')

@app.route('/shop/<shop_id>', methods=['GET'])
def shop_details(shop_id):
    # kintoneからselect id = shop_id
    return render_template('shop/details.html')

@app.route('/ticket', methods=['GET'])
def ticket_list():
    # kintoneからselect
    return render_template('ticket/list.html')

@app.route('/ticket/<ticket_id>', methods=['GET'])
def ticket_details(ticket_id):
    # kintoneからselect id = ticket_id
    return render_template('ticket/details.html')

if __name__ == '__main__':
    app.run(debug=True, port="5000")