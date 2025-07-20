import customtkinter as ctk

# Importiere Funktionen aus den Dateien
from src.LinearAlgebra import Matrix, ComplexNumbers
from NumberTheory import is_prime, ggT, kgV, prime_factors, euler_phi, find_invertible
from Polynomial import Polynom
from NumberBases import convertToDecimal, convertToBaseX, intTRoman, romantoInt


# ------------------------------------------------------------------------------------------------------#

# Gennerelle Funktionen
def parse_matrix(input_str):
    # Matrix-String z.B. "1, 2; 3, 4" wird in eine Liste von Listen umgewandelt
    rows = input_str.split(';')
    return [list(map(int, row.split(','))) for row in rows]


def on_select_scrollbar(value):
    rounded_value = round(value / 100) * 100
    label_selected_number.configure(text=f"Integrations-Genauigkeit: {rounded_value}")
    scrollbar.set(rounded_value)


def on_select_scrollbarzahlensys(value):
    rounded_value = round(value)
    label_number.configure(text=f"Zahlensystem: {rounded_value}")
    scrollbar1.set(rounded_value)


# ------------------------------------------------------------------------------------------------------#

# Hauptfenster
app = ctk.CTk()
app.title("Math Script by Finn")
app.geometry("800x600")

# Tabs erstellen
tabview = ctk.CTkTabview(app)
tabview.pack(pady=20, padx=20, fill="both", expand=True)

# ------------------------------------------------------------------------------------------------------#

# Lineare Algebra Tab
tab_algebra = tabview.add("Lineare Algebra")

label_matrix1 = ctk.CTkLabel(tab_algebra, text="Matrix 1 (z.B. 1,2; 3,4)", font=("Arial", 16))
label_matrix1.pack(pady=5)
entry_matrix1 = ctk.CTkEntry(tab_algebra, width=600, height=50, font=("Arial", 14))
entry_matrix1.pack(pady=10)

label_matrix2 = ctk.CTkLabel(tab_algebra, text="Matrix 2 für Multiplikation (z.B. 1,2; 3,4)", font=("Arial", 16))
label_matrix2.pack(pady=5)
entry_matrix2 = ctk.CTkEntry(tab_algebra, width=600, height=50, font=("Arial", 14))
entry_matrix2.pack(pady=10)


def matrix_multiply():
    try:
        matrix1 = parse_matrix(entry_matrix1.get())
        matrix2 = parse_matrix(entry_matrix2.get())
        m1 = Matrix(matrix1)
        m2 = Matrix(matrix2)
        result = m1 * m2
        ergebnis_text.set(f"Ergebnis der Matrixmultiplikation:\n{result}")
    except Exception as e:
        ergebnis_text.set(f"Fehler: {str(e)}")


def berechne_determinante():
    try:
        matrix = parse_matrix(entry_matrix1.get())
        m = Matrix(matrix)
        det = m.findDet()
        ergebnis_text.set(f"Determinante: {det}")
    except Exception as e:
        ergebnis_text.set(f"Fehler: {str(e)}")


def berechne_charpoly():
    try:
        matrix = parse_matrix(entry_matrix1.get())
        m = Matrix(matrix)
        char = m.findCharPoly()
        ergebnis_text.set(f"Polynom: {char}")
    except Exception as e:
        ergebnis_text.set(f"Fehler: {str(e)}")


def berechne_eigenwerte():
    try:
        matrix = parse_matrix(entry_matrix1.get())
        m = Matrix(matrix)
        invert = m.isInvertible()
        if not invert:
            ergebnis_text.set("Diese Matrix hat keine Eigenwertre, da die Determinante gleich 0 ist.")
        else:
            eig = m.findEigenwerte()
            ergebnis_text.set(f"Eigenwerte: {eig}")
    except Exception as e:
        ergebnis_text.set(f"Fehler: {str(e)}")


# Buttons für Lineare Algebra
button_multiply = ctk.CTkButton(tab_algebra, text="Matrix multiplizieren", command=matrix_multiply, width=125,
                                height=40, font=("Arial", 16))
button_multiply.pack(pady=20)

button_det = ctk.CTkButton(tab_algebra, text="Determinante berechnen", command=berechne_determinante, width=125,
                           height=40, font=("Arial", 16))
