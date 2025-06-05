import xml.etree.ElementTree as ET
import mysql.connector

# Establish MySQL connection
conn = mysql.connector.connect(
    user='root',
    password='aldrin04',
    host='localhost',
    database='securin'
)
print("Connection established")

# Define namespaces
namespaces = {
    'cpe-23': 'http://scap.nist.gov/schema/cpe-extension/2.3',
    'default': 'http://cpe.mitre.org/dictionary/2.0'
}

# Parse XML file
tree = ET.parse(r"C:\Users\SEC\Desktop\GIT HUB\securin\backend\data\official-cpe-dictionary_v2.3.xml")
root = tree.getroot()

# Find all 'cpe-item' elements (with default namespace)
data2 = root.findall('.//default:cpe-item', namespaces)

if data2:
    print(f"Found {len(data2)} cpe-item entries")
else:
    print("Error: No cpe-item found")

# Prepare MySQL insert
cursor = conn.cursor()

for index, item in enumerate(data2[:-1], 1):  
    # Title
    title_elem = item.find('default:title', namespaces)
    title = title_elem.text if title_elem is not None else None

    # URI - (crying emoji - so darn difficult)
    cpe_23_elem = item.find('cpe-23:cpe23-item', namespaces)
    cpe_23_uri = cpe_23_elem.attrib.get('name') if cpe_23_elem is not None else None

    # References
    references = item.findall('default:references/default:reference', namespaces)
    reference_links = [ref.attrib.get('href') for ref in references if ref.attrib.get('href')]
    reference_links_str = ', '.join(reference_links) if reference_links else None

    # Deprecation Date( some of them doesnt have a deprecation date and im too tired to look for it )
    deprecation_date = item.attrib.get('deprecation_date', None)

    # SQL Insert
    query = """
    INSERT INTO securin (cpe_title, cpe_23_uri, reference_links, cpe_23_deprecation_date)
    VALUES (%s, %s, %s, %s)
    """
    values = (title, cpe_23_uri, reference_links_str, deprecation_date)

    try:
        cursor.execute(query, values)
        conn.commit()
        print(f"Row {index} inserted successfully")
    except Exception as e:
        print(f"Error inserting row {index}: {e}")

# Close connection
cursor.close()
conn.close()
print("MySQL connection closed")
