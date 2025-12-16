import json
import os
import glob

# Update all existing metadata files to add verification field
metadata_files = glob.glob("metadata/*/*/*.json")
print(f"Found {len(metadata_files)} metadata files")

if not metadata_files:
    metadata_files = glob.glob("metadata/*/*.json")
    print(f"Searching alternative pattern: {len(metadata_files)} files")

for file_path in metadata_files:
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        # Add verification if not present
        if "verification" not in data:
            data["verification"] = "This asset is officially presented at salutetosouldiers.nft"
            
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=2)
            
            print(f"Updated: {file_path}")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

print("Done updating metadata files")
