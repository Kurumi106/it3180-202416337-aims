from aims.cart import Cart
from aims.dvd import DigitalVideoDisc

def main():
    print("=== AIMS-mini v1.1.0-dev ===")
    cart = Cart()
    
    # Thêm các đĩa DVD vào giỏ hàng
    cart.add_dvd(DigitalVideoDisc("The Lion King", "Animation", "Roger Allers", 87, 19.95))
    cart.add_dvd(DigitalVideoDisc("Aladdin", "Animation", cost=18.99))
    cart.add_dvd(DigitalVideoDisc("Star Wars", "Science Fiction", "George Lucas", 87, 24.95))

    print("\n--- Giỏ hàng ban đầu ---")
    cart.print_cart()

    # Kiểm tra tính năng sắp xếp theo tiêu đề
    print("\n--- Sau khi sắp xếp theo tiêu đề (Title) ---")
    cart.sort_by_title()
    cart.print_cart()

    # Kiểm tra tính năng sắp xếp theo chi phí
    print("\n--- Sau khi sắp xếp theo chi phí (Cost) ---")
    cart.sort_by_cost()
    cart.print_cart()

if __name__ == "__main__":
    main()