#!/usr/bin/env python3

import time
import requests
import json

UID = "u-s4t2ud-6f00f915a8502d3af9d46351766176e32619718d006f2088cc14307c7efbbb8e"
SECRET = "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"

def post42(url, payload):
    url = "https://api.intra.42.fr" + url
    payload = payload
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()

def get42(url, payload):
    url = "https://api.intra.42.fr" + url
    payload = payload
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json()

wtoken = post42("/oauth/token", {"grant_type": "client_credentials", \
                                "client_id": UID, "client_secret": SECRET})
campus_users = []
temp = []

campus_users_general = '/v2/campus/55'
campus_users_total = get42(campus_users_general, {"access_token": wtoken["access_token"]})
total_users = campus_users_total["users_count"]

total_pages = ( total_users // 100 + 1 ) + 1

print(f"Total users: {total_users} Total pages: {total_pages}")
print("Please wait while data from API is retrieved...")

for i in range(1, total_pages):  
    campus_users += get42("/v2/campus/55/users?page[number]=" + str(i) + "&page[size]=100", \
                                                   {"access_token": wtoken["access_token"]})

for user in campus_users:
    temp.append({
        "login": user.get("login"),  
        "correction_point":  user.get("correction_point"),
        "pool_year": user.get("pool_year"),
        "location": user.get("location"),  
        "updated_at": user.get("updated_at").split("T")[1].split(".")[0],
        "wallet": user.get("wallet")
    })

for entry in temp:
    if entry["location"] is not None and entry["pool_year"] == '2022':
        print(f"\033[91m{entry['login']:<10}\033[0m Updated: {entry['updated_at']:<8} Eval Points: {str(entry['correction_point']):<5} Location: {str(entry['location']):<10} Wallet: {str(entry['wallet']):<10}")
    elif entry["location"] is not None and entry["pool_year"] == '2023':
        print(f"\033[92m{entry['login']:<10}\033[0m Updated: {entry['updated_at']:<8} Eval Points: {str(entry['correction_point']):<5} Location: {str(entry['location']):<10} Wallet: {str(entry['wallet']):<10}")