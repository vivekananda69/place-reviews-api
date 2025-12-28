# streamlit_app.py

import streamlit as st
import requests

BASE_URL = "https://place-reviews-api.onrender.com"


st.set_page_config(page_title="Place Reviews Demo", layout="centered")

st.title("📍 Place Reviews – Demo UI")

# ------------------ SESSION STATE ------------------
if "token" not in st.session_state:
    st.session_state.token = None

# ------------------ REGISTER ------------------
st.subheader("🔐 Register User")

phone = st.text_input("Phone")
name = st.text_input("Name")
password = st.text_input("Password", type="password")

if st.button("Register"):
    res = requests.post(
        f"{BASE_URL}/register/",
        json={"phone": phone, "name": name, "password": password}
    )

    if res.status_code == 201:
        st.session_state.token = res.json()["token"]
        st.success("Registered & logged in successfully")
    else:
        st.error(res.json().get("error", "Registration failed"))

# ------------------ ADD REVIEW ------------------
if st.session_state.token:
    st.subheader("✍️ Add Review")

    place_name = st.text_input("Place Name")
    address = st.text_input("Address")
    rating = st.slider("Rating", 1, 5, 5)
    text = st.text_area("Review")

    if st.button("Submit Review"):
        headers = {
            "Authorization": f"Token {st.session_state.token}"
        }

        res = requests.post(
            f"{BASE_URL}/review/",
            headers=headers,
            json={
                "name": place_name,
                "address": address,
                "rating": rating,
                "text": text
            }
        )

        if res.status_code == 201:
            st.success("Review added successfully")
        else:
            st.error(res.json().get("error", "Error adding review"))

# ------------------ SEARCH ------------------
st.subheader("🔍 Search Places")

search_name = st.text_input("Search by Name")
min_rating = st.selectbox("Minimum Rating", ["", 1, 2, 3, 4, 5])

params = {}
if search_name:
    params["name"] = search_name
if min_rating:
    params["min_rating"] = min_rating

if st.button("Search"):
    res = requests.get(f"{BASE_URL}/search/", params=params)

    if res.status_code == 200:
        for p in res.json():
            st.write(f"⭐ **{p['name']}** — Avg Rating: {p['average_rating']}")
    else:
        st.error("Search failed")

# ------------------ PLACE DETAIL ------------------
if st.session_state.token:
    st.subheader("🏠 Place Detail")

    place_id = st.number_input("Place ID", min_value=1, step=1)

    if st.button("Get Details"):
        headers = {
            "Authorization": f"Token {st.session_state.token}"
        }

        res = requests.get(
            f"{BASE_URL}/place/{place_id}/",
            headers=headers
        )

        if res.status_code == 200:
            data = res.json()
            st.write(f"### {data['name']}")
            st.write(data["address"])
            st.write(f"⭐ Average Rating: {data['average_rating']}")

            st.write("### Reviews")
            for r in data["reviews"]:
                st.markdown(
                    f"""
                    **{r['user']}**  
                    ⭐ {r['rating']}  
                    {r['text']}
                    ---
                    """
                )
        else:
            st.error("Place not found or unauthorized")
