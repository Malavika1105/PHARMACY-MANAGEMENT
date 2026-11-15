import mysql.connector

def test_id_logic():
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1105",
            database="login_1"
        )
        cursor = db.cursor(dictionary=True)
        
        # 1. Clean up existing test data
        cursor.execute("DELETE FROM medicine WHERE MEDICINE_NAME = 'TestMed'")
        db.commit()
        
        # 2. Add first entry
        name = "TestMed"
        m_id_provided = "" # Empty to trigger auto-gen
        cat = "TestCat"
        
        # Simulate add_medicine logic
        cursor.execute("SELECT MEDICINE_ID, CATEGORY FROM medicine WHERE MEDICINE_NAME = %s LIMIT 1", (name,))
        existing = cursor.fetchone()
        
        if existing:
            m_id = existing['MEDICINE_ID']
            cat = existing['CATEGORY']
        else:
            cursor.execute("SELECT COUNT(DISTINCT MEDICINE_ID) as total FROM medicine")
            count = cursor.fetchone()['total']
            m_id = f"MED-{(count + 1):03d}"
            
        print(f"Adding first batch: Name={name}, Generated ID={m_id}")
        cursor.execute("INSERT INTO medicine (MEDICINE_ID, MEDICINE_NAME, BATCH_NO, CATEGORY, EXPIRY_DATE, PRICE, STOCK_QUANTITY) VALUES (%s, %s, %s, %s, %s, %s, %s)", 
                       (m_id, name, 'B1', cat, '2026-12-31', 10.0, 100))
        db.commit()
        
        # 3. Add second batch with same name but different details
        name2 = "TestMed"
        # Simulate add_medicine logic again
        cursor.execute("SELECT MEDICINE_ID, CATEGORY FROM medicine WHERE MEDICINE_NAME = %s LIMIT 1", (name2,))
        existing2 = cursor.fetchone()
        
        if existing2:
            m_id2 = existing2['MEDICINE_ID']
            cat2 = existing2['CATEGORY']
            print(f"Found existing! Reusing ID={m_id2}, Cat={cat2}")
        else:
            m_id2 = "FAILED"
            
        cursor.execute("INSERT INTO medicine (MEDICINE_ID, MEDICINE_NAME, BATCH_NO, CATEGORY, EXPIRY_DATE, PRICE, STOCK_QUANTITY) VALUES (%s, %s, %s, %s, %s, %s, %s)", 
                       (m_id2, name2, 'B2', cat2, '2027-12-31', 10.0, 50))
        db.commit()
        
        # 4. Verify results
        cursor.execute("SELECT MEDICINE_NAME, MEDICINE_ID, BATCH_NO FROM medicine WHERE MEDICINE_NAME = 'TestMed'")
        results = cursor.fetchall()
        print("Inventory records for TestMed:")
        for r in results:
            print(r)
            
        # Clean up
        cursor.execute("DELETE FROM medicine WHERE MEDICINE_NAME = 'TestMed'")
        db.commit()
        
        cursor.close()
        db.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_id_logic()
