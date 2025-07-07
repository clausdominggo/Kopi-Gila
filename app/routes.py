from flask import Blueprint, render_template, session, request, redirect, url_for, flash

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/about')
def about():
    return render_template('about.html')


@main.route('/menu', methods=['GET', 'POST'])
def menu():
    coffee_data = [
        {"name": "Java Aren", "price": 15000, "image": "images/Java Aren.jpg"},
        {"name": "Latte CSS", "price": 20000, "image": "images/Latte CSS.jpg"},
        {"name": "Moccahino", "price": 18000, "image": "images/moccahino python.webp"},
        {"name": "Long Dark", "price": 16000, "image": "images/Long Dark.jpg"},
        {"name": "Expreso HTML", "price": 21000, "image": "images/Expreso HTML.jpg"},
        {"name": "Kopi JS", "price": 17000, "image": "images/Kopi JS.jpg"},
        {"name": "Robusta PHP", "price": 14000, "image": "images/Robusta PHP.jpg"},
        {"name": "Classic React", "price": 19000, "image": "images/Classic React.jpg"},
        {"name": "Hazelnut XML", "price": 22000, "image": "images/Hazelnut XML.webp"},
        {"name": "Caramelo Kotlin", "price": 25000, "image": "images/Caramelo Kotlin.jpg"},
    ]

    if 'cart' not in session:
        session['cart'] = []

    if request.method == 'POST':
        item_name = request.form['item']
        quantity = int(request.form['quantity'])
        item = next((coffee for coffee in coffee_data if coffee['name'] == item_name), None)
        if item:
            session['cart'].append({
                'name': item['name'],
                'price': item['price'],
                'image': item['image'],
                'quantity': quantity
            })
            session.modified = True
        return redirect(url_for('main.menu'))

    return render_template('menu.html', coffee_data=coffee_data)


@main.route('/cart', methods=['GET', 'POST'])
def cart():
    if 'cart' not in session:
        session['cart'] = []

    message = None
    total_price = 0

    if request.method == 'POST':
        seat = request.form.get('seat')
        message = f"Pesanan berhasil dikonfirmasi untuk kursi nomor {seat}."
        session['cart'] = []

    cart_items = session['cart']
    for item in cart_items:
        try:
            total_price += item['price'] * item['quantity']
        except:
            pass

    return render_template(
        'cart.html',
        cart=cart_items,
        message=message,
        total_price=total_price
    )

@main.route('/products')
def products():
    return render_template('products.html')

@main.route('/review')
def review():
    return render_template('review.html')

@main.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # TODO: 
        flash('Pesan Anda telah dikirim. Terima kasih!', 'success')
        return redirect(url_for('main.contact'))
    return render_template('contact.html')


@main.route('/blogs')
def blogs():
    return render_template('blogs.html')
