MAX_NUMBERS_ORDERED = 20


class Cart:
    """Giỏ hàng chứa tối đa MAX_NUMBERS_ORDERED đĩa DVD."""

    def __init__(self):
        self.items = []

    def add_dvd(self, dvd):
        if len(self.items) >= MAX_NUMBERS_ORDERED:
            print("The cart is almost full")
            return False
        self.items.append(dvd)
        print("The disc has been added")
        return True

    def remove_dvd(self, dvd):
        if dvd in self.items:
            self.items.remove(dvd)
            print("The disc has been removed")
            return True
        print("The disc is not in the cart")
        return False

    def total_cost(self):
        return sum(item.cost for item in self.items)

    def print_cart(self):
        """In danh sách các sản phẩm trong giỏ hàng và tổng chi phí."""
        print("***********************CART***********************")
        print("Ordered Items:")
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item}")
        print(f"Total cost: {self.total_cost()} $")
        print("**************************************************")

    def search_by_title(self, title):
        """Tìm kiếm DVD trong giỏ hàng theo tiêu đề (hỗ trợ tìm gần đúng)."""
        results = [item for item in self.items if title.lower() in item.title.lower()]
        return results


def calculate_discount(total, percent):
    """Tính toán tổng tiền sau khi giảm giá và kiểm tra hợp lệ phần trăm."""
    if percent < 0 or percent > 100:
        raise ValueError("Percent must be between 0 and 100")
    discounted_total = total * (100 - percent) / 100
    return discounted_total