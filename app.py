import streamlit as st
import requests as req
import json
from key import key

base_url = "https://api.aimlapi.com/v1"
headers = {"Authorization": f"Bearer {key}"}
