from django.shortcuts import render, redirect
from django.shortcuts import render, redirect

cart_items = []

def home_redirect(request):
    return redirect('login')

def login_view(request):
    if request.method == "POST":
        # You can add authentication here later
        return redirect('shop')  # Redirect to shop after login
    return render(request, "boards/login.html")


def shop_view(request):
    products = [
        {"name": "Filipiniana Gown", "image": "boards/img/tshirt.jpg"},
        {"name": "Barong Tagalog", "image": "boards/img/men1.jpg"},
        {"name": "Barot’ Saya", "image": "boards/img/women1.jpg"},
    ]
    return render(request, "boards/shop.html", {"products": products})


def home(request):
    return render(request, 'boards/home.html')


def men_view(request):
    products = [
        {"name": "Barong Tagalog Classic", "image": "boards/img/men1.jpg"},
        {"name": "Modern Barong", "image": "boards/img/men2.jpg"},
        {"name": "Embroidered Barong", "image": "boards/img/men3.jpg"},
        {"name": "Short-Sleeve Barong", "image": "boards/img/men4.jpg"},
        {"name": "Formal Barong", "image": "boards/img/men5.jpg"},
    ]
    return render(request, "boards/category.html", {"category": "MEN", "products": products})


def women_view(request):
    products = [
        {"name": "Filipiniana Gown", "image": "boards/img/women1.jpg"},
        {"name": "Maria Clara Dress", "image": "boards/img/women2.jpg"},
        {"name": "Modern Filipiniana", "image": "boards/img/women3.jpg"},
        {"name": "Terno Gown", "image": "boards/img/women4.jpg"},
        {"name": "Traditional Gown", "image": "boards/img/women5.jpg"},
    ]
    return render(request, "boards/category.html", {"category": "WOMEN", "products": products})


def kids_view(request):
    products = [
        {"name": "Kids Barong", "image": "boards/img/kid1.jpg"},
        {"name": "Kids Filipiniana", "image": "boards/img/kid2.jpg"},
        {"name": "Mini Terno", "image": "boards/img/kid3.jpg"},
        {"name": "Kids Formal", "image": "boards/img/kid4.jpg"},
        {"name": "Kids Barot Saya", "image": "boards/img/kid5.jpg"},
    ]
    return render(request, "boards/category.html", {"category": "KIDS", "products": products})


def product_detail(request, category, product_name):
    product_data = {
        "MEN": [
            {"name": "Barong Tagalog Classic", "image": "boards/img/men1.jpg", "price": 2800, "description": "Classic embroidered barong made from fine piña fabric."},
            {"name": "Modern Barong", "image": "boards/img/men2.jpg", "price": 3000, "description": "Modern-cut barong with detailed hand-stitching."},
            {"name": "Embroidered Barong", "image": "boards/img/men3.jpg", "price": 3200, "description": "Detailed embroidery barong."},
            {"name": "Short-Sleeve Barong", "image": "boards/img/men4.jpg", "price": 2500, "description": "Casual short-sleeve barong for events."},
            {"name": "Formal Barong", "image": "boards/img/men5.jpg", "price": 3500, "description": "Traditional formal wear for men."},
        ],
        "WOMEN": [
            {"name": "Filipiniana Gown", "image": "boards/img/women1.jpg", "price": 3500, "description": "Elegant Filipiniana gown with butterfly sleeves."},
            {"name": "Maria Clara Dress", "image": "boards/img/women2.jpg", "price": 3000, "description": "Modern gown inspired by traditional design."},
            {"name": "Modern Filipiniana", "image": "boards/img/women3.jpg", "price": 3200, "description": "Red gown with detailed embroidery."},
            {"name": "Terno Gown", "image": "boards/img/women4.jpg", "price": 3200, "description": "Elegant Terno Gown perfect for formal events."},
            {"name": "Traditional Gown", "image": "boards/img/women5.jpg", "price": 3200, "description": "Traditional Filipino gown with intricate patterns."},
        ],
        "KIDS": [
            {"name": "Kids Barong", "image": "boards/img/kid1.jpg", "price": 1500, "description": "Adorable kid’s Barong outfit."},
            {"name": "Kids Filipiniana", "image": "boards/img/kid2.jpg", "price": 1600, "description": "Beautiful Filipiniana for kids."},
            {"name": "Mini Terno", "image": "boards/img/kid3.jpg", "price": 1800, "description": "Perfect for special events."},
            {"name": "Kids Formal", "image": "boards/img/kid4.jpg", "price": 1800, "description": "PFormal attire designed especially for children."},
            {"name": "Kids Barot Saya", "image": "boards/img/kid5.jpg", "price": 1800, "description": "Adorable Baro’t Saya outfit perfect for school events and fiestas."},
        ],
    }

    product = next((item for item in product_data.get(category, []) if item["name"] == product_name), None)
    if not product:
        return redirect('shop')

    if request.method == "POST":
        if "add_to_cart" in request.POST:
            cart = request.session.get("cart", [])
            cart.append(product)
            request.session["cart"] = cart
            return redirect("cart")

        elif "buy_now" in request.POST:
            request.session["buy_now_item"] = product
            return redirect("checkout")

    return render(request, "boards/product_detail.html", {"product": product, "category": category})


def add_to_cart(request, category, product_name):
    global cart_items

    product = {
        "category": category,
        "name": product_name,
        "price": "₱5,000",
        "image": "boards/img/tshirt.jpg"
    }

    # Avoid duplicates
    if not any(item["name"] == product_name for item in cart_items):
        cart_items.append(product)

    return redirect('cart')


def cart(request):
    """Display temporary cart"""
    global cart_items
    context = {"cart_items": cart_items, "cart_empty": not cart_items}
    return render(request, "boards/cart.html", context)


def checkout_view(request, product_name):
    return render(request, "boards/checkout.html", {"product_name": product_name})


def about(request):
    return render(request, 'boards/about.html')


def contact(request):
    return render(request, 'boards/contact.html')


def thank_you(request):
    return render(request, 'boards/thank_you.html')

