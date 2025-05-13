import streamlit as st

# -------- MOCK DATA -------- #
CITY_DATA = {
    'Mumbai': {
        'area_m2': 603E6,     # in square meters
        'pwv_kg_per_m2': {'April': 40, 'May': 60, 'June': 65},
        'consumption_m3_per_month': 450_000_000
    },
    'Bengaluru': {
        'area_m2': 709E6,
        'pwv_kg_per_m2': {'April': 35, 'May': 45, 'June': 60},
        'consumption_m3_per_month': 130_000_000
    },
    'Delhi': {
        'area_m2': 1_484E6,
        'pwv_kg_per_m2': {'April': 30, 'May': 40, 'June': 55},
        'consumption_m3_per_month': 350_000_000
    }
}

MONTHS = ['April','May','June']

# --------- CORE CALC --------- #
def calculate_flux(area_m2, pwv_kg_per_m2):
    flux = area_m2 * pwv_kg_per_m2 * 0.001  # convert kg to m3
    return round(flux)

# --------- UI --------- #
st.title("☁️ Monthly Water Vapor Flux Over Cities")
st.write("Enter a city and month to view estimated atmospheric water vapor flux and municipal water consumption.")

city = st.selectbox("Select City", sorted(CITY_DATA))
month = st.selectbox("Select Month", MONTHS)

if city and month:
    data = CITY_DATA[city]
    pwv = data['pwv_kg_per_m2'].get(month, list(data['pwv_kg_per_m2'].values())[0])
    flux = calculate_flux(data['area_m2'], pwv)
    consumption = data['consumption_m3_per_month']

    st.subheader(f"Results for {city} ({month})")
    st.markdown(f"**Water Vapor Flux:** {flux:,} m³/month")
    st.markdown(f"**Water Consumption:** {consumption:,} m³/month")
    st.caption("Data is for demonstration purposes.")

