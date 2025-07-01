from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    admin = {
        "name": "Hồ Bi",
        "sdt": "09xxxxxxxx"  # Thay bằng số thật nếu muốn
    }
    return render_template("index.html", admin=admin)

@app.route("/places")
def places():
    # Danh sách địa điểm, mỗi phần tử là dict chứa ảnh, tên, mô tả
    places_data = [
        {"image": "halong.jpg", "title": "Vịnh Hạ Long (Quảng Ninh)", "desc": "Kỳ quan thiên nhiên thế giới với hàng nghìn đảo đá vôi và hang động kỳ ảo giữa làn nước biển trong xanh."},
        {"image": "sapa.jpg", "title": "Sa Pa (Lào Cai)", "desc": "Thị trấn mờ sương nằm giữa núi rừng Tây Bắc với ruộng bậc thang, bản làng và đỉnh Fansipan."},
        {"image": "phongnha.jpg", "title": "Phong Nha - Kẻ Bàng (Quảng Bình)", "desc": "Di sản thiên nhiên thế giới với hệ thống hang động kỳ vĩ, nổi bật là hang Sơn Đoòng – lớn nhất thế giới."},
        {"image": "phuquoc.jpg", "title": "Phú Quốc (Kiên Giang)", "desc": "Hòn đảo ngọc với biển xanh cát trắng, rừng nguyên sinh và các khu bảo tồn sinh thái đa dạng."},
        {"image": "baoloc.jpg", "title": "Bảo Lộc (Lâm Đồng)", "desc": "Thành phố nhỏ yên bình với đồi chè, thác nước và khí hậu mát mẻ quanh năm."},
        {"image": "trangan.jpg", "title": "Tràng An (Ninh Bình)", "desc": "Quần thể danh thắng với sông núi thơ mộng, di sản văn hóa và thiên nhiên thế giới."},

        # Thêm ảnh mới:
        {"image": "new_place1.jpg", "title": "Địa điểm mới 1", "desc": "Mô tả địa điểm mới 1."},
        {"image": "new_place2.jpg", "title": "Địa điểm mới 2", "desc": "Mô tả địa điểm mới 2."}
    ]
    return render_template("places.html", places=places_data)
@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
