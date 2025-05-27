import sqlite3
import csv
from datetime import datetime

class Sample:
    def __init__(self, sample_id, planet, sample_type, date_collected):
        self.sample_id = sample_id
        self.planet = planet
        self.sample_type = sample_type
        self.date_collected = date_collected

    def __str__(self):
        return f"Sample {self.sample_id}: {self.sample_type} from {self.planet}, collected on {self.date_collected}"

    def to_tuple(self):
        return (self.sample_id, self.planet, self.sample_type, self.date_collected.strftime("%Y-%m-%d"))

sample = Sample("001", "Mars", "Rock", datetime(2023, 6, 15))
print(sample)  # This will use our __str__ method
print(sample.to_tuple())  # This will return a tuple representation of our sample

def create_connection():
    try:
        conn = sqlite3.connect('samples.db')
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def create_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS samples (
                id TEXT PRIMARY KEY,
                planet TEXT NOT NULL,
                sample_type TEXT NOT NULL,
                date_collected TEXT NOT NULL
            )
        ''')
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")

def init_db():
    conn = create_connection()
    if conn is not None:
        create_table(conn)
        conn.close()
    else:
        print("Error! Cannot create the database connection.")


init_db()
print("Database initialized successfully.")

def add_sample(sample):
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO samples(id, planet, sample_type, date_collected)
                VALUES(?,?,?,?)
            ''', sample.to_tuple())
            conn.commit()
            print(f"Sample {sample.sample_id} added successfully.")
        except sqlite3.Error as e:
            print(f"Error adding sample: {e}")
        finally:
            conn.close()
    else:
        print("Error! Cannot create the database connection.")

def get_all_samples():
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM samples")
            rows = cursor.fetchall()
            samples = []
            for row in rows:
                sample = Sample(row[0], row[1], row[2], datetime.strptime(row[3], "%Y-%m-%d"))
                samples.append(sample)
            return samples
        except sqlite3.Error as e:
            print(f"Error retrieving samples: {e}")
        finally:
            conn.close()
    else:
        print("Error! Cannot create the database connection.")
    return []

sample_to_add = Sample("001", "Mars", "Rock", datetime(2023, 6, 15))
add_sample(sample_to_add)

samples = get_all_samples()
for sample in samples:
    print(sample)

def get_sample_by_id(sample_id):
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM samples WHERE id = ?", (sample_id,))
            row = cursor.fetchone()
            if row:
                return Sample(row[0], row[1], row[2], datetime.strptime(row[3], "%Y-%m-%d"))
            else:
                print(f"No sample found with ID {sample_id}")
        except sqlite3.Error as e:
            print(f"Error retrieving sample: {e}")
        finally:
            conn.close()
    else:
        print("Error! Cannot create the database connection.")
    return None

sample = get_sample_by_id("001")
print(sample)

sample = get_sample_by_id(sample_to_add.sample_id)
print(sample)

def update_sample(sample):
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE samples
                SET planet = ?, sample_type = ?, date_collected = ?
                WHERE id = ?
            ''', (sample.planet, sample.sample_type, sample.date_collected.strftime("%Y-%m-%d"), sample.sample_id))
            conn.commit()
            if cursor.rowcount > 0:
                print(f"Sample {sample.sample_id} updated successfully.")
            else:
                print(f"No sample found with ID {sample.sample_id}")
        except sqlite3.Error as e:
            print(f"Error updating sample: {e}")
        finally:
            conn.close()
    else:
        print("Error! Cannot create the database connection.")

updated_sample = Sample("001", "Mars", "Rock", datetime(2024, 6, 15))
update_sample(updated_sample)

sample = get_sample_by_id(updated_sample.sample_id)
print(sample)

def delete_sample(sample_id):
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('''
            DELETE FROM samples
            WHERE id = ?
            ''', (sample_id,))
            conn.commit()
            if cursor.rowcount > 0:
                print(f"Sample {sample_id} deleted successfully.")
            else:
                print(f"No sample found with ID {sample_id}")
        except sqlite3.Error as e:
            print(f"Error deleting sample: {e}")
        finally:
            conn.close()
    else:
        print("Error! Cannot create the database connection.")

delete_sample(sample.sample_id)
get_sample_by_id(sample.sample_id)

def display_menu():
    print("\n--- Intergalactic Sample Database ---")
    print("1. Add a new sample")
    print("2. View all samples")
    print("3. Search for a sample")
    print("4. Update a sample")
    print("5. Delete a sample")
    print("6. Generate samples per planet report")
    print("7. Export data to CSV")
    print("8. Exit")
    return input("Enter your choice (1-8): ")

def input_new_sample():
    while True:
        sample_id = input("Enter sample ID: ").strip()
        if not sample_id:
            print("Sample ID cannot be empty.")
            continue
            
        planet = input("Enter planet of origin: ").strip()
        if not planet:
            print("Planet cannot be empty.")
            continue
        
        sample_type = input("Enter sample type: ").strip()
        if not sample_type:
            print("Sample type cannot be empty.")
            continue
        
        date_str = input("Enter date collected (YYYY-MM-DD): ").strip()
        date_collected = validate_date(date_str)
        if not date_collected:
            continue
        
        return Sample(sample_id, planet, sample_type, date_collected)
    
def input_sample_id():
    while True:
        sample_id = input("Enter sample ID: ").strip()
        if sample_id:
            return sample_id
        else:
            print("Sample ID cannot be empty. Please try again.")

def input_updated_sample(sample):
    planet = input(f"Enter new planet of origin (current: {sample.planet}): ") or sample.planet
    sample_type = input(f"Enter new sample type (current: {sample.sample_type}): ") or sample.sample_type
    date_str = input(f"Enter new date collected (current: {sample.date_collected.strftime('%Y-%m-%d')}, format YYYY-MM-DD): ") \
        or sample.date_collected.strftime("%Y-%m-%d")
    date_collected = datetime.strptime(date_str, "%Y-%m-%d")
    return Sample(sample.sample_id, planet, sample_type, date_collected)

def validate_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")

def samples_per_planet():
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT planet, COUNT(*) AS sample_count
                FROM samples
                GROUP BY planet
                ORDER BY sample_count DESC
            ''')
            results = cursor.fetchall()
            print("\n--- Samples per Planet Report ---")
            for planet, count in results:
                sample_word = "sample" if count == 1 else "samples"
                print(f"{planet}: {count} {sample_word}")
        except sqlite3.Error as e:
            print(f"Error generating report: {e}")
        finally:
            conn.close()
    else:
        print("Error! Cannot create the database connection.")

