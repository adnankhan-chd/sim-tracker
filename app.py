
import os
import re

import streamlit as st
from google import genai

# --------------------------------
# Page configuration
# --------------------------------

st.set_page_config(
    page_title="Pakistan SIM Network Checker",
    page_icon="📱",
    layout="centered",
)

st.title("🇵🇰 Pakistan SIM Network Checker")
st.write("Find the likely mobile network of a Pakistani phone number.")

# --------------------------------
# Network prefix database
# --------------------------------

NETWORK_PREFIXES = {
    "Jazz": ["0300", "0301", "0302", "0303", "0304",
             "0305", "0306", "0307", "0308", "0309"],

    "Zong": ["0310", "0311", "0312", "0313", "0314",
             "0315", "0316", "0317", "0318", "0319"],

    "Ufone": ["0330", "0331", "0332", "0333", "0334",
              "0335", "0336", "0337", "0338", "0339"],

    "Telenor": ["0340", "0341", "0342", "0343", "0344",
                "0345", "0346", "0347", "0348", "0349"],
}


def normalize_number(phone):
    """Normalize Pakistani mobile number to 03XXXXXXXXX."""

    phone = re.sub(r"[\s\-()]", "", phone)

    if phone.startswith("+92"):
        phone = "0" + phone[3:]

    elif phone.startswith("0092"):
        phone = "0" + phone[4:]

    return phone


def detect_network(phone):
    """Return likely network based on number prefix."""

    phone = normalize_number(phone)

    if not re.fullmatch(r"03\d{9}", phone):
        return None

    prefix = phone[:4]

    for network, prefixes in NETWORK_PREFIXES.items():
        if prefix in prefixes:
            return network

    return "Unknown / Other Network"


# --------------------------------
# User interface
# --------------------------------

phone_number = st.text_input(
    "Enter Pakistani mobile number",
    placeholder="03XXXXXXXXX",
    max_chars=20,
)

if st.button("Check Network", use_container_width=True):

    if not phone_number.strip():
        st.warning("Please enter a phone number.")

    else:
        normalized = normalize_number(phone_number)

        if not re.fullmatch(r"03\d{9}", normalized):
            st.error(
                "Invalid number. Enter a Pakistani mobile number "
                "such as 03001234567 or +923001234567."
            )

        else:
            network = detect_network(normalized)

            st.success(f"Likely Network: {network}")

            st.info(
                "This result is based on the number prefix. "
                "Mobile Number Portability (MNP) means the current "
                "network may be different."
            )

            # --------------------------------
            # Optional Gemini AI explanation
            # --------------------------------

            if st.checkbox("Explain result using Gemini AI"):

                api_key = st.secrets.get(
                    "GEMINI_API_KEY",
                    os.getenv("GEMINI_API_KEY", "")
                )

                if not api_key:
                    st.warning(
                        "Gemini API key is missing. "
                        "Configure it in Streamlit Secrets."
                    )

                else:
                    try:
                        client = genai.Client(api_key=api_key)

                        prompt = f"""
                        Explain briefly in simple English:
                        The Pakistani phone number prefix is
                        associated with {network}.

                        Explain that prefix-based detection is
                        not guaranteed because of Mobile Number
                        Portability.

                        Do not claim to know the current SIM
                        provider with certainty.
                        """

                        with st.spinner("Generating explanation..."):
                            response = client.models.generate_content(
                                model="gemini-2.5-flash",
                                contents=prompt,
                            )

                        st.markdown("### AI Explanation")
                        st.write(response.text)

                    except Exception:
                        st.error(
                            "AI explanation failed. Check your "
                            "API key and model configuration."
                        )

st.caption("Educational project | Python + Streamlit + Gemini")
