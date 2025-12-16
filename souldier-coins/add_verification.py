import json
import os

realms = ['aurora', 'prime', 'shadow']
base_path = 'metadata'

for realm in realms:
    realm_path = os.path.join(base_path, realm)
    for i in range(1, 11):
        edition = str(i).zfill(4)
        file_path = os.path.join(realm_path, f'{edition}.json')
        
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                data = json.load(f)
            
            # Add verification field
            data['verification'] = 'This asset is officially presented at salutetosouldiers.nft'
            
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=2)
            
            print(f'Updated {file_path}')
        else:
            print(f'File not found: {file_path}')

print('\nDone updating all metadata files with verification field')
