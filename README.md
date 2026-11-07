# IT3180 - AIMS Project
Lab01
1. Hệ thống quản lý phiên bản (VCS) là gì và tại sao cần sử dụng?
VCS (Version Control System) là hệ thống ghi lại toàn bộ lịch sử thay đổi của tệp tin hoặc thư mục theo thời gian, cho phép người dùng khôi phục lại các trạng thái trước đó.
Tầm quan trọng: Giúp an toàn dữ liệu (dễ dàng hoàn tác khi code hỏng), hỗ trợ làm việc nhóm hiệu quả (nhiều người cùng sửa code mà không bị ghi đè file của nhau), và theo dõi trách nhiệm (biết rõ ai đã thêm/sửa dòng code nào và vào lúc nào).
2. Phân biệt Git và GitHub?
Git: Là một công cụ (phần mềm) quản lý phiên bản phân tán chạy trực tiếp trên máy tính cá nhân. Git làm nhiệm vụ theo dõi thay đổi và quản lý lịch sử commit cục bộ.
GitHub: Là một dịch vụ máy chủ đám mây chuyên lưu trữ các kho (repository) sử dụng Git. GitHub cung cấp giao diện web trực quan cùng các công cụ hỗ trợ cộng tác mạnh mẽ như Pull Request, Issues, wiki và review code.

Lab02
1. Vì sao phải đồng bộ master vào nhánh tính năng trước khi gửi PR?
Để phát hiện và giải quyết sớm các xung đột (merge conflict) cũng như kiểm tra tích hợp (chạy thử chương trình/test) ngay trên nhánh riêng trước khi đưa vào master, đảm bảo nhánh master luôn ở trạng thái ổn định và chạy được.
2. Khi nào không được dùng rebase?
Không được rebase trên các nhánh công khai đã chia sẻ cho nhiều người cùng làm việc (như master, release/*), vì rebase viết lại lịch sử (tạo mã băm SHA mới), làm lệch lịch sử với máy của các thành viên khác.
3. Nhánh feature/* khác nhánh topic/* như thế nào?
feature/*: Dùng để phát triển các tính năng mới của sản phẩm dành cho người dùng (ví dụ: feature/cart-print, feature/search-by-title).
topic/*: Dùng cho các công việc kỹ thuật, tài liệu, cấu hình hoặc thử nghiệm không trực tiếp thêm tính năng phần mềm (ví dụ: topic/pr-template, topic/use-case-diagram).

Lab03
1. Merge base là gì?
Merge base là điểm kỳ cựu chung (common ancestor) gần nhất của hai nhánh đang được hợp nhất. Trong giao diện Pull Request trên GitHub, "base branch" được hiểu là nhánh đích mà bạn muốn gộp code vào (ví dụ: master hoặc feature/discount).
2. Vì sao master/release/* phải dùng revert?
Các nhánh master và release/* là nhánh công khai (đã chia sẻ cho nhiều người hoặc đã phát hành). Nếu dùng reset (hay rebase, amend), ta sẽ thay đổi/viết lại lịch sử. Khi đẩy lên, sự sai lệch lịch sử sẽ gây ra lỗi nghiêm trọng (conflict) cho các lập trình viên khác khi họ git pull. Lệnh git revert tạo ra một commit hoàn toàn mới nhằm đảo ngược sự thay đổi, giúp bảo toàn toàn bộ lịch sử trước đó, do vậy an toàn khi làm việc nhóm.

Lab04
1. Vì sao release/* không bao giờ merge ngược vào master?
Nhánh release/* là nhánh đóng băng để bảo trì một phiên bản cụ thể. Nếu ta merge toàn bộ nhánh release/* vào master, ta có thể vô tình làm rối loạn cấu trúc hoặc đè lên các tính năng mới đang được phát triển tích cực trên master. Nếu có lỗi (bug) trên release, ta tạo nhánh hotfix và dùng lệnh cherry-pick để nhặt đúng đoạn mã sửa lỗi đó đưa về master.
2. So sánh quy trình này với GitFlow?
GitFlow: Dùng nhánh develop để tích hợp tính năng hàng ngày và nhánh master chỉ để lưu các bản đã phát hành.
Release Flow (của học phần): Chỉ có một nhánh chính sống lâu dài là master. Khi cần phát hành, ta tách nhánh release/* từ master ra để ổn định và bảo trì. Cách này giúp nhánh sống ngắn hơn, giữ mọi thứ gần master nhất có thể và tránh được tình trạng "merge hell".
3. Vì sao nâng lên 1.0.0 mà không phải 0.4.0?
Theo nguyên tắc Semantic Versioning (SemVer), các phiên bản bắt đầu bằng 0.y.z là giai đoạn phát triển ban đầu, mã nguồn chưa ổn định và API có thể thay đổi liên tục. Khi ứng dụng đạt mốc ổn định, hoàn thiện các tính năng cốt lõi và sẵn sàng xuất bản/nộp bài, ta phải nâng phiên bản MAJOR lên 1.0.0 để đánh dấu sự phá vỡ tính không ổn định của giai đoạn nháp.

Lab05
1. Upstream first vs Release first?
Upstream first (Sửa master trước, cherry-pick về release):
Ưu: Không bao giờ quên cập nhật bản sửa lỗi cho các tính năng tương lai.
Nhược: Dễ bị xung đột (conflict) nặng hoặc không tương thích khi mang ngược một đoạn code từ môi trường mới nhất về môi trường cũ.
Release first (Sửa release trước, cherry-pick về master - Cách Lab 05 làm):
Ưu: Cứu khách hàng ngay lập tức trên môi trường bản cũ, độ tương thích 100% không rủi ro.
Nhược: Lập trình viên dễ "quên" thao tác cherry-pick mang bản vá lên nhánh master/các nhánh release tương lai, khiến lỗi tái bùng phát ở bản cập nhật sau.
2. Nếu quên lan truyền lỗi sang release/lab05, lệnh kiểm toán nào phát hiện?
Lệnh git tag --contains <FIX_SHA> sẽ chỉ liệt kê v1.0.1 mà vắng bóng v1.1.0.
Chạy script kiểm thử sẽ thấy nhánh v1.1.0 trả về 0 kết quả (Fail) thay vì 1 (Pass).
