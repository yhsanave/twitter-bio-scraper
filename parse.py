import json
from dataclasses import dataclass

@dataclass
class User():
    id: str
    name: str
    username: str
    links: list

users: list[User] = []

with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    for u in data['data']:
        # User id, name, and handle
        user = User(id=u.get('id'),name=u.get('name'),username=u.get('username'),links=[])
        
        # URL
        try: 
            user.links.append(u['entities']['url']['urls'][0]['expanded_url'])
        except:
            pass
        
        # Links in bio
        try:
            user.links.extend(link.get('expanded_url') for link in u['entities']['description']['urls'])
        except:
            pass

        users.append(user)

with open('output.md', 'w', encoding='utf-8') as f:
    for user in users:
        f.write(f'## {user.name}\n\n')
        f.write(f'### {user.username} ({user.id})\n\n')
        f.write('\n\n'.join(user.links))
        f.write(f'\n\n---\n\n')