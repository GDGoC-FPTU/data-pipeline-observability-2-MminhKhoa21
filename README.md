[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=24112860&assignment_repo_type=AssignmentRepo)

# Day 10 Lab: Data Pipeline & Data Observability

**Student Email:** mminhkhoa2102@gmail.com  
**Name:** Nguyễn Minh Khoa  

---

## Mo ta

Day 10 Lab yeu cau xay dung mot ETL Pipeline don gian bang Python de xu ly du lieu san pham tu file JSON. Trong bai lab nay, em da hoan thanh cac buoc Extract, Validate, Transform va Load.

Pipeline se doc du lieu tu `raw_data.json`, kiem tra va loai bo cac record khong hop le nhu `price <= 0` hoac `category` rong. Sau do, du lieu hop le se duoc transform bang cach chuan hoa `category` sang Title Case, tinh them cot `discounted_price` voi muc giam gia 10%, va them cot `processed_at` de ghi lai thoi diem xu ly. Cuoi cung, ket qua duoc luu vao file `processed_data.csv`.

Ngoai ra, bai lab con co phan Agent Simulation de so sanh tac dong cua du lieu sach va du lieu rac doi voi cau tra loi cua AI Agent. Ket qua cho thay chat luong du lieu dau vao anh huong truc tiep den do chinh xac cua Agent.

---

## Cach chay (How to Run)

### Prerequisites

Neu may da nhan lenh `pip`, chay:

```bash
pip install pandas