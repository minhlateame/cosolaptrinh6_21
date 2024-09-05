# Hàm để tính điểm trung bình
def tinh_diem_trung_binh(diem1, diem2):
    return (diem1 + diem2) / 2

# Nhập vào danh sách sinh viên và điểm của 2 môn
danh_sach_sinh_vien = []

while True:
    ma_sv = input("Nhập Mã Sinh Viên (hoặc nhấn Enter để kết thúc): ")
    if ma_sv == "":
        break
    ho_ten = input("Nhập Họ Tên: ")
    diem1 = float(input("Nhập Điểm Môn 1: "))
    diem2 = float(input("Nhập Điểm Môn 2: "))
    
    diem_tb = tinh_diem_trung_binh(diem1, diem2)
    
    sinh_vien = {
        "MaSV": ma_sv,
        "HoTen": ho_ten,
        "Diem1": diem1,
        "Diem2": diem2,
        "DiemTB": diem_tb
    }
    
    danh_sach_sinh_vien.append(sinh_vien)

# Tính điểm trung bình của Diem1 và Diem2 cho toàn bộ danh sách
diem1_tb = sum(sinh_vien["Diem1"] for sinh_vien in danh_sach_sinh_vien) / len(danh_sach_sinh_vien)
diem2_tb = sum(sinh_vien["Diem2"] for sinh_vien in danh_sach_sinh_vien) / len(danh_sach_sinh_vien)

print(f"Điểm Trung Bình Môn 1: {diem1_tb}")
print(f"Điểm Trung Bình Môn 2: {diem2_tb}")

# Sắp xếp danh sách SV theo cột điểm TB
danh_sach_sinh_vien.sort(key=lambda x: x["DiemTB"])

# In danh sách sinh viên đã sắp xếp
print("\nDanh sách sinh viên đã sắp xếp tăng dần theo Điểm Trung Bình:")
for sinh_vien in danh_sach_sinh_vien:
    print(f"Mã SV: {sinh_vien['MaSV']}, Họ Tên: {sinh_vien['HoTen']}, Điểm TB: {sinh_vien['DiemTB']}")
