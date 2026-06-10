# Experiment Report: Data Quality Impact on AI Agent

**Student ID:** AI20K-2A202600974  
**Name:** Nguyễn Minh Khoa  
**Date:** 10/06/2026  

---

## 1. Ket qua thi nghiem

Chay `agent_simulation.py` voi 2 bo du lieu va ghi lai ket qua:

| Scenario | Agent Response | Accuracy (1-10) | Notes |
|----------|----------------|-----------------|-------|
| Clean Data (`processed_data.csv`) | Agent chon san pham hop le trong category Electronics, vi du Laptop hoac Monitor, dua tren du lieu da duoc lam sach. | 9 | Du lieu da duoc validate nen khong con price am, category rong. Agent co the dua ra ket qua dang tin cay hon. |
| Garbage Data (`garbage_data.csv`) | Agent co the chon ket qua sai hoac bat thuong, vi du san pham co gia qua lon, duplicate ID, null value hoac sai kieu du lieu. | 4 | Du lieu rac lam agent bi nhieu, de chon sai san pham hoac dua ra nhan xet khong chinh xac. |

---

## 2. Phan tich & nhan xet

### Tai sao Agent tra loi sai khi dung Garbage Data?

Agent tra loi sai khi dung Garbage Data vi chat luong du lieu dau vao khong dam bao. Trong bo du lieu rac co nhieu van de nhu duplicate IDs, wrong data types, outliers va null values. Duplicate IDs lam agent kho xac dinh dau la record dung. Wrong data types, vi du gia san pham bi ghi thanh chuoi thay vi so, co the lam qua trinh tinh toan hoac so sanh bi sai. Outliers nhu mot san pham co gia qua lon co the khien agent chon no la ket qua tot nhat, mac du thuc te no khong hop ly. Null values lam thieu thong tin quan trong, khien agent khong co du ngu canh de dua ra cau tra loi chinh xac. Dieu nay cho thay loi cua AI khong chi den tu prompt hay model, ma con den tu du lieu dau vao.

---

## 3. Ket luan

**Quality Data > Quality Prompt?**

Em dong y. Du lieu chat luong cao quan trong hon prompt trong nhieu truong hop, vi prompt tot van khong the sua hoan toan du lieu dau vao bi sai. Neu data co price am, category rong, duplicate hoac outlier, agent van co nguy co dua ra ket qua sai. Khi du lieu da duoc validate va transform tot, agent co nen tang dang tin cay hon de tra loi chinh xac.