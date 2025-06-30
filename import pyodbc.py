import pyodbc

# Cấu hình kết nối SQL Server
conn_str = (
    "Driver={SQL Server};"
    "Server=DESKTOP-Q3MHK7P;"
    "Database=HoBiDB;"
    "Trusted_Connection=yes;"
)

try:
    # Nhập thông tin từ bàn phím
    name = input("Nhập tên: ")
    sdt = input("Nhập số điện thoại: ")

    # Kết nối
    conn = pyodbc.connect(conn_str)
    print("✅ Kết nối thành công SQL Server!")

    # Tạo cursor và thêm dữ liệu
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO admin_info (name, sdt) VALUES (?, ?)", (name, sdt)
    )
    conn.commit()
    print("✅ Đã thêm vào bảng admin_info!")

    # Truy vấn lại dữ liệu để hiển thị
    cursor.execute("SELECT * FROM admin_info")
    print("📄 Dữ liệu hiện tại:")
    for row in cursor.fetchall():
        print(f"Tên: {row.name}, SĐT: {row.sdt}")

    conn.close()

except Exception as e:
    print("❌ Lỗi kết nối:", e)
