projects = {
    "project1": {
        "project_key": "TE1",
        "project_name": "Teir 1 Project"
    },
    "project2": {
        "project_key": "RRB",
        "project_name": "Risk Register Project",
        "custom_fields": {
            "Risk Identification Source": "paragraph",
            "Affected Users": "dropdown",
            "Inherent Likelihood Risk Score": "number"
        }
    }
}


# Function to display project details
def display_project_details(projects):
    for project_id, details in projects.items():
        print(f"\nProject ID: {project_id}")
        print(f"Project Key: {details.get('project_key', 'N/A')}")
        print(f"Project Name: {details.get('project_name', 'N/A')}")

        # Check and display custom fields if available
        custom_fields = details.get("custom_fields")
        if custom_fields:
            print("Custom Fields:")
            for field, field_type in custom_fields.items():
                print(f"  - {field}: {field_type}")
        else:
            print("Custom Fields: None")


# Main function to enhance functionality
def main():
    while True:
        print("\n--- Project Viewer ---")
        print("1. View All Projects")
        print("2. Search for a Project by ID")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            display_project_details(projects)
        elif choice == "2":
            project_id = input("Enter the project ID (e.g., project1): ")
            if project_id in projects:
                display_project_details({project_id: projects[project_id]})
            else:
                print("Project ID not found.")
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# Run the script
if __name__ == "__main__":
    main()
