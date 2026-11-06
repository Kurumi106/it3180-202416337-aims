import unittest
from aims.cart import calculate_discount


class TestDiscount(unittest.TestCase):

    def test_valid_discount(self):
        # Kiểm tra giảm giá hợp lệ: tổng 100, giảm 20% -> kỳ vọng kết quả là 80
        result = calculate_discount(100, 20)
        self.assertEqual(result, 80)

    def test_invalid_percent_discount(self):
        # Kiểm tra phần trăm không hợp lệ (> 100 hoặc < 0) phải ném ra ValueError
        with self.assertRaises(ValueError):
            calculate_discount(100, 150)
        with self.assertRaises(ValueError):
            calculate_discount(100, -10)


if __name__ == "__main__":
    unittest.main()