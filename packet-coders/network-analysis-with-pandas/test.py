import pandas as pd


df = pd.DataFrame(
    {
        "vlan_id": ["100","101","102"],
        "vlan_name": ["VLAN-100","VLAN-200","VLAN-300"]
    }
)

print(df)

# df.drop(0, axis=0, inplace=True)
# print(df)

df.replace({"vlan_id": {"10[1-4]": "100"}}, regex=True)

print(df)