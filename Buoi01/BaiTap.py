# snake_case
# Kiểu dữ liệu: str, int, float, list [], dict {}, None


def tinh_tien(so_tien):
    if so_tien > 150:
        tien_tra = so_tien - 50
    elif so_tien > 100:
        tien_tra = so_tien - 25
    elif so_tien > 75:
        tien_tra = so_tien - 15
    else:
        tien_tra = so_tien
    return tien_tra

if __name__ == "__main__":
    so_tien = int(input("Nhập số tiền: "))
    # print(type(so_tien))
    print("Số tiền trả: ", tinh_tien(so_tien))

