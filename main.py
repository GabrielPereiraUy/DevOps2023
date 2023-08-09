# Gabriel test
hostname = "csr1kv"
# print(hostname)

ios_version = "15.8"
# print(ios_version)

hostname_upper = hostname.upper()

#print(hostname)

#print("")

#print(hostname_upper)

#print(hostname.capitalize())
#print(hostname)

vlan_names = ["HR", "R_and_D", "Marketing", "Accounting", "Sales", "Engineering"]
#print(vlan_names)

#print(len(vlan_names))

#print(vlan_names[5])
#print(vlan_names[-1])
#print(vlan_names[2:-1])
#print(vlan_names[2:])

vlan_names.index("Engineering")
#print(vlan_names.index("Engineering"))
#vlan_names[0] = "Engineering"

#print(vlan_names)

device_facts = {"vendor": "cisco", "os_version": 16.8, "platform": "csr1kv", "os_type": "ios", "hostname": "csrikv1"}
#print(device_facts)
#print(device_facts.keys())
#print(device_facts.values())
print(device_facts["vendor"])
print(device_facts.get("vendor"))