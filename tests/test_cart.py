import unittest
from aims.cart import Cart, MAX_NUMBERS_ORDERED
from aims.dvd import DigitalVideoDisc


class TestCart(unittest.TestCase):

    def test_add_dvd_until_full(self):
        cart = Cart()
        # Thêm đủ số lượng tối đa (20 đĩa)
        for i in range(MAX_NUMBERS_ORDERED):
            dvd = DigitalVideoDisc(f"DVD {i}", "Category", "Director", 90, 10.0)
            result = cart.add_dvd(dvd)
            self.assertTrue(result)

        # Thêm đĩa thứ 21 (vượt quá giới hạn -> phải trả về False)
        extra_dvd = DigitalVideoDisc("DVD 21", "Category", "Director", 90, 10.0)
        result_extra = cart.add_dvd(extra_dvd)
        self.assertFalse(result_extra, "Cart should reject the 21st DVD")


if __name__ == "__main__":
    unittest.main()