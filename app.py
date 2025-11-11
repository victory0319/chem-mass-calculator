import streamlit as st

atomic_mass = {
    "H": 1.008,
    "C": 12.01,
    "O": 16.00,
    "N": 14.01,
    "Na": 22.99,
    "Cl": 35.45,
    "K": 39.10,
    "Ca": 40.08,
    "Mg": 24.31,
    "S": 32.07,
    "P": 30.97,
    "Fe": 55.85,
    "Zn": 65.38,
    "Cu": 63.55,
    "Ag": 107.87,
    "Au": 196.97,
    "Al": 26.98,
    "Si": 28.09,
    "F": 18.998,
    "I": 126.90,
    "Br": 79.90,
    "Mn": 54.94,
    "Co": 58.93
}

def formula(molecule):
    components = {}
    element = ""
    number = ""

    for i in molecule:
        if i.isupper():
            if element:
                if not number:
                    number = "1"
                if element in components:
                    components[element] += int(number)
                else:
                    components[element] = int(number)
            element = i
            number = ""
        elif i.islower():
            element += i
        elif i.isdigit():
            number += i
    if element:
        if not number:
            number = "1"
        if element in components:
            components[element] += int(number)
        else:
            components[element] = int(number)

    return components

st.title("화학식량 계산기")

molecule = st.text_input("분자식 입력", "Na2ClNNa")
mass = st.number_input("분자의 질량 입력 (g)", value=236.86)

if molecule:
    components = formula(molecule)
    mol_mass = 0
    for i in components:
        if i in atomic_mass:
            mol_mass += atomic_mass[i] * components[i]
        else:
            st.error(f"알 수 없는 원소: {i}")

    n_mols = mass / mol_mass
    NA = 6.022e23
    n_particles = n_mols * NA

    st.write(f"**분자량**: {mol_mass:.4f} g/mol")
    st.write(f"**몰 수**: {n_mols:.6f} mol")
    st.write(f"**입자 수**: {n_particles:.4e} 개")
