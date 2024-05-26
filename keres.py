import json
import os

def betoltes_irsz():
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, 'cleaned_output.json')
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def keres_iranyitoszam_szerint(iranyitoszam, data):
    results = [item for item in data if item['iranyitoszam'] == iranyitoszam]
    if results:
        for result in results:
            print(json.dumps(result, ensure_ascii=False, indent=4))
    else:
        print("Nincs találat az adott irányítószámra.")

def main():
    iranyitoszam = int(input("Adjon meg egy irányítószámot: "))
    data = betoltes_irsz()
    keres_iranyitoszam_szerint(iranyitoszam, data)

if __name__ == '__main__':
    main()
