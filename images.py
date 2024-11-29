import os
import re
import shutil

# Paths
posts_dir = "/home/utkarsh/Documents/Notes/UtkarshDeoli/010 Blogs"
attachments_dir = "/home/utkarsh/Documents/Notes/UtkarshDeoli/images"
static_images_dir = "/home/utkarsh/Documents/Projects/personal-website/static/images"

# Ensure the static images directory exists
os.makedirs(static_images_dir, exist_ok=True)

# Step 1: Process each markdown file in the posts directory
for filename in os.listdir(posts_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(posts_dir, filename)
        
        with open(filepath, "r") as file:
            content = file.read()
        
        # Step 2: Find all image links in the format [[Image.png]]
        images = re.findall(r'\[\[([^]]*\.png)\]\]', content)
        
        # Step 3: Replace image links and ensure URLs are correctly formatted
        for image in images:
            # Generate the new Markdown-compatible image path
            markdown_image = f"![Image Description](/static/images/{image.replace(' ', '%20')})"
            content = content.replace(f"[[{image}]]", markdown_image)
            
            # Step 4: Copy the image to the Hugo static/images directory if it exists
            image_source = os.path.join(attachments_dir, image)
            image_destination = os.path.join(static_images_dir, image)

            if os.path.exists(image_source):
                shutil.copy(image_source, image_destination)
                print(f"Copied {image} to {image_destination}")
            else:
                print(f"Image not found: {image_source}")

        # Step 5: Write the updated content back to the markdown file
        with open(filepath, "w") as file:
            file.write(content)

print("Markdown files processed and images copied successfully.")

