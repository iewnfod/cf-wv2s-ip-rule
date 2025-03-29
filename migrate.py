import re
FIND_STR = input("Enter the string you want to find: ")
# Open the file and read lines
with open('/Users/jessiezhu/Library/Mobile Documents/iCloud~com~nssurge~inc/Documents/WgetCloud Local.conf', 'r') as file:
    lines = file.readlines()

# Filter lines ending with "no-resolve"
no_resolve_lines = [line.strip() for line in lines if line.strip().endswith(f"{FIND_STR},extended-matching")]

with open(f'/Users/jessiezhu/Documents/GitHub/cf-wv2s-ip-rule-rararxd/list/{FIND_STR}.list', 'w') as file:
    file.write('\n'.join([re.sub(r',[^,]*,[^,]*$', '', line) for line in no_resolve_lines]))