button_det.pack(pady=20)

button_char = ctk.CTkButton(tab_algebra, text="Charakteristisches Polynom berechnen", command=berechne_charpoly,
                            width=125, height=40, font=("Arial", 16))
button_char.pack(pady=20)

button_eig = ctk.CTkButton(tab_algebra, text="Eigenwerte berechnen", command=berechne_eigenwerte, width=125, height=40,
                           font=("Arial", 16))
button_eig.pack(pady=20)

# ------------------------------------------------------------------------------------------------------#

# Zahlensysteme Tab
tab_zahlensys = tabview.add("Zahlen Systeme")


def change_base():
    try:
        zahl, base = entry_zahl_sys.get().split(',')
        wantedBase = round(int(scrollbar1.get()))
        print(f"Zahl : {zahl}, Base : {base}, WantedBase: {wantedBase}")
        if not base == 10:
            zahl = convertToDecimal(str(zahl), int(base))
        ergebnis_text.set(f"Zahl: {convertToBaseX(zahl, wantedBase)}")
    except Exception as e:
        ergebnis_text.set(f"Fehler: {str(e)}")


# Buttons für Zahlensysteme

label_zahl_sys = ctk.CTkLabel(tab_zahlensys, text="Zahl, Basis z.B. (A2, 16)", font=("Arial", 16))
label_zahl_sys.pack(pady=5)
entry_zahl_sys = ctk.CTkEntry(tab_zahlensys, width=600, height=50, font=("Arial", 14))
entry_zahl_sys.pack(pady=10)

label_number = ctk.CTkLabel(tab_zahlensys, text="Zalensystem: ", font=("Arial", 16))
label_number.pack(pady=10)

scrollbar1 = ctk.CTkSlider(tab_zahlensys, from_=2, to=16, orientation="horizontal", width=200,
                           command=on_select_scrollbarzahlensys)
scrollbar1.pack(pady=20)

button_add = ctk.CTkButton(tab_zahlensys, text="Umwandeln", command=change_base, width=200, height=50,
                           font=("Arial", 16))
button_add.pack(pady=20)

# ------------------------------------------------------------------------------------------------------#

# Komplexe Zahhlen Tab
tab_complexn = tabview.add("Komplexe Zahlen")


def komplex_mul():
    try:
        k1_re, k1_im = map(int, entry_kzahl1.get().split(','))
        k2_re, k2_im = map(int, entry_kzahl2.get().split(','))
        zahl1 = ComplexNumbers(k1_re, k1_im)
        zahl2 = ComplexNumbers(k2_re, k2_im)
        res = zahl1 * zahl2
        ergebnis_text.set(f"Ergebnis: {res}")
    except Exception as e:
        ergebnis_text.set(f"Fehler: {e}")


def komplex_len():
    try:
        k_re, k_im = map(int, entry_kzahl1.get().split(','))
        res = ComplexNumbers(k_re, k_im)
        ergebnis_text.set(f"Länge: {res.len}")
    except Exception as e:
        ergebnis_text.set(f"Fehler: {e}")


# Buttons für Komplexe Zahhlen

label_kzahl1 = ctk.CTkLabel(tab_complexn, text="Zahl 1 (re, im) 1 (z.B. 1,2)", font=("Arial", 16))
label_kzahl1.pack(pady=5)
entry_kzahl1 = ctk.CTkEntry(tab_complexn, width=600, height=50, font=("Arial", 14))
entry_kzahl1.pack(pady=10)

label_kzahl2 = ctk.CTkLabel(tab_complexn, text="Zahl 2 ", font=("Arial", 16))
label_kzahl2.pack(pady=5)
entry_kzahl2 = ctk.CTkEntry(tab_complexn, width=600, height=50, font=("Arial", 14))
entry_kzahl2.pack(pady=10)

button_mul = ctk.CTkButton(tab_complexn, text="Multiplikation", command=komplex_mul, width=200, height=50,
                           font=("Arial", 16))
button_mul.pack(pady=20)

button_length = ctk.CTkButton(tab_complexn, text="Länge", command=komplex_len, width=200, height=50,
                              font=("Arial", 16))
button_length.pack(pady=20)