def export_to_csv():
    samples = get_all_samples()
    if not samples:
        print("No samples to export.")
        return

    filename = input("Enter the filename for the CSV export (default: samples_export.csv): ").strip() or "samples_export.csv"
    
    try:
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['ID', 'Planet', 'Sample Type', 'Date Collected'])  # Header row
            for sample in samples:
                writer.writerow(sample.to_tuple())
        print(f"Data exported successfully to {filename}")
    except IOError as e:
        print(f"Error exporting data: {e}")

def search_samples():
    print("\n--- Search Samples ---")
    print("1. Search by ID")
    print("2. Search by Planet")
    print("3. Search by Sample Type")
    print("4. Search by Date Range")
    choice = input("Enter your choice (1-4): ")

    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            if choice == '1':
                sample_id = input("Enter sample ID: ")
                cursor.execute("SELECT * FROM samples WHERE id = ?", (sample_id,))
            elif choice == '2':
                planet = input("Enter planet name: ")
                cursor.execute("SELECT * FROM samples WHERE planet LIKE ?", ('%' + planet + '%',))
            elif choice == '3':
                sample_type = input("Enter sample type: ")
                cursor.execute("SELECT * FROM samples WHERE sample_type LIKE ?", ('%' + sample_type + '%',))
            elif choice == '4':
                while True:
                    try:
                        start_date = validate_date(input("Enter start date (YYYY-MM-DD): "))
                        end_date = validate_date(input("Enter end date (YYYY-MM-DD): "))
                        if start_date > end_date:
                            print("Start date must be before end date. Please try again.")
                        else:
                            break
                    except ValueError as e:
                        print(f"Error: {e}")
                cursor.execute("SELECT * FROM samples WHERE date_collected BETWEEN ? AND ?", 
                               (start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d")))
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
                return

            results = cursor.fetchall()
            if results:
                print("\nSearch Results:")
                for row in results:
                    print(f"ID: {row[0]}, Planet: {row[1]}, Type: {row[2]}, Date Collected: {row[3]}")
                print(f"\nTotal results: {len(results)} sample{'s' if len(results) != 1 else ''}")
            else:
                print("No samples found matching your search criteria.")

        except sqlite3.Error as e:
            print(f"Database error: {e}")
        finally:
            conn.close()
    else:
        print("Error! Cannot create the database connection.")

def main():
    while True:
        try:
            choice = display_menu()
            
            if choice == '1':
                sample = input_new_sample()
                add_sample(sample)
            
            elif choice == '2':
                samples = get_all_samples()
                if samples:
                    for sample in samples:
                        print(sample)
                else:
                    print("No samples found in the database.")
            
            elif choice == '3':
                search_samples()
            
            elif choice == '4':
                sample_id = input_sample_id()
                sample = get_sample_by_id(sample_id)
                if sample:
                    updated_sample = input_updated_sample(sample)
                    update_sample(updated_sample)
                else:
                    print(f"No sample found with ID {sample_id}")
            
            elif choice == '5':
                sample_id = input_sample_id()
                delete_sample(sample_id)
            
            elif choice == '6':
                samples_per_planet()

            elif choice == '7':
                export_to_csv()

            elif choice == '8':
                print("Thank you for using the Intergalactic Sample Database. Goodbye!")
                break
            
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
        
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Please try again.")

if __name__ == "__main__":
    init_db()
    main()
