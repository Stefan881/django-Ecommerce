from .cart import Cart


# Create a context processors so that our app can work on all pages of the site

def cart(request):
    # Return the default data from our cart
    return {'cart': Cart(request)}