# ------------------------------------------------------------------------------------------------------#

# Polynom Tab

tab_poly = tabview.add("Polynome")

label_poly = ctk.CTkLabel(tab_poly, text="Polynom eingeben (z.B. 4,2 = 4x + 2)", font=("Arial", 16))
label_poly.pack(pady=5)
entry_poly = ctk.CTkEntry(tab_poly, width=600, height=50, font=("Arial", 14))
entry_poly.pack(pady=10)

label_poly1 = ctk.CTkLabel(tab_poly, text="f(x) z.B (4) ; Integratinsgrenzen z.B (1,2)", font=("Arial", 16))
label_poly1.pack(pady=5)
entry_poly1 = ctk.CTkEntry(tab_poly, width=600, height=50, font=("Arial", 14))
entry_poly1.pack(pady=10)

label_selected_number = ctk.CTkLabel(tab_poly, text="Integratins-Genauigkeit: ", font=("Arial", 16))
label_selected_number.pack(pady=10)

# Horizontaler Scrollbar, der Zahlen von 1 bis 100 enthält
scrollbar = ctk.CTkSlider(tab_poly, from_=100, to=10000, orientation="horizontal", width=200,
                          command=on_select_scrollbar)
scrollbar.pack(pady=20)


# Funktioen für Polynome
def nullst():
    try:
        zahlen = Polynom(entry_poly.get().split(','))
        result = zahlen.null_stellen()
        ergebnis_text.set(f"Nullstellen: {result}")
    except Exception as e:
        ergebnis_text.set(f"Fehler: {str(e)}")


def evalP():
    try:
        zahlen = Polynom(entry_poly.get().split(','))
        evalPoint = int(entry_poly1.get())
        result = zahlen.evaluate(evalPoint)
        ergebnis_text.set(f"f({evalPoint}): {result}")
    except Exception as e:
        ergebnis_text.set(f"Fehler: {str(e)}")


def integrate():
    try:
        zahlen = Polynom(entry_poly.get().split(','))
        integrationPoint = (entry_poly1.get().split(','))
        result = zahlen.integration_trapez(int(integrationPoint[0]), int(integrationPoint[1]), int(scrollbar.get()))
        ergebnis_text.set(f"Integration: {result}")
    except Exception as e:
        ergebnis_text.set(f"Fehler: {str(e)}")


# Buttons für Polynome

button_ns = ctk.CTkButton(tab_poly, text="Nullstellen", command=nullst, width=200, height=50, font=("Arial", 16))
button_ns.pack(pady=20)

button_ev = ctk.CTkButton(tab_poly, text="Evaluate", command=evalP, width=200, height=50, font=("Arial", 16))
button_ev.pack(pady=20)

button_in = ctk.CTkButton(tab_poly, text="Integriere", command=integrate, width=200, height=50, font=("Arial", 16))
button_in.pack(pady=20)

# ------------------------------------------------------------------------------------------------------#

# Zahlentheorie Tab
tab_zahlentheorie = tabview.add("Zahlentheorie")

label_zahl = ctk.CTkLabel(tab_zahlentheorie, text="Zahl eingeben (z.B. 42)", font=("Arial", 16))
label_zahl.pack(pady=5)
entry_zahl = ctk.CTkEntry(tab_zahlentheorie, width=600, height=50, font=("Arial", 14))
entry_zahl.pack(pady=10)


def ist_primzahl():
    try:
        zahl = int(entry_zahl.get())
        is_prime_result = is_prime(zahl)
        ergebnis_text.set(f"Ist Primzahl: {is_prime_result}")
    except Exception as e:
        ergebnis_text.set(f"Fehler: {str(e)}")


def primefs():
    try:
        zahl = int(entry_zahl.get())
        is_prime_result = prime_factors(zahl)
        ergebnis_text.set(f"Primzahlzerlegung: {is_prime_result}")
    except Exception as e:
        ergebnis_text.set(f"Fehler: {str(e)}")


def berechne_ggt():
    try:
        zahl1, zahl2 = map(int, entry_zahl.get().split(','))
        ggt_result = ggT(zahl1, zahl2)
        ergebnis_text.set(f"ggT: {ggt_result}")
    except Exception as e:
        ergebnis_text.set(f"Fehler: {str(e)}")


