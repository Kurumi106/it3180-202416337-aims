# Changelog

## [Unreleased]

## [1.0.0] - 2026-11-06
### Added
- Thêm tính năng in giỏ hàng (`print_cart`) và cập nhật demo (`693b47f`)
- Thêm tính năng tìm kiếm theo tiêu đề (`search_by_title`) (`3877215`)
- Thêm tài liệu biểu đồ ca sử dụng (Use case diagram) (`0bf6174`)
- Thêm mẫu Pull Request template (`d19d343`)
- Thêm phương thức `sort_by_title()` và `sort_by_cost()` vào lớp `Cart` để sắp xếp giỏ hàng theo tiêu đề và chi phí.

### Fixed
- Sửa lỗi giới hạn giỏ hàng, từ chối đĩa DVD vượt quá `MAX_NUMBERS_ORDERED` (#6) (`a562aba`)
- Sửa công thức tính giảm giá và kiểm tra hợp lệ phần trăm (`0e8a8a5`)




