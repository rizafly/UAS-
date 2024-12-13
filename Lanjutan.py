import streamlit as st
import math
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# Judul Aplikasi
st.title("Kalkulator Matematika Lanjutan")

# Pilih Mode Kalkulator
st.sidebar.title("Mode Kalkulator")
mode = st.sidebar.selectbox("Pilih mode:", [
    "Kalkulator Integral",
    "Kalkulator Turunan",
    "Operasi Matriks",
    "Visualisasi Grafik"
])

# Mode Kalkulator Integral
if mode == "Kalkulator Integral":
    st.header("Kalkulator Integral")
    expression = st.text_input("Masukkan ekspresi fungsi (contoh: x**2)")
    variable = st.text_input("Masukkan variabel (contoh: x)", value="x")
    lower_limit = st.number_input("Batas bawah integral (opsional, kosongkan jika tidak tentu)", value=None, step=1.0, format="%f")
    upper_limit = st.number_input("Batas atas integral (opsional, kosongkan jika tidak tentu)", value=None, step=1.0, format="%f")

    if st.button("Hitung Integral"):
        try:
            x = sp.Symbol(variable)
            func = sp.sympify(expression)
            if lower_limit is None or upper_limit is None:
                result = sp.integrate(func, x)
            else:
                result = sp.integrate(func, (x, lower_limit, upper_limit))
            st.success(f"Hasil integral: {result}")
        except Exception as e:
            st.error(f"Terjadi kesalahan: {str(e)}")

# Mode Kalkulator Turunan
elif mode == "Kalkulator Turunan":
    st.header("Kalkulator Turunan")
    expression = st.text_input("Masukkan ekspresi fungsi (contoh: x**2)")
    variable = st.text_input("Masukkan variabel (contoh: x)", value="x")

    if st.button("Hitung Turunan"):
        try:
            x = sp.Symbol(variable)
            func = sp.sympify(expression)
            derivative = sp.diff(func, x)
            st.success(f"Hasil turunan: {derivative}")
        except Exception as e:
            st.error(f"Terjadi kesalahan: {str(e)}")

# Mode Operasi Matriks
elif mode == "Operasi Matriks":
    st.header("Operasi Matriks")
    matrix1 = st.text_area("Masukkan matriks pertama (contoh: [[1, 2], [3, 4]])")
    matrix2 = st.text_area("Masukkan matriks kedua (opsional, untuk operasi biner)")
    operation = st.selectbox("Pilih operasi:", ["Penjumlahan", "Pengurangan", "Perkalian", "Determinan"])

    if st.button("Hitung Matriks"):
        try:
            mat1 = np.array(eval(matrix1))
            if matrix2:
                mat2 = np.array(eval(matrix2))

            if operation == "Penjumlahan":
                result = mat1 + mat2
            elif operation == "Pengurangan":
                result = mat1 - mat2
            elif operation == "Perkalian":
                result = np.dot(mat1, mat2)
            elif operation == "Determinan":
                result = np.linalg.det(mat1)

            st.success(f"Hasil operasi matriks: {result}")
        except Exception as e:
            st.error(f"Terjadi kesalahan: {str(e)}")

# Mode Visualisasi Grafik
elif mode == "Visualisasi Grafik":
    st.header("Visualisasi Grafik")
    expression = st.text_input("Masukkan ekspresi fungsi (contoh: x**2)")
    variable = st.text_input("Masukkan variabel (contoh: x)", value="x")
    x_min = st.number_input("Masukkan nilai x minimum", value=-10.0, step=1.0, format="%f")
    x_max = st.number_input("Masukkan nilai x maksimum", value=10.0, step=1.0, format="%f")

    if st.button("Tampilkan Grafik"):
        try:
            x = sp.Symbol(variable)
            func = sp.lambdify(x, sp.sympify(expression), "numpy")
            x_vals = np.linspace(x_min, x_max, 500)
            y_vals = func(x_vals)

            plt.figure(figsize=(10, 6))
            plt.plot(x_vals, y_vals, label=f"f({variable}) = {expression}")
            plt.title("Grafik Fungsi")
            plt.xlabel(variable)
            plt.ylabel("f(x)")
            plt.legend()
            st.pyplot(plt)
        except Exception as e:
            st.error(f"Terjadi kesalahan: {str(e)}")