def berechne_kgV():
    try:
        zahl1, zahl2 = map(int, entry_zahl.get().split(','))
        kgV_result = kgV(zahl1, zahl2)
        ergebnis_text.set(f"kgV: {kgV_result}")
    except Exception as e:
        ergebnis_text.set(f"Fehler: {str(e)}")


def euler_phi_berechnen():
    try:
        zahl = int(entry_zahl.get())
        res = euler_phi(zahl)
        ergebnis_text.set(f"Euler-Phi: {res}")
    except Exception as e:
        ergebnis_text.set(f"Fehler: {str(e)}")


def inverse_berechnen():
    try:
        zahl, k = map(int, entry_zahl.get().split(','))
        res = find_invertible(zahl, k)
        ergebnis_text.set(f"Inverse: {res}")
    except Exception as e:
        ergebnis_text.set(f"Fehler: {str(e)}")


# ------------------------------------------------------------------------------------------------------#

# Römische Zahlen Tab
tab_roman = tabview.add("Römische Zahlen")


def romantoDez():
    try:
        rZahl = entry_roman.get()
        try:
            int(rZahl)
            ergebnis_text.set("Fehler: Keine Römisce Zahl angegeben")
        except ValueError:
            res = romantoInt(rZahl)
            ergebnis_text.set(f"Dezimal Zahl: {res}")
    except Exception as e:
        ergebnis_text.set(f"Fehler: {e}")


def dezToRoman():
    try:
        dZahl = int(entry_roman.get())
        res = intTRoman(dZahl)
        ergebnis_text.set(f"Römischee Zahl: {res}")
    except Exception as e:
        ergebnis_text.set(f"Fehler: {e}")


# Buttons für Römische Zahlen

label_roman = ctk.CTkLabel(tab_roman, text="Zahl z.B. (15, IX)", font=("Arial", 16))
label_roman.pack(pady=5)
entry_roman = ctk.CTkEntry(tab_roman, width=600, height=50, font=("Arial", 14))
entry_roman.pack(pady=10)

button_rToI = ctk.CTkButton(tab_roman, text="Römisch zu Dez", command=romantoDez, width=200, height=50,
                            font=("Arial", 16))
button_rToI.pack(pady=20)

button_iToR = ctk.CTkButton(tab_roman, text="Dez zu Römisch", command=dezToRoman, width=200, height=50,
                            font=("Arial", 16))
button_iToR.pack(pady=20)

# Buttons für Zahlentheorie
button_primzahl = ctk.CTkButton(tab_zahlentheorie, text="Primzahl testen", command=ist_primzahl, width=200, height=50,
                                font=("Arial", 16))
button_primzahl.pack(pady=20)

button_ggt = ctk.CTkButton(tab_zahlentheorie, text="ggT berechnen", command=berechne_ggt, width=200, height=50,
                           font=("Arial", 16))
button_ggt.pack(pady=20)

button_kgV = ctk.CTkButton(tab_zahlentheorie, text="kgV berechnen", command=berechne_kgV, width=200, height=50,
                           font=("Arial", 16))
button_kgV.pack(pady=20)

button_pf = ctk.CTkButton(tab_zahlentheorie, text="Primfaktor zerlegung", command=primefs, width=200, height=50,
                          font=("Arial", 16))
button_pf.pack(pady=20)

button_ep = ctk.CTkButton(tab_zahlentheorie, text="Euler-Phi-Fkt", command=euler_phi_berechnen, width=200, height=50,
                          font=("Arial", 16))
button_ep.pack(pady=20)

button_inv = ctk.CTkButton(tab_zahlentheorie, text="Inverse", command=inverse_berechnen, width=200, height=50,
                           font=("Arial", 16))
button_inv.pack(pady=20)

# ------------------------------------------------------------------------------------------------------#

# Ergebnisfeld für alle Tabs
ergebnis_text = ctk.StringVar()
ergebnis_label = ctk.CTkLabel(app, textvariable=ergebnis_text, font=("Arial", 18), width=600, height=200,
                              text_color="white", fg_color="darkgray", corner_radius=10)
ergebnis_label.pack(pady=30)

app.mainloop()
