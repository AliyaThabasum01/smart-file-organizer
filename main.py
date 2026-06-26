from organizer import organize_folder

print("=" * 50)
print("📂 Smart File Organizer")
print("=" * 50)

folder = input("\nEnter folder path: ")

try:
    organize_folder(folder)
    print("\n✅ Files organized successfully!")

except Exception as e:
    print("\n❌ Error:", e)
