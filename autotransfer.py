import os
import shutil

# Set the path to the MalReport and MalReport2 folders 
malreport_path = '/home/abc/Documents/MalReport' 
malreport2_path = '/home/abc/Documents/MalReport2'

# Create the MalReport2 folder if it doesn't exist 
if not os.path.exists(malreport2_path):
    os.makedirs(malreport2_path)

# Iterate over the subfolders in MalReport
for i in range(1, 501):
    malreport_subfolder_path = os.path.join(malreport_path, str(i)) 
    
    # Check if the subfolder exists
    if os.path.exists(malreport_subfolder_path):
        # Check if the reports folder exists in the subfolder
        reports_path = os.path.join(malreport_subfolder_path, 'reports') 
        
        if os.path.exists(reports_path):
            # Create the corresponding subfolder in MalReport2 
            malreport2_subfolder_path = os.path.join(malreport2_path, str(i)) 
            
            if not os.path.exists(malreport2_subfolder_path): 
                os.makedirs(malreport2_subfolder_path)

            # Move the reports folder to the corresponding subfolder in MalReport2 
            shutil.move(reports_path, malreport2_subfolder_path)
