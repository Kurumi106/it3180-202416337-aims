from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


def main():
    print("=== AIMS-mini v1.0.0 ===")
    cart = Cart()
    cart.add_dvd(
        DigitalVideoDisc(
            "The Lion King", "Animation", "Roger Allers", 87, 19.95
        )
    )
    cart.add_dvd(
        DigitalVideoDisc("Star Wars", "Science Fiction", "George Lucas", 87, 24.95)
    )
    cart.add_dvd(DigitalVideoDisc("Aladdin", "Animation", cost=18.99))

    print("\n--- Danh sach trong gio hang ---")
    cart.print_cart()

    print("\n--- Ket qua tim kiem theo tieu de ('lion') ---")
    results = cart.search_by_title("lion")
    if results:
        for item in results:
            print(item)
    else:
        print("No match found!")


if __name__ == "__main__":
    main()