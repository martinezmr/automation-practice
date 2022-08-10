for org in orgs:
    if org['name'] == 'DevNet Sandbox':
        orgId = org['id']

print(orgId